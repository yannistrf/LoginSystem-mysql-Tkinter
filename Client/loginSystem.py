import socket

LOGIN = "LOG "
REGISTER = "REG "
EXIT = "EXIT"
OK = "OK  "
ERR = "ERR "
MSGSIZE = 4

"""
    An interface that connects to the server and performs different tasks on it.
"""
class LoginSystem:
    def __init__(self, serverIP, serverPort):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((serverIP, serverPort))


    def login(self, username, password):
        # Send "login" code, followed by the user's info
        self.sock.send(LOGIN.encode())
        data = username + "-" + password
        self.sock.send(data.encode())

        # Wait for the response of the server
        response = self.sock.recv(MSGSIZE).decode()
        # Correct info
        if response == OK:
            return True

        return False

    def register(self, username, password):
        # Send "login" code, followed by the user's info
        self.sock.send(REGISTER.encode())
        data = username + "-" + password
        self.sock.send(data.encode())

        # Wait for the response of the server
        response = self.sock.recv(MSGSIZE).decode()
        # Correct info
        if response == OK:
            return True

        return False

    def exit(self):
        self.sock.send(EXIT.encode())
        self.sock.close()

