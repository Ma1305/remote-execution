import time
from datetime import datetime

from config import setup_firebase
from firebase_admin import firestore
import subprocess
from threading import Thread
from command import Command, Error, Output
from database import add_error, add_output


snapshot_initialization = True

process = subprocess.Popen(["/bin/bash"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           shell=True, text=True)


def on_new_command(doc_snapshots, changes, read_time, *args, **kwargs):
    global snapshot_initialization

    if snapshot_initialization:
        snapshot_initialization = False
        return

    commands = [Command(**change.document.to_dict()) for change in changes]
    commands.sort(key=lambda x: x.time_stamp)
    for command in commands:
        process.stdin.write(command.command + "\n")
        process.stdin.flush()


def output_lines():
    global process
    for line in process.stdout:
        output_line = line.replace("\n", "")
        output = Output(output_line, datetime.now())
        add_output(output)


def error_lines():
    global process
    for line in process.stderr:
        error_line = line.replace("\n", "")
        error = Error(error_line, datetime.now())
        add_error(error)


output_lines_thread = Thread(target=output_lines)
output_lines_thread.start()

error_lines_thread = Thread(target=error_lines)
error_lines_thread.start()

db = firestore.client()

collection = db.collection("commands")

collection.on_snapshot(on_new_command)

while True:
    time.sleep(1)


