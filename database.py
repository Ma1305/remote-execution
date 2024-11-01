from firebase_admin import firestore

db = firestore.client()


def add_command(command):
    db.collection("commands").add(command.__dict__)


def add_output(output):
    db.collection("outputs").add(output.__dict__)


def add_error(error):
    db.collection("errors").add(error.__dict__)
