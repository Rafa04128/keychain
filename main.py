import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import bcrypt  # Make sure to install the bcrypt library
from loginapp import LoginApp

my_obj = LoginApp()

if __name__ == "__main__":
    app = my_obj()
    app.root.mainloop()
