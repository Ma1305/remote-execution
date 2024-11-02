class Command:
    def __init__(self, command, time_stamp, **kwargs):
        self.command = command
        self.time_stamp = time_stamp


class Output:
    def __init__(self, output, time_stamp, **kwargs):
        self.output = output
        self.time_stamp = time_stamp


class Error:
    def __init__(self, error, time_stamp, **kwargs):
        self.error = error
        self.time_stamp = time_stamp


class Device:
    def __init__(self, device_name, time_created, **kwargs):
        self.device_name = device_name
        self.time_created = time_created
