import main
import sqlite3
import time
import os
import shutil
import tkinter
from tkinter import *
from tkinter import messagebox


def set_src(self):
    print("Nothing here yet")


def set_dst(self):
    print('Nothing here yet')


def create_db():
    conn = sqlite3.connect('db_file_transfer.db')
    with conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE if not exists tbl_dir( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,'
                    'col_src_dir TEXT,'
                    'col_dst_dir TEXT'
                    ');')
        # You must commit() to save changes and close the database connection
        conn.commit()
    conn.close()
    first_run()


def first_run():
    conn = sqlite3.connect('db_file_transfer.db')
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        if count < 1:
            cur.execute('''INSERT INTO tbl_dir (col_src_dir, col_dst_dir)
                        VALUES (?, ?)''',
                        ('C:\\Users\\benja\\Desktop\\CustomerSource', 'C:\\Users\\benja\\Desktop\\CustomerDestination'))
    conn.close()


def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_dir""")
    count = cur.fetchone()[0]
    return cur, count


def sourceDir(self):
    selectSourceDir = tkinter.filedialog.askdirectory()
    self.source_dir.delete(0, END)
    self.source_dir.insert(0, selectSourceDir)


def destDir(self):
    selectDestDir = tkinter.filedialog.askdirectory()
    self.destination_dir.delete(0, END)
    self.destination_dir.insert(0, selectDestDir)


def transferFiles(self):
    # Get the current time
    current_time = time.time()
    # Define the threshold for "recently modified" (24 hours in seconds)
    recently_modified_threshold = 24 * 60 * 60

    source = self.source_dir.get()
    destination = self.destination_dir.get()
    for source_files in os.listdir(source):
        file_path = os.path.join(source + '/', source_files)
        if os.path.isfile(file_path) and (current_time - os.path.getmtime(file_path)) < recently_modified_threshold:
            shutil.move(source + '/' + source_files, destination)
            print(source_files + ' was successfully transferred')


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes the app
        self.master.destroy()
        os._exit(0)


if __name__ == "__main__":
    pass
