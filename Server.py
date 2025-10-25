import socket

server = socket.socket()
hostname = "26.182.186.124"
port = 8000
server.bind((hostname, port))
server.listen()

print("Server running")


server.close()