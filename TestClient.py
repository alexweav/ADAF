import socket
import sys

messages = ['Message part 1, ', 'part 2, ', 'and part 3.']
server_address = ('localhost', 10000)

sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM),
           socket.socket(socket.AF_INET, socket.SOCK_STREAM)]

for s in sockets:
    s.connect(server_address)

for message in messages:
    for s in sockets:
        s.send(message.encode())

    for s in sockets:
        data = s.recv(1024)
        print('%s received %s', s.getsockname(), data)
        if not data:
            print('closing socket %s', s.getsockname())
            s.close()
