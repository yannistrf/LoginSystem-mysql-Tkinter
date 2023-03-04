import socket

class LoginSystem:
    def __init__(self, serverIP, serverPort):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((serverIP, serverPort))


    def login(self, username, password):
        # Send "login" code, followed by the user's info
        self.sock.send("login".encode())
        data = username + "-" + password
        self.sock.send(data.encode())

        # Wait for the response of the server
        response = self.sock.recv(4).decode()
        # Correct info
        if response == "OK":
            return True

        return False

    def register(self, username, password):
        # Send "login" code, followed by the user's info
        self.sock.send("register".encode())
        data = username + "-" + password
        self.sock.send(data.encode())

        # Wait for the response of the server
        response = self.sock.recv(4).decode()
        # Correct info
        if response == "OK":
            return True

        return False

    def exit(self):
        self.sock.send("exit".encode())
        self.sock.close()

