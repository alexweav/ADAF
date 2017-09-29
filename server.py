import socket
import threading
import pickle
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
        self.start()

    def run(self):
        while True:
            data = self.socket.recv(1024)
            if data != b'':
                arr = pickle.loads(data)
                print(repr(arr))

socket.listen(5)
while True:
    (client_socket, address) = socket.accept()
    print("connection found")
    Client(client_socket, address)
