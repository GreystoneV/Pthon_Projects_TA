import os
import shutil
import time
import datetime


# Function to transfer files from one directory to the next.
def file_transfer():
    # Path we want the files to go
    dst_path = 'C:\\Users\\benja\\Desktop\\CustomerDestination'
    # Path we want the files to come from
    src_path = 'C:\\Users\\benja\\Desktop\\CustomerSource'

    # Get the current time
    current_time = time.time()
    # Define the threshold for "recently modified" (24 hours in seconds)
    recently_modified_threshold = 24 * 60 * 60

    # Loop through all the files in the directory
    for filename in os.listdir(src_path):
        file_path = os.path.join(src_path, filename)
        destination = os.path.join(dst_path, filename)
        # Check if the file was modified within the last 24 hours
        if os.path.isfile(file_path) and (current_time - os.path.getmtime(file_path)) < recently_modified_threshold:
            shutil.move(file_path, destination)
            print(filename + ' was successfully transferred')


if __name__ == '__main__':
    # Continuous loop until we hit the time we want
    while True:
        # Gets the current time
        now = datetime.datetime.now()
        # Compares the target time with now
        if now.hour == 19 and now.minute == 41:
            # Calls function
            file_transfer()
            # Exits Program
            quit()
