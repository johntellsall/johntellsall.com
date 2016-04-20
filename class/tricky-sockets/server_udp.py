import socket 

addr = ('', 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.bind(addr)
while True: 
    data, addr = s.recvfrom(1024)
    print("from: {}\tgot: {}\n".format(
        addr, data.rstrip()
    ))


