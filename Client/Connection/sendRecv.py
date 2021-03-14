import struct


def recv(sock):
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


def send(sock, msg):
    msg = str(msg).encode()

    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)


__all__ = ["send", "recv"]
