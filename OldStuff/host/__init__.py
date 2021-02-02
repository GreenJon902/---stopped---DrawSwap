from threading import Thread

from OldStuff.host import graphics
from OldStuff.host.dataTransfer import *
from OldStuff.host import ROOM

rooms = {}
graphics = graphics.GRAPHICS()
threads = {}


class _mainServer:
    def accept_incoming_connections(self):
        global graphics

        while True:
            client, client_address = SERVER.accept()
            added = 0
            graphics.sendInfo(PORT, str(client_address) + " joined")

            for room in rooms:
                if rooms[room].space_available():
                    port = rooms[port].port
                    added = 1

                    break

            if added == 0:
                port = get_free_port()
                print("Creating new room on port", port)

                rooms[port] = ROOM(port)
                threads[port] = Thread(target=rooms[port].accept_incoming_connections)
                graphics.addRoom(port, threads[port], rooms[port])
                threads[port].start()

            graphics.sendInfo(PORT, str(client_address) + " is being moved to room " + str(port))

            send_msg(client, port)

    def stop(self):
        SERVER.close()


HOST = ''
PORT = 33000
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

mainServer = _mainServer()

SERVER.listen(5)
print("Created main server")
accept_incoming_connections_thread = Thread(target=mainServer.accept_incoming_connections)
accept_incoming_connections_thread.start()

print("Starting Graphics")
graphics.setInfo(PORT)
graphics.addRoom(PORT, accept_incoming_connections_thread, mainServer)
graphics.start()
