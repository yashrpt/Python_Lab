
import tkinter as tk
from tkinter import messagebox
import json

# Main Application Class
class DashboardApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Frame Dashboard")
        self.root.geometry("700x500")

        # Application state
        self.username = tk.StringVar()
        self.theme = tk.StringVar(value="Light")

        # Create menu bar
        self.create_menu()

        # Main container
        self.container = tk.Frame(root)
        self.container.pack(fill="both", expand=True)

        # Create frames
        self.frames = {}

        for F in (HomePage, SettingsPage, AboutPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    # Create menu bar
    def create_menu(self):
        menubar = tk.Menu(self.root)

        # Navigation menu
        nav_menu = tk.Menu(menubar, tearoff=0)
        nav_menu.add_command(
            label="Home",
            command=lambda: self.show_frame(HomePage)
        )
        nav_menu.add_command(
            label="Settings",
            command=lambda: self.show_frame(SettingsPage)
        )
        nav_menu.add_command(
            label="About",
            command=lambda: self.show_frame(AboutPage)
        )
        menubar.add_cascade(label="Navigate", menu=nav_menu)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(
            label="Save Configuration",
            command=self.save_config
        )
        file_menu.add_separator()
        file_menu.add_command(
            label="Exit",
            command=self.root.destroy
        )
        menubar.add_cascade(label="File", menu=file_menu)

        self.root.config(menu=menubar)

    # Display selected frame
    def show_frame(self, page):
        self.frames[page].tkraise()

    # Save configuration
    def save_config(self):
        config = {
            "username": self.username.get(),
            "theme": self.theme.get()
        }

        try:
            with open("dashboard_config.json", "w") as file:
                json.dump(config, file, indent=4)

            messagebox.showinfo(
                "Success",
                "Dashboard configuration saved successfully!"
            )

        except Exception as e:
            messagebox.showerror("Error", str(e))


# Home Page
class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        tk.Label(
            self,
            text="WELCOME TO DASHBOARD",
            font=("Arial", 22, "bold"),
            fg="blue"
        ).pack(pady=30)

        tk.Label(
            self,
            text="This is the Home Page",
            font=("Arial", 14)
        ).pack(pady=10)

        tk.Button(
            self,
            text="Go to Settings",
            command=lambda: controller.show_frame(SettingsPage)
        ).pack(pady=10)

        tk.Button(
            self,
            text="About Application",
            command=lambda: controller.show_frame(AboutPage)
        ).pack(pady=10)


# Settings Page
class SettingsPage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        tk.Label(
            self,
            text="DASHBOARD SETTINGS",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        # Username input
        tk.Label(self, text="Enter Username:").pack()

        tk.Entry(
            self,
            textvariable=controller.username,
            width=30
        ).pack(pady=10)

        # Theme selection
        tk.Label(self, text="Select Theme:").pack()

        tk.Radiobutton(
            self,
            text="Light",
            variable=controller.theme,
            value="Light"
        ).pack()

        tk.Radiobutton(
            self,
            text="Dark",
            variable=controller.theme,
            value="Dark"
        ).pack()

        tk.Button(
            self,
            text="Save Configuration",
            command=controller.save_config,
            bg="lightgreen"
        ).pack(pady=15)

        tk.Button(
            self,
            text="Back to Home",
            command=lambda: controller.show_frame(HomePage)
        ).pack()


# About Page
class AboutPage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(
            self,
            text="ABOUT APPLICATION",
            font=("Arial", 22, "bold"),
            fg="blue"
        ).pack(pady=30)

        tk.Label(
            self,
            text="Multi-Frame Graphical Dashboard\n"
                 "Developed using Python Tkinter.",
            font=("Arial", 14),
            justify="center"
        ).pack(pady=20)

        tk.Button(
            self,
            text="Back to Home",
            command=lambda: controller.show_frame(HomePage)
        ).pack(pady=10)


# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()
