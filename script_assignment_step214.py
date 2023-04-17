# This imports the os and time module
import os
import time


# This function takes user input and calls the respective function.
def one_or_all():
    choice = input("Would you like to see all(A) text file mod times or a specific(S) file? (A/S) \n>>> ").upper()
    if choice == "S":
        choose_file()
    elif choice == "A":
        all_txt()
    else:
        print("That was not a valid choice.")


# This function lists out the files ending in txt for the user to choose from
# The function passes that choice into the check_time function
def choose_file():
    this_dir = os.listdir('C:\\Users\\benja\\Documents\\GitHub\\Python_Projects_TA')
    print(f"The text files available in this directory are: ")

    for i in this_dir:
        if 'txt' in i:
            print(i)

    pick_file = input("Pick a text file to check time last modified: \n>>>")
    check_time(pick_file)


# This function takes the file picked by choose file
# and appends it to the file path of its directory.
# It then gets its modified time, converts it to local time and prints that out.
def check_time(file):
    file_path = 'C:\\Users\\benja\\Documents\\GitHub\\Python_Projects_TA'
    readme_path = os.path.join(file_path, file)
    timestamp = os.path.getmtime(readme_path)
    local_time = time.ctime(timestamp)
    print(local_time)


# This function lists the absolute path of all the txt files in the directory
# and when they were modified.

def all_txt():
    this_dir = os.listdir('C:\\Users\\benja\\Documents\\GitHub\\Python_Projects_TA')
    file_path = 'C:\\Users\\benja\\Documents\\GitHub\\Python_Projects_TA'
    for i in this_dir:
        if 'txt' in i:
            readme_path = os.path.join(file_path, i)
            timestamp = os.path.getmtime(readme_path)
            local_time = time.ctime(timestamp)
            print(f"\nThe absolute path for the file {i} is: \n{readme_path} \nIt was last modified "
                  f"on: \n{local_time}\n")


# Calls the function one_or_ all
one_or_all()
