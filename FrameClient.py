import json
import socket
import sys
import time
import picamera
import io
import struct

"""
Frame Client

A simple client script for transporting JPEG frames.
Opens one socket

"""

#start up camera
camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.hflip = True
camera.vflip = True
# Start a preview and let the camera warm up for 2 seconds
camera.start_preview()
time.sleep(2)

frame_header = json.dumps({'type': 'FrameStream'})
server_address = ('192.168.1.8', 10000)


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



