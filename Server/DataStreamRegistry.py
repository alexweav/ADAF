import socket
import select
import sys
import queue

from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))


from AbcStream import *
from Socket import *
from ControllerSocket import *
from DataStream import *
from PluginSystem import PluginEngine
from UninitializedStream import *

"""
Manages all available data streams and handles requests for them
"""
class DataStreamRegistry(object):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.address = (ip, port)
        self.engine = PluginEngine.PluginEngine()
        self.registry = {}
        self.controller = ControllerSocket((ip, port), "Controller")
        self.registry[self.controller.Socket()] = self.controller
        self.inputs = [self.controller]
        self.outputs = []
        self.uninitialized = []
        self.message_queues = {}

    """
    Checks for socket updates from the OS and handles them according to their type
    """
    def ReadSockets(self):
        readable, writable, exceptional = self.SelectSockets(self.inputs, self.outputs, self.inputs)
        for s in readable:
            if s is self.controller:
                self.HandleController(s)
            elif s in self.uninitialized:
                self.HandleUninitialized(s)
            else:
                self.HandleReadStream(s)
        for s in writable:
            self.HandleWritable(s)

    """
    Handles the controller socket if there is a known update. This usually indicates the creation of a new socket
    """
    def HandleController(self, socket):
        connection = self.controller.ReadCallback()
        stream = UninitializedStream((self.ip, self.port), connection, self, 'Uninitialized')
        self.RegisterDataStream(stream)
        self.uninitialized.append(stream)

    """
    Handles uninitialized streams which are waiting for a json structure"
    """
    def HandleUninitialized(self, socket):
        json = socket.ReadCallback()
        stream = socket.HandleStream(json)
        self.uninitialized.remove(socket)
        socket.Socket().send(json)#####
        if socket in self.outputs:
            self.outputs.remove(socket)
        self.inputs.remove(socket)
        del self.message_queues[socket]
        del self.registry[socket.Socket()]
        self.RegisterDataStream(stream)

    """
    Handles a DataStream if there is a known read-style update. This usually indicates that new data has been written to the socket
    """
    def HandleReadStream(self, socket):
        name = socket.Name()
        data = socket.ReadCallback()
        result = socket.HandleStream(data)
        if result is not None:
            self.engine.ExecutePlugin(name, result)
        if data:
            #print(sys.stderr, 'received', data, 'from', socket.Socket().getpeername())
            self.message_queues[socket].put(str(len(data)).encode())
            if socket not in self.outputs:
                self.outputs.append(socket)
        else:
            print(sys.stderr, 'closing', socket.Address)
            if socket in self.outputs:
                self.outputs.remove(socket)
            self.inputs.remove(socket)
            del self.message_queues[socket]
            del self.registry[socket.Socket()]

    """
    Handles a Socket if there is a known write-style update. By default, just write the data back to the socket for parity
    """
    def HandleWritable(self, socket):
        try:
            next_msg = self.message_queues[socket].get_nowait()
        except queue.Empty:
            self.outputs.remove(socket)
        else:
            socket.Socket().send(next_msg)

    """
    Handles errored Sockets. If a socket errors, drop it
    """
    def HandleExceptional(self, socket):
        inputs.remove(socket)
        if socket in self.outputs:
            self.outputs.remove(socket)
        socket.Close()
        del message_queues[socket]
        del self.registry[socket.Socket()]

    """
    Returns a list of Sockets which are known, active providers of data
    """
    def GetInputs(self):
        return self.inputs

    """
    Given a list of Socket objects, returns a list of raw python sockets
    """
    def GetRawSocketList(self, sockets):
        return [socket.Socket() for socket in sockets]

    """
    Runs the pselect OS call which checks for socket updates on the system level
    Takes a list of sockets to check for read, write, and exceptional changes
    Returns corresponding lists of known socket updates
    """
    def SelectSockets(self, read_sockets, write_sockets, exceptional_sockets):
        select_read = self.GetRawSocketList(read_sockets)
        select_write = self.GetRawSocketList(write_sockets)
        select_exceptional = self.GetRawSocketList(exceptional_sockets)
        readable_select, writable_select, exceptional_select = select.select(select_read, select_write, select_exceptional)
        readable = [self.registry[socket] for socket in readable_select]
        writable = [self.registry[socket] for socket in writable_select]
        exceptional = [self.registry[socket] for socket in exceptional_select]
        return readable, writable, exceptional

    """
    Registers a new datastream with the system
    Doesn't take care of any special cases, such as uninitialized streams
    """
    def RegisterDataStream(self, stream):
        self.registry[stream.Socket()] = stream
        self.message_queues[stream] = queue.Queue()
        self.inputs.append(stream)

