import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import mysql.connector

# Database connection
def connect_to_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nimisha@2004",  # Replace with your MySQL password
            database="dbmsproj"
        )
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error connecting to database: {err}")
        return None


def add_student_course(course_window, student_id, entry_course_id):
    conn = connect_to_db()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        course_data = (student_id, entry_course_id.get())
        cursor.execute("INSERT INTO stud_course (s_id, course_id) VALUES (%s, %s)", course_data)
        conn.commit()
        messagebox.showinfo("Success", "Course added for student successfully!")
        course_window.destroy()  # Close the course input window
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")
    finally:
        cursor.close()
        conn.close()

def ask_for_course_details(student_id):
    # Create a new window for course input
    course_window = tk.Toplevel(app)
    course_window.title("Add Course for Student")
    course_window.geometry("300x200")

    tk.Label(course_window, text="Course ID:", bg="#ffffff").pack(pady=5)
    entry_course_id = tk.Entry(course_window)
    entry_course_id.pack(pady=5)

    # Pass course_window and entry_course_id to the function
    tk.Button(course_window, text="Add Course", command=lambda: add_student_course(course_window, student_id, entry_course_id), 
              font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=10)

    # Back button to close course window
    tk.Button(course_window, text="Back", command=course_window.destroy, font=("Arial", 10), bg="#FF9800", fg="white").pack(pady=5)


# Function to insert data into the student table
def add_student():
    conn = connect_to_db()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        student_data = (
            entry_sid.get(),
            entry_name.get(),
            entry_mobileno.get(),
            entry_birthdate.get(),
            entry_address.get(),
            entry_email.get()
        )
        
        cursor.execute(
            "INSERT INTO student (s_id, name, mobileno, birth_date, address, email_id) VALUES (%s, %s, %s, %s, %s, %s)",
            student_data
        )
        
        conn.commit()
        messagebox.showinfo("Success", "Student added successfully!")
        ask_for_course_details(student_data[0])
        clear_student_entries()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")
    finally:
        cursor.close()
        conn.close()
# Ensure the function is defined before being used


def clear_student_entries():
    entry_sid.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_mobileno.delete(0, tk.END)
    entry_birthdate.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Function to insert data into the course table
def add_course():
    conn = connect_to_db()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        course_data = (entry_course_id.get(), entry_cname.get())
        cursor.execute("INSERT INTO course (course_id, cname) VALUES (%s, %s)", course_data)
        conn.commit()
        messagebox.showinfo("Success", "Course added successfully!")
        clear_course_entries()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")
    finally:
        cursor.close()
        conn.close()

def clear_course_entries():
    entry_course_id.delete(0, tk.END)
    entry_cname.delete(0, tk.END)

# Function to insert data into the faculty table
def add_faculty():
    conn = connect_to_db()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        faculty_data = (
            entry_fid.get(),
            entry_fname.get(),
            entry_qualification.get(),
            entry_fmobileno.get(),
            entry_femail.get()
        )
        cursor.execute("INSERT INTO faculty (f_id, f_name, qualification, mobileno, email_id) VALUES (%s, %s, %s, %s, %s)", faculty_data)
        conn.commit()
        messagebox.showinfo("Success", "Faculty added successfully!")
        clear_faculty_entries()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")
    finally:
        cursor.close()
        conn.close()

def clear_faculty_entries():
    entry_fid.delete(0, tk.END)
    entry_fname.delete(0, tk.END)
    entry_qualification.delete(0, tk.END)
    entry_fmobileno.delete(0, tk.END)
    entry_femail.delete(0, tk.END)

# View Records Functions
def view_records():
    show_frame(view_records_page)

def show_student_records():
    conn = connect_to_db()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # Clear the existing data in the treeview
    for row in student_tree.get_children():
        student_tree.delete(row)
    
    # Insert new data
    for record in records:
        student_tree.insert("", tk.END, values=record)

def show_course_records():
    conn = connect_to_db()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course")
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # Clear the existing data in the treeview
    for row in course_tree.get_children():
        course_tree.delete(row)

    # Insert new data
    for record in records:
        course_tree.insert("", tk.END, values=record)

def show_faculty_records():
    conn = connect_to_db()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM faculty")
    records = cursor.fetchall()
    cursor.close()
    conn.close()

    # Clear the existing data in the treeview
    for row in faculty_tree.get_children():
        faculty_tree.delete(row)

    # Insert new data
    for record in records:
        faculty_tree.insert("", tk.END, values=record)

# Load and set the background image
def load_background():
    try:
        background_image = Image.open("image4.jpg")
        background_image = background_image.resize((600, 550), Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(background_image)

        bg_label = tk.Label(app, image=bg_img)
        bg_label.image = bg_img  # Keep a reference to avoid garbage collection
        bg_label.place(relwidth=1, relheight=1)
    except FileNotFoundError:
        print("FileNotFoundError: Background image not found. Please check the path.")
    except Exception as e:
        print("Error loading background image:", e)

# GUI Setup
app = tk.Tk()
app.title("DBMS Project - MySQL Records Management")
app.geometry("600x550")

load_background()

# Navigation between pages
def show_frame(frame):
    frame.tkraise()

# Front Page
front_page = tk.Frame(app, bg="#ffffff", bd=2, relief="raised")
front_page.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

tk.Label(front_page, text="Welcome to the DBMS Project", font=("Arial", 24, "bold"), bg="#ffffff").pack(pady=50)

tk.Button(front_page, text="Add Student", command=lambda: show_frame(student_page), font=("Arial", 16), bg="#4CAF50", fg="white").pack(pady=10)
tk.Button(front_page, text="Add Course", command=lambda: show_frame(course_page), font=("Arial", 16), bg="#2196F3", fg="white").pack(pady=10)
tk.Button(front_page, text="Add Faculty", command=lambda: show_frame(faculty_page), font=("Arial", 16), bg="#FF9800", fg="white").pack(pady=10)
tk.Button(front_page, text="View Records", command=view_records, font=("Arial", 16), bg="#F44336", fg="white").pack(pady=10)

# View Records Page
view_records_page = tk.Frame(app, bg="#ffffff", bd=2, relief="raised")
view_records_page.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

tk.Label(view_records_page, text="View Records", font=("Arial", 18, "bold"), bg="#ffffff").pack(pady=20)

tk.Button(view_records_page, text="View Student Records", command=lambda: [show_student_records(), show_frame(student_records_page)], font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(view_records_page, text="View Course Records", command=lambda: [show_course_records(), show_frame(course_records_page)], font=("Arial", 12), bg="#2196F3", fg="white").pack(pady=5)
tk.Button(view_records_page, text="View Faculty Records", command=lambda: [show_faculty_records(), show_frame(faculty_records_page)], font=("Arial", 12), bg="#FF9800", fg="white").pack(pady=5)

# Button to view specific student details
tk.Button(view_records_page, text="View Specific Student", command=lambda: show_frame(specific_student_page), font=("Arial", 12), bg="#FF9800", fg="white").pack(pady=5)

tk.Button(view_records_page, text="Back to Home", command=lambda: show_frame(front_page), font=("Arial", 10, "bold"), bg="#FF9800", fg="white").pack()

# Student Page Setup
student_page = tk.Frame(app, bg="#ffffff", bd=2, relief="raised")
student_page.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

tk.Label(student_page, text="Add Student", font=("Arial", 18, "bold"), bg="#ffffff").pack(pady=20)

# Entry fields for student data
tk.Label(student_page, text="Student ID:", bg="#ffffff").pack()
entry_sid = tk.Entry(student_page)
entry_sid.pack()

tk.Label(student_page, text="Name:", bg="#ffffff").pack()
entry_name = tk.Entry(student_page)
entry_name.pack()

tk.Label(student_page, text="Mobile No:", bg="#ffffff").pack()
entry_mobileno = tk.Entry(student_page)
entry_mobileno.pack()

tk.Label(student_page, text="Birth Date (YYYY-MM-DD):", bg="#ffffff").pack()
entry_birthdate = tk.Entry(student_page)
entry_birthdate.pack()

tk.Label(student_page, text="Address:", bg="#ffffff").pack()
entry_address = tk.Entry(student_page)
entry_address.pack()

tk.Label(student_page, text="Email:", bg="#ffffff").pack()
entry_email = tk.Entry(student_page)
entry_email.pack()

# Button to add student
tk.Button(student_page, text="Add Student", command=add_student, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=10)

# Clear entries button (optional)
tk.Button(student_page, text="Clear Entries", command=clear_student_entries, font=("Arial", 10), bg="#FF9800", fg="white").pack(pady=10)

# Back button for Student Page
tk.Button(student_page, text="Back", command=lambda: show_frame(front_page), font=("Arial", 10), bg="#FF9800", fg="white").pack(pady=10)

# Course Page Setup
course_page = tk.Frame(app, bg="#ffffff", bd=2, relief="raised")
course_page.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

tk.Label(course_page, text="Add Course", font=("Arial", 18, "bold"), bg="#ffffff").pack(pady=20)

# Entry fields for course data
tk.Label(course_page, text="Course ID:", bg="#ffffff").pack()
entry_course_id = tk.Entry(course_page)
entry_course_id.pack()

tk.Label(course_page, text="Course Name:", bg="#ffffff").pack()
entry_cname = tk.Entry(course_page)
entry_cname.pack()

# Button to add course
tk.Button(course_page, text="Add Course", command=add_course, font=("Arial", 12), bg="#2196F3", fg="white").pack(pady=10)

# Clear entries button (optional)
tk.Button(course_page, text="Clear Entries", command=clear_course_entries, font=("Arial", 10), bg="#FF9800", fg="white").pack(pady=10)

# Back button for Course Page
tk.Button(course_page, text="Back", command=lambda: show_frame(front_page), font=("Arial", 10), bg="#FF9800", fg="white").pack(pady=10)

# Faculty Page Setup
faculty_page = tk.Frame(app, bg="#ffffff", bd=2, relief="raised")
faculty_page.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

tk.Label(faculty_page, text="Add Faculty", font=("Arial", 18, "bold"), bg="#ffffff").pack(pady=20)

# Entry fields for faculty data
tk.Label(faculty_page, text="Faculty ID:", bg="#ffffff").pack()
entry_fid = tk.Entry(faculty_page)
entry_fid.pack()

tk.Label(faculty_page, text="Name:", bg="#ffffff").pack()
entry_fname = tk.Entry(faculty_page)
entry_fname.pack()

tk.Label(faculty_page, text="Qualification:", bg="#ffffff").pack()
entry_qualification = tk.Entry(faculty_page)
entry_qualification.pack()

tk.Label(faculty_page, text="Mobile No:", bg="#ffffff").pack()
entry_fmobileno = tk.Entry(faculty_page)
entry_fmobileno.pack()

tk.Label(faculty_page, text="Email:", bg="#ffffff").pack()
entry_femail = tk.Entry(faculty_page)
entry_femail.pack()

# Button to add faculty
tk.Button(faculty_page, text="Add Faculty", command=add_faculty, font=("Arial", 12), bg="#FF9800", fg="white").pack(pady=10)

# Clear entries button (optional)
tk.Button(faculty_page, text="Clear Entries", command=clear_faculty_entries, font=("Arial", 10), bg="#FF9800", fg="white").pack(pady=10)

# Back button for Faculty Page
tk.Button(faculty_page, text="Back", command=lambda: show_frame(front_page), font=("Arial", 10), bg="#FF9800", fg="white").pack(pady=10)

# Student Records Page Setup
student_records_page = tk.Frame(app, bg="#ffffff", bd=2, relief="raised")
student_records_page.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

tk.Label(student_records_page, text="Student Records", font=("Arial", 18, "bold"), bg="#ffffff").pack(pady=20)

# Treeview for displaying student records
student_tree = ttk.Treeview(student_records_page, columns=("s_id", "name", "mobileno", "birth_date", "address", "email_id"), show='headings')
student_tree.heading("s_id", text="Student ID")
student_tree.heading("name", text="Name")
student_tree.heading("mobileno", text="Mobile No")
student_tree.heading("birth_date", text="Birth Date")
student_tree.heading("address", text="Address")
student_tree.heading("email_id", text="Email")
student_tree.pack(expand=True, fill=tk.BOTH)

tk.Button(student_records_page, text="Back", command=lambda: show_frame(view_records_page), font=("Arial", 10), bg="#FF9800", fg="white").pack(pady=10)

# Course Records Page Setup
course_records_page = tk.Frame(app, bg="#ffffff", bd=2, relief="raised")
course_records_page.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

tk.Label(course_records_page, text="Course Records", font=("Arial", 18, "bold"), bg="#ffffff").pack(pady=20)

# Treeview for displaying course records
course_tree = ttk.Treeview(course_records_page, columns=("course_id", "cname"), show='headings')
course_tree.heading("course_id", text="Course ID")
course_tree.heading("cname", text="Course Name")
course_tree.pack(expand=True, fill=tk.BOTH)

tk.Button(course_records_page, text="Back", command=lambda: show_frame(view_records_page), font=("Arial", 10), bg="#FF9800", fg="white").pack(pady=10)

# Faculty Records Page Setup
faculty_records_page = tk.Frame(app, bg="#ffffff", bd=2, relief="raised")
faculty_records_page.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

tk.Label(faculty_records_page, text="Faculty Records", font=("Arial", 18, "bold"), bg="#ffffff").pack(pady=20)

# Treeview for displaying faculty records
faculty_tree = ttk.Treeview(faculty_records_page, columns=("f_id", "f_name", "qualification", "mobileno", "email_id"), show='headings')
faculty_tree.heading("f_id", text="Faculty ID")
faculty_tree.heading("f_name", text="Name")
faculty_tree.heading("qualification", text="Qualification")
faculty_tree.heading("mobileno", text="Mobile No")
faculty_tree.heading("email_id", text="Email")
faculty_tree.pack(expand=True, fill=tk.BOTH)

tk.Button(faculty_records_page, text="Back", command=lambda: show_frame(view_records_page), font=("Arial", 10), bg="#FF9800", fg="white").pack(pady=10)

# Specific Student Details Page Setup
specific_student_page = tk.Frame(app, bg="#ffffff", bd=2, relief="raised")
specific_student_page.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

tk.Label(specific_student_page, text="View Specific Student", font=("Arial", 18, "bold"), bg="#ffffff").pack(pady=20)

tk.Label(specific_student_page, text="Enter Roll Number:", bg="#ffffff").pack()
entry_roll_no = tk.Entry(specific_student_page)
entry_roll_no.pack()

# Button to fetch student details
tk.Button(specific_student_page, text="Get Details", command=lambda: fetch_student_details(entry_roll_no.get()), font=("Arial", 12), bg="#FF9800", fg="white").pack(pady=10)

# Display area for student details
student_details_text = tk.Text(specific_student_page, height=10, width=50)
student_details_text.pack(pady=10)

# Button to fetch academic details
tk.Button(specific_student_page, text="Get Academic Details", command=lambda: fetch_academic_details(entry_roll_no.get()), font=("Arial", 12), bg="#FF9800", fg="white").pack(pady=10)

# Back button for Specific Student Page
tk.Button(specific_student_page, text="Back", command=lambda: show_frame(view_records_page), font=("Arial", 10), bg="#FF9800", fg="white").pack(pady=10)

def fetch_student_details(roll_no):
    conn = connect_to_db()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM student WHERE s_id = %s", (roll_no,))
        record = cursor.fetchone()
        if record:
            details = f"Student ID: {record[0]}\nName: {record[1]}\nMobile No: {record[2]}\nBirth Date: {record[3]}\nAddress: {record[4]}\nEmail: {record[5]}"
            student_details_text.delete(1.0, tk.END)  # Clear previous text
            student_details_text.insert(tk.END, details)
        else:
            messagebox.showinfo("No Record", "No student found with that Roll Number.")
            student_details_text.delete(1.0, tk.END)
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")
    finally:
        cursor.close()
        conn.close()

def fetch_academic_details(roll_no):
    conn = connect_to_db()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM academic WHERE s_id = %s", (roll_no,))
        records = cursor.fetchall()
        if records:
            academic_details = "Academic Details:\n"
            for record in records:
                academic_details += f"Course ID: {record[1]}, Grade: {record[2]}\n"
            student_details_text.insert(tk.END, academic_details)
        else:
            messagebox.showinfo("No Record", "No academic details found for that Roll Number.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")
    finally:
        cursor.close()
        conn.close()

show_frame(front_page)  # Show the front page initially
app.mainloop()
