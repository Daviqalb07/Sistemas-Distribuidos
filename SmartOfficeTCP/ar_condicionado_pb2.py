# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ar-condicionado.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ar-condicionado.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15\x61r-condicionado.proto\"5\n\x0e\x41rCondicionado\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x13\n\x0btemperatura\x18\x02 \x01(\x05\x62\x06proto3'
)




_ARCONDICIONADO = _descriptor.Descriptor(
  name='ArCondicionado',
  full_name='ArCondicionado',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ArCondicionado.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='temperatura', full_name='ArCondicionado.temperatura', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=25,
  serialized_end=78,
)

DESCRIPTOR.message_types_by_name['ArCondicionado'] = _ARCONDICIONADO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ArCondicionado = _reflection.GeneratedProtocolMessageType('ArCondicionado', (_message.Message,), {
  'DESCRIPTOR' : _ARCONDICIONADO,
  '__module__' : 'ar_condicionado_pb2'
  # @@protoc_insertion_point(class_scope:ArCondicionado)
  })
_sym_db.RegisterMessage(ArCondicionado)


# @@protoc_insertion_point(module_scope)
