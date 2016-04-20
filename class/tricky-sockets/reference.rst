

Reference
---------

* `AF_UNIX sockets and the abstract namespace, inter-process communication <http://blog.eduardofleury.com/archives/2007/09/13>`_ by Eduardo Fleury

* http://highscalability.com/blog/2014/2/12/paper-network-stack-specialization-for-performance.html


   



	
traditional TCP sockets

UDP sockets


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


