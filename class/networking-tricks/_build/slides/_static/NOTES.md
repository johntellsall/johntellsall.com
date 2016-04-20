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

http://stackoverflow.com/questions/3324619/unix-domain-socket-using-datagram-communication-between-one-server-process-and

"However, unix domain datagram sockets are different. In fact, the write() will actually block if the client's receive buffer is full rather than drop the packet. . This makes unix domain datagram sockets much superior to UDP for IPC because UDP will most certainly drop packets when under load, even on localhost. "

AF_UNIX SOCK_STREAM

AF_DBUS -- multicast Unix domain sockets, aka multicast pipes!

https://lkml.org/lkml/2012/2/20/208



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



* sendmsg()
# find . -name '*.c' | xargs egrep -q sendmsg | egrep -v zmq
- Redis: no
- Apache: ?
	http://httpd.apache.org/docs/current/mod/mod_proxy_fdpass.html
- Nginx: yes
	ngx_channel.c:ngx_write_channel

- Unicorn/Gunicorn:
- Uwsgi: yes
- Varnish: no?
- also
	https://github.com/slideinc/sendmsg -- for Python


Apache doesn't use sendfd() trick!  I haven't braved the code base yet
-- it likely uses something even more awesome than the parent process
copying bytes back and forth. Uwsgi and Nginx use sendmsg(), but
Apache, Gunicorn, Redis, Unicorn, and Varnish don't.

*theme: everything you know is wrong
- socket is stream, once bytes are read they're gone

LPI book: ioctl(fd, FIONREAD, &count) to get number of unread bytes in stream, or # bytes next read on datagram socket -- Linux only.

stream: reliable, connection-oriented
datagram: message boundaries preserved

- "reliable" means unaltered data goes through _or_ you get an error

- datagram: esrver doesn't have to be up

- stream: doesn't provide priority, can't "interrupt" big upload/download

- SSE: stream down to browser, dgram (POST) up
- WebSocket: two streams

- "proto" arg always zero, except for IPPROTO_RAW (SOCK_RAW -- TODO)

- "well known address"

- server can skip bind(), call listen() directly -- it'll get an
_ephemeral_ port. Server must register for clients to find it (cf
"well known")

(listen SOMAXCONN) was 5, Linux default max now 128

- multiple fds on same socket

- _connected_ datagram sockets (Linux only?)

- bind Unix domain in an accessible, writable directory -> security

- Unix domain datagram: reliable, in-order, no duplicates

- dgram size: SO_SNDBUF, 2KB = safe

- possible silent truncation on receiver

Linux Abstract Socket Namespace

- automatically removed! no unlink required

- can be used in chroot w/o filesystem -> security

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

- send/recv: socket additional options: nonblock, OOB, PEEK, WAITALL,
MORE/CORK)

- sendfile w/ FD mmap'able, ~ regular file

	- specify offset + count _per call_ -- array of messages! TRICK

*SECTION: overview
*SECTION: caveats / tricks
*SECTION: services (NETLINK)
*SECTION: future (Docker, Cgroups) and past (mmap IPC; last month)

TODO: splice, vmsplice, tee

- CORK ex: HTTP headers + data

(TIME_WAIT + SO_REUSEADDR)

(OOB: SIGURL for socket owner
- hmm: max one byte, one outstanding at a time
- discouraged, unreliable)

- sendmsg/recvmsg most flexible, including scatter/gather, _ancillary
data_
	- (recv in msg() - get multiple messages)

	- ancillary: send FD, send rights

- Sequenced Packet Sockets (Unixdom)
	- conn, _msg boundaries_, reliable, no dups, in order
	- SCTP: seq packet over internet; DCCP(?)
	multi stream: logical over one connection

(signalfd, pselect)

(self-pipe trick)


