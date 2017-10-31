import json
import socket
import sys
import time

"""
TEST CLIENT

A simple tester client script.
Opens two sockets for streaming data, and cyclically streams values for each one

"""

abc_header = json.dumps({'type': 'AbcStream'})
def_header = json.dumps({'type': 'DefStream'})
server_address = ('10.42.0.1', 10000)

#sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM),
#           socket.socket(socket.AF_INET, socket.SOCK_STREAM)]

abc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

streams = {}
streams[abc_socket] = ['a', 'b', 'c']
streams[def_socket] = ['d', 'e', 'f']

#for s in sockets:
#    s.connect(server_address)

abc_socket.connect(server_address)
def_socket.connect(server_address)

i = 0
abc_socket.send(abc_header.encode())
def_socket.send(def_header.encode())
print('sent headers for each stream')
data = abc_socket.recv(1024)
if not data:
    print('closing %s', abc_socket.getsockname())
    abc_socket.close()
else:
    print('beginning abc stream')
data = def_socket.recv(1024)
if not data:
    print('closing %s', def_socket.getsockname())
    def_socket.close()
else:
    print('beginning def stream')

while True:
    abc_socket.send(streams[abc_socket][i].encode())
    def_socket.send((streams[def_socket][i] * 1024*5).encode())
    i = (i+1) % 3

    data = abc_socket.recv(1024)
    if not data:
        print('closing socket %s', abc_socket.getsockname())
        abc_socket.close()
    data = def_socket.recv(1024*50)
    if not data:
        print('closing socket %s', def_socket.getsockname())
        def_socket.close()
    time.sleep(0.4)
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

