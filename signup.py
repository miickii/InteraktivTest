import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import sqlite3

class Signup(ctk.CTkFrame):
    def __init__(self, master, db_manager):
        super().__init__(master)
        self.master = master
        self.db_manager = db_manager
        self.widgets = []
    
    def create(self):
        self.signup_frame = ctk.CTkFrame(self.master, width=400, height=300, fg_color="#3A3845")
        self.signup_frame.grid(row=0, column=0, sticky="")
        self.widgets.append(self.signup_frame)

        self.widgets_frame = ctk.CTkFrame(self.signup_frame, width=400, height=300, fg_color="#3A3845")
        self.widgets_frame.grid(row=0, column=0, sticky="", padx=50, pady=(10, 50))
        self.widgets.append(self.widgets_frame)

        self.title = ctk.CTkLabel(self.widgets_frame, text="Signup", font=ctk.CTkFont(size=20, weight="bold"))
        self.title.grid(row=0, column=0, padx=5, pady=5, sticky="news")
        self.widgets.append(self.title)

        self.username_entry = ctk.CTkEntry(self.widgets_frame, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=5, pady=5, sticky="news", columnspan=2)
        self.widgets.append(self.username_entry)

        self.password_entry = ctk.CTkEntry(self.widgets_frame, placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=5, pady=5, sticky="news", columnspan=2)
        self.password_entry.configure(show="*")
        self.widgets.append(self.password_entry)

        self.password2_entry = ctk.CTkEntry(self.widgets_frame, placeholder_text="password")
        self.password2_entry.grid(row=3, column=0, padx=5, pady=5, sticky="news", columnspan=2)
        self.password2_entry.configure(show="*")
        self.widgets.append(self.password2_entry)

        self.signup_button = ctk.CTkButton(self.widgets_frame, text="Sign up", command=self.submit)
        self.signup_button.grid(row=4, column=0, padx=5, pady=5)
        self.widgets.append(self.signup_button)

        self.back_button = ctk.CTkButton(self.widgets_frame, text="Back", command=self.back)
        self.back_button.grid(row=4, column=1, padx=5, pady=5)
        self.widgets.append(self.back_button)
    
    def destroy_widgets(self):
        self.signup_frame.destroy()

    def submit(self):
        name = self.username_entry.get()
        password = self.password_entry.get()
        password2 = self.password2_entry.get()


        if name and password and password2:
            if password != password2:
                messagebox.showerror("Error", "Passords do not match")
                return

            user = self.db_manager.get_user(name)

            if user:
                messagebox.showerror("Error", "Username already exists")
                return
            
            self.db_manager.add_user(name, password)

            messagebox.showinfo("Info", "Sign up successful!")
            self.master.show_frame("login")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def back(self):
        self.master.show_frame("login")

