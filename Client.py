import socket

client = socket.socket()
hostname = "26.182.186.124"
port = 8000
client.connect((hostname, port))

client.close()