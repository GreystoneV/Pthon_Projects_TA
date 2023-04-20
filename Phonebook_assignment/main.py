# Python Version 3.9
#
# Author: Benjamin Pritchard
#
# Purpose: Phonebook demo. Demonstrating OOP, Tkinter GUI module,
#          using Tkinter Parent and Child relationships.
#
# Tested OS: This code was written and tested to work with Windows 10.

# Import modules
from tkinter import *
from tkinter import messagebox
import tkinter as tk

# Import other modules to have access to them
import pb_func
import pb_gui


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500, 300)  # (height, Width)
        self.master.maxsize(500, 300)
        # This CenterWindow method will center our app on the user's screen
        pb_func.center_window(self, 500, 300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg='#F0F0F0')
        # This protocol method is a tkinter built-in method to cat if
        # the user clicks the upper corner, "x" on Windows os.
        self.master.protocol("WM_DELETE_WINDOW", lambda: pb_func.ask_quit(self))
        arg = self.master

        # Load in GUI widgets from a separate module,
        # keeping your code compartmentalized and clutter-free.
        pb_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

