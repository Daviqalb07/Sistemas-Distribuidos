# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='SmartOffice',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rmessage.proto\x12\x0bSmartOffice\"\"\n\x06\x41\x63tion\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xa7\x01\n\x06\x44\x65vice\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\n\n\x02on\x18\x03 \x01(\x08\x12*\n\x06sensor\x18\x04 \x01(\x0b\x32\x1a.SmartOffice.Device.Sensor\x12$\n\x07\x61\x63tions\x18\x05 \x03(\x0b\x32\x13.SmartOffice.Action\x1a%\n\x06Sensor\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x05\"6\n\x0bMeasurement\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x02\";\n\x07Request\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08idDevice\x18\x02 \x01(\x05\x12\x10\n\x08idAction\x18\x03 \x01(\x05\"0\n\x08Response\x12$\n\x07\x64\x65vices\x18\x01 \x03(\x0b\x32\x13.SmartOffice.Device\"\xca\x01\n\x07Message\x12\x0c\n\x04type\x18\x01 \x01(\t\x12%\n\x06\x64\x65vice\x18\x02 \x01(\x0b\x32\x13.SmartOffice.DeviceH\x00\x12/\n\x0bmeasurement\x18\x03 \x01(\x0b\x32\x18.SmartOffice.MeasurementH\x00\x12%\n\x06\x61\x63tion\x18\x04 \x01(\x0b\x32\x13.SmartOffice.ActionH\x00\x12\'\n\x07request\x18\x05 \x01(\x0b\x32\x14.SmartOffice.RequestH\x00\x42\t\n\x07\x63ontentb\x06proto3'
)




_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='SmartOffice.Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SmartOffice.Action.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='SmartOffice.Action.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=30,
  serialized_end=64,
)


_DEVICE_SENSOR = _descriptor.Descriptor(
  name='Sensor',
  full_name='SmartOffice.Device.Sensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='SmartOffice.Device.Sensor.name', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='SmartOffice.Device.Sensor.value', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=197,
  serialized_end=234,
)

_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='SmartOffice.Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SmartOffice.Device.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='SmartOffice.Device.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='on', full_name='SmartOffice.Device.on', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sensor', full_name='SmartOffice.Device.sensor', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actions', full_name='SmartOffice.Device.actions', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DEVICE_SENSOR, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=234,
)


_MEASUREMENT = _descriptor.Descriptor(
  name='Measurement',
  full_name='SmartOffice.Measurement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SmartOffice.Measurement.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='SmartOffice.Measurement.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='SmartOffice.Measurement.value', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=236,
  serialized_end=290,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='SmartOffice.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='SmartOffice.Request.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='idDevice', full_name='SmartOffice.Request.idDevice', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='idAction', full_name='SmartOffice.Request.idAction', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=292,
  serialized_end=351,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='SmartOffice.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='devices', full_name='SmartOffice.Response.devices', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=353,
  serialized_end=401,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='SmartOffice.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='SmartOffice.Message.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device', full_name='SmartOffice.Message.device', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='measurement', full_name='SmartOffice.Message.measurement', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action', full_name='SmartOffice.Message.action', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request', full_name='SmartOffice.Message.request', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='content', full_name='SmartOffice.Message.content',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=404,
  serialized_end=606,
)

_DEVICE_SENSOR.containing_type = _DEVICE
_DEVICE.fields_by_name['sensor'].message_type = _DEVICE_SENSOR
_DEVICE.fields_by_name['actions'].message_type = _ACTION
_RESPONSE.fields_by_name['devices'].message_type = _DEVICE
_MESSAGE.fields_by_name['device'].message_type = _DEVICE
_MESSAGE.fields_by_name['measurement'].message_type = _MEASUREMENT
_MESSAGE.fields_by_name['action'].message_type = _ACTION
_MESSAGE.fields_by_name['request'].message_type = _REQUEST
_MESSAGE.oneofs_by_name['content'].fields.append(
  _MESSAGE.fields_by_name['device'])
_MESSAGE.fields_by_name['device'].containing_oneof = _MESSAGE.oneofs_by_name['content']
_MESSAGE.oneofs_by_name['content'].fields.append(
  _MESSAGE.fields_by_name['measurement'])
_MESSAGE.fields_by_name['measurement'].containing_oneof = _MESSAGE.oneofs_by_name['content']
_MESSAGE.oneofs_by_name['content'].fields.append(
  _MESSAGE.fields_by_name['action'])
_MESSAGE.fields_by_name['action'].containing_oneof = _MESSAGE.oneofs_by_name['content']
_MESSAGE.oneofs_by_name['content'].fields.append(
  _MESSAGE.fields_by_name['request'])
_MESSAGE.fields_by_name['request'].containing_oneof = _MESSAGE.oneofs_by_name['content']
DESCRIPTOR.message_types_by_name['Action'] = _ACTION
DESCRIPTOR.message_types_by_name['Device'] = _DEVICE
DESCRIPTOR.message_types_by_name['Measurement'] = _MEASUREMENT
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), {
  'DESCRIPTOR' : _ACTION,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:SmartOffice.Action)
  })
_sym_db.RegisterMessage(Action)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), {

  'Sensor' : _reflection.GeneratedProtocolMessageType('Sensor', (_message.Message,), {
    'DESCRIPTOR' : _DEVICE_SENSOR,
    '__module__' : 'message_pb2'
    # @@protoc_insertion_point(class_scope:SmartOffice.Device.Sensor)
    })
  ,
  'DESCRIPTOR' : _DEVICE,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:SmartOffice.Device)
  })
_sym_db.RegisterMessage(Device)
_sym_db.RegisterMessage(Device.Sensor)

Measurement = _reflection.GeneratedProtocolMessageType('Measurement', (_message.Message,), {
  'DESCRIPTOR' : _MEASUREMENT,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:SmartOffice.Measurement)
  })
_sym_db.RegisterMessage(Measurement)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:SmartOffice.Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:SmartOffice.Response)
  })
_sym_db.RegisterMessage(Response)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:SmartOffice.Message)
  })
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
