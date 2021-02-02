import tkinter as Tk

from PIL import Image, ImageTk

from local import info, options, stats, join


def oppClicked(c):
    c.config(background="#F0F0F0")


def oppReleased(c, window):
    c.config(background="#3c3f41")

    options.main(window.winfo_geometry(), window)


def start(window):
    join.main(window)


def main(wg=None, window=None):
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

    window.grid_rowconfigure(1, minsize=350)
    window.grid_columnconfigure(2, minsize=150)
    window.grid_columnconfigure(1, minsize=200)
    window.grid_columnconfigure(0, minsize=200)

    img = Image.open("data/img.png")
    img = img.resize((600, 400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    Tk.Label(window, image=img, background="#2b2b2b").grid(row=0, column=0, columnspan=4, rowspan=2, sticky="NSEW")

    Tk.Button(window, text="Play", font=("Odin Rounded", 36), background="#3c3f41", borderwidth=1, relief=Tk.SUNKEN,
              command=lambda: start(window.winfo_geometry(), window), highlightcolor="#515151").grid(row=2, column=0, sticky="NSEW")
    Tk.Button(window, text="Stats", font=("Odin Rounded", 36), background="#3c3f41", borderwidth=1, relief=Tk.SUNKEN,
              command=lambda: stats.main(window.winfo_geometry(), window), highlightcolor="#515151").grid(row=2,
                                                                                                          column=1,
                                                                                                          sticky="NSEW")
    Tk.Button(window, text="Quit", font=("Odin Rounded", 36), background="#3c3f41", borderwidth=1, relief=Tk.SUNKEN,
              highlightcolor="#515151", command=window.destroy).grid(row=2, column=2, sticky="NSEW", columnspan=2)

    c = Tk.Canvas(window, background="#3c3f41", highlightthickness=1, highlightcolor="#515151", height=50,
                  relief=Tk.SUNKEN, width=50)
    c.create_text(26, 26, fill="#000000", text=u"\u2699", font=("Odin Rounded", 25))
    c.grid(row=0, column=3, sticky="NSEW")

    c.bind("<Button-1>", lambda x: oppClicked(c))
    c.bind("<ButtonRelease-1>", lambda x: oppReleased(c, window))

    window.mainloop()


if __name__ == '__main__':
    main()
