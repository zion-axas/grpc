# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: my.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08my.proto\x12\tmypackage\"\x15\n\x07SubData\x12\n\n\x02id\x18\x01 \x01(\x05\"M\n\x03Req\x12\x0f\n\x07\x63ounter\x18\x01 \x01(\x05\x12\x10\n\x08products\x18\x02 \x03(\t\x12#\n\x07subdata\x18\x03 \x01(\x0b\x32\x12.mypackage.SubData\"\x15\n\x03Res\x12\x0e\n\x06\x61nswer\x18\x01 \x01(\t2\x96\x01\n\x05MySrv\x12(\n\x04Send\x12\x0e.mypackage.Req\x1a\x0e.mypackage.Res\"\x00\x12\x30\n\nSendStream\x12\x0e.mypackage.Req\x1a\x0e.mypackage.Res\"\x00\x30\x01\x12\x31\n\tGetStream\x12\x0e.mypackage.Req\x1a\x0e.mypackage.Res\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'my_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SUBDATA']._serialized_start=23
  _globals['_SUBDATA']._serialized_end=44
  _globals['_REQ']._serialized_start=46
  _globals['_REQ']._serialized_end=123
  _globals['_RES']._serialized_start=125
  _globals['_RES']._serialized_end=146
  _globals['_MYSRV']._serialized_start=149
  _globals['_MYSRV']._serialized_end=299
# @@protoc_insertion_point(module_scope)
