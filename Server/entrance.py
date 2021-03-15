import logging
import socket
import uuid

import database
from config import Config
from functions import recv, send
from loggerFunctions import info

logger = logging.getLogger("Entrance")


class Entrance:
    def __init__(self):
        self.port = Config.getint("ServerSettings", "port")
        self.s = None

        info(logger, "Entrance is initiated")

    def start(self):
        self.s = socket.socket()

        self.s.bind(("", self.port))
        info(logger, "Socket bound to", self.port)

        self.s.listen(5)
        info(logger, "Socket is listening")

    def accept_incoming_connections(self):
        info(logger, "Waiting for incoming connections")
        while True:
            c, addr = self.s.accept()
            info(logger, "Incoming connection from", addr)

            request = int(recv(c))
            info(logger, "Request Code", request, "was received")

            # 1 - request new uuid

            if request == 1:
                info(logger, "Code", request, "means that a new uuid was requested by the client")

                while True:
                    new_uuid = uuid.uuid4()
                    if not database.check_for_uuid(new_uuid):
                        break

                info(logger, "Generated new uuid -", new_uuid)
                send(c, new_uuid)

                password = recv(c)
                info(logger, "Received password")

                c.close()



            info(logger, )

    def stop(self):
        self.s.close()
