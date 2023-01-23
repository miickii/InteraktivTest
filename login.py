import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import sqlite3

class Login(ctk.CTkFrame):
    def __init__(self, master, db_manager):
        super().__init__(master, fg_color="#333333")
        self.master = master
        self.db_manager = db_manager

        self.widgets = []
    
    def create(self):
        self.login_frame = ctk.CTkFrame(self.master, width=400, height=300, fg_color="#3A3845")
        self.login_frame.grid(row=0, column=0, sticky="")
        self.widgets.append(self.login_frame)
        
        self.widgets_frame = ctk.CTkFrame(self.login_frame, width=400, height=300, fg_color="#3A3845")
        self.widgets_frame.grid(row=0, column=0, sticky="", padx=50, pady=(10, 50))
        self.widgets.append(self.widgets_frame)

        self.title = ctk.CTkLabel(self.widgets_frame, text="Login", font=ctk.CTkFont(size=20, weight="bold"))
        self.title.grid(row=0, column=0, padx=5, pady=5, sticky="news")
        self.widgets.append(self.title)

        self.username_entry = ctk.CTkEntry(self.widgets_frame, placeholder_text="username...")
        self.username_entry.grid(row=1, column=0, padx=5, pady=5, sticky="news", columnspan=2)
        self.widgets.append(self.username_entry)

        self.password_entry = ctk.CTkEntry(self.widgets_frame, placeholder_text="password...")
        self.password_entry.grid(row=2, column=0, padx=5, pady=5, sticky="news", columnspan=2)
        self.password_entry.configure(show="*")
        self.widgets.append(self.password_entry)

        self.login_button = ctk.CTkButton(self.widgets_frame, text="Login", command=self.login)
        self.login_button.grid(row=3, column=0, padx=5, pady=5)
        self.widgets.append(self.login_button)

        self.signup_button = ctk.CTkButton(self.widgets_frame, text="Sign up", command=self.signup)
        self.signup_button.grid(row=3, column=1, padx=5, pady=5)
        self.widgets.append(self.signup_button)
    
    def destroy_widgets(self):
        self.login_frame.destroy()

    def login(self):
        name = self.username_entry.get()
        password = self.password_entry.get()
        if name and password:
            user = self.db_manager.get_user(name)

            if not user:
                messagebox.showerror("Error", "Username invalid")
                return
            
            id, user_name, user_password = user
            if user_password != password:
                messagebox.showerror("Error", "Password incorrect")
                return
            
            self.master.user_id = id
            self.master.show_frame("home")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def signup(self):
        self.master.show_frame("signup")