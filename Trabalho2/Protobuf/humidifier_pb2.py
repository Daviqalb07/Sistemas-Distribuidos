# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: humidifier.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10humidifier.proto\x12\x0bSmartOffice\"\x18\n\x07Request\x12\r\n\x05Value\x18\x01 \x01(\x02\"\x1a\n\x08Response\x12\x0e\n\x06Status\x18\x01 \x01(\x08\x32\xc2\x01\n\nHumidifier\x12\x38\n\x07OnHumid\x12\x14.SmartOffice.Request\x1a\x15.SmartOffice.Response\"\x00\x12\x39\n\x08OffHumid\x12\x14.SmartOffice.Request\x1a\x15.SmartOffice.Response\"\x00\x12?\n\x0e\x43hangeVelocity\x12\x14.SmartOffice.Request\x1a\x15.SmartOffice.Response\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'humidifier_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=33
  _REQUEST._serialized_end=57
  _RESPONSE._serialized_start=59
  _RESPONSE._serialized_end=85
  _HUMIDIFIER._serialized_start=88
  _HUMIDIFIER._serialized_end=282
# @@protoc_insertion_point(module_scope)