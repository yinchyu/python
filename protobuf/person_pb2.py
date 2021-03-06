# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: person.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='person.proto',
  package='people',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cperson.proto\x12\x06people\"\xdc\x01\n\x06person\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\x12\x0b\n\x03sex\x18\x03 \x01(\t\x12\x10\n\x08idnumber\x18\x04 \x01(\t\x12)\n\x05phone\x18\x05 \x03(\x0b\x32\x1a.people.person.phonenumber\x1a\x41\n\x0bphonenumber\x12%\n\x04type\x18\x01 \x01(\x0e\x32\x17.people.person.phontype\x12\x0b\n\x03num\x18\x02 \x01(\t\"*\n\x08phontype\x12\n\n\x06mobile\x10\x00\x12\x08\n\x04home\x10\x01\x12\x08\n\x04work\x10\x02\",\n\x06people\x12\"\n\npeople\x18\x01 \x03(\x0b\x32\x0e.people.personb\x06proto3'
)


_PERSON_PHONTYPE = _descriptor.EnumDescriptor(
  name='phontype',
  full_name='people.person.phontype',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='mobile', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='home', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='work', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=203,
  serialized_end=245,
)
_sym_db.RegisterEnumDescriptor(_PERSON_PHONTYPE)


_PERSON_PHONENUMBER = _descriptor.Descriptor(
  name='phonenumber',
  full_name='people.person.phonenumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='people.person.phonenumber.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num', full_name='people.person.phonenumber.num', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=136,
  serialized_end=201,
)

_PERSON = _descriptor.Descriptor(
  name='person',
  full_name='people.person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='people.person.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='age', full_name='people.person.age', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sex', full_name='people.person.sex', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='idnumber', full_name='people.person.idnumber', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone', full_name='people.person.phone', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PERSON_PHONENUMBER, ],
  enum_types=[
    _PERSON_PHONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=245,
)


_PEOPLE = _descriptor.Descriptor(
  name='people',
  full_name='people.people',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='people', full_name='people.people.people', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=247,
  serialized_end=291,
)

_PERSON_PHONENUMBER.fields_by_name['type'].enum_type = _PERSON_PHONTYPE
_PERSON_PHONENUMBER.containing_type = _PERSON
_PERSON.fields_by_name['phone'].message_type = _PERSON_PHONENUMBER
_PERSON_PHONTYPE.containing_type = _PERSON
_PEOPLE.fields_by_name['people'].message_type = _PERSON
DESCRIPTOR.message_types_by_name['person'] = _PERSON
DESCRIPTOR.message_types_by_name['people'] = _PEOPLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

person = _reflection.GeneratedProtocolMessageType('person', (_message.Message,), {

  'phonenumber' : _reflection.GeneratedProtocolMessageType('phonenumber', (_message.Message,), {
    'DESCRIPTOR' : _PERSON_PHONENUMBER,
    '__module__' : 'person_pb2'
    # @@protoc_insertion_point(class_scope:people.person.phonenumber)
    })
  ,
  'DESCRIPTOR' : _PERSON,
  '__module__' : 'person_pb2'
  # @@protoc_insertion_point(class_scope:people.person)
  })
_sym_db.RegisterMessage(person)
_sym_db.RegisterMessage(person.phonenumber)

people = _reflection.GeneratedProtocolMessageType('people', (_message.Message,), {
  'DESCRIPTOR' : _PEOPLE,
  '__module__' : 'person_pb2'
  # @@protoc_insertion_point(class_scope:people.people)
  })
_sym_db.RegisterMessage(people)


# @@protoc_insertion_point(module_scope)
