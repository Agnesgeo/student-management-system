
import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Database connection
def connect_to_db():
    
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mila@2004",   # Replace with your MySQL password
            database="dbmsproj"
        )
# Function to insert data into the student table
def add_student():
    conn = connect_to_db()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO student (s_id, name, mobileno, birth_date, address, email_id) VALUES (%s, %s, %s, %s, %s, %s)",
                       (entry_sid.get(), entry_name.get(), entry_mobileno.get(), entry_birthdate.get(), entry_address.get(), entry_email.get()))
        conn.commit()
        messagebox.showinfo("Success", "Student added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")
    finally:
        cursor.close()
        conn.close()

# Function to insert data into the course table
def add_course():
    conn = connect_to_db()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO course (course_id, cname) VALUES (%s, %s)",
                       (entry_course_id.get(), entry_cname.get()))
        conn.commit()
        messagebox.showinfo("Success", "Course added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")
    finally:
        cursor.close()
        conn.close()

# Function to insert data into the faculty table
def add_faculty():
    conn = connect_to_db()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO faculty (f_id, f_name, qualification, mobileno, email_id) VALUES (%s, %s, %s, %s, %s)",
                       (entry_fid.get(), entry_fname.get(), entry_qualification.get(), entry_fmobileno.get(), entry_femail.get()))
        conn.commit()
        messagebox.showinfo("Success", "Faculty added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")
    finally:
        cursor.close()
        conn.close()

# GUI Setup
app = tk.Tk()
app.title("DBMS Project - MySQL Records Management")
app.geometry("500x500")
app.configure(bg="#f5f5f5")

# Navigation between pages
def show_frame(frame):
    frame.tkraise()

# Student Page
student_page = tk.Frame(app, bg="#f5f5f5")
student_page.grid(row=0, column=0, sticky="nsew")

tk.Label(student_page, text="Add Student", font=("Arial", 18), bg="#f5f5f5").pack(pady=10)

entry_sid = tk.Entry(student_page, width=40)
entry_name = tk.Entry(student_page, width=40)
entry_mobileno = tk.Entry(student_page, width=40)
entry_birthdate = tk.Entry(student_page, width=40)
entry_address = tk.Entry(student_page, width=40)
entry_email = tk.Entry(student_page, width=40)

for label_text, entry in [("Student ID", entry_sid), ("Name", entry_name), ("Mobile No", entry_mobileno),
                          ("Birth Date (YYYY-MM-DD)", entry_birthdate), ("Address", entry_address), ("Email ID", entry_email)]:
    tk.Label(student_page, text=label_text, font=("Arial", 12), bg="#f5f5f5").pack()
    entry.pack(pady=5)

tk.Button(student_page, text="Add Student", command=add_student, bg="#4CAF50", fg="white").pack(pady=10)
tk.Button(student_page, text="Next to Course", command=lambda: show_frame(course_page), bg="#2196F3", fg="white").pack()

# Course Page
course_page = tk.Frame(app, bg="#f5f5f5")
course_page.grid(row=0, column=0, sticky="nsew")

tk.Label(course_page, text="Add Course", font=("Arial", 18), bg="#f5f5f5").pack(pady=10)

entry_course_id = tk.Entry(course_page, width=40)
entry_cname = tk.Entry(course_page, width=40)

for label_text, entry in [("Course ID", entry_course_id), ("Course Name", entry_cname)]:
    tk.Label(course_page, text=label_text, font=("Arial", 12), bg="#f5f5f5").pack()
    entry.pack(pady=5)

tk.Button(course_page, text="Add Course", command=add_course, bg="#4CAF50", fg="white").pack(pady=10)
tk.Button(course_page, text="Next to Faculty", command=lambda: show_frame(faculty_page), bg="#2196F3", fg="white").pack()
tk.Button(course_page, text="Back to Student", command=lambda: show_frame(student_page), bg="#FF9800", fg="white").pack()

# Faculty Page
faculty_page = tk.Frame(app, bg="#f5f5f5")
faculty_page.grid(row=0, column=0, sticky="nsew")

tk.Label(faculty_page, text="Add Faculty", font=("Arial", 18), bg="#f5f5f5").pack(pady=10)

entry_fid = tk.Entry(faculty_page, width=40)
entry_fname = tk.Entry(faculty_page, width=40)
entry_qualification = tk.Entry(faculty_page, width=40)
entry_fmobileno = tk.Entry(faculty_page, width=40)
entry_femail = tk.Entry(faculty_page, width=40)

for label_text, entry in [("Faculty ID", entry_fid), ("Name", entry_fname), ("Qualification", entry_qualification),
                          ("Mobile No", entry_fmobileno), ("Email ID", entry_femail)]:
    tk.Label(faculty_page, text=label_text, font=("Arial", 12), bg="#f5f5f5").pack()
    entry.pack(pady=5)

tk.Button(faculty_page, text="Add Faculty", command=add_faculty, bg="#4CAF50", fg="white").pack(pady=10)
tk.Button(faculty_page, text="Back to Course", command=lambda: show_frame(course_page), bg="#FF9800", fg="white").pack()
tk.Button(faculty_page, text="Exit", command=app.quit, bg="#F44336", fg="white").pack(pady=10)

# Start on the student page
show_frame(student_page)

app.mainloop()
