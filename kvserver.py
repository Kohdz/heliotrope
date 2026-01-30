import kvapp
from message import message
from socket import socket, AF_INET, SOCK_STREAM


KVADDRESS = ('localhost', 15000)

class KVServer:
    def __init__(self):
        self.app = kvapp.KVApp()
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind(KVADDRESS)
        self.sock.listen()

    
    def run(self):
        while True:
            client, addr = self.sock.accept()
            print("Connection from: ", addr)
            self.handle_client(client)
    
    def handle_client(self, sock):
        while True:
            cmd = message.recv_message(sock).decode('uft-8')
            response = self.app.run_command(cmd)
            message.send_message(sock, response.encode('uft-8'))

if __name__ == '__main__':
    serv = KVServer()
    serv.run()