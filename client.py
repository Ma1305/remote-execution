from datetime import datetime

import database
from config import setup_firebase

from firebase_admin import firestore
from command import Command, Output, Error
from database import add_command


db = firestore.client()
output_initialization = True
error_initialization = True


def output_lines(doc_snapshots, changes, read_time, *args, **kwargs):
    global output_initialization
    if output_initialization:
        output_initialization = False
        return

    for change in changes:
        output = Output(**change.document.to_dict())
        print(output.output)


def error_lines(doc_snapshots, changes, read_time, *args, **kwargs):
    global error_initialization
    if error_initialization:
        error_initialization = False
        return

    for change in changes:
        error = Error(**change.document.to_dict())
        print(error.error)

available_devices = database.get_devices()
print("available devices are: ")
for i, device in enumerate(available_devices):
    print(f"{i}: name: {device}, created_at: {device.time_created}")

print("\n")

device_name = None
while device_name is None:
    device_num = input("Enter your choice number: ")
    try:
        device_name = available_devices[int(device_num)].device_name
    except:
        print("Invalid choice!!\n")


db.collection("devices").document(device_name).collection("outputs").on_snapshot(output_lines)
db.collection("devices").document(device_name).collection("errors").on_snapshot(error_lines)


user_input = input("user?: ")
while user_input != "!!exit!!":
    command = Command(user_input, datetime.now())
    if command.command == "clear":
        print("\n"*10)
    add_command(command)
    user_input = input("user?: ")
