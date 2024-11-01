from datetime import datetime
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


db.collection("outputs").on_snapshot(output_lines)
db.collection("errors").on_snapshot(error_lines)


user_input = input("user?: ")
while user_input != "!!exit!!":
    command = Command(user_input, datetime.now())
    add_command(command)
    user_input = input("user?: ")
