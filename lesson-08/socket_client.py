import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 15000))

sock.send("secret_data это безопасноо".encode())

data = sock.recv(4096)
print("client recv", data.decode())

sock.close()
