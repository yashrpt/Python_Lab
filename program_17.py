
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Desktop Calculator")
root.geometry("350x450")
root.resizable(False, False)

# Display variable
expression = ""

# Display field
display = tk.Entry(
    root,
    font=("Arial", 22),
    borderwidth=5,
    relief="ridge",
    justify="right"
)
display.grid(row=0, column=0, columnspan=4,
             padx=10, pady=15, ipady=10, sticky="nsew")


# Button click function
def button_click(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)


# Clear function
def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)


# Calculate function
def calculate():
    global expression

    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
        expression = str(result)

    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(tk.END, "Cannot divide by zero")
        expression = ""

    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Invalid Input")
        expression = ""


# Calculator buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Create buttons using grid
for (text, row, col) in buttons:
    if text == "=":
        command = calculate
    else:
        command = lambda value=text: button_click(value)

    tk.Button(
        root,
        text=text,
        font=("Arial", 18),
        width=5,
        height=2,
        command=command
    ).grid(row=row, column=col, padx=5, pady=5)


# Clear button
tk.Button(
    root,
    text="CLEAR",
    font=("Arial", 16),
    command=clear,
    bg="lightcoral"
).grid(row=5, column=0, columnspan=4,
       padx=5, pady=10, sticky="nsew")


# Run application
root.mainloop()
