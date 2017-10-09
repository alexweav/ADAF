import socket
import select
import sys
import queue

from Socket import *
from ControllerSocket import *
from DataStream import *

def GetRawSocketList(sockets):
    return [socket.Socket() for socket in sockets]

def SelectSockets(read_sockets, write_sockets, exceptional_sockets):
    select_inputs = GetRawSocketList(inputs)
    select_outputs = GetRawSocketList(outputs)
    readable_select, writable_select, exceptional_select = select.select(select_inputs, select_outputs, select_inputs)
    readable = [registry[socket] for socket in readable_select]
    writable = [registry[socket] for socket in writable_select]
    exceptional = [registry[socket] for socket in exceptional_select]
    return readable, writable, exceptional


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
    readable, writable, exceptional = SelectSockets(inputs, outputs, inputs)

    for s in readable:
        if s is controller:
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
                print(sys.stderr, 'closing', s.Address)
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
        s.Close()
        del message_queues[s]
            
