import sys

from Socket import *

class ControllerSocket(Socket):

    def __init__(self, address):
        super().__init__(address)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.address)
        self.socket.listen(5)

    def ReadCallback(self):
        connection, client_address = self.socket.accept()
        print(sys.stderr, 'New connection from', client_address)
        connection.setblocking(0)
        return connection


