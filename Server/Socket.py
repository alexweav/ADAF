import socket

"""
Generic wrapper class for an arbitrary websocket
"""
class Socket:

    def __init__(self, address, name):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = address
        self.name = name

    """
    The (Ip, Port) of the socket as a tuple
    """
    def Address(self):
        return self.address

    """
    The IP of the socket
    """
    def Ip(self):
        return self.address[0]

    """
    The port of the socket
    """
    def Port(self):
        return self.address[1]

    """
    The raw python socket object
    """
    def Socket(self):
        return self.socket

    """
    Closes this socket
    """
    def Close(self):
        self.socket.close()

    """
    Gives the name of this socket
    """
    def Name(self):
        return self.name

    """
    Callback which reads from this socket
    """
    def ReadCallback(self):
        raise NotImplementedError('Calling an abstract method')


