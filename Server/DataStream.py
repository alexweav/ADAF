from Socket import *

class DataStream(Socket):

    def __init__(self, address, socket):
        self.address = address
        self.socket = socket

    def ReadCallback(self):
        data = self.socket.recv(1024)
        if not data:
            self.socket.close()
        return data


