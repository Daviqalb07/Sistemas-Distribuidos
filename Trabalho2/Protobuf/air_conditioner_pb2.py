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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61ir_conditioner.proto\x12\x0bSmartOffice\"\x17\n\x15RequestAirConditioner\"Y\n\x16ResponseAirConditioner\x12\x0c\n\x04tipo\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\x08\x12\x13\n\x0btemperature\x18\x04 \x01(\x05\"0\n\x1eResponseOnOffTemperatureSensor\x12\x0e\n\x06status\x18\x01 \x01(\x08\x32\xe5\x03\n\x0e\x41irConditioner\x12Y\n\x0cOnOffAirCond\x12\".SmartOffice.RequestAirConditioner\x1a#.SmartOffice.ResponseAirConditioner\"\x00\x12V\n\tUpperTemp\x12\".SmartOffice.RequestAirConditioner\x1a#.SmartOffice.ResponseAirConditioner\"\x00\x12V\n\tLowerTemp\x12\".SmartOffice.RequestAirConditioner\x1a#.SmartOffice.ResponseAirConditioner\"\x00\x12[\n\x0eGetAirCondInfo\x12\".SmartOffice.RequestAirConditioner\x1a#.SmartOffice.ResponseAirConditioner\"\x00\x12k\n\x16OnOffTemperatureSensor\x12\".SmartOffice.RequestAirConditioner\x1a+.SmartOffice.ResponseOnOffTemperatureSensor\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'air_conditioner_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUESTAIRCONDITIONER._serialized_start=38
  _REQUESTAIRCONDITIONER._serialized_end=61
  _RESPONSEAIRCONDITIONER._serialized_start=63
  _RESPONSEAIRCONDITIONER._serialized_end=152
  _RESPONSEONOFFTEMPERATURESENSOR._serialized_start=154
  _RESPONSEONOFFTEMPERATURESENSOR._serialized_end=202
  _AIRCONDITIONER._serialized_start=205
  _AIRCONDITIONER._serialized_end=690
# @@protoc_insertion_point(module_scope)
