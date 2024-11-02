from firebase_admin import firestore
from command import Device

db = firestore.client()


def add_command(command, device):
    db.collection("devices").document(device).collection("commands").add(command.__dict__)


def add_output(output, device):
    db.collection("devices").document(device).collection("outputs").add(output.__dict__)


def add_error(error, device):
    db.collection("devices").document(device).collection("errors").add(error.__dict__)


def get_devices():
    return [Device(**device.to_dict()) for device in db.collection("devices").stream()]


def get_device(device_name):
    device = db.collection("devices").document(device_name).get()
    if not device:
        return False
    return Device(**device.to_dict())


def add_device(device):
    db.collection("devices").document(device.device_name).set(device.__dict__)
    return True


def delete_device(device_name):
    db.collection("devices").document(device_name).delete()
    return True
