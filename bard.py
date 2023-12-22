import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

class LoginApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login Screen")
        self.setup_ui()

    def setup_ui(self):
        # Center the window
        window_width = 300
        window_height = 300
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Create login widgets
        self.label_username = tk.Label(self.root, text="Username:")
        self.label_username.pack(pady=5)
        self.entry_username = tk.Entry(self.root)
        self.entry_username.pack(pady=5)
        # Create password label and entry
        self.label_password = tk.Label(self.root, text="Password:")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(self.root, show="*")  # Hide password characters
        self.entry_password.pack(pady=5)

        
        # Create login button
        self.button_login = tk.Button(self.root, text="Login", command=self.login)
        self.button_login.pack(pady=5)

        # Create error label
        self.error_label = tk.Label(self.root, text="", fg="red")
        self.error_label.pack(pady=5)

        # Create register button
        self.button_register = tk.Button(self.root, text="Register", command=self.open_registration_window)
        self.button_register.pack(pady=10)

        self.error_label = tk.Label(self.root, text="", fg="red")
        self.error_label.pack(pady=5)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        try:
            with sqlite3.connect("user_database.db") as connection:
                cursor = connection.cursor()

                cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
                user = cursor.fetchone()

                if user:
                    self.error_label.config(text="")  # Clear any previous error messages
                    messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
                    # Redirect to the main application or perform other actions after successful login
                else:
                    self.error_label.config(text="Invalid username or password")

        except sqlite3.Error as error:
            self.error_label.config(text="Database error: {}".format(error))

    def open_registration_window(self):
        
        self.registration_window = tk.Toplevel(self.root)
        self.registration_window.title("RafaKC Registration")

        # Create registration widgets (similar to main window)
        
        self.label_reg_username = tk.Label(self.registration_window, text="Username:")
        self.entry_reg_username = tk.Entry(self.registration_window)
        # ... (Add other labels and entry fields for password, name, and last name)

        self.button_register = tk.Button(self.registration_window, text="Register", command=self.register_user)
        self.error_label_reg = tk.Label(self.registration_window, text="", fg="red")

        self.label_reg_username.grid(row=0, column=0, sticky="W", padx=5, pady=5)
        self.entry_reg_username.grid(row=0, column=1, padx=5, pady=5)

        self.label_reg_password = tk.Label(self.registration_window, text="Password:")
        self.label_reg_password.grid(row=1, column=0, sticky="W", padx=5, pady=5)
        self.entry_reg_password = tk.Entry(self.registration_window, show="*")
        self.entry_reg_password.grid(row=1, column=1, padx=5, pady=5)

        self.label_name = tk.Label(self.registration_window, text="Name:")
        self.label_name.grid(row=2, column=0, sticky="W", padx=5, pady=5)
        self.entry_name = tk.Entry(self.registration_window)
        self.entry_name.grid(row=2, column=1, padx=5, pady=5)

        self.label_last_name = tk.Label(self.registration_window, text="Last Name:")
        self.label_last_name.grid(row=3, column=0, sticky="W", padx=5, pady=5)
        self.entry_last_name = tk.Entry(self.registration_window)
        self.entry_last_name.grid(row=3, column=1, padx=5, pady=5)

        self.button_register.grid(row=4, column=0, columnspan=2, pady=10)
        self.error_label_reg.grid(row=5, column=0, columnspan=2, pady=5)

    def register_user(self):
        new_username = self.entry_reg_username.get()
        new_password = self.entry_reg_password.get()
        new_name = self.entry_name.get()  # Assuming you've added these entry fields
        new_last_name = self.entry_last_name.get()

        try:
            with sqlite3.connect("user_database.db") as connection:
                cursor = connection.cursor()

                cursor.execute("SELECT * FROM users WHERE username=?", (new_username,))
                existing_user = cursor.fetchone()

                if existing_user:
                    self.error_label_reg.config(text="Username already exists")
                else:
                    if not new_username or not new_password or not new_name or not new_last_name:
                        self.error_label_reg.config(text="All fields must be filled")
                    else:
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        cursor.execute(
                            "INSERT INTO users (username, password, name, last_name, registration_time) VALUES (?, ?, ?, ?, ?)",
                            (new_username, new_password, new_name, new_last_name, current_time)
                        )
                        connection.commit()
                        self.error_label_reg.config(text="New user registered")
                        self.registration_window.destroy()  # Close registration window

        except sqlite3.Error as error:
            self.error_label_reg.config(text="Database error: {}".format(error))

if __name__ == "__main__":
    app = LoginApp()
    app.root.mainloop()