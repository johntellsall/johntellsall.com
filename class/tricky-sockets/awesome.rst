AF_DBUS -- multicast Unix domain sockets, aka multicast pipes!

https://lkml.org/lkml/2012/2/20/208


TODO: shmem recent


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

