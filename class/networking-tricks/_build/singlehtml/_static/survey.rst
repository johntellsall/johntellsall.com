SURVEY
============================

performance tools
-----------------

http://www.brendangregg.com/linuxperf.html


what types of IPC are there?

Internet socket survey
----------------------

TCP sockets
	reliable stream of bytes

    bidirectional


UDP sockets
    small packets (0.5KB - 63KB)

	fast, low latency

    unreliable

    super powers!


.. note::

   drops, dups, reordering

   generally a mistake to use IP-Size > PMTU (commonly ~1500)

   Q: but what about in a LAN?  A: unknown; congestion?

   TCP vs UDP for gaming: in practice
   http://gafferongames.com/networking-for-game-programmers/udp-vs-tcp/


TCP sockets
-----------



UDP socket
-----------

- address: Internet, IP+port
- small packets (0.5KB - 63KB)
- fast, low latency
- unreliable: drops, dups, reordering
- feature: multicast!


UDP Multicast
-------------

- any number producers and consumers
- unreliable: reorder, dropped, duplicate

TODO


Unix sockets
------------

- address: unnamed, path, or "abstract namespace"
- same machine, bidirectional
- byte streams, packets, and seq packets

* fast!

* low latency!
 

Pipes
named pipes
shared memory
queues
signals

LATER: ICMP -- Redirect!

