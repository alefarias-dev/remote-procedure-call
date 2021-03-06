# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='server.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0cserver.proto\"\x06\n\x04void\"\x17\n\x04\x42ool\x12\x0f\n\x07\x62oolean\x18\x01 \x01(\x08\"\x14\n\x05\x46loat\x12\x0b\n\x03num\x18\x01 \x01(\x02\"\x1a\n\x07Integer\x12\x0f\n\x07integer\x18\x01 \x01(\x05\"\x19\n\x04Long\x12\x11\n\tlongValue\x18\x01 \x01(\x03\"\x16\n\x06String\x12\x0c\n\x04text\x18\x01 \x01(\t\"3\n\x06Object\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\x12\x0e\n\x06weight\x18\x03 \x01(\x02\"\x1c\n\x0bStringArray\x12\r\n\x05texts\x18\x01 \x03(\t\"\x1b\n\x08IntArray\x12\x0f\n\x07numbers\x18\x01 \x03(\x05\"\x1d\n\nFloatArray\x12\x0f\n\x07numbers\x18\x01 \x03(\x02\"0\n\x10\x45uclidianVectors\x12\x1c\n\x07vectors\x18\x01 \x03(\x0b\x32\x0b.FloatArray2\xf4\x02\n\x06Server\x12\x1e\n\x0cvoidFunction\x12\x05.void\x1a\x05.void\"\x00\x12\x1e\n\x0c\x62oolFunction\x12\x05.Bool\x1a\x05.Bool\"\x00\x12\x1e\n\x06intArg\x12\x08.Integer\x1a\x08.Integer\"\x00\x12\x19\n\x07longArg\x12\x05.Long\x1a\x05.Long\"\x00\x12\x1f\n\tstringArg\x12\x07.String\x1a\x07.String\"\x00\x12\x1f\n\tobjectArg\x12\x07.Object\x1a\x07.Object\"\x00\x12-\n\rstringListArg\x12\x0c.StringArray\x1a\x0c.StringArray\"\x00\x12\"\n\x08intArray\x12\t.IntArray\x1a\t.IntArray\"\x00\x12(\n\nfloatArray\x12\x0b.FloatArray\x1a\x0b.FloatArray\"\x00\x12\x30\n\x11\x65uclideanDistance\x12\x11.EuclidianVectors\x1a\x06.Float\"\x00\x62\x06proto3')
)




_VOID = _descriptor.Descriptor(
  name='void',
  full_name='void',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=16,
  serialized_end=22,
)


_BOOL = _descriptor.Descriptor(
  name='Bool',
  full_name='Bool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boolean', full_name='Bool.boolean', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=24,
  serialized_end=47,
)


_FLOAT = _descriptor.Descriptor(
  name='Float',
  full_name='Float',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='Float.num', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=49,
  serialized_end=69,
)


_INTEGER = _descriptor.Descriptor(
  name='Integer',
  full_name='Integer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='integer', full_name='Integer.integer', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=71,
  serialized_end=97,
)


_LONG = _descriptor.Descriptor(
  name='Long',
  full_name='Long',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='longValue', full_name='Long.longValue', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=99,
  serialized_end=124,
)


_STRING = _descriptor.Descriptor(
  name='String',
  full_name='String',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='String.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=126,
  serialized_end=148,
)


_OBJECT = _descriptor.Descriptor(
  name='Object',
  full_name='Object',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Object.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age', full_name='Object.age', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='Object.weight', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=150,
  serialized_end=201,
)


_STRINGARRAY = _descriptor.Descriptor(
  name='StringArray',
  full_name='StringArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='texts', full_name='StringArray.texts', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=203,
  serialized_end=231,
)


_INTARRAY = _descriptor.Descriptor(
  name='IntArray',
  full_name='IntArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='numbers', full_name='IntArray.numbers', index=0,
      number=1, type=5, cpp_type=1, label=3,
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
  serialized_start=233,
  serialized_end=260,
)


_FLOATARRAY = _descriptor.Descriptor(
  name='FloatArray',
  full_name='FloatArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='numbers', full_name='FloatArray.numbers', index=0,
      number=1, type=2, cpp_type=6, label=3,
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
  serialized_start=262,
  serialized_end=291,
)


_EUCLIDIANVECTORS = _descriptor.Descriptor(
  name='EuclidianVectors',
  full_name='EuclidianVectors',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vectors', full_name='EuclidianVectors.vectors', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=293,
  serialized_end=341,
)

_EUCLIDIANVECTORS.fields_by_name['vectors'].message_type = _FLOATARRAY
DESCRIPTOR.message_types_by_name['void'] = _VOID
DESCRIPTOR.message_types_by_name['Bool'] = _BOOL
DESCRIPTOR.message_types_by_name['Float'] = _FLOAT
DESCRIPTOR.message_types_by_name['Integer'] = _INTEGER
DESCRIPTOR.message_types_by_name['Long'] = _LONG
DESCRIPTOR.message_types_by_name['String'] = _STRING
DESCRIPTOR.message_types_by_name['Object'] = _OBJECT
DESCRIPTOR.message_types_by_name['StringArray'] = _STRINGARRAY
DESCRIPTOR.message_types_by_name['IntArray'] = _INTARRAY
DESCRIPTOR.message_types_by_name['FloatArray'] = _FLOATARRAY
DESCRIPTOR.message_types_by_name['EuclidianVectors'] = _EUCLIDIANVECTORS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

void = _reflection.GeneratedProtocolMessageType('void', (_message.Message,), dict(
  DESCRIPTOR = _VOID,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:void)
  ))
_sym_db.RegisterMessage(void)

Bool = _reflection.GeneratedProtocolMessageType('Bool', (_message.Message,), dict(
  DESCRIPTOR = _BOOL,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:Bool)
  ))
_sym_db.RegisterMessage(Bool)

Float = _reflection.GeneratedProtocolMessageType('Float', (_message.Message,), dict(
  DESCRIPTOR = _FLOAT,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:Float)
  ))
_sym_db.RegisterMessage(Float)

Integer = _reflection.GeneratedProtocolMessageType('Integer', (_message.Message,), dict(
  DESCRIPTOR = _INTEGER,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:Integer)
  ))
_sym_db.RegisterMessage(Integer)

Long = _reflection.GeneratedProtocolMessageType('Long', (_message.Message,), dict(
  DESCRIPTOR = _LONG,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:Long)
  ))
_sym_db.RegisterMessage(Long)

String = _reflection.GeneratedProtocolMessageType('String', (_message.Message,), dict(
  DESCRIPTOR = _STRING,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:String)
  ))
_sym_db.RegisterMessage(String)

Object = _reflection.GeneratedProtocolMessageType('Object', (_message.Message,), dict(
  DESCRIPTOR = _OBJECT,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:Object)
  ))
_sym_db.RegisterMessage(Object)

StringArray = _reflection.GeneratedProtocolMessageType('StringArray', (_message.Message,), dict(
  DESCRIPTOR = _STRINGARRAY,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:StringArray)
  ))
_sym_db.RegisterMessage(StringArray)

IntArray = _reflection.GeneratedProtocolMessageType('IntArray', (_message.Message,), dict(
  DESCRIPTOR = _INTARRAY,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:IntArray)
  ))
_sym_db.RegisterMessage(IntArray)

FloatArray = _reflection.GeneratedProtocolMessageType('FloatArray', (_message.Message,), dict(
  DESCRIPTOR = _FLOATARRAY,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:FloatArray)
  ))
_sym_db.RegisterMessage(FloatArray)

EuclidianVectors = _reflection.GeneratedProtocolMessageType('EuclidianVectors', (_message.Message,), dict(
  DESCRIPTOR = _EUCLIDIANVECTORS,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:EuclidianVectors)
  ))
_sym_db.RegisterMessage(EuclidianVectors)



_SERVER = _descriptor.ServiceDescriptor(
  name='Server',
  full_name='Server',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=344,
  serialized_end=716,
  methods=[
  _descriptor.MethodDescriptor(
    name='voidFunction',
    full_name='Server.voidFunction',
    index=0,
    containing_service=None,
    input_type=_VOID,
    output_type=_VOID,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='boolFunction',
    full_name='Server.boolFunction',
    index=1,
    containing_service=None,
    input_type=_BOOL,
    output_type=_BOOL,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='intArg',
    full_name='Server.intArg',
    index=2,
    containing_service=None,
    input_type=_INTEGER,
    output_type=_INTEGER,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='longArg',
    full_name='Server.longArg',
    index=3,
    containing_service=None,
    input_type=_LONG,
    output_type=_LONG,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='stringArg',
    full_name='Server.stringArg',
    index=4,
    containing_service=None,
    input_type=_STRING,
    output_type=_STRING,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='objectArg',
    full_name='Server.objectArg',
    index=5,
    containing_service=None,
    input_type=_OBJECT,
    output_type=_OBJECT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='stringListArg',
    full_name='Server.stringListArg',
    index=6,
    containing_service=None,
    input_type=_STRINGARRAY,
    output_type=_STRINGARRAY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='intArray',
    full_name='Server.intArray',
    index=7,
    containing_service=None,
    input_type=_INTARRAY,
    output_type=_INTARRAY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='floatArray',
    full_name='Server.floatArray',
    index=8,
    containing_service=None,
    input_type=_FLOATARRAY,
    output_type=_FLOATARRAY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='euclideanDistance',
    full_name='Server.euclideanDistance',
    index=9,
    containing_service=None,
    input_type=_EUCLIDIANVECTORS,
    output_type=_FLOAT,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVER)

DESCRIPTOR.services_by_name['Server'] = _SERVER

# @@protoc_insertion_point(module_scope)
