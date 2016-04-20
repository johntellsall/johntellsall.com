TCP server
----------

.. code-block:: python

   import socket 
   addr = ('', 5000)
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
   s.bind(addr)
   s.listen(5) 
   while True: 
      client, _address = s.accept() 
      data = client.recv(1024)
      if data: 
         client.send("got: {}\n".format(data.rstrip()))
      client.close()
                


UDP send multicast
------------------

.. code-block:: python

    import socket
    
    MYPORT = 8123
    MYGROUP_4 = '225.0.0.250'
    MYTTL = 1 # Increase to reach other networks
    
    sock = socket.socket(
        socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MYTTL)
    sock.sendto("robot", (MYGROUP_4, MYPORT))



UDP multicast example
---------------------

::

   $ ./mcast2.py 
   ('192.168.7.120', 52933)  'robot'
   $ ./mcast2.py 
   ('192.168.7.120', 50801)  'robot'


Unix socket server
------------------

.. code-block:: python

    SOCK_NAME = '\0beer'           # note null byte

    sock = socket(AF_UNIX, SOCK_STREAM)
    sock.bind(SOCK_NAME)
    sock.listen(1)
    conn,addr = sock.accept()
    conn.send('Hello World\n')
    print 'from {}: {}\n'.format( 
        addr, conn.recv(100) )
    conn.close()                    # unblock other peer

Unix socket client
------------------

.. code-block:: python

    SOCK_NAME = '\0beer'           # note null byte

    sock = socket(AF_UNIX, SOCK_STREAM)
    sock.connect(SOCK_NAME)
    print sock.recv(100)
    sock.send( ' '.join(sys.argv[1:]) )
    msg = sock.recv(100)
    if not msg:
        print 'other side is gone'
    sock.close()
    

listing Unix sockets
--------------------

::

   $ netstat -plx | egrep beer
   unix  2      [ ACC ]     STREAM     LISTENING     22418333 
   22882/python        @beer

   $ lsof -U | egrep beer
   python    22882 johnm    3u  unix 0x0000000000000000 
   0t0 22418333 @beer

* **@** = abstract, otherwise file path



UDP server
----------

.. code-block:: python

    import socket 
    addr = ('', 5000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    s.bind(addr)
    while True: 
        data, addr = s.recvfrom(1024)
        print("from: {}\tgot: {}\n".format(
            addr, data.rstrip()
        ))
    
    
