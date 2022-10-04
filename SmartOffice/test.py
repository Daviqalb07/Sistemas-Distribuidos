from Device import *
import device_pb2

device = Device(id=1, name= "lampada", multicast_ip="227.1.1.192", multicast_port=63052, 
                sensor= device_pb2.Device.Sensor(name= "presenca", value= 0),
                actuator= device_pb2.Device.Actuator(name="teste", state=True))

print(device.sensor.value)