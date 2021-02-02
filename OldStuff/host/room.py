from random import shuffle

from OldStuff.host.dataTransfer import *


class ROOM:
    def __init__(self, port):

        global graphics

        self.client_sockets = {}
        self.client_infos = {}

        HOST = ''
        self.port = port
        ADDR = (HOST, self.port)

        self.SERVER = socket(AF_INET, SOCK_STREAM)
        self.SERVER.bind(ADDR)

        self.SERVER.listen(5)
        print("Room", port, "has been created")

    def accept_incoming_connections(self):

        global graphics

        print("Room", self.port, "is waiting to be joined")
        while True:
            client, client_address = self.SERVER.accept()
            print(client_address, "joined room", self.port)

            self.client_sockets[client_address] = client

            if len(self.client_sockets) == 3:
                break

        self.start()

    def space_available(self):
        if len(self.client_sockets) == 3:
            return False
        else:
            return True

    def start(self):
        order = {0: "d1", 1: "d2", 2: "j"}
        shuffle(order)
        teams = {}

        for n, client in enumerate(self.client_sockets):
            send_msg(self.client_sockets[client], order[n])

        for n, client in enumerate(self.client_sockets):
            self.client_infos[client] = {"team": order[n]}

            teams[order[n]] = {}

            name = None
            while name is None:
                name = recv_msg(self.client_sockets[client])

            self.client_infos[client]["name"] = name

            teams[order[n]]["name"] = name

            img = None
            while img is None:
                img = recv_img(self.client_sockets[client])

            self.client_infos[client]["img"] = img

            teams[order[n]]["img"] = img

        self.broadcast(teams["d1"]["name"])
        self.broadcast(teams["d1"]["img"])
        self.broadcast(teams["d2"]["name"])
        self.broadcast(teams["d2"]["img"])
        self.broadcast(teams["j"]["name"])
        self.broadcast(teams["j"]["img"])

    def broadcast(self, msg):
        for client in self.client_sockets:
            send_msg(self.client_sockets[client], msg)

    def stop(self):
        self.broadcast("__ENDING__")

        self.SERVER.close()
