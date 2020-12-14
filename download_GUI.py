"""
Download GUI
"""
#import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import download_logic


class downloadApp(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.winfo_toplevel().title(
            "TR8100 Program Backup&Restore Tool Ver1.0.0")
        self.grid()
        self.StartPage()

    def StartPage(self):

        self.it = Label(self)
        self.it["text"] = "SN："
        self.it.grid(row=0, column=0, sticky=N + E)
        self.SN = Entry(self)
        self.SN["width"] = 30
        self.SN.grid(row=0, column=1, columnspan=1, sticky=N + W)

        self.ot = Label(self)
        self.ot["text"] = "PN："
        self.ot.grid(row=2, column=0, sticky=N + E)
        self.PN = Entry(self)
        self.PN["width"] = 30
        self.PN.grid(row=2, column=1, columnspan=6, sticky=N + W)
        self.nb = Button(self, command=lambda: self.search_download())
        self.nb["text"] = "Down"
        self.nb.grid(row=3, column=4, sticky=N + W)

        self.select = Radiobutton(self)
        self.select['text'] = "D"
        self.select.grid(row=4, column=0, sticky=N + E)

    def search_download(self):
        SN = self.SN.get()
        PN = self.PN.get()
        download_search_mode = download_logic.down_search.search(SN, PN)


if __name__ == "__main__":
    root = Tk()
    root.geometry('460x600+30+30')
    app = downloadApp(master=root)
    root.mainloop()
