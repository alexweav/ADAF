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
camera.resolution = (50, 50)
camera.hflip = True
camera.vflip = True
# Start a preview and let the camera warm up for 2 seconds
#camera.start_preview()
time.sleep(2)

frame_header = json.dumps({'type': 'FrameStream'})
server_address = ('169.254.227.100', 10000)


frame_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


streams = {}
streams[frame_socket] = ['j', 'p', 'g']

frame_socket.connect(server_address)

i = 0
frame_socket.send(frame_header.encode())
print('sent headers for frame stream')
data = frame_socket.recv(1024*50)
if not data:
    print('closing %s', frame_socket.getsockname())
    frame_socket.close()
else:
    print('beginning frame stream')

# Make a file-like object out of the connection
#connection = frame_socket.makefile('wb')
stream = io.BytesIO()
count = 0
print(count)
    
for foo in camera.capture_continuous(stream, 'png'):
    print(stream.tell())
    # Write the length of the capture to the stream and flush to
    # ensure it actually gets sent            
    
    # Rewind the stream and send the image data over the wire
    stream.seek(0)
    #connection.write(stream.read())
    frame_socket.send(stream.read())
    count = count +1
    # If we've been capturing for more than 30 seconds, quit
    #if time.time() - start > 30:
    if count == 10 :
        break
    # Reset the stream for the next capture
    stream.seek(0)
    stream.truncate()
    print(count)    
    time.sleep(1)

    
"""
while True:
    frame_socket.send(streams[frame_socket][i].encode())
    
    i = (i+1) % 3

    data = frame_socket.recv(1024)
    if not data:
        print('closing socket %s', frame_socket.getsockname())
        frame_socket.close()
    time.sleep(1)
"""


