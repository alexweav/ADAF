import socket
import threading

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "10.203.1.88"
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
            message = self.socket.recv(1024).decode()
            if message != "":
                print("Got a message: ", message)

socket.listen(5)
while True:
    (client_socket, address) = socket.accept()
    print("connection found")
    Client(client_socket, address)
