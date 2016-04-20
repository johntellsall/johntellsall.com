Cheating with Unix sockets
--------------------------

* packets are nice: can't get partial JSON message

* can use "abstract namespace" ensure server only runs once

* send/receive credentials via the kernel

* send file descriptors: rebind TCP sockets!


Unix socket vs Named Pipe
-------------------------

UNIX-domain sockets are generally more flexible than named pipes. Some
of their advantages are:

You can use them for more than two processes communicating (eg. a server process with potentially multiple client processes connecting);
They are bidirectional;
They support passing kernel-verified UID / GID credentials between processes;
They support passing file descriptors between processes;
They support packet and sequenced packet modes.

`source <http://stackoverflow.com/questions/9475442/unix-domain-socket-vs-named-pipes>`_


TODO: dgram packet size

TODO: socketpair?

This is used by real code -- like Kismet

AF_UNIX SOCK_DGRAM in Kismet

.. code::

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


http://stackoverflow.com/questions/3324619/unix-domain-socket-using-datagram-communication-between-one-server-process-and

"However, unix domain datagram sockets are different. In fact, the write() will actually block if the client's receive buffer is full rather than drop the packet. . This makes unix domain datagram sockets much superior to UDP for IPC because UDP will most certainly drop packets when under load, even on localhost. "


* sendmsg()

- Redis: no
- Apache: ?
- Nginx: yes
- Unicorn/Gunicorn:
- Uwsgi: yes
- Varnish: no?

.. note::

	http://httpd.apache.org/docs/current/mod/mod_proxy_fdpass.html

	ngx_channel.c:ngx_write_channel

    https://github.com/slideinc/sendmsg -- for Python


   Apache doesn't use sendfd() trick!  I haven't braved the code base yet
   it likely uses something even more awesome than the parent process
   copying bytes back and forth. Uwsgi and Nginx use sendmsg(), but
   Apache, Gunicorn, Redis, Unicorn, and Varnish don't.


- server can skip bind(), call listen() directly
  it'll get an _ephemeral_ port

.. note::
   . Server must register for clients to find it (cf "well known")


TODO - multiple fds on same socket


TODO - _connected_ datagram sockets (Linux only?)

- bind Unix domain in an accessible, writable directory -> security

- Unix domain datagram: reliable, in-order, no duplicates

- dgram size: SO_SNDBUF, 2KB = safe

- possible silent truncation on receiver XXXX?


Linux Abstract Socket Namespace

- automatically removed! no unlink required

- can be used in chroot w/o filesystem -> security


- sendfile w/ FD mmap'able, ~ regular file

	- specify offset + count _per_call_ -- array of messages! TRICK


MAYBE: - send/recv: socket additional options: nonblock, OOB, PEEK,
WAITALL, MORE/CORK)

- CORK ex: HTTP headers + data


TODO: splice, vmsplice, tee

- sendmsg/recvmsg most flexible
  including scatter/gather, _ancillary_data_

	- (recv in msg() - get multiple messages)

	- ancillary: send FD, send rights

- Sequenced Packet Sockets (Unixdom)
	- conn, _msg_boundaries_, reliable, no dups, in order
	- SCTP: seq packet over internet; DCCP(?)

.. note::
   multi stream: logical over one connection


