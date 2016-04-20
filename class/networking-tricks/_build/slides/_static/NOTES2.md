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
- cool ipfilter tricks, out of scope

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
