import base64
import pickle

windowName = "Draw Swap"
ip = "127.0.0.1"
port = "33000"


class _all:
    def get(self):
        file = open("data/info.ds", "rb")

        contents = pickle.load(file)

        return contents

    def set(self, info):
        file = open("data/info.ds", "wb")

        pickle.dump(info, file)


class _wins:
    def get(self):
        file = open("data/info.ds", "rb")

        contents = pickle.load(file)

        return contents["wins"]

    def set(self, info):
        file = open("data/info.ds", "wb")

        contents = _all().get()

        contents["wins"] = info

        pickle.dump(contents, file)


class _losses:
    def get(self):
        file = open("data/info.ds", "rb")

        contents = pickle.load(file)

        return contents["losses"]

    def set(self, info):
        file = open("data/info.ds", "wb")

        contents = _all().get()

        contents["losses"] = info

        pickle.dump(contents, file)


class _games:
    def get(self):
        file = open("data/info.ds", "rb")

        contents = pickle.load(file)

        return contents["games"]

    def set(self, info):
        contents = _all().get()

        file = open("data/info.ds", "wb")

        contents["games"] = info

        pickle.dump(contents, file)


class _name:
    def get(self):
        file = open("data/info.ds", "rb")

        contents = pickle.load(file)

        return contents["name"]

    def set(self, info):
        contents = _all().get()

        file = open("data/info.ds", "wb")

        contents["name"] = info

        pickle.dump(contents, file)


all = _all()
wins = _wins()
losses = _losses()
games = _games()
name = _name()
