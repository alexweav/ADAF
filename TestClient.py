import json
import socket
import sys
import time

"""
TEST CLIENT

A simple tester client script.
Opens two sockets for streaming data, and cyclically streams values for each one

"""

messages = ['Message part 1, ', 'part 2, ', 'and part 3.']
header = json.dumps({'type': 'AbcStream'})
server_address = ('localhost', 10000)

#sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM),
#           socket.socket(socket.AF_INET, socket.SOCK_STREAM)]

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

streams = {}
streams[socket] = ['a', 'b', 'c']
#streams[sockets[1]] = ['d', 'e', 'f']

#for s in sockets:
#    s.connect(server_address)

socket.connect(server_address)

i = 0
socket.send(header.encode())
print('sent header')
data = socket.recv(1024)
if not data:
    print('closing %s', socket.getsockname())
    socket.close()

while True:
    socket.send(streams[socket][i].encode())
    i = (i+1) % 3

    data = socket.recv(1024)
    if not data:
        print('closing socket %s', socket.getsockname())
        socket.close()
    time.sleep(1)
"""
while True:
    for s in sockets:
        s.send(streams[s][i].encode())
    i = (i+1) % 3

    for s in sockets:
        data = s.recv(1024)
        if not data:
            print('closing socket %s', s.getsockname())
            s.close()
"""

