import socket
import pickle
import numpy as np

arr = np.array([[1, 2], [3, 4]])

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "10.203.62.151"
port = 6677
socket.connect((host, port))

input("Press enter to send a test message.")
print(pickle.dumps(arr))
socket.send(pickle.dumps(arr))

