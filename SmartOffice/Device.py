import device_pb2


class Device:
    def __init__(self, id: int, name: str, multicast_group_ip: str, multicast_port: int, sensor, actuator) -> None:
        self.id = id
        self.name = name
        self.multicast_group_ip = multicast_group_ip
        self.multicast_port = multicast_port
        self.sensor = sensor
        self.actuator = actuator