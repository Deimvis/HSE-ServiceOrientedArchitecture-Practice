# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mafia.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmafia.proto\x1a\x1bgoogle/protobuf/empty.proto\"F\n\x11\x44isconnectRequest\x12\x13\n\x04User\x18\x01 \x01(\x0b\x32\x05.User\x12\x1c\n\x06RoomId\x18\x02 \x01(\x0b\x32\x0c.Room.RoomId\">\n\x0bVoteRequest\x12\x13\n\x04User\x18\x01 \x01(\x0b\x32\x05.User\x12\x1a\n\x0bSuspectUser\x18\x02 \x01(\x0b\x32\x05.User\"A\n\rExposeRequest\x12\x13\n\x04User\x18\x01 \x01(\x0b\x32\x05.User\x12\x1b\n\x0cUserToExpose\x18\x02 \x01(\x0b\x32\x05.User\"\x18\n\x04User\x12\x10\n\x08Username\x18\x01 \x01(\t\"\xfa\x02\n\x06Player\x12\x10\n\x08Username\x18\x01 \x01(\t\x12 \n\x04Role\x18\x02 \x01(\x0e\x32\x12.Player.PlayerRole\x12$\n\x06Status\x18\x03 \x01(\x0e\x32\x14.Player.PlayerStatus\x12\x12\n\x05\x43olor\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x0f\n\x07\x45xposed\x18\x05 \x01(\x08\"K\n\nPlayerRole\x12\x0e\n\nPR_UNKNOWN\x10\x00\x12\x0f\n\x0bPR_CIVILIAN\x10\x01\x12\x0c\n\x08PR_MAFIA\x10\x02\x12\x0e\n\nPR_SHERIFF\x10\x03\"9\n\x0cPlayerStatus\x12\x0e\n\nPS_UNKNOWN\x10\x00\x12\x0c\n\x08PS_ALIVE\x10\x01\x12\x0b\n\x07PS_DEAD\x10\x02\"_\n\x12PlayerExposeStatus\x12\x0f\n\x0bPES_UNKNOWN\x10\x00\x12\x1b\n\x17PES_EXPOSED_TO_SHERIFFS\x10\x01\x12\x1b\n\x17PES_EXPOSED_TO_EVERYONE\x10\x02\x42\x08\n\x06_Color\"\x1d\n\tSpectator\x12\x10\n\x08Username\x18\x01 \x01(\t\"X\n\x04\x43hat\x12\x1f\n\x08Messages\x18\x01 \x03(\x0b\x32\r.Chat.Message\x1a/\n\x07Message\x12\x16\n\x0e\x41uthorUsername\x18\x01 \x01(\t\x12\x0c\n\x04Text\x18\x02 \x01(\t\"[\n\x06Voting\x12\x1b\n\x05Votes\x18\x01 \x03(\x0b\x32\x0c.Voting.Vote\x1a\x34\n\x04Vote\x12\x17\n\x0fSuspectUsername\x18\x01 \x01(\t\x12\x13\n\x0bVotesNumber\x18\x02 \x01(\x03\"T\n\x08\x45ventBus\x12\x1f\n\x06\x45vents\x18\x01 \x03(\x0b\x32\x0f.EventBus.Event\x1a\'\n\x05\x45vent\x12\r\n\x05Index\x18\x01 \x01(\x03\x12\x0f\n\x07Message\x18\x02 \x01(\t\"\xc7\x03\n\x04Room\x12\x18\n\x02Id\x18\x01 \x01(\x0b\x32\x0c.Room.RoomId\x12 \n\x06Status\x18\x02 \x01(\x0e\x32\x10.Room.RoomStatus\x12\x1d\n\tGameRules\x18\x03 \x01(\x0b\x32\n.GameRules\x12\x18\n\x07Players\x18\x04 \x03(\x0b\x32\x07.Player\x12\x1e\n\nSpectators\x18\x05 \x03(\x0b\x32\n.Spectator\x12\x18\n\x04\x43hat\x18\x06 \x01(\x0b\x32\x05.ChatH\x00\x88\x01\x01\x12\x1c\n\x06Voting\x18\x07 \x01(\x0b\x32\x07.VotingH\x01\x88\x01\x01\x12 \n\x08\x45ventBus\x18\x08 \x01(\x0b\x32\t.EventBusH\x02\x88\x01\x01\x12\x11\n\tDayNumber\x18\t \x01(\x03\x1a\x17\n\x06RoomId\x12\r\n\x05Value\x18\x01 \x01(\t\"\x82\x01\n\nRoomStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x17\n\x13WAITING_FOR_PLAYERS\x10\x01\x12\x0e\n\nCHAT_PHASE\x10\x02\x12\x0e\n\nVOTE_PHASE\x10\x03\x12\x0f\n\x0bNIGHT_PHASE\x10\x04\x12\r\n\tMAFIA_WON\x10\x05\x12\x0e\n\nMAFIA_LOST\x10\x06\x42\x07\n\x05_ChatB\t\n\x07_VotingB\x0b\n\t_EventBus\"T\n\tGameRules\x12\x1b\n\x13\x41\x63tivePlayersNumber\x18\x01 \x01(\x03\x12\x13\n\x0bMafiaNumber\x18\x02 \x01(\x03\x12\x15\n\rSheriffNumber\x18\x03 \x01(\x03\x32\x9c\x03\n\x0b\x43oordinator\x12\x1b\n\x07\x43onnect\x12\x05.User\x1a\x05.Room\"\x00\x30\x01\x12:\n\nDisconnect\x12\x12.DisconnectRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x36\n\x0bSendMessage\x12\r.Chat.Message\x1a\x16.google.protobuf.Empty\"\x00\x12,\n\tBeginVote\x12\x05.User\x1a\x16.google.protobuf.Empty\"\x00\x12.\n\x04Vote\x12\x0c.VoteRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x33\n\tMafiaVote\x12\x0c.VoteRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x35\n\x0bSheriffVote\x12\x0c.VoteRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x32\n\x06\x45xpose\x12\x0e.ExposeRequest\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mafia_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DISCONNECTREQUEST._serialized_start=44
  _DISCONNECTREQUEST._serialized_end=114
  _VOTEREQUEST._serialized_start=116
  _VOTEREQUEST._serialized_end=178
  _EXPOSEREQUEST._serialized_start=180
  _EXPOSEREQUEST._serialized_end=245
  _USER._serialized_start=247
  _USER._serialized_end=271
  _PLAYER._serialized_start=274
  _PLAYER._serialized_end=652
  _PLAYER_PLAYERROLE._serialized_start=411
  _PLAYER_PLAYERROLE._serialized_end=486
  _PLAYER_PLAYERSTATUS._serialized_start=488
  _PLAYER_PLAYERSTATUS._serialized_end=545
  _PLAYER_PLAYEREXPOSESTATUS._serialized_start=547
  _PLAYER_PLAYEREXPOSESTATUS._serialized_end=642
  _SPECTATOR._serialized_start=654
  _SPECTATOR._serialized_end=683
  _CHAT._serialized_start=685
  _CHAT._serialized_end=773
  _CHAT_MESSAGE._serialized_start=726
  _CHAT_MESSAGE._serialized_end=773
  _VOTING._serialized_start=775
  _VOTING._serialized_end=866
  _VOTING_VOTE._serialized_start=814
  _VOTING_VOTE._serialized_end=866
  _EVENTBUS._serialized_start=868
  _EVENTBUS._serialized_end=952
  _EVENTBUS_EVENT._serialized_start=913
  _EVENTBUS_EVENT._serialized_end=952
  _ROOM._serialized_start=955
  _ROOM._serialized_end=1410
  _ROOM_ROOMID._serialized_start=1221
  _ROOM_ROOMID._serialized_end=1244
  _ROOM_ROOMSTATUS._serialized_start=1247
  _ROOM_ROOMSTATUS._serialized_end=1377
  _GAMERULES._serialized_start=1412
  _GAMERULES._serialized_end=1496
  _COORDINATOR._serialized_start=1499
  _COORDINATOR._serialized_end=1911
# @@protoc_insertion_point(module_scope)
