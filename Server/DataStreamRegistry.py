import socket
import select
import sys
import queue

from Socket import *
from ControllerSocket import *
from DataStream import *

class DataStreamRegistry(object):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.address = (ip, port)
        self.registry = {}
        self.controller = ControllerSocket((ip, port))
        self.registry[self.controller.Socket()] = self.controller
        self.inputs = [self.controller]
        self.outputs = []
        self.message_queues = {}

    def ReadSockets(self):
        print(sys.stderr, 'Waiting for the next event')
        readable, writable, exceptional = self.SelectSockets(self.inputs, self.outputs, self.inputs)
        for s in readable:
            if s is self.controller:
                self.HandleController(s)
            else:
                self.HandleReadStream(s)
        for s in writable:
            self.HandleWritable(s)

    def HandleController(self, socket):
        connection = self.controller.ReadCallback()
        stream = DataStream((ip, port), connection)
        self.registry[connection] = stream
        self.message_queues[stream] = queue.Queue()
        self.inputs.append(stream)

    def HandleReadStream(self, socket):
        data = socket.ReadCallback()
        if data:
            print(sys.stderr, 'received', data, 'from', socket.Socket().getpeername())
            self.message_queues[socket].put(data)
            if socket not in self.outputs:
                self.outputs.append(socket)
        else:
            print(sys.stderr, 'closing', socket.Address)
            if socket in self.outputs:
                self.outputs.remove(socket)
            self.inputs.remove(socket)
            del self.message_queues[socket]
            del self.registry[socket.Socket()]

    def HandleWritable(self, socket):
        try:
            next_msg = self.message_queues[socket].get_nowait()
        except queue.Empty:
            self.outputs.remove(socket)
        else:
            socket.Socket().send(next_msg)

    def HandleExceptional(self, socket):
        inputs.remove(socket)
        if socket in self.outputs:
            self.outputs.remove(socket)
        socket.Close()
        del message_queues[socket]
        del self.registry[socket.Socket()]

    def GetInputs(self):
        return self.inputs

    def GetRawSocketList(self, sockets):
        return [socket.Socket() for socket in sockets]

    def SelectSockets(self, read_sockets, write_sockets, exceptional_sockets):
        select_read = self.GetRawSocketList(read_sockets)
        select_write = self.GetRawSocketList(write_sockets)
        select_exceptional = self.GetRawSocketList(exceptional_sockets)
        readable_select, writable_select, exceptional_select = select.select(select_read, select_write, select_exceptional)
        readable = [self.registry[socket] for socket in readable_select]
        writable = [self.registry[socket] for socket in writable_select]
        exceptional = [self.registry[socket] for socket in exceptional_select]
        return readable, writable, exceptional


ip = 'localhost'
port = 10000
reg = DataStreamRegistry(ip, port)
while reg.inputs:
    reg.ReadSockets()
            
