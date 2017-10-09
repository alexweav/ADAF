import socket

"""
Generic wrapper class for an arbitrary websocket
"""
class Socket:

    def __init__(self, address):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = address

    def Address(self):
        return self.address

    def Ip(self):
        return self.address[0]

    def Port(self):
        return self.address[1]

    def Socket(self):
        return self.socket

    def Close(self):
        self.socket.close()

    def ReadCallback(self):
        raise NotImplementedError('Calling an abstract method')


