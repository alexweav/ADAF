import socket
import sys

messages = ['Message part 1, ', 'part 2, ', 'and part 3.']
server_address = ('localhost', 10000)

sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM),
           socket.socket(socket.AF_INET, socket.SOCK_STREAM)]

streams = {}
streams[sockets[0]] = ['a', 'b', 'c']
streams[sockets[1]] = ['d', 'e', 'f']

for s in sockets:
    s.connect(server_address)

"""
for message in messages:
    for s in sockets:
        s.send(message.encode())

    for s in sockets:
        data = s.recv(1024)
        print('%s received %s', s.getsockname(), data)
        if not data:
            print('closing socket %s', s.getsockname())
            s.close()
"""

i = 0
while True:
    for s in sockets:
        s.send(streams[s][i].encode())
    i = (i+1) % 3

    for s in sockets:
        data = s.recv(1024)
        if not data:
            print('closing socket %s', s.getsockname())
            s.close()

