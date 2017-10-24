import json
import socket
import sys
import time

"""
Frame Client

A simple client script for transporting JPEG frames.
Opens one socket

"""

frame_header = json.dumps({'type': 'FrameStream'})
server_address = ('localhost', 10000)


frame_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


streams = {}
streams[frame_socket] = ['j', 'p', 'g']

frame_socket.connect(server_address)

i = 0
frame_socket.send(frame_header.encode())
print('sent headers for frame stream')
data = frame_socket.recv(1024)
if not data:
    print('closing %s', frame_socket.getsockname())
    frame_socket.close()
else:
    print('beginning frame stream')


while True:
    frame_socket.send(streams[frame_socket][i].encode())
    
    i = (i+1) % 3

    data = frame_socket.recv(1024)
    if not data:
        print('closing socket %s', frame_socket.getsockname())
        frame_socket.close()
    time.sleep(1)


