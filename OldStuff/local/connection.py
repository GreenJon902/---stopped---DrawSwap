import io
import struct
from socket import AF_INET, socket, SOCK_STREAM

from PIL import Image

import info


def send_msg(sock, msg):
    msg = str(msg).encode()

    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)


def send_img(sock, filepath):
    with open(filepath, "rb") as image:
        msg = image.read()

        msg = struct.pack('>I', len(msg)) + msg
        sock.sendall(msg)


def recv_img(sock):
    raw_msglen = recall(sock, 4)

    if not raw_msglen:
        return None

    msglen = struct.unpack('>I', raw_msglen)[0]
    data = recall(sock, msglen)

    return Image.open(io.StringIO(str(data)).read())
    # return Image.frombytes("RGB", (40, 40), bytes(data))


def recv_msg(sock):
    raw_msglen = recall(sock, 4)

    if not raw_msglen:
        return None

    msglen = struct.unpack('>I', raw_msglen)[0]
    return recall(sock, msglen).decode()


def recall(sock, n):
    data = bytearray()

    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None

        data.extend(packet)

    return data


class connection:
    def __init__(self):
        self.port = 33000
        self.address = info.ip

        self.team = None

    def join(self):
        self.SERVER = socket(AF_INET, SOCK_STREAM)
        self.SERVER.connect((self.address, self.port))
        print("Connected to server")

        newPort = None
        while newPort is None:
            newPort = recv_msg(self.SERVER)

        self.port = int(newPort)
        print("Moving to port " + str(self.port))

        self.SERVER = socket(AF_INET, SOCK_STREAM)
        self.SERVER.connect((self.address, self.port))

        print("Connected to server on new port")

        team = None
        while team is None:
            team = recv_msg(self.SERVER)

        self.team = team

        print("Received team - " + self.team)

        send_msg(self.SERVER, info.name.get())
        send_img(self.SERVER, "data/your img.png")

        print("Sent Player Name and Player Image")

        d1 = recv_msg(self.SERVER), recv_img(self.SERVER)
        d2 = recv_msg(self.SERVER), recv_img(self.SERVER)
        j = recv_msg(self.SERVER), recv_img(self.SERVER)

        print("Received Teams")

        self.teams = {"d1": d1, "d2": d2, "j": j}
