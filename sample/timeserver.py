import time
from socket import socket, AF_INET, SOCK_STREAM

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("", 12345))

sock.listen()
while True:
    client, addr = sock.accept()
    print("Connection from", addr)
    msg = time.ctime()  # Get current time
    client.sendall(msg.encode("utf-8"))
    client.close()
