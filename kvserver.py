import kvapp
from message import message
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import threading

KVADDRESS = ('localhost', 15000)

class KVServer:
    def __init__(self):
        self.app = kvapp.KVApp()
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
        self.sock.bind(KVADDRESS)
        self.sock.listen()

    
    def run(self):
        while True:
            client, addr = self.sock.accept()
            print("Connection from: ", addr)
            threading.Thread(target=self.handle_client, args=[client]).start()
    
    def handle_client(self, sock):
        try:
            while True:
                cmd = message.recv_message(sock)
                response = self.app.run_command(cmd)
                message.send_message(sock, response)
        except IOError:
            print("Client disconnected")

if __name__ == '__main__':
    serv = KVServer() 
    serv.run()