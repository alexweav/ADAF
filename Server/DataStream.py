from Socket import *

"""
Represents a single source of streaming data from a client
"""
class DataStream(Socket):

    def __init__(self, address, socket):
        self.address = address
        self.socket = socket

    """
    Reads a message, with a max of one kb, from the associated raw socket and return it
    If data is unavailable, close the socket and return None
    """
    def ReadCallback(self):
        data = self.socket.recv(1024)
        if not data:
            self.socket.close()
        return data


