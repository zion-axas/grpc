# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/my.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eproto/my.proto\x12\tmypackage\"\x15\n\x07SubData\x12\n\n\x02id\x18\x01 \x01(\x05\"M\n\x03Req\x12\x0f\n\x07\x63ounter\x18\x01 \x01(\x05\x12\x10\n\x08products\x18\x02 \x03(\t\x12#\n\x07subdata\x18\x03 \x01(\x0b\x32\x12.mypackage.SubData\"\x15\n\x03Res\x12\x0e\n\x06\x61nswer\x18\x01 \x01(\t\"\xd2\x01\n\x07MapType\x12\x32\n\x08projects\x18\x01 \x03(\x0b\x32 .mypackage.MapType.ProjectsEntry\x12\x1f\n\x05medal\x18\x02 \x01(\x0e\x32\x10.mypackage.Medal\x12\x0f\n\x05smart\x18\x03 \x01(\tH\x00\x12\x10\n\x06\x62\x65\x61uty\x18\x04 \x01(\tH\x00\x1a/\n\rProjectsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x42\x0c\n\ntest_oneofJ\x04\x08\x07\x10\x08J\x04\x08\x08\x10\tJ\x04\x08\t\x10\x0c*3\n\x05Medal\x12\x08\n\x04zero\x10\x00\x12\x08\n\x04gold\x10\x01\x12\n\n\x06silver\x10\x02\x12\n\n\x06\x62ronze\x10\x03\x32\x96\x01\n\x05MySrv\x12(\n\x04Send\x12\x0e.mypackage.Req\x1a\x0e.mypackage.Res\"\x00\x12\x30\n\nSendStream\x12\x0e.mypackage.Req\x1a\x0e.mypackage.Res\"\x00\x30\x01\x12\x31\n\tGetStream\x12\x0e.mypackage.Req\x1a\x0e.mypackage.Res\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.my_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MAPTYPE_PROJECTSENTRY']._loaded_options = None
  _globals['_MAPTYPE_PROJECTSENTRY']._serialized_options = b'8\001'
  _globals['_MEDAL']._serialized_start=367
  _globals['_MEDAL']._serialized_end=418
  _globals['_SUBDATA']._serialized_start=29
  _globals['_SUBDATA']._serialized_end=50
  _globals['_REQ']._serialized_start=52
  _globals['_REQ']._serialized_end=129
  _globals['_RES']._serialized_start=131
  _globals['_RES']._serialized_end=152
  _globals['_MAPTYPE']._serialized_start=155
  _globals['_MAPTYPE']._serialized_end=365
  _globals['_MAPTYPE_PROJECTSENTRY']._serialized_start=286
  _globals['_MAPTYPE_PROJECTSENTRY']._serialized_end=333
  _globals['_MYSRV']._serialized_start=421
  _globals['_MYSRV']._serialized_end=571
# @@protoc_insertion_point(module_scope)
