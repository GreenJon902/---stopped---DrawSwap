import sys
import tkinter


class GRAPHICS:
    def __init__(self):
        self.window = tkinter.Tk()
        self.bus = list()
        self.roomTexts = {}
        self.rooms = {}
        self.threads = {}

        self.window.protocol("WM_DELETE_WINDOW", self.stop)


        self.roomText = tkinter.Text(self.window)
        self.roomText.grid(row=0, column=0)

        self.roomsList = tkinter.Listbox(self.window)
        self.roomsList.grid(row=0, column=1)
        self.roomsList.bind("<Button-1>", self.switchRoom)

    def setInfo(self, port):
        self.bus.append(lambda: self.window.title("DrawSwap Server on Port " + str(port)))

    def start(self):
        while True:

            tmpBus = self.bus.copy()

            for item in tmpBus:
                print(item)
                item()

            self.bus.clear()

            self.window.update()


    def addRoom(self, port, room, thread):
        self.roomTexts[port] = list()

        self.bus.append(lambda: self.roomsList.insert(tkinter.END, port))

        self.rooms[port] = room
        self.threads[port] = thread

    def sendInfo(self, port, info):
        def send():
            if self.roomsList.get(self.roomsList.curselection()) == port:
                self.roomText.insert(tkinter.END, info)

        self.roomTexts[port].append(info)

        self.bus.append(send)

    def switchRoom(self, event):
        port = self.roomsList.get(self.roomsList.curselection())

        self.roomText.delete("1.0", tkinter.END)

        for line in self.roomTexts[port]:
            self.roomText.insert(tkinter.END, line)
            self.roomText.insert(tkinter.END, "\n")

    def stop(self):
        for room in self.rooms:
            self.rooms[room].stop()

        for thread in self.threads:
            self.threads[thread]._stop()
