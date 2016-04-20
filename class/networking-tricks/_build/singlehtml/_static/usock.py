#!/usr/bin/env python

import os, sys
from socket import *

SOCK_NAME = '\0beer'           # note null byte

if sys.argv[1] == '-s':
    # server
    sock = socket(AF_UNIX, SOCK_STREAM)
    sock.bind(SOCK_NAME)
    sock.listen(1)
    conn,addr = sock.accept()
    conn.send('Hello World\n')
    print 'from {}: {}\n'.format( 
        addr, conn.recv(100) )
    conn.close()                    # unblock other peer
else:
    # client
    sock = socket(AF_UNIX, SOCK_STREAM)
    sock.connect(SOCK_NAME)
    print sock.recv(100)
    sock.send( ' '.join(sys.argv[1:]) )
    msg = sock.recv(100)
    if not msg:
        print 'other side is gone'
    sock.close()

    
