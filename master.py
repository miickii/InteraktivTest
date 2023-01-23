import tkinter as tk
import customtkinter as ctk
from login import Login
from signup import Signup
from home import Home
from create_test import CreateTest
from select_test import SelectTest
from test import Test
from test_results import TestResults
from db_manager import DBManager

class Master(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.db_manager = DBManager()

        self.title("Interaktiv test")
        self.geometry("600x450")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.curr_frame = None

        self.selected_test_id = None
        self.user_id = None

        # initializing frames to an empty array
        self.frames = {}
        login_frame = Login(self, self.db_manager)
        login_frame.grid(row=0, column=0, sticky="nsew")
        self.frames["login"] = login_frame

        signup_frame = Signup(self, self.db_manager)
        signup_frame.grid(row=0, column=0, sticky="nsew")
        self.frames["signup"] = signup_frame

        home_frame = Home(self)
        home_frame.grid(row=0, column=0, sticky="nsew")
        self.frames["home"] = home_frame

        create_test_frame = CreateTest(self, self.db_manager)
        create_test_frame.grid(row=0, column=0, sticky="nsew")
        self.frames["create_test"] = create_test_frame

        select_test_frame = SelectTest(self, self.db_manager)
        select_test_frame.grid(row=0, column=0, sticky="nsew")
        self.frames["select_test"] = select_test_frame

        test_frame = Test(self, self.db_manager)
        test_frame.grid(row=0, column=0, sticky="nsew")
        self.frames["test"] = test_frame

        test_results_frame = TestResults(self, self.db_manager)
        test_results_frame.grid(row=0, column=0, sticky="nsew")
        self.frames["test_results"] = test_results_frame

        self.show_frame("login")
    
    def show_frame(self, cont):
        if self.curr_frame:
            self.curr_frame.destroy_widgets()

        self.curr_frame = self.frames[cont]
        self.curr_frame.create()
