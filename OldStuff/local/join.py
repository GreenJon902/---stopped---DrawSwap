from tkinter import Tk

from PIL import ImageTk, Image
from connection import connection

import info


def main(wg=None, window=None):
    conn = connection()
    conn.join()

    if wg is None:
        window = Tk.Tk()
        window.title(info.windowName)
        window.geometry("600x492")
        window.iconbitmap(default="data/img.ico")
        window.configure(background="#2b2b2b")
        window.resizable(False, False)

    else:
        window.destroy()

        window = Tk.Tk()
        window.title(info.windowName)
        window.geometry(wg)
        window.iconbitmap(default="data/img.ico")
        window.configure(background="#2b2b2b")
        window.resizable(False, False)

    img = Image.open("data/img.png")
    img = img.resize((600, 400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    Tk.Label(window, image=img, background="#2b2b2b").grid(row=0, column=0, columnspan=2, sticky="NSEW")

    d1img = ImageTk.PhotoImage(connection.teams["d1"][1])
    d2img = ImageTk.PhotoImage(connection.teams["d2"][1])
    jimg = ImageTk.PhotoImage(connection.teams["j"][1])

    Tk.Label(window, image=d1img, background="#2b2b2b").grid(row=1, column=0, sticky="NSEW")
    Tk.Label(window, text="Drawer 1: " + connection.teams["d1"][0], background="#2b2b2b", font=("Odin Rounded", 20)).grid(
        row=1, column=1, sticky="NSEW")
    Tk.Label(window, image=d2img, background="#2b2b2b").grid(row=2, column=0, sticky="NSEW")
    Tk.Label(window, text="Drawer 2: " + connection.teams["d2"][0], background="#2b2b2b", font=("Odin Rounded", 20)).grid(
        row=2, column=1, sticky="NSEW")
    Tk.Label(window, image=jimg, background="#2b2b2b").grid(row=3, column=0, sticky="NSEW")
    Tk.Label(window, text="Judge: " + connection.teams["j"][0], background="#2b2b2b", font=("Odin Rounded", 20)).grid(
        row=3, column=1, sticky="NSEW")

    window.update()
    window.mainloop()

if __name__ == '__main__':
    main()
