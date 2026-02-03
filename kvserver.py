import kvapp
from message import message
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import threading




KVADDRESS = ('localhost', 15000)

# server object with the app inside it
# 
class KVServer:
    def __init__(self):
        self.app = kvapp.KVApp() # the state machine
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
            # give me a message from the network, I am going to
            # shove it into the app and what ever response I get
            # just return it
            # a bit of decoupling happening here
            while True:
                cmd = message.recv_message(sock) # Step (1) client receives a command
                
                # self.consessus_module.(cmd) # Step 2 replicate
                # somehow .... time passes and we end up here. Run the command
                
                response = self.app.run_command(cmd) # Step 3 execute the command
                message.send_message(sock, response) # Step 4 sending the response back 
        except IOError:
            print("Client disconnected")

if __name__ == '__main__':
    serv = KVServer() 
    serv.run()