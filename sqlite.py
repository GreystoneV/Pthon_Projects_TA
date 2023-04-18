import sqlite3

# conn = sqlite3.connect('test.db')

# with conn:
#     cur = conn.cursor()
#     cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
#     ID INTEGER PRIMARY KEY AUTOINCREMENT, \
#     col_fname TEXT, \
#     col_lname TEXT, \
#     col_email TEXT \
#     )")
#     conn.commit()
# conn.close()
#
# conn = sqlite3.connect('test.db')
#
# with conn:
#     cur = conn.cursor()
#     cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)",
#                 ('Bob', 'Smith', 'bsmith@gmail.com'))
#     cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)",
#                 ('Sara', 'Jones', 'sjones@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)",
                ('Kevin', 'Bacon', 'kbacon@gmail.com'))
#     conn.commit()
# conn.close()

conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname, col_lname, col_email FROM tbl_persons WHERE col_fname = 'Sara'")
    var_person = cur.fetchall()
    for i in var_person:
        msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(i[0], i[1], i[2])
    print(msg)
    conn.commit()
conn.close()
