#! /usr/bin/python2.7
import socket

MYPORT = 8123
MYGROUP_4 = '225.0.0.250'
MYTTL = 1 # Increase to reach other networks

sock = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MYTTL)
sock.sendto("robot", (MYGROUP_4, MYPORT))
