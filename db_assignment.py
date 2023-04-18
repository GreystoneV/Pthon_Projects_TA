# Import the sqlite 3 module
import sqlite3

# Create a list with file names
file_list = ['information.docx', 'Hello.txt', 'my_image.png', 'my_movie.mpg', 'world.txt', 'data.pfd', 'my_photo.jpeg']

# Initialize empty list for later use
storage = []
# Run a for loop to narrow our file_list down to only those files with a txt ending. Append to storage.
# (If working with larger or unknown data, would be wise to check ending not just 'in'
# because a file could have the letters txt in the name, and it not be the extension.)
for i in file_list:
    if 'txt' in i:
        storage.append(i)

# Assign connecting to our db with the variable conn for later use.
# First time connection creates the db if it doesn't exist
conn = sqlite3.connect('assignment.db')

# Connect, establish cur to execute commands. Create table if it doesn't exist
# and create primary key and a column named col_file_name.
# Commit and close db
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_file_name STRING)")
    conn.commit()
conn.close()

# Connect to db again
conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
    # Run for loop to insert data into the table under the appropriate column.
    for i in range(0, len(storage)):
        cur.execute("INSERT INTO tbl_files(col_file_name) VALUES (?) ", (storage[i],))
        i += 1
    conn.commit()
conn.close()


# Following block connects to db, selects the column col_file name and returns the values
# Value's get stored in variable var file. Loop through var_files to store values in a tuple.
# Print out all file names from our db.
conn = sqlite3.connect('assignment.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_file_name FROM tbl_files")
    var_files = cur.fetchall()
    files_from_db = ()
    for i in var_files:
        files_from_db += i
    print(f"The files in the data base are: {files_from_db}")
    conn.commit()
conn.close()
