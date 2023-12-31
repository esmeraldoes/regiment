# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prayer_tracker.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14prayer_tracker.proto\x12\rprayertracker\"%\n\x12StartPrayerRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"&\n\x13StartPrayerResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"#\n\x10\x45ndPrayerRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"$\n\x11\x45ndPrayerResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\" \n\rPrayerRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"!\n\x0ePrayerResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"D\n\x14PrayerUpdateResponse\x12\x16\n\x0evoice_detected\x18\x01 \x01(\x08\x12\x14\n\x0cprayer_ended\x18\x02 \x01(\x08\":\n\x13ProcessVoiceRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x12\n\naudio_data\x18\x02 \x01(\x0c\"*\n\x14ProcessVoiceResponse\x12\x12\n\ntranscript\x18\x01 \x01(\t2\xfb\x02\n\x14PrayerTrackerService\x12V\n\x0bStartPrayer\x12!.prayertracker.StartPrayerRequest\x1a\".prayertracker.StartPrayerResponse\"\x00\x12P\n\tEndPrayer\x12\x1f.prayertracker.EndPrayerRequest\x1a .prayertracker.EndPrayerResponse\"\x00\x12V\n\rPrayerUpdates\x12\x1c.prayertracker.PrayerRequest\x1a#.prayertracker.PrayerUpdateResponse\"\x00\x30\x01\x12\x61\n\x12ProcessVoiceStream\x12\".prayertracker.ProcessVoiceRequest\x1a#.prayertracker.ProcessVoiceResponse(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'prayer_tracker_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_STARTPRAYERREQUEST']._serialized_start=39
  _globals['_STARTPRAYERREQUEST']._serialized_end=76
  _globals['_STARTPRAYERRESPONSE']._serialized_start=78
  _globals['_STARTPRAYERRESPONSE']._serialized_end=116
  _globals['_ENDPRAYERREQUEST']._serialized_start=118
  _globals['_ENDPRAYERREQUEST']._serialized_end=153
  _globals['_ENDPRAYERRESPONSE']._serialized_start=155
  _globals['_ENDPRAYERRESPONSE']._serialized_end=191
  _globals['_PRAYERREQUEST']._serialized_start=193
  _globals['_PRAYERREQUEST']._serialized_end=225
  _globals['_PRAYERRESPONSE']._serialized_start=227
  _globals['_PRAYERRESPONSE']._serialized_end=260
  _globals['_PRAYERUPDATERESPONSE']._serialized_start=262
  _globals['_PRAYERUPDATERESPONSE']._serialized_end=330
  _globals['_PROCESSVOICEREQUEST']._serialized_start=332
  _globals['_PROCESSVOICEREQUEST']._serialized_end=390
  _globals['_PROCESSVOICERESPONSE']._serialized_start=392
  _globals['_PROCESSVOICERESPONSE']._serialized_end=434
  _globals['_PRAYERTRACKERSERVICE']._serialized_start=437
  _globals['_PRAYERTRACKERSERVICE']._serialized_end=816
# @@protoc_insertion_point(module_scope)
