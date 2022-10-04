# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: device.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='device.proto',
  package='SmartOffice',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x64\x65vice.proto\x12\x0bSmartOffice\"\xc6\x01\n\x06\x44\x65vice\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12*\n\x06sensor\x18\x03 \x01(\x0b\x32\x1a.SmartOffice.Device.Sensor\x12+\n\x07\x61\x63tions\x18\x04 \x03(\x0b\x32\x1a.SmartOffice.Device.Action\x1a%\n\x06Sensor\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x05\x1a\"\n\x06\x41\x63tion\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\tb\x06proto3')
)




_DEVICE_SENSOR = _descriptor.Descriptor(
  name='Sensor',
  full_name='SmartOffice.Device.Sensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='SmartOffice.Device.Sensor.name', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='SmartOffice.Device.Sensor.value', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=192,
)

_DEVICE_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='SmartOffice.Device.Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SmartOffice.Device.Action.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='SmartOffice.Device.Action.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=228,
)

_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='SmartOffice.Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SmartOffice.Device.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='SmartOffice.Device.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensor', full_name='SmartOffice.Device.sensor', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actions', full_name='SmartOffice.Device.actions', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEVICE_SENSOR, _DEVICE_ACTION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=228,
)

_DEVICE_SENSOR.containing_type = _DEVICE
_DEVICE_ACTION.containing_type = _DEVICE
_DEVICE.fields_by_name['sensor'].message_type = _DEVICE_SENSOR
_DEVICE.fields_by_name['actions'].message_type = _DEVICE_ACTION
DESCRIPTOR.message_types_by_name['Device'] = _DEVICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), dict(

  Sensor = _reflection.GeneratedProtocolMessageType('Sensor', (_message.Message,), dict(
    DESCRIPTOR = _DEVICE_SENSOR,
    __module__ = 'device_pb2'
    # @@protoc_insertion_point(class_scope:SmartOffice.Device.Sensor)
    ))
  ,

  Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), dict(
    DESCRIPTOR = _DEVICE_ACTION,
    __module__ = 'device_pb2'
    # @@protoc_insertion_point(class_scope:SmartOffice.Device.Action)
    ))
  ,
  DESCRIPTOR = _DEVICE,
  __module__ = 'device_pb2'
  # @@protoc_insertion_point(class_scope:SmartOffice.Device)
  ))
_sym_db.RegisterMessage(Device)
_sym_db.RegisterMessage(Device.Sensor)
_sym_db.RegisterMessage(Device.Action)


# @@protoc_insertion_point(module_scope)