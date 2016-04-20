
.. Tricking out Linux Networking slides file, created by
   hieroglyph-quickstart on Wed Aug 20 15:12:52 2014.


Tricking out Linux Networking
=============================


ME
====

   - Senior dev/server consultant; DevOps
   - 20 years experience with Python
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

	
traditional TCP sockets

UDP sockets

UDP multicast

- any number producers and consumers
- unreliable: reorder, dropped, duplicate


AF_UNIX SOCK_DGRAM

AF_UNIX

AF_UNIX, AF_LOCAL   Local communication              unix(7)
AF_INET             IPv4 Internet protocols          ip(7)
AF_INET6            IPv6 Internet protocols          ipv6(7)
AF_IPX              IPX - Novell protocols
AF_NETLINK          Kernel user interface device     netlink(7)
AF_X25              ITU-T X.25 / ISO-8208 protocol   x25(7)
AF_AX25             Amateur radio AX.25 protocol
AF_ATMPVC           Access to raw ATM PVCs
AF_APPLETALK        AppleTalk                        ddp(7)
AF_PACKET           Low level packet interface       packet(7)

SOCK_STREAM     Provides sequenced, reliable, two-way, connection-
based byte streams.  An out-of-band data transmission
mechanism may be supported.

SOCK_DGRAM      Supports datagrams (connectionless, unreliable
messages of a fixed maximum length).

SOCK_SEQPACKET  Provides a sequenced, reliable, two-way connection-
based data transmission path for datagrams of fixed
maximum length; a consumer is required to read an
entire packet with each input system call.

SOCK_RAW        Provides raw network protocol access.

SOCK_RDM        Provides a reliable datagram layer that does not
guarantee ordering.

http://man7.org/linux/man-pages/man7/unix.7.html

The AF_UNIX (also known as AF_LOCAL) socket family is used to
communicate between processes on the same machine efficiently.
Traditionally, UNIX domain sockets can be either unnamed, or bound to
a filesystem pathname (marked as being of type socket).  Linux also
supports an abstract namespace which is independent of the
filesystem.

Valid types are: SOCK_STREAM, for a stream-oriented socket and
SOCK_DGRAM, for a datagram-oriented socket that preserves message
boundaries (as on most UNIX implementations, UNIX domain datagram
sockets are always reliable and don't reorder datagrams); and (since
Linux 2.6.4) SOCK_SEQPACKET, for a connection-oriented socket that
preserves message boundaries and delivers messages in the order that
they were sent.

UNIX domain sockets support passing file descriptors or process
credentials to other processes using ancillary data.



TIP: SO_REUSEADDR

AF_UNIX SOCK_STREAM



References
==========

https://wiki.python.org/moin/UdpCommunication

sudo apt-get install python-examples




* audience: sr engineer, CTO, DevOps

* concept doesn't always match implementation 

what is a file?
	seekable collection of persistent bytes
how do you get one?
	ask kernel, get handle
what can you do with it?
	close, read/write, fctrl
"disk file": really?
	/dev/null, /proc/fd, named pipes!
=> concept doesn't match

what is a socket?
	stream of bytes, bidirectional, multi-machine
how do you get one?
	ask kernel, get handle
what can you do with it?
	close, ioctl?, send/recv
"stream of bytes": really?
	mostly; what about UDP; 
=> concept doesn't match
(default TCP settings are for file transfer, want to change settings for HTTP-ish traffic, matters if you're internet-facing vs LAN; bufferbloat)

namespaces
- socket: IP? multiple IPs? IPv6? TIPC address?
- filesystem
- in-kernel socket space!
( - cool ipfilter tricks, out of scope )

* kernel provides (file like) abstractions over *lots* of different
services, in different namespaces.  *
* actual implementation differs!
Ex: "stream of bytes" vs send fd to unrelated proc over X socket
Ex: tell kernel to send signal over fd(?)

(OSI model vs reality)

Won't cover: (kernel) queues, RT signals, ipfilter subsystem; also TIPC, inotify

* don't be afraid of code
- Python TCP socket server
- C TCP server
- Python UDP socket server

* powerful software uses kernel/hardware knowledge to accomplish magic
- Redis
- Apache
- Varnish vs Squid(?)
- Docker vs LXC + Namespaces + Aufs; layers are *different*
- ? uWSGI, unicorn/gunicorn

* Netflix diagram




stream: reliable, connection-oriented
datagram: message boundaries preserved

- "reliable" means unaltered data goes through _or_ you get an error

- datagram: esrver doesn't have to be up

- stream: doesn't provide priority, can't "interrupt" big upload/download

- SSE: stream down to browser, dgram (POST) up
- WebSocket: two streams

- "proto" arg always zero, except for IPPROTO_RAW (SOCK_RAW -- TODO)

- "well known address"

(listen SOMAXCONN) was 5, Linux default max now 128

(modern TCP discovers "path MTU" to avoid IP fragmentation)

(INADDR_ANY aka 0.0.0.0)

(FQDN terminated by period: example.com = domain; example.com. = FQDN)

- Unix vs Inet socket: Unix sometimes faster, dir (+file) perms, pass
FDs, pass credentials

- official Echo server -- in Inetd

- multiproc server: each child does accept(), or server accept(), pass
FD to child

Theme: every one knows TCP + UDP networking; most of what we know is
wrong, and there's a lot of other services.

TODO: xinetd

(inetd rebinds TCP/UDP to stdio)

(socket half close, SHUT_WR; on socket FD _not_ link)

*SECTION: overview
*SECTION: caveats / tricks
*SECTION: services (NETLINK)
*SECTION: future (Docker, Cgroups) and past (mmap IPC; last month)

(TIME_WAIT + SO_REUSEADDR)

(OOB: SIGURL for socket owner
- hmm: max one byte, one outstanding at a time
- discouraged, unreliable)

(signalfd, pselect)

(self-pipe trick)


