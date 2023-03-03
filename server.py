import socket
import threading
from database import Database


class Server:
    def __init__(self, port, host, user, passwd, database):
        # Initialize our database
        self.db = Database(host, user, passwd, database)
        # Make our socket for incoming connections
        self.acceptSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port

        # Try to setup the socket        
        try:
            self.acceptSock.bind(("", self.port))
        except socket.error:
            print("[PORT IS USED FROM ANOTHER SERVICE]")
            print("[EXITING...]")
            exit(-1)
        except OverflowError:
            print("[PORT MUST BE 0-65535]")
            print("[EXITING...]")
            exit(-1)

        self.acceptSock.listen()
        print("[SERVER LISTENING...]")   

    def handle_client(self, sock, addr):
        
        while True:
            # Receive action from the user
            mode = sock.recv(1024).decode()

            if mode == "login":
                self.login()
            elif mode == "register":
                self.register()
            elif mode == "exit":
                break        

    def login(self):
        pass

    def register(self):
        pass

    def run(self):
        while True:
            sock, addr = self.acceptSock.accept()
            print(f"[CONNECTED {addr[0]}:{addr[1]}]")
            # For each connection we create a thread
            threading.Thread(target=self.handle_client, args=(sock, addr)).start()
            
