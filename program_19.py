
import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
from PIL import Image, ImageTk

# Create main window
root = tk.Tk()
root.title("Dynamic Image/File Viewer")
root.geometry("700x600")

# Heading
heading = tk.Label(
    root,
    text="IMAGE / FILE VIEWER",
    font=("Arial", 20, "bold"),
    fg="blue"
)
heading.pack(pady=10)

# File name label
file_label = tk.Label(
    root,
    text="No file selected",
    font=("Arial", 12)
)
file_label.pack(pady=5)

# Display area
display = tk.Label(
    root,
    text="Open an image or text file",
    font=("Arial", 14),
    bg="lightgray",
    width=60,
    height=15
)
display.pack(padx=10, pady=10)

# Store image reference
current_image = None


# Open file function
def open_file():
    global current_image

    filename = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[
            ("All Supported Files", "*.png *.jpg *.jpeg *.gif *.txt"),
            ("Image Files", "*.png *.jpg *.jpeg *.gif"),
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if not filename:
        return

    file_label.config(text="File: " + filename)

    try:
        if filename.lower().endswith(
            (".png", ".jpg", ".jpeg", ".gif")
        ):
            img = Image.open(filename)
            img.thumbnail((500, 350))

            current_image = ImageTk.PhotoImage(img)

            display.config(
                image=current_image,
                text="",
                bg="white"
            )

        elif filename.lower().endswith(".txt"):
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()

            display.config(
                image="",
                text=content,
                font=("Arial", 12),
                bg="white",
                width=65,
                height=15,
                wraplength=550
            )

        else:
            messagebox.showwarning(
                "Unsupported File",
                "Please select an image or text file."
            )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Change background color
def change_color():
    color = colorchooser.askcolor(
        title="Choose Background Color"
    )

    if color[1]:
        display.config(bg=color[1])


# Clear display
def clear_display():
    global current_image

    current_image = None

    display.config(
        image="",
        text="Open an image or text file",
        bg="lightgray"
    )

    file_label.config(text="No file selected")


# Enter key event
def enter_event(event):
    open_file()


# Buttons
tk.Button(
    root,
    text="OPEN FILE",
    font=("Arial", 12),
    command=open_file,
    bg="lightgreen"
).pack(pady=5)

tk.Button(
    root,
    text="CHANGE COLOR",
    font=("Arial", 12),
    command=change_color,
    bg="lightblue"
).pack(pady=5)

tk.Button(
    root,
    text="CLEAR",
    font=("Arial", 12),
    command=clear_display,
    bg="lightcoral"
).pack(pady=5)

# Bind Enter key
root.bind("<Return>", enter_event)

# Exit button
tk.Button(
    root,
    text="EXIT",
    command=root.destroy,
    bg="orange"
).pack(pady=5)

# Run application
root.mainloop()
