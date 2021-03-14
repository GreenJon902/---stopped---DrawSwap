import logging
import struct

from loggerFunctions import debug

logger = logging.getLogger("functions")


def recv(sock):
    debug(logger, "Receiving")
    raw_msglen = recall(sock, 4)

    if not raw_msglen:
        return None

    msglen = struct.unpack('>I', raw_msglen)[0]
    data = recall(sock, msglen).decode()
    debug(logger, "Received " + str(recall(sock, msglen).decode()))
    return data


def recall(sock, n):
    data = bytearray()

    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None

        data.extend(packet)

    return data


def send(sock, msg):
    debug(logger, "Sending " + str(msg))
    msg = str(msg).encode()

    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)
