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

