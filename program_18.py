
import tkinter as tk
from tkinter import messagebox, filedialog

# Create main window
root = tk.Tk()
root.title("Student Record Manager")
root.geometry("550x650")

# Variables
name_var = tk.StringVar()
roll_var = tk.StringVar()
course_var = tk.StringVar()
gender_var = tk.StringVar(value="Male")

# Heading
tk.Label(
    root,
    text="STUDENT RECORD MANAGER",
    font=("Arial", 18, "bold"),
    fg="blue"
).pack(pady=10)

# Student Name
tk.Label(root, text="Student Name:").pack()
name_entry = tk.Entry(root, textvariable=name_var, width=40)
name_entry.pack(pady=5)

# Roll Number
tk.Label(root, text="Roll Number:").pack()
roll_entry = tk.Entry(root, textvariable=roll_var, width=40)
roll_entry.pack(pady=5)

# Course
tk.Label(root, text="Course:").pack()
course_entry = tk.Entry(root, textvariable=course_var, width=40)
course_entry.pack(pady=5)

# Gender
tk.Label(root, text="Gender:").pack()

gender_frame = tk.Frame(root)
gender_frame.pack()

tk.Radiobutton(
    gender_frame, text="Male",
    variable=gender_var, value="Male"
).pack(side=tk.LEFT)

tk.Radiobutton(
    gender_frame, text="Female",
    variable=gender_var, value="Female"
).pack(side=tk.LEFT)

# Subjects
tk.Label(root, text="Select Subjects:").pack(pady=5)

python_var = tk.IntVar()
java_var = tk.IntVar()
dbms_var = tk.IntVar()

tk.Checkbutton(
    root, text="Python", variable=python_var
).pack()

tk.Checkbutton(
    root, text="Java", variable=java_var
).pack()

tk.Checkbutton(
    root, text="DBMS", variable=dbms_var
).pack()

# Address
tk.Label(root, text="Address:").pack(pady=5)

address_text = tk.Text(root, width=40, height=4)
address_text.pack(pady=5)

# Record display
tk.Label(
    root, text="Student Records",
    font=("Arial", 12, "bold")
).pack(pady=5)

record_display = tk.Text(root, width=60, height=10)
record_display.pack(pady=5)


# Get student details
def get_record():
    name = name_var.get().strip()
    roll = roll_var.get().strip()
    course = course_var.get().strip()
    gender = gender_var.get()

    subjects = []

    if python_var.get():
        subjects.append("Python")
    if java_var.get():
        subjects.append("Java")
    if dbms_var.get():
        subjects.append("DBMS")

    address = address_text.get("1.0", tk.END).strip()

    if not name or not roll or not course:
        messagebox.showwarning(
            "Warning", "Please fill all required fields!"
        )
        return None

    return (
        f"Name: {name}\n"
        f"Roll Number: {roll}\n"
        f"Course: {course}\n"
        f"Gender: {gender}\n"
        f"Subjects: {', '.join(subjects)}\n"
        f"Address: {address}\n"
        f"{'-'*40}\n"
    )


# Add record
def add_record():
    record = get_record()

    if record is not None:
        record_display.insert(tk.END, record)
        messagebox.showinfo(
            "Success", "Student record added successfully!"
        )


# Save records
def save_records():
    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(record_display.get("1.0", tk.END))

        messagebox.showinfo(
            "Success", "Records saved successfully!"
        )


# Open records
def open_records():
    filename = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )

    if filename:
        with open(filename, "r", encoding="utf-8") as file:
            data = file.read()

        record_display.delete("1.0", tk.END)
        record_display.insert(tk.END, data)

        messagebox.showinfo(
            "Success", "Records loaded successfully!"
        )


# Delete records
def delete_record():
    selected = record_display.tag_ranges(tk.SEL)

    if selected:
        record_display.delete(tk.SEL_FIRST, tk.SEL_LAST)
    else:
        record_display.delete("1.0", tk.END)

    messagebox.showinfo(
        "Deleted", "Selected text or all records deleted!"
    )


# Search record
def search_record():
    roll = roll_var.get().strip()

    if not roll:
        messagebox.showwarning(
            "Warning", "Enter roll number to search!"
        )
        return

    data = record_display.get("1.0", tk.END)
    records = data.split("-" * 40)

    for record in records:
        if f"Roll Number: {roll}\n" in record:
            messagebox.showinfo("Record Found", record)
            return

    messagebox.showinfo(
        "Not Found", "Student record not found!"
    )


# Buttons
tk.Button(
    root, text="ADD RECORD",
    command=add_record, bg="lightgreen"
).pack(pady=5)

tk.Button(
    root, text="SEARCH RECORD",
    command=search_record, bg="lightblue"
).pack(pady=5)

tk.Button(
    root, text="DELETE RECORD",
    command=delete_record, bg="lightcoral"
).pack(pady=5)

tk.Button(
    root, text="SAVE RECORDS",
    command=save_records
).pack(pady=5)

tk.Button(
    root, text="OPEN RECORDS",
    command=open_records
).pack(pady=5)

# Run application
root.mainloop()
