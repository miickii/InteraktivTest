import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import sqlite3

class Home(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.widgets = []
    
    def create(self):
        self.container = ctk.CTkFrame(self.master, width=400, height=100, fg_color="#3A3845")
        self.container.grid(row=0, column=0, sticky="")

        self.widgets_frame = ctk.CTkFrame(self.container, width=400, height=300, fg_color="#3A3845")
        self.widgets_frame.grid(row=0, column=0, sticky="", padx=50)

        self.select_test_button = ctk.CTkButton(self.widgets_frame, text="Select test", command=self.select_test)
        self.select_test_button.grid(row=0, column=0, pady=15)

        self.create_test_button = ctk.CTkButton(self.widgets_frame, text="Create test", command=self.create_test)
        self.create_test_button.grid(row=1, column=0, pady=15)

        self.test_results_button = ctk.CTkButton(self.widgets_frame, text="Test results", command=lambda: self.master.show_frame("test_results"))
        self.test_results_button.grid(row=2, column=0, pady=15)

        self.logout_button = ctk.CTkButton(self.widgets_frame, text="Log out", command=self.log_out)
        self.logout_button.grid(row=3, column=0, pady=15)
    
    def destroy_widgets(self):
        self.container.destroy()
    
    def select_test(self):
        self.master.show_frame("select_test")

    def show_test_results(self):
        pass

    def create_test(self):
        self.master.show_frame("create_test")
    
    def log_out(self):
        self.master.user_id = None
        self.master.show_frame("login")