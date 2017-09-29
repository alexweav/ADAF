import socket
import threading
import pickle
import subprocess
import numpy as np

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "10.203.62.151"
port = 6677
socket.bind((host, port))

class Client(threading.Thread):
    def __init__(self, socket, address):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.connection = self.socket.makefile('rb')
        self.start()

    def run(self):
        cmdline = ['vlc', '--demux', 'h264', '-']
        player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
        while True:
            data = self.connection.read(1024)
            if not data:
                return
            player.stdin.write(data)

socket.listen(5)
while True:
    (client_socket, address) = socket.accept()
    print("connection found")
    Client(client_socket, address)
