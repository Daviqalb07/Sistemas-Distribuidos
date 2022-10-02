# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lampada.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='lampada.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rlampada.proto\"o\n\x07Lampada\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x1d\n\x05\x63olor\x18\x02 \x01(\x0e\x32\x0e.Lampada.Color\x12\x0e\n\x06sensor\x18\x03 \x01(\x08\"%\n\x05\x43olor\x12\x07\n\x03RED\x10\x00\x12\t\n\x05GREEN\x10\x01\x12\x08\n\x04\x42LUE\x10\x02\x62\x06proto3'
)



_LAMPADA_COLOR = _descriptor.EnumDescriptor(
  name='Color',
  full_name='Lampada.Color',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GREEN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BLUE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=91,
  serialized_end=128,
)
_sym_db.RegisterEnumDescriptor(_LAMPADA_COLOR)


_LAMPADA = _descriptor.Descriptor(
  name='Lampada',
  full_name='Lampada',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='Lampada.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='color', full_name='Lampada.color', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sensor', full_name='Lampada.sensor', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LAMPADA_COLOR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=128,
)

_LAMPADA.fields_by_name['color'].enum_type = _LAMPADA_COLOR
_LAMPADA_COLOR.containing_type = _LAMPADA
DESCRIPTOR.message_types_by_name['Lampada'] = _LAMPADA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Lampada = _reflection.GeneratedProtocolMessageType('Lampada', (_message.Message,), {
  'DESCRIPTOR' : _LAMPADA,
  '__module__' : 'lampada_pb2'
  # @@protoc_insertion_point(class_scope:Lampada)
  })
_sym_db.RegisterMessage(Lampada)


# @@protoc_insertion_point(module_scope)
