import socket
import select
import sys
import queue

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
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(self.server_address)
        self.server.listen(5)

    def GetIp(self):
        return self.ip

    def GetPort(self):
        return self.port

    def GetServer(self):
        return self.server

ip = 'localhost'
port = 10000
manager = NetworkManager(ip, port)
inputs = [manager.GetServer()]
outputs = []

message_queues = {}

while inputs:
    print(sys.stderr, 'Waiting for the next event')
    readable, writable, exceptional = select.select(inputs, outputs, inputs)

    for s in readable:
        if s is manager.GetServer():
            connection, client_address = s.accept()
            print(sys.stderr, 'New connection from', client_address)
            connection.setblocking(0)
            inputs.append(connection)

            message_queues[connection] = queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                print(sys.stderr, 'received %s from %s', data, s.getpeername())
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                print(sys.stderr, 'closing', client_address)
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]

    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            outputs.remove(s)
        else:
            s.send(next_msg)

    for s in exceptional:
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]
            
