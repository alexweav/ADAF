import socket
import select
import sys
import queue

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

    def ReadCallback(self):
        raise NotImplementedError('Calling an abstract method')

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

class DataStream(Socket):

    def __init__(self, address, socket):
        self.address = address
        self.socket = socket

    def ReadCallback(self):
        data = self.socket.recv(1024)
        if not data:
            self.socket.close()
        return data

def GetRawSocketList(sockets):
    return [socket.Socket() for socket in sockets]

ip = 'localhost'
port = 10000
registry = {}
controller = ControllerSocket((ip, port))
registry[controller.Socket()] = controller
inputs = [controller]
outputs = []

message_queues = {}

while inputs:
    print(sys.stderr, 'Waiting for the next event')
    select_inputs = GetRawSocketList(inputs)
    select_outputs = GetRawSocketList(outputs)
    readable_select, writable_select, exceptional_select = select.select(select_inputs, select_outputs, select_inputs)
    readable = [registry[socket] for socket in readable_select]
    writable = [registry[socket] for socket in writable_select]
    exceptional = [registry[socket] for socket in exceptional_select]

    for s in readable:
        if s is controller:
            print('asdfasdf')
            connection = controller.ReadCallback()
            stream = DataStream((ip, port), connection)
            registry[connection] = stream
            message_queues[stream] = queue.Queue()
            inputs.append(stream)
        else:
            data = s.ReadCallback()
            if data:
                print(sys.stderr, 'received', data, 'from', s.Socket().getpeername())
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                print(sys.stderr, 'closing', client_address)
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                del message_queues[s]
                del registry[s.Socket()]

    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            outputs.remove(s)
        else:
            s.Socket().send(next_msg)

    for s in exceptional:
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]
            
