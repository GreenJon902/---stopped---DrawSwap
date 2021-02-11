import shutil
import tkinter as Tk
from tkinter import filedialog

from PIL import ImageTk, Image

import info, home

img2 = None


def back(window, text):
    info.name.set(text.get(1.0, Tk.END))
    home.main(window.winfo_geometry(), window)


def load():
    global img2

    img2 = Image.open("data/your img.png")
    img2 = img2.resize((40, 40), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)

    l.configure(image=img2)
    l.update()


def change(_):
    global img2

    path = Tk.filedialog.askopenfilename(filetypes=[("png Image", '.png'), ("All files", '.*')])

    shutil.copy(path, "data/your img.png")

    load()


def main(wg=None, window=None):
    global img2, l

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

    Tk.Label(window, image=img, background="#2b2b2b").grid(row=0, column=0, columnspan=2)
    text = Tk.Text(window, font=("Odin Rounded", 20), height=1, width=10)
    text.grid(row=1, column=0)
    text.insert(Tk.END, info.name.get().rstrip("\n"))
    text.update()

    l = Tk.Label(window, background="#2b2b2b")
    l.grid(row=1, column=1)
    l.bind("<Button-1>", change)

    Tk.Button(window, text="Back", font=("Odin Rounded", 20), background="#3c3f41", borderwidth=1, relief=Tk.SUNKEN,
              highlightcolor="#515151", command=lambda: back(window, text)).grid(row=2,
                                                                                 column=0,
                                                                                 columnspan=2,
                                                                                 sticky="NSEW")

    load()

    window.mainloop()


if __name__ == '__main__':
    main()
