import socket

from config import config


class Entrance:
    def __init__(self):
        self.port = config.getint("ServerSettings", "port")
        self.s = None

        print("Entrance is initiated")

    def start(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.s.bind(("", self.port))
        print("Socket bound to", self.port)

        self.s.listen(5)
        print("Socket is listening")

    def accept_incoming_connections(self):
        print("Waiting for incoming connections")
        while True:
            c, addr = self.s.accept()
            print("Incoming connection from", addr)
