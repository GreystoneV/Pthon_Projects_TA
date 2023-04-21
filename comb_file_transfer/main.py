import tkinter as tk
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
import os
import shutil
import datetime
import time
import sqlite3
import func

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("File Transfer")

        self.master.protocol("WM_DELETE_WINDOW", lambda: func.ask_quit(self))


if __name__ == "__main__":
    func.create_db()
    while True:
        root = tk.Tk()
        App = ParentWindow(root)
        now = datetime.datetime.now()
        if now.hour == 20 and now.minute == 20:
            tf = ParentWindow(root)
            func.transferFiles()
        root.mainloop()
        # Add quit after main loop because if you try to close the program before the now.hour and now.minute
        # the window will reopen.
        quit()

# ############## Create a button and function that will allow user to save src and dstn directories.
# The window can then close and the program will auto quit after the files are transferred
