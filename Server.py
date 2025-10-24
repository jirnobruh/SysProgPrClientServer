import socket

server = socket.socket()
hostname = socket.gethostname()
port = 8000
server.bind((hostname, port))
server.listen(5)

print("Server running")

con, _ = server.accept()
filename = "hello.txt"
file = open(filename, "rb")
print("sending data to client")

line = file.read(1024)
while line:
    con.send(line)
    line = file.read(1024)

file.close()
con.close()
server.close()