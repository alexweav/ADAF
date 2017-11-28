from Socket import *

"""
Represents a single source of streaming data from a client
"""
class DataStream(Socket):

    def __init__(self, address, socket, registry, name):
        self.address = address
        self.socket = socket
        self.registry = registry
        self.name = name

    """
    Reads a message, with a max of one kb, from the associated raw socket and return it
    If data is unavailable, close the socket and return None
    """
    def ReadCallback(self):
        data = self.socket.recv(1024)
        if not data:
            self.socket.close()
        return data

    """
    Abstract method for handling the specific stream type
    """
    def HandleStream(self, data):
        raise NotImplementedError('Calling an abstract method')
       
