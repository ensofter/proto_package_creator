# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qa_split_grpc_client/api/v1/split.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from github.com.envoyproxy.protoc_gen_validate.validate import validate_pb2 as github_dot_com_dot_envoyproxy_dot_protoc__gen__validate_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='qa_split_grpc_client/api/v1/split.proto',
  package='wms.go.service.batching.split.v1',
  syntax='proto3',
  serialized_options=b'Z3gitlab.ozon.ru/wms/go/service/batching/split/pkg/v1\222A\374\001\022\017\n\rWMS SPLIT APIR2\n\003400\022+\n)Returned when the request is not correct.ZR\n$\n\rx-o3-app-name\022\023\010\002\032\rx-o3-app-name \002\n*\n\020x-o3-app-version\022\026\010\002\032\020x-o3-app-version \002b)\n\021\n\rx-o3-app-name\022\000\n\024\n\020x-o3-app-version\022\000r6\n\017Confluence Page\022#https://confluence.ozon.ru/x/fEz8BQ',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'qa_split_grpc_client/api/v1/split.proto\x12 wms.go.service.batching.split.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x41github.com/envoyproxy/protoc-gen-validate/validate/validate.proto\"~\n\x1bPostingsSplitReasonsRequest\x12_\n\x16postings_split_reasons\x18\x01 \x03(\x0b\x32\x35.wms.go.service.batching.split.v1.PostingSplitReasonsB\x08\xfa\x42\x05\x92\x01\x02\x08\x01\"\x82\x01\n\x13PostingSplitReasons\x12\x1b\n\nposting_id\x18\x01 \x01(\x03\x42\x07\xfa\x42\x04\"\x02 \x00\x12N\n\rsplit_reasons\x18\x02 \x03(\x0e\x32-.wms.go.service.batching.split.v1.SplitReasonB\x08\xfa\x42\x05\x92\x01\x02\x08\x01\"z\n\x08Restrict\x12\x32\n\x05price\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x05price\x12:\n\tweight_gr\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\tweight_gr\"\xc8\x02\n\x04Item\x12\x18\n\x07item_id\x18\x01 \x01(\x03R\x07item_id\x12M\n\x13\x64\x65livery_variant_id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x13\x64\x65livery_variant_id\x12\x39\n\tseller_id\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\tseller_id\x12\x10\n\x03qty\x18\x04 \x01(\x05R\x03qty\x12\x1c\n\tweight_gr\x18\x05 \x01(\x01R\tweight_gr\x12\x1a\n\x08width_mm\x18\x06 \x01(\x03R\x08width_mm\x12\x1c\n\theight_mm\x18\x07 \x01(\x03R\theight_mm\x12\x1c\n\tlength_mm\x18\x08 \x01(\x03R\tlength_mm\x12\x14\n\x05price\x18\t \x01(\x01R\x05price\"N\n\nItemWhcomm\x12\x18\n\x07item_id\x18\x01 \x01(\x03R\x07item_id\x12\x10\n\x03qty\x18\x04 \x01(\x05R\x03qty\x12\x14\n\x05price\x18\t \x01(\x01R\x05price\"\x8e\x01\n\x0fSplitCollection\x12\x35\n\x05items\x18\x01 \x03(\x0b\x32&.wms.go.service.batching.split.v1.Item\x12\x44\n\rsplit_reasons\x18\x02 \x03(\x0e\x32-.wms.go.service.batching.split.v1.SplitReason\"\xb9\x02\n\x13SplitPostingRequest\x12\"\n\x0cwarehouse_id\x18\x01 \x01(\x03R\x0cwarehouse_id\x12.\n\x12virtual_posting_id\x18\x02 \x01(\x03R\x12virtual_posting_id\x12\x35\n\x05items\x18\x03 \x03(\x0b\x32&.wms.go.service.batching.split.v1.Item\x12<\n\x08restrict\x18\x04 \x01(\x0b\x32*.wms.go.service.batching.split.v1.Restrict\x12=\n\x19split_for_mono_prohibited\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x1a\n\x08is_legal\x18\x06 \x01(\x08R\x08is_legal\"Y\n\x14SplitPostingResponse\x12\x41\n\x06splits\x18\x01 \x03(\x0b\x32\x31.wms.go.service.batching.split.v1.SplitCollection\"\xe0\x02\n\x19SplitPostingWhCommRequest\x12\"\n\x0cwarehouse_id\x18\x01 \x01(\x03R\x0cwarehouse_id\x12M\n\x13\x64\x65livery_variant_id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x13\x64\x65livery_variant_id\x12\x39\n\tseller_id\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\tseller_id\x12;\n\x05items\x18\x04 \x03(\x0b\x32,.wms.go.service.batching.split.v1.ItemWhcomm\x12<\n\x08restrict\x18\x05 \x01(\x0b\x32*.wms.go.service.batching.split.v1.Restrict\x12\x1a\n\x08is_legal\x18\x06 \x01(\x08R\x08is_legal\"_\n\x1aSplitPostingWhCommResponse\x12\x41\n\x06splits\x18\x01 \x03(\x0b\x32\x31.wms.go.service.batching.split.v1.SplitCollection*\x9a\x01\n\x0bSplitReason\x12\x0f\n\x0bNotSplitted\x10\x00\x12\x1b\n\x17PhysicalCharacteristics\x10\x01\x12\x0c\n\x08ItemTags\x10\x02\x12\t\n\x05Price\x10\x03\x12\n\n\x06Weight\x10\x04\x12\n\n\x06Volume\x10\x05\x12\x16\n\x12SingleInstanceTags\x10\x06\x12\n\n\x06MaxQty\x10\x07\x12\x08\n\x04Mono\x10\x08\x32\xad\x06\n\x05Split\x12\xb6\x01\n\x0cSplitPosting\x12\x35.wms.go.service.batching.split.v1.SplitPostingRequest\x1a\x36.wms.go.service.batching.split.v1.SplitPostingResponse\"7\x82\xd3\xe4\x93\x02\x16\"\x11/v1/split-posting:\x01*\x92\x41\x18*\x16split-v1-split-posting\x12\xd5\x01\n\x12SplitPostingWhComm\x12;.wms.go.service.batching.split.v1.SplitPostingWhCommRequest\x1a<.wms.go.service.batching.split.v1.SplitPostingWhCommResponse\"D\x82\xd3\xe4\x93\x02\x1d\"\x18/v1/split-posting-whcomm:\x01*\x92\x41\x1e*\x1csplit-v1-split-posting-whcom\x12\xc3\x01\n\x17\x41\x64\x64PostingsSplitReasons\x12=.wms.go.service.batching.split.v1.PostingsSplitReasonsRequest\x1a\x16.google.protobuf.Empty\"Q\x82\xd3\xe4\x93\x02#\"\x1e/v1/split-postings-reasons/add:\x01*\x92\x41%*#split-v1-split-postings-reasons-add\x12\xcc\x01\n\x12SplitPostingByTags\x12\x35.wms.go.service.batching.split.v1.SplitPostingRequest\x1a\x36.wms.go.service.batching.split.v1.SplitPostingResponse\"G\x82\xd3\xe4\x93\x02\x1e\"\x19/v1/split-posting-by-tags:\x01*\x92\x41 *\x1esplit-v1-split-posting-by-tagsB\xb5\x02Z3gitlab.ozon.ru/wms/go/service/batching/split/pkg/v1\x92\x41\xfc\x01\x12\x0f\n\rWMS SPLIT APIR2\n\x03\x34\x30\x30\x12+\n)Returned when the request is not correct.ZR\n$\n\rx-o3-app-name\x12\x13\x08\x02\x1a\rx-o3-app-name \x02\n*\n\x10x-o3-app-version\x12\x16\x08\x02\x1a\x10x-o3-app-version \x02\x62)\n\x11\n\rx-o3-app-name\x12\x00\n\x14\n\x10x-o3-app-version\x12\x00r6\n\x0f\x43onfluence Page\x12#https://confluence.ozon.ru/x/fEz8BQb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,protoc__gen__openapiv2_dot_options_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,github_dot_com_dot_envoyproxy_dot_protoc__gen__validate_dot_validate_dot_validate__pb2.DESCRIPTOR,])

_SPLITREASON = _descriptor.EnumDescriptor(
  name='SplitReason',
  full_name='wms.go.service.batching.split.v1.SplitReason',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NotSplitted', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PhysicalCharacteristics', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ItemTags', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Price', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Weight', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Volume', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SingleInstanceTags', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MaxQty', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Mono', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2084,
  serialized_end=2238,
)
_sym_db.RegisterEnumDescriptor(_SPLITREASON)

SplitReason = enum_type_wrapper.EnumTypeWrapper(_SPLITREASON)
NotSplitted = 0
PhysicalCharacteristics = 1
ItemTags = 2
Price = 3
Weight = 4
Volume = 5
SingleInstanceTags = 6
MaxQty = 7
Mono = 8



_POSTINGSSPLITREASONSREQUEST = _descriptor.Descriptor(
  name='PostingsSplitReasonsRequest',
  full_name='wms.go.service.batching.split.v1.PostingsSplitReasonsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='postings_split_reasons', full_name='wms.go.service.batching.split.v1.PostingsSplitReasonsRequest.postings_split_reasons', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005\222\001\002\010\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=283,
  serialized_end=409,
)


_POSTINGSPLITREASONS = _descriptor.Descriptor(
  name='PostingSplitReasons',
  full_name='wms.go.service.batching.split.v1.PostingSplitReasons',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='posting_id', full_name='wms.go.service.batching.split.v1.PostingSplitReasons.posting_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004\"\002 \000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='split_reasons', full_name='wms.go.service.batching.split.v1.PostingSplitReasons.split_reasons', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005\222\001\002\010\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=412,
  serialized_end=542,
)


_RESTRICT = _descriptor.Descriptor(
  name='Restrict',
  full_name='wms.go.service.batching.split.v1.Restrict',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='price', full_name='wms.go.service.batching.split.v1.Restrict.price', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='price', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='weight_gr', full_name='wms.go.service.batching.split.v1.Restrict.weight_gr', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='weight_gr', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=544,
  serialized_end=666,
)


_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='wms.go.service.batching.split.v1.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='wms.go.service.batching.split.v1.Item.item_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='item_id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delivery_variant_id', full_name='wms.go.service.batching.split.v1.Item.delivery_variant_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='delivery_variant_id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seller_id', full_name='wms.go.service.batching.split.v1.Item.seller_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='seller_id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='qty', full_name='wms.go.service.batching.split.v1.Item.qty', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='qty', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='weight_gr', full_name='wms.go.service.batching.split.v1.Item.weight_gr', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='weight_gr', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width_mm', full_name='wms.go.service.batching.split.v1.Item.width_mm', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='width_mm', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height_mm', full_name='wms.go.service.batching.split.v1.Item.height_mm', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='height_mm', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length_mm', full_name='wms.go.service.batching.split.v1.Item.length_mm', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='length_mm', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='wms.go.service.batching.split.v1.Item.price', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='price', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=669,
  serialized_end=997,
)


_ITEMWHCOMM = _descriptor.Descriptor(
  name='ItemWhcomm',
  full_name='wms.go.service.batching.split.v1.ItemWhcomm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='wms.go.service.batching.split.v1.ItemWhcomm.item_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='item_id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='qty', full_name='wms.go.service.batching.split.v1.ItemWhcomm.qty', index=1,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='qty', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='wms.go.service.batching.split.v1.ItemWhcomm.price', index=2,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='price', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=999,
  serialized_end=1077,
)


_SPLITCOLLECTION = _descriptor.Descriptor(
  name='SplitCollection',
  full_name='wms.go.service.batching.split.v1.SplitCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='wms.go.service.batching.split.v1.SplitCollection.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='split_reasons', full_name='wms.go.service.batching.split.v1.SplitCollection.split_reasons', index=1,
      number=2, type=14, cpp_type=8, label=3,
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
  serialized_start=1080,
  serialized_end=1222,
)


_SPLITPOSTINGREQUEST = _descriptor.Descriptor(
  name='SplitPostingRequest',
  full_name='wms.go.service.batching.split.v1.SplitPostingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='warehouse_id', full_name='wms.go.service.batching.split.v1.SplitPostingRequest.warehouse_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='warehouse_id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='virtual_posting_id', full_name='wms.go.service.batching.split.v1.SplitPostingRequest.virtual_posting_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='virtual_posting_id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='items', full_name='wms.go.service.batching.split.v1.SplitPostingRequest.items', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='restrict', full_name='wms.go.service.batching.split.v1.SplitPostingRequest.restrict', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='split_for_mono_prohibited', full_name='wms.go.service.batching.split.v1.SplitPostingRequest.split_for_mono_prohibited', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_legal', full_name='wms.go.service.batching.split.v1.SplitPostingRequest.is_legal', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='is_legal', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1225,
  serialized_end=1538,
)


_SPLITPOSTINGRESPONSE = _descriptor.Descriptor(
  name='SplitPostingResponse',
  full_name='wms.go.service.batching.split.v1.SplitPostingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='splits', full_name='wms.go.service.batching.split.v1.SplitPostingResponse.splits', index=0,
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
  serialized_start=1540,
  serialized_end=1629,
)


_SPLITPOSTINGWHCOMMREQUEST = _descriptor.Descriptor(
  name='SplitPostingWhCommRequest',
  full_name='wms.go.service.batching.split.v1.SplitPostingWhCommRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='warehouse_id', full_name='wms.go.service.batching.split.v1.SplitPostingWhCommRequest.warehouse_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='warehouse_id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delivery_variant_id', full_name='wms.go.service.batching.split.v1.SplitPostingWhCommRequest.delivery_variant_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='delivery_variant_id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seller_id', full_name='wms.go.service.batching.split.v1.SplitPostingWhCommRequest.seller_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='seller_id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='items', full_name='wms.go.service.batching.split.v1.SplitPostingWhCommRequest.items', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='restrict', full_name='wms.go.service.batching.split.v1.SplitPostingWhCommRequest.restrict', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_legal', full_name='wms.go.service.batching.split.v1.SplitPostingWhCommRequest.is_legal', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='is_legal', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1632,
  serialized_end=1984,
)


_SPLITPOSTINGWHCOMMRESPONSE = _descriptor.Descriptor(
  name='SplitPostingWhCommResponse',
  full_name='wms.go.service.batching.split.v1.SplitPostingWhCommResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='splits', full_name='wms.go.service.batching.split.v1.SplitPostingWhCommResponse.splits', index=0,
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
  serialized_start=1986,
  serialized_end=2081,
)

_POSTINGSSPLITREASONSREQUEST.fields_by_name['postings_split_reasons'].message_type = _POSTINGSPLITREASONS
_POSTINGSPLITREASONS.fields_by_name['split_reasons'].enum_type = _SPLITREASON
_RESTRICT.fields_by_name['price'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_RESTRICT.fields_by_name['weight_gr'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_ITEM.fields_by_name['delivery_variant_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_ITEM.fields_by_name['seller_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_SPLITCOLLECTION.fields_by_name['items'].message_type = _ITEM
_SPLITCOLLECTION.fields_by_name['split_reasons'].enum_type = _SPLITREASON
_SPLITPOSTINGREQUEST.fields_by_name['items'].message_type = _ITEM
_SPLITPOSTINGREQUEST.fields_by_name['restrict'].message_type = _RESTRICT
_SPLITPOSTINGREQUEST.fields_by_name['split_for_mono_prohibited'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_SPLITPOSTINGRESPONSE.fields_by_name['splits'].message_type = _SPLITCOLLECTION
_SPLITPOSTINGWHCOMMREQUEST.fields_by_name['delivery_variant_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_SPLITPOSTINGWHCOMMREQUEST.fields_by_name['seller_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_SPLITPOSTINGWHCOMMREQUEST.fields_by_name['items'].message_type = _ITEMWHCOMM
_SPLITPOSTINGWHCOMMREQUEST.fields_by_name['restrict'].message_type = _RESTRICT
_SPLITPOSTINGWHCOMMRESPONSE.fields_by_name['splits'].message_type = _SPLITCOLLECTION
DESCRIPTOR.message_types_by_name['PostingsSplitReasonsRequest'] = _POSTINGSSPLITREASONSREQUEST
DESCRIPTOR.message_types_by_name['PostingSplitReasons'] = _POSTINGSPLITREASONS
DESCRIPTOR.message_types_by_name['Restrict'] = _RESTRICT
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['ItemWhcomm'] = _ITEMWHCOMM
DESCRIPTOR.message_types_by_name['SplitCollection'] = _SPLITCOLLECTION
DESCRIPTOR.message_types_by_name['SplitPostingRequest'] = _SPLITPOSTINGREQUEST
DESCRIPTOR.message_types_by_name['SplitPostingResponse'] = _SPLITPOSTINGRESPONSE
DESCRIPTOR.message_types_by_name['SplitPostingWhCommRequest'] = _SPLITPOSTINGWHCOMMREQUEST
DESCRIPTOR.message_types_by_name['SplitPostingWhCommResponse'] = _SPLITPOSTINGWHCOMMRESPONSE
DESCRIPTOR.enum_types_by_name['SplitReason'] = _SPLITREASON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PostingsSplitReasonsRequest = _reflection.GeneratedProtocolMessageType('PostingsSplitReasonsRequest', (_message.Message,), {
  'DESCRIPTOR' : _POSTINGSSPLITREASONSREQUEST,
  '__module__' : 'qa_split_grpc_client.api.v1.split_pb2'
  # @@protoc_insertion_point(class_scope:wms.go.service.batching.split.v1.PostingsSplitReasonsRequest)
  })
_sym_db.RegisterMessage(PostingsSplitReasonsRequest)

PostingSplitReasons = _reflection.GeneratedProtocolMessageType('PostingSplitReasons', (_message.Message,), {
  'DESCRIPTOR' : _POSTINGSPLITREASONS,
  '__module__' : 'qa_split_grpc_client.api.v1.split_pb2'
  # @@protoc_insertion_point(class_scope:wms.go.service.batching.split.v1.PostingSplitReasons)
  })
_sym_db.RegisterMessage(PostingSplitReasons)

Restrict = _reflection.GeneratedProtocolMessageType('Restrict', (_message.Message,), {
  'DESCRIPTOR' : _RESTRICT,
  '__module__' : 'qa_split_grpc_client.api.v1.split_pb2'
  # @@protoc_insertion_point(class_scope:wms.go.service.batching.split.v1.Restrict)
  })
_sym_db.RegisterMessage(Restrict)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
  'DESCRIPTOR' : _ITEM,
  '__module__' : 'qa_split_grpc_client.api.v1.split_pb2'
  # @@protoc_insertion_point(class_scope:wms.go.service.batching.split.v1.Item)
  })
_sym_db.RegisterMessage(Item)

ItemWhcomm = _reflection.GeneratedProtocolMessageType('ItemWhcomm', (_message.Message,), {
  'DESCRIPTOR' : _ITEMWHCOMM,
  '__module__' : 'qa_split_grpc_client.api.v1.split_pb2'
  # @@protoc_insertion_point(class_scope:wms.go.service.batching.split.v1.ItemWhcomm)
  })
_sym_db.RegisterMessage(ItemWhcomm)

SplitCollection = _reflection.GeneratedProtocolMessageType('SplitCollection', (_message.Message,), {
  'DESCRIPTOR' : _SPLITCOLLECTION,
  '__module__' : 'qa_split_grpc_client.api.v1.split_pb2'
  # @@protoc_insertion_point(class_scope:wms.go.service.batching.split.v1.SplitCollection)
  })
_sym_db.RegisterMessage(SplitCollection)

SplitPostingRequest = _reflection.GeneratedProtocolMessageType('SplitPostingRequest', (_message.Message,), {
  'DESCRIPTOR' : _SPLITPOSTINGREQUEST,
  '__module__' : 'qa_split_grpc_client.api.v1.split_pb2'
  # @@protoc_insertion_point(class_scope:wms.go.service.batching.split.v1.SplitPostingRequest)
  })
_sym_db.RegisterMessage(SplitPostingRequest)

SplitPostingResponse = _reflection.GeneratedProtocolMessageType('SplitPostingResponse', (_message.Message,), {
  'DESCRIPTOR' : _SPLITPOSTINGRESPONSE,
  '__module__' : 'qa_split_grpc_client.api.v1.split_pb2'
  # @@protoc_insertion_point(class_scope:wms.go.service.batching.split.v1.SplitPostingResponse)
  })
_sym_db.RegisterMessage(SplitPostingResponse)

SplitPostingWhCommRequest = _reflection.GeneratedProtocolMessageType('SplitPostingWhCommRequest', (_message.Message,), {
  'DESCRIPTOR' : _SPLITPOSTINGWHCOMMREQUEST,
  '__module__' : 'qa_split_grpc_client.api.v1.split_pb2'
  # @@protoc_insertion_point(class_scope:wms.go.service.batching.split.v1.SplitPostingWhCommRequest)
  })
_sym_db.RegisterMessage(SplitPostingWhCommRequest)

SplitPostingWhCommResponse = _reflection.GeneratedProtocolMessageType('SplitPostingWhCommResponse', (_message.Message,), {
  'DESCRIPTOR' : _SPLITPOSTINGWHCOMMRESPONSE,
  '__module__' : 'qa_split_grpc_client.api.v1.split_pb2'
  # @@protoc_insertion_point(class_scope:wms.go.service.batching.split.v1.SplitPostingWhCommResponse)
  })
_sym_db.RegisterMessage(SplitPostingWhCommResponse)


DESCRIPTOR._options = None
_POSTINGSSPLITREASONSREQUEST.fields_by_name['postings_split_reasons']._options = None
_POSTINGSPLITREASONS.fields_by_name['posting_id']._options = None
_POSTINGSPLITREASONS.fields_by_name['split_reasons']._options = None

_SPLIT = _descriptor.ServiceDescriptor(
  name='Split',
  full_name='wms.go.service.batching.split.v1.Split',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=2241,
  serialized_end=3054,
  methods=[
  _descriptor.MethodDescriptor(
    name='SplitPosting',
    full_name='wms.go.service.batching.split.v1.Split.SplitPosting',
    index=0,
    containing_service=None,
    input_type=_SPLITPOSTINGREQUEST,
    output_type=_SPLITPOSTINGRESPONSE,
    serialized_options=b'\202\323\344\223\002\026\"\021/v1/split-posting:\001*\222A\030*\026split-v1-split-posting',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SplitPostingWhComm',
    full_name='wms.go.service.batching.split.v1.Split.SplitPostingWhComm',
    index=1,
    containing_service=None,
    input_type=_SPLITPOSTINGWHCOMMREQUEST,
    output_type=_SPLITPOSTINGWHCOMMRESPONSE,
    serialized_options=b'\202\323\344\223\002\035\"\030/v1/split-posting-whcomm:\001*\222A\036*\034split-v1-split-posting-whcom',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddPostingsSplitReasons',
    full_name='wms.go.service.batching.split.v1.Split.AddPostingsSplitReasons',
    index=2,
    containing_service=None,
    input_type=_POSTINGSSPLITREASONSREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002#\"\036/v1/split-postings-reasons/add:\001*\222A%*#split-v1-split-postings-reasons-add',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SplitPostingByTags',
    full_name='wms.go.service.batching.split.v1.Split.SplitPostingByTags',
    index=3,
    containing_service=None,
    input_type=_SPLITPOSTINGREQUEST,
    output_type=_SPLITPOSTINGRESPONSE,
    serialized_options=b'\202\323\344\223\002\036\"\031/v1/split-posting-by-tags:\001*\222A *\036split-v1-split-posting-by-tags',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SPLIT)

DESCRIPTOR.services_by_name['Split'] = _SPLIT

# @@protoc_insertion_point(module_scope)
