import socket
from picamera import PiCamera
from time import sleep

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "10.203.62.151"
port = 6677
socket.connect((host, port))

connection = socket.makefile('wb')

try:
    with PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 24
        camera.hflip = True
        camera.vflip = True
        camera.start_preview()
        sleep(2)
        camera.start_recording(connection, format='h264')
        camera.wait_recording(60)
        camera.stop_recording()
finally:
    connection.close()
    socket.close()
