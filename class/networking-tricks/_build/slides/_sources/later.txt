INBOX/LATER

yet more goodies
================

RAW and DGRAM sockets

.. note::
   http://man7.org/linux/man-pages/man7/packet.7.html
   http://sock-raw.org/papers/sock_raw


trick: send/receive credentials via the kernel. In general a server has to do its own authentication. For IPC, the client can send its user ID to a server, and the server can trust it, using a special sendmsg() call




What is an IP address?
* used for IP, UDP, TCP
How many do you get?
* convention: one per adapter
* also “localhost”
* can create or destroy them, that receive on one or multiple addrs (promiscuous mode)
XX
stream/dgram/seqpacket


3: ICMP ping, broadcast
Usage: network-management, not for users
Like DNS: connectionless, fast unreliable data


Details matter: IP, UDP, TCP give differing levels of checksum protection for different fields. See also: Packet in Packet security attacks.

- sendfile w/ FD mmap'able, ~ regular file

        - specify offset + count _per_call_ -- array of messages! TRICK


(signalfd, pselect)

(self-pipe trick)

TODO: - multiple fds on same socket


* * send credentials over fd XX
* cool settings: http://man7.org/linux/man-pages/man7/socket.7.html


Trick: HTTP has redirect; so does IP!  DNS router


(ping 224.0.0.1 = ping multicast “all hosts”, sort of equivalent to ping broadcast)
JM: think of publish/subscribe like with ZeroMQ or Redis or AMQP
JM: There’s also IP-based multicast


http://www.lognormal.com/blog/2012/09/27/linux-tcpip-tuning/
Address Discovery
“well known address”: http 80, ssh 22?
LAN: UDP: 0.5KiB - 63KiB, generally 1536 bytes
get Ops to stick internal service in /etc/services


file desc (from Glibc, kernel? XX)
later: IP
(low level services)
ICMP: ping
(IGMP)
summary: tons of stuff with different hassle / reliability / latency / bandwidth tradeoffs
statistics: UDP; easy single machine: UDP=portable, Unix domain socket
? cool services: traceroute uses UDP or ICMP
not yet
* shared memory, queues, locks, signals, RT signals


(not yet: practical concerns: 1) kill process hogging my port, 2) list all running servers and their ports, 3) using Supervisor to start, stop, monitor servers running on ports)


what happens when do you do read(fd)
=> blocks, unless you do fcntrl(NONBLOCK)
=> kernel does what it wants, based on what you tell it, and it’s own objectives


Other:
IP, 802.11 for wifi, Bluetooth, BTLE, packet radio


ZeroMQ: client can connect to server that isn’t up


code:
mkfifo --mode=0666 /tmp/namedPipe
gzip --stdout -d file.gz > /tmp/namedPipe
Then load the uncompressed data into a MySQL table[1] like so:
LOAD DATA INFILE '/tmp/namedPipe' INTO TABLE tableName;




.. note:
   (?) Q: can you put stdin+stdout on a single socket?

First cool trick: MySQL can load data from a file path, with named pipe can efficiently load from a compressed stream. Ref: http://en.wikipedia.org/wiki/Named_pipe

Named Pipes can have multiple readers/writers (JM: ?)








http://collections.lacma.org/sites/default/files/remote_images/piction/ma-31824080-WEB.jpg
 ma-31824080-WEB.jpg 

 chickenfridaynight.jpg 
 Radio_farm_family_ca1930_dbloc_sa.gif 

 kkk-ferris-wheel.jpg 

 013_rant.gif


_static/udp-reliablility.jpg

Addresses
=========

AF: unnamed, path, or “abstract namespace”
Address Family (AF)
TCP: IP and port
UDP: IP and (UDP) port
named pipe: file path
Linux Abstract XX

.. note:
   IPv6
   MAC

trick: reliable server process ID file. Classical server writes its PID to a magic file path. To signal a process, read the PID file.
Drawbacks:
* server crash: leaves “dangling” PID file
A: bind to Linux Abstract space. When server exits or crashes, socket is automatically destroyed!



Overview
========

In general, we work with kernel objects by asking for something, we
get a descriptor to use it in the future.


what is a file?
===============

.. image:: _static/csv.jpg

seekable, rewritable sequence of persistent bytes
   how do you get one?

   have a path, system gives you a “handle”. This lets you control the
   file.  If you give the handle to the system you can control it (Note a
   path is an “address” of a resource) what can you do with it?  close,
   read, write, fcntrl


what is a (TCP) socket?
-----------------------

x

.. note::
   connection btw two endpoints
   a “stream” of bytes -- they’re “consumed” on each side X
   how do you get one?
   ask for “handle” given an address (+ family)
   what can you do with it?
   close, recv, send, ioctl

``sock = socket.socket(AF_INET, SOCK_STREAM)``
``try:``
``    # Connect to server and send data``
``    sock.connect((HOST, PORT))``
``    sock.sendall(data + "\n")``
``    # Receive data from the server and shut down``
``    received = sock.recv(1024)``
``finally:``
``    sock.close()``


similar
=======

files/sockets have open/close, read/write, and “control” interfaces


but… not really
===============



What is a file -- “disk file”, really?
/dev/null, /proc/fs, named pipe
=> theme: concept doesn’t match implementation




socket ~ stream of bytes
========================

What is a TCP socket -- “stream of bytes”, really?

Linux lets you “peek”

TCP defaults to file transfer

.. note::
   http://stackoverflow.com/questions/864731/if-a-nonblocking-recv-with-msg-peek-succeeds-will-a-subsequent-recv-without-msg

   ? Not all TCP sockets are the same

   default TCP settings are for file transfer, experiment for HTTP-ish
   traffic; matters if Internet-facing vs LAN; (?bufferbloat)


files and sockets are APIs to kernel software
=============================================

Kernel/libc produces (file like) abstractions over lots of different
services, in different namespaces, with different tradeoffs




but, what’s the application?
============================

Socket is not only a stream of bytes, it’s a handle

* standard trick: send fd to unrelated process over socket XX JM expand

=> theme: concept doesn’t match implementation

.. note::
   http://stackoverflow.com/questions/13953912/difference-between-unix-domain-stream-and-datagram-sockets


UDP multicast
=============

Q: who uses Publish/Subscribe with Redis or ZeroMQ?

Example: Facebook/Twitter updates. Reads are common, writes are
rare. When account gets a new update, all his friends are sent an
update

=> we can replace some of these use cases with UDP multicast, on many machines!

Metaphor: radio with channels
Most protocols are two point streams of bytes or packets; UDP multicast is one-to-many
(or many to many) metaphor: radio with channels: multiple switchable stations, each one broadcasting to many people, unreliable. 

In practice: this could be used for statistics


Everything we Know is Wrong
===========================

.
=
.. figure:: _static/KKKFerrisWheel2.jpg
   :class: fill



zombie file!
============

What happens when you open a file, then delete it?

zombie: answer
=============

not much!

.. note::
   details matter!

   http://stackoverflow.com/questions/2028874/what-happens-to-an-open-file-handler-on-linux-if-the-pointed-file-gets-moved-de

   XX http://alban-apinc.blogspot.com/2011/12/introducing-multicast-unix-sockets.html

