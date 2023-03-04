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
            action = sock.recv(8).decode()

            if action == "login":
                if self.login(sock) == True:
                    sock.send("OK".encode())
                else:
                    sock.send("ERR".encode())

            elif action == "register":
                if self.register(sock) == True:
                    sock.send("OK".encode())
                else:
                    sock.send("ERR".encode())
                
            elif action == "exit":
                print(f"[DISCONNECTED {addr[0]}:{addr[1]}]")
                break

        sock.close()

    def login(self, sock):
        info = sock.recv(128).decode()
        info = info.split("-")
        username = info[0]
        password = info[1]

        print(username, password)
        return self.db.login(username, password)

    def register(self, sock):
        info = sock.recv(128).decode()
        info = info.split("-")
        username = info[0]
        password = info[1]

        print(username, password)
        return self.db.register(username, password)     

    def run(self):
        while True:
            sock, addr = self.acceptSock.accept()
            print(f"[CONNECTED {addr[0]}:{addr[1]}]")
            # For each connection we create a thread
            threading.Thread(target=self.handle_client, args=(sock, addr)).start()
            break

        self.acceptSock.close()
            