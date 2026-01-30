from socket import socket, AF_INET, SOCK_STREAM
from message import send_message, recv_message
from threading import Thread


def echo_messages(sock):
    try:
        while True:
            msg = recv_message(sock)
            send_message(sock, msg)
    except IOError:
        sock.close()


def main(addr):
    sock = socket(AF_INET, SOCK_STREAM)
    # A common problem with sockets is getting an error
    # message "Address already in use."  This can be suppressed by
    # including the following operation involving setsockopt()
    from socket import SOL_SOCKET, SO_REUSEADDR

    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)

    sock.bind(addr)
    sock.listen()
    while True:
        client, addr = sock.accept()
        print("Connection from:", addr)
        Thread(target=echo_messages, args=[client]).start()


main(("localhost", 12345))
