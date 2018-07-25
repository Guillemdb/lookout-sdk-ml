# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service_analyzer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .github.com.gogo.protobuf.gogoproto import gogo_pb2 as github_dot_com_dot_gogo_dot_protobuf_dot_gogoproto_dot_gogo__pb2
from . import event_pb2 as event__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='service_analyzer.proto',
  package='pb',
  syntax='proto3',
  serialized_pb=_b('\n\x16service_analyzer.proto\x12\x02pb\x1a-github.com/gogo/protobuf/gogoproto/gogo.proto\x1a\x0b\x65vent.proto\"H\n\rEventResponse\x12\x18\n\x10\x61nalyzer_version\x18\x01 \x01(\t\x12\x1d\n\x08\x63omments\x18\x02 \x03(\x0b\x32\x0b.pb.Comment\"G\n\x07\x43omment\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t\x12\x0c\n\x04line\x18\x02 \x01(\x05\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x12\n\nconfidence\x18\x04 \x01(\r2x\n\x08\x41nalyzer\x12\x37\n\x11NotifyReviewEvent\x12\x0f.pb.ReviewEvent\x1a\x11.pb.EventResponse\x12\x33\n\x0fNotifyPushEvent\x12\r.pb.PushEvent\x1a\x11.pb.EventResponseB\x04\xc8\xe1\x1e\x00\x62\x06proto3')
  ,
  dependencies=[github_dot_com_dot_gogo_dot_protobuf_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,event__pb2.DESCRIPTOR,])




_EVENTRESPONSE = _descriptor.Descriptor(
  name='EventResponse',
  full_name='pb.EventResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='analyzer_version', full_name='pb.EventResponse.analyzer_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comments', full_name='pb.EventResponse.comments', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=162,
)


_COMMENT = _descriptor.Descriptor(
  name='Comment',
  full_name='pb.Comment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='pb.Comment.file', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='line', full_name='pb.Comment.line', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='pb.Comment.text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='pb.Comment.confidence', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=235,
)

_EVENTRESPONSE.fields_by_name['comments'].message_type = _COMMENT
DESCRIPTOR.message_types_by_name['EventResponse'] = _EVENTRESPONSE
DESCRIPTOR.message_types_by_name['Comment'] = _COMMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventResponse = _reflection.GeneratedProtocolMessageType('EventResponse', (_message.Message,), dict(
  DESCRIPTOR = _EVENTRESPONSE,
  __module__ = 'service_analyzer_pb2'
  # @@protoc_insertion_point(class_scope:pb.EventResponse)
  ))
_sym_db.RegisterMessage(EventResponse)

Comment = _reflection.GeneratedProtocolMessageType('Comment', (_message.Message,), dict(
  DESCRIPTOR = _COMMENT,
  __module__ = 'service_analyzer_pb2'
  # @@protoc_insertion_point(class_scope:pb.Comment)
  ))
_sym_db.RegisterMessage(Comment)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\310\341\036\000'))

_ANALYZER = _descriptor.ServiceDescriptor(
  name='Analyzer',
  full_name='pb.Analyzer',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=237,
  serialized_end=357,
  methods=[
  _descriptor.MethodDescriptor(
    name='NotifyReviewEvent',
    full_name='pb.Analyzer.NotifyReviewEvent',
    index=0,
    containing_service=None,
    input_type=event__pb2._REVIEWEVENT,
    output_type=_EVENTRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='NotifyPushEvent',
    full_name='pb.Analyzer.NotifyPushEvent',
    index=1,
    containing_service=None,
    input_type=event__pb2._PUSHEVENT,
    output_type=_EVENTRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ANALYZER)

DESCRIPTOR.services_by_name['Analyzer'] = _ANALYZER

# @@protoc_insertion_point(module_scope)
