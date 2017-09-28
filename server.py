import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "10.203.1.88"
port = 6677
socket.bind((host, port))

socket.listen(5)
while True:
    (client_socket, address) = socket.accept()
    print("connection found")
