from tkinter import *


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='')

if __name__ == "__main__":
    root = Tk()
    app = ParentWindow(root)
    root.mainloop()
