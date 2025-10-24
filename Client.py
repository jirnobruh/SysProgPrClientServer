import socket

client = socket.socket()
hostname = socket.gethostname()
port = 8000
client.connect((hostname, port))

file = open('test.txt', 'wb')
print("receiving data from server")
while True:
    data = client.recv(1024)
    file.write(data)
    print(bytes.decode(data))
    if not data: break
file.close()
print("data saved")
client.close()