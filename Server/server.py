import socket
import threading
from database import Database

LOGIN = "LOG "
REGISTER = "REG "
EXIT = "EXIT"
OK = "OK  "
ERR = "ERR "
MSGSIZE = 4
INFOLEN = 128

"""
    The Server class is responsible for handling the incoming requests
    from the clients and then communicating with the database. Basically
    acts as a middle man between the user and the database.
"""
class Server:
    def __init__(self, port, host, user, passwd, database, users_table):
        # Initialize our database
        self.db = Database(host, user, passwd, database, users_table)
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
        print("[SERVER LISTENING...]\n")   

    def handle_client(self, sock, addr):
        
        while True:
            # Receive action from the user
            action = sock.recv(MSGSIZE).decode()

            if action == LOGIN:
                if self.login(sock) == True:
                    sock.send(OK.encode())
                else:
                    sock.send(ERR.encode())

            elif action == REGISTER:
                if self.register(sock) == True:
                    sock.send(OK.encode())
                else:
                    sock.send(ERR.encode())
                
            elif action == EXIT:
                print(f"[DISCONNECTED {addr[0]}:{addr[1]}]")
                break

        sock.close()

    def login(self, sock):
        info = sock.recv(INFOLEN).decode()
        info = info.split("-")
        username = info[0]
        password = info[1]

        return self.db.login(username, password)

    def register(self, sock):
        info = sock.recv(INFOLEN).decode()
        info = info.split("-")
        username = info[0]
        password = info[1]

        return self.db.register(username, password)     

    def run(self):
        while True:
            sock, addr = self.acceptSock.accept()
            print(f"[CONNECTED {addr[0]}:{addr[1]}]")
            # For each connection we create a thread
            threading.Thread(target=self.handle_client, args=(sock, addr)).start()
            

        self.acceptSock.close()
    
server = Server(5050, "localhost","root", "root!", "LoginDB", "name_passwd")
server.run()