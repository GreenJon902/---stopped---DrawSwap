import tkinter as Tk

from PIL import ImageTk, Image

from local import info, home


def main(wg=None, window=None):
    if wg is None:
        window = Tk.Tk()
        window.title(info.windowName)
        window.geometry("600x492")
        window.iconbitmap(default="data/img.ico")
        window.configure(background="#2b2b2b")
        #window.resizable(False, False)

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
    Tk.Label(window, image=img, background="#2b2b2b").grid(row=0, column=0, columnspan=3, sticky="NSEW")
    Tk.Label(window, text="Wins: " + str(info.wins.get()), background="#2b2b2b", font=("Odin Rounded", 20)).grid(
        row=1, column=0, sticky="NSEW")
    Tk.Label(window, text="Losses: " + str(info.losses.get()), background="#2b2b2b", font=("Odin Rounded", 20)).grid(
        row=1, column=1, sticky="NSEW")
    Tk.Label(window, text="Games: " + str(info.games.get()), background="#2b2b2b", font=("Odin Rounded", 20)).grid(
        row=1, column=2, sticky="NSEW")

    Tk.Button(window, text="Back", font=("Odin Rounded", 20), background="#3c3f41", borderwidth=1, relief=Tk.SUNKEN,
              highlightcolor="#515151", command=lambda: home.main(window.winfo_geometry(), window)).grid(row=2,
                                                                                                         column=0,
                                                                                                         columnspan=3,
                                                                                                         sticky="NSEW")

    window.mainloop()


if __name__ == '__main__':
    main()
