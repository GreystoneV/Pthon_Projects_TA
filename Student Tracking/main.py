import tkinter as tk
import sqlite3

# Create a connection to the database
conn = sqlite3.connect('students.db')
c = conn.cursor()

# Create the students table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS students
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              first_name TEXT,
              last_name TEXT,
              phone TEXT,
              email TEXT,
              course TEXT)''')


# Define the function to add a new student
def add_student():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    course = entry_course.get()

    # Insert the new student into the database
    c.execute('''INSERT INTO students
                 (first_name, last_name, phone, email, course)
                 VALUES (?, ?, ?, ?, ?)''',
              (first_name, last_name, phone, email, course))
    conn.commit()

    # Clear the form fields
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_course.delete(0, tk.END)

    # Refresh the student list
    show_students()


# Define the function to delete a student
def delete_student():
    selected_student = listbox_students.curselection()[0]
    student_id = listbox_students.get(selected_student)[0]
    c.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    show_students()


# Define the function to show the list of students
def show_students():
    # Clear the listbox
    listbox_students.delete(0, tk.END)

    # Query the database for all students
    c.execute("SELECT * FROM students")
    rows = c.fetchall()

    # Add each student to the listbox
    for row in rows:
        listbox_students.insert(tk.END, row)


# Create the main window
root = tk.Tk()
root.title("Student Tracking")

# Create the form for adding a student
frame_form = tk.Frame(root)
frame_form.pack(padx=10, pady=10)

label_first_name = tk.Label(frame_form, text="First name")
label_first_name.grid(row=0, column=0, padx=5, pady=5)
entry_first_name = tk.Entry(frame_form)
entry_first_name.grid(row=0, column=1, padx=5, pady=5)

label_last_name = tk.Label(frame_form, text="Last name")
label_last_name.grid(row=1, column=0, padx=5, pady=5)
entry_last_name = tk.Entry(frame_form)
entry_last_name.grid(row=1, column=1, padx=5, pady=5)

label_phone = tk.Label(frame_form, text="Phone")
label_phone.grid(row=2, column=0, padx=5, pady=5)
entry_phone = tk.Entry(frame_form)
entry_phone.grid(row=2, column=1, padx=5, pady=5)

label_email = tk.Label(frame_form, text="Email")
label_email.grid(row=3, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame_form)
entry_email.grid(row=3, column=1, padx=5, pady=5)

label_course = tk.Label(frame_form, text="Current course")
label_course.grid(row=4, column=0, padx=5, pady=5)
entry_course = tk.Entry(frame_form)
entry_course.grid(row=4, column=1, padx=5, pady=5)

# Create the submit button
button_submit = tk.Button(frame_form, text="Submit", command=add_student)
button_submit.grid(row=5, column=1, padx=5, pady=5)

# Create the section for displaying the list of students
frame_list = tk.Frame(root)
frame_list.pack(padx=10, pady=10)

label_students = tk.Label(frame_list, text="List of Students")
label_students.pack()

listbox_students = tk.Listbox(frame_list)
listbox_students.pack()

# Create the delete button
button_delete = tk.Button(frame_list, text="Delete", command=delete_student)
button_delete.pack(padx=5, pady=5)

# Show the initial list of students
show_students()

# Start the main loop
root.mainloop()

# Close the connection to the database
conn.close()
