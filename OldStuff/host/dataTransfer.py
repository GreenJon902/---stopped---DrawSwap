import struct
from contextlib import closing
import io
from socket import SOL_SOCKET, SO_REUSEADDR, AF_INET, SOCK_STREAM, socket

from PIL import Image


def get_free_port():
    with closing(socket(AF_INET, SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        return s.getsockname()[1]


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
