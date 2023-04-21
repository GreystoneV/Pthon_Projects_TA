from tkinter import *
import tkinter as tk
import main
import func


def load_gui(self):
    self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
    self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

    self.source_dir = Entry(width=75)
    self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

    self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
    self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

    self.destination_dir = Entry(width=75)
    self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

    self.set_src_btn = Button(text="Set Source", width=20, command=self.set_src)
    self.set_src_btn.grid(row=2, column=0, padx=(20, 10), pady=(0, 10))

    self.set_dst_btn = Button(text="Set Destination", width=15, command=self.set_dst)
    self.set_dst_btn.grid(row=2, column=1, padx=(0, 100), pady=(0, 15))

    self.transfer_btn = Button(text="Transfer Now", width=15, command=self.transferFiles)
    self.transfer_btn.grid(row=2, column=1, padx=(200, 15), pady=(0, 15))

    self.exit_btn = Button(text="Exit", width=15, command=self.ask_quit)
    self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))


if __name__ == "__main__":
    pass