from kivy.logger import Logger
import socket

from staticConfigurables import connection


def join_public():
    Logger.info("Connection: Joining a public game")


def get_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((get_ip(), get_port()))


def get_ip():
    return connection.get("Server", "ip")


def get_port():
    return connection.getint("Server", "port")
