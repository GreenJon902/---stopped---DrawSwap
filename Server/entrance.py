import socket
import uuid

from config import config
from functions import recv, send


class Entrance:
    def __init__(self):
        self.port = config.getint("ServerSettings", "port")
        self.s = None

        print("Entrance is initiated")

    def start(self):
        self.s = socket.socket()

        self.s.bind(("", self.port))
        print("Socket bound to", self.port)

        self.s.listen(5)
        print("Socket is listening")

    def accept_incoming_connections(self):
        print("Waiting for incoming connections\n")
        while True:
            c, addr = self.s.accept()
            print("Incoming connection from", addr)

            request = int(recv(c))
            print("Request Code", request, "was received")

            # 1 - request new uuid

            if request == 1:
                print("Code", request, "means that a new uuid was requested by the client")

                new_uuid = uuid.uuid4()
                print("Generated new uuid -", new_uuid)
                send(c, new_uuid)

                password = recv(c)
                print("Received password")

                c.close()

            print()
