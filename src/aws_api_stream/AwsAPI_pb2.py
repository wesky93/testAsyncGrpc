# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AwsAPI.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='AwsAPI.proto',
  package='AwsAPI',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0c\x41wsAPI.proto\x12\x06\x41wsAPI\"#\n\x11GetObjectsRequest\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\t\")\n\x0bObjectReply\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t2F\n\x02S3\x12@\n\nGetObjects\x12\x19.AwsAPI.GetObjectsRequest\x1a\x13.AwsAPI.ObjectReply\"\x00\x30\x01\x62\x06proto3'
)




_GETOBJECTSREQUEST = _descriptor.Descriptor(
  name='GetObjectsRequest',
  full_name='AwsAPI.GetObjectsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bucket', full_name='AwsAPI.GetObjectsRequest.bucket', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=24,
  serialized_end=59,
)


_OBJECTREPLY = _descriptor.Descriptor(
  name='ObjectReply',
  full_name='AwsAPI.ObjectReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='AwsAPI.ObjectReply.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='etag', full_name='AwsAPI.ObjectReply.etag', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=61,
  serialized_end=102,
)

DESCRIPTOR.message_types_by_name['GetObjectsRequest'] = _GETOBJECTSREQUEST
DESCRIPTOR.message_types_by_name['ObjectReply'] = _OBJECTREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetObjectsRequest = _reflection.GeneratedProtocolMessageType('GetObjectsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETOBJECTSREQUEST,
  '__module__' : 'AwsAPI_pb2'
  # @@protoc_insertion_point(class_scope:AwsAPI.GetObjectsRequest)
  })
_sym_db.RegisterMessage(GetObjectsRequest)

ObjectReply = _reflection.GeneratedProtocolMessageType('ObjectReply', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTREPLY,
  '__module__' : 'AwsAPI_pb2'
  # @@protoc_insertion_point(class_scope:AwsAPI.ObjectReply)
  })
_sym_db.RegisterMessage(ObjectReply)



_S3 = _descriptor.ServiceDescriptor(
  name='S3',
  full_name='AwsAPI.S3',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=104,
  serialized_end=174,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetObjects',
    full_name='AwsAPI.S3.GetObjects',
    index=0,
    containing_service=None,
    input_type=_GETOBJECTSREQUEST,
    output_type=_OBJECTREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_S3)

DESCRIPTOR.services_by_name['S3'] = _S3

# @@protoc_insertion_point(module_scope)