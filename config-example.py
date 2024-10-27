#!/usr/bin/env python3

from meshtastic.protobuf import portnums_pb2

### Bridge will not work on the default server - you must specify a private broker
BROKER = "mqtt.meshtastic.org"
PORT = 1883
USER = "meshdev"
PASSWORD = "large4cats"
TOPIC_1 = "msh/US/OR/BRIDGE/2/e/LongFast"
TOPIC_2 = "msh/US/OR/BRIDGE/2/e/MediumFast"
KEY = "AQ=="
FORWARDED_PORTNUMS = [
    portnums_pb2.TEXT_MESSAGE_APP, 
    portnums_pb2.NODEINFO_APP, 
    portnums_pb2.POSITION_APP, 
    portnums_pb2.ROUTING_APP
]