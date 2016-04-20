
.. Tricking out Linux Networking slides file, created by
   hieroglyph-quickstart on Wed Aug 20 15:12:52 2014.


Tricking out Linux Networking
=============================


ME
====

   - Senior dev/server consultant; DevOps
   - 15 years experience with Python
   - john@johntellsall.com


THEME
=====

Linux networking is cool, by understanding details you can do useful
tricks

- brief survey of sockets
- a few tricks
- other awesome networking


socket address families (AF)
----------------------------

=================== ==============================
**AF_INET**             IPv4 Internet protocols
AF_INET6            IPv6 Internet protocols
**AF_NETLINK**          Kernel user interface device
AF_PACKET           Low level packet interface
**AF_UNIX**   			Local communication
=================== ==============================


.. note::

   AF_APPLETALK        AppleTalk
   AF_ATMPVC           Access to raw ATM PVCs
   AF_AX25             Amateur radio AX
   AF_IPX              IPX - Novell protocols
   AF_X25              ITU-T X.25



TCP sockets
-----------

- address: Internet, IP+port
- reliable stream of bytes

Q: what happens if your process exits w/o closing the socket?

.. note::

   socket.error: [Errno 98] Address already in use


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
                

UDP socket
-----------

- address: Internet, IP+port
- small packets (0.5KB - 63KB)
- fast, low latency
- unreliable: drops, dups, reordering
- feature: multicast!


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

Any number of clients and servers!


UDP multicast example
---------------------

::

   $ ./mcast2.py 
   ('192.168.7.120', 52933)  'robot'
   $ ./mcast2.py 
   ('192.168.7.120', 50801)  'robot'


"socket" creates a record in the kernel, which talks to a driver


Unix sockets
------------

- address: unnamed, path, or "abstract namespace"
- same machine, bidirectional
- byte streams, packets, and seq packets
* fast!
* low latency!
 

Cheating with Unix sockets
--------------------------

* packets are nice: can't get partial JSON message

* can use "abstract namespace" ensure server only runs once

* send/receive credentials via the kernel

* send file descriptors: rebind TCP sockets!


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


other goodies
---------------

* **Netlink**: talk to/from kernel

  - subscribe to kernel events
  - sort of like *inotify*
  - ROUTE, FIREWALL, NFLOG, ARPD
  - also user-user!

* **TIPC**: multiple clusters

* Bypass the kernel => profit

  - special-purpose web server
  - achieves 2-10x performance of Nginx
  - low CPU, scales, saturates 6 10g cards!


☃
=


Reference
---------

* `AF_UNIX sockets and the abstract namespace, inter-process communication <http://blog.eduardofleury.com/archives/2007/09/13>`_ by Eduardo Fleury

* http://highscalability.com/blog/2014/2/12/paper-network-stack-specialization-for-performance.html


johntellsall.com
================

   


Unix socket vs Named Pipe
-------------------------

UNIX-domain sockets are generally more flexible than named pipes. Some of their advantages are:

You can use them for more than two processes communicating (eg. a server process with potentially multiple client processes connecting);
They are bidirectional;
They support passing kernel-verified UID / GID credentials between processes;
They support passing file descriptors between processes;
They support packet and sequenced packet modes.

`source <http://stackoverflow.com/questions/9475442/unix-domain-socket-vs-named-pipes>`_


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
    
    


LATER: Inotify


AF_UNIX SOCK_DGRAM in Kismet

int IPCRemote::SpawnIPC() {
	// Don't build the socket pair if we're in exec child mode
	if (child_exec_mode == 0) {
		// Generate the socket pair before the split
		if (socketpair(AF_UNIX, SOCK_DGRAM, 0, sockpair) < 0) {
			_MSG("Unable to great socket pair for IPC communication: " +
				 string(strerror(errno)), MSGFLAG_FATAL);
			globalreg->fatal_condition = 1;
			return -1;
		}

		unsigned int socksize = 32768;
		setsockopt(sockpair[0], SOL_SOCKET, SO_SNDBUF, &socksize, sizeof(socksize));
		setsockopt(sockpair[1], SOL_SOCKET, SO_SNDBUF, &socksize, sizeof(socksize));

	
