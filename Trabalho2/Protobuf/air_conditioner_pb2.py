# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: air_conditioner.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61ir_conditioner.proto\x12\x0bSmartOffice\"&\n\x15RequestAirConditioner\x12\r\n\x05Value\x18\x01 \x01(\x02\"(\n\x16ResponseAirConditioner\x12\x0e\n\x06status\x18\x01 \x01(\x05\x32\x9b\x02\n\x0e\x41irConditioner\x12Y\n\x0cOnOffAirCond\x12\".SmartOffice.RequestAirConditioner\x1a#.SmartOffice.ResponseAirConditioner\"\x00\x12V\n\tUpperTemp\x12\".SmartOffice.RequestAirConditioner\x1a#.SmartOffice.ResponseAirConditioner\"\x00\x12V\n\tLowerTemp\x12\".SmartOffice.RequestAirConditioner\x1a#.SmartOffice.ResponseAirConditioner\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'air_conditioner_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUESTAIRCONDITIONER._serialized_start=38
  _REQUESTAIRCONDITIONER._serialized_end=76
  _RESPONSEAIRCONDITIONER._serialized_start=78
  _RESPONSEAIRCONDITIONER._serialized_end=118
  _AIRCONDITIONER._serialized_start=121
  _AIRCONDITIONER._serialized_end=404
# @@protoc_insertion_point(module_scope)