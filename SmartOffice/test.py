import device_pb2

device = device_pb2.Device(sensor=device_pb2.Device.Sensor(id=1, name="alo", value= True))

print(device.sensor.id)