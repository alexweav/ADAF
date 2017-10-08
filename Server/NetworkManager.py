import socket
import select

"""
Handles creation of sockets for the ADAF
"""
class NetworkManager:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setblocking(0)
        self.server_address = (ip, port)
        server.bind(server_address)
        server.listen(5)

    def GetIp(self):
        return self.ip

    def GetPort(self):
        return self.port

