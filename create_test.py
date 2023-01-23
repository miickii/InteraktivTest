from tkinter import messagebox
import customtkinter as ctk
import sqlite3

class CreateTest(ctk.CTkFrame):
    def __init__(self, master, db_manager):
        super().__init__(master)
        self.master = master
        self.db_manager = db_manager

        self.test_id = None
        self.curr_question_id = 1
    
    def create(self):
        self.container = ctk.CTkFrame(self.master, width=400, height=100)
        self.container.grid(row=0, column=0, sticky="nsew")
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(1, weight=1)
    
        self.topbar = ctk.CTkFrame(self.container, width=400, height=100, fg_color="#3A3845")
        self.topbar.grid(row=0, column=0, sticky="nwe")
        self.topbar.grid_columnconfigure(0, weight=1)

        self.topbar_buttons_frame = ctk.CTkFrame(self.topbar, width=400, height=100, fg_color="#3A3845")
        self.topbar_buttons_frame.grid(row=0, column=0, sticky="", pady=20)
        self.topbar_buttons_frame.grid_columnconfigure(0, weight=1)

        self.home_button = ctk.CTkButton(self.topbar_buttons_frame, text="Home", command=self.home)
        self.home_button.grid(row=0, column=0, padx=15)

        self.test_results_button = ctk.CTkButton(self.topbar_buttons_frame, text="Test results", command=self.show_test_results)
        self.test_results_button.grid(row=0, column=1, padx=15)

        self.logout_button = ctk.CTkButton(self.topbar_buttons_frame, text="Log out", command=self.log_out)
        self.logout_button.grid(row=0, column=3, padx=15)

        self.content = ctk.CTkFrame(self.container, width=400)
        self.content.grid(row=1, column=0, sticky="nsew")
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_rowconfigure(0, weight=1)

        self.create_frame = ctk.CTkFrame(self.content, width=400, height=300, fg_color="#3A3845")
        self.create_frame.grid(row=0, column=0, sticky="")

        self.create_widgets_frame = ctk.CTkFrame(self.create_frame, width=400, height=300, fg_color="#3A3845")
        self.create_widgets_frame.grid(row=0, column=0, sticky="", padx=50, pady=(10, 50))

        self.test_name_label = ctk.CTkLabel(self.create_widgets_frame, text="Test name", font=ctk.CTkFont(size=20, weight="bold"))
        self.test_name_label.grid(row=0, column=0, pady=5, sticky="n")

        self.test_name_entry = ctk.CTkEntry(self.create_widgets_frame, placeholder_text="name")
        self.test_name_entry.grid(row=1, column=0, pady=5, sticky="n")

        self.next_button = ctk.CTkButton(self.create_widgets_frame, text="Next", command=self.create_test)
        self.next_button.grid(row=2, column=0, padx=5, pady=5)
    
    def destroy_widgets(self):
        self.container.destroy()
    
    def create_test(self):
        test_name = self.test_name_entry.get()
        if self.db_manager.get_test(test_name):
            messagebox.showerror("Error", "A test with that name already exists")
        else:
            self.db_manager.add_test(test_name)
            self.test_id = self.db_manager.get_test(test_name)[0]
            self.update_question()
    
    def update_question(self):
            self.create_widgets_frame.destroy()
            self.create_widgets_frame = ctk.CTkFrame(self.create_frame, width=400, height=300, fg_color="#3A3845")
            self.create_widgets_frame.grid(row=0, column=0, sticky="", padx=50, pady=(10, 50))

            self.question_label = ctk.CTkLabel(self.create_widgets_frame, text=str(self.curr_question_id) + " Question: ", font=ctk.CTkFont(size=16, weight="bold"))
            self.question_label.grid(row=1, column=0, pady=5, sticky="n")
            self.question_entry = ctk.CTkEntry(self.create_widgets_frame)
            self.question_entry.grid(row=1, column=1, pady=(5, 15), sticky="n")

            self.choice1_entry = ctk.CTkEntry(self.create_widgets_frame, placeholder_text="Choice 1")
            self.choice1_entry.grid(row=2, column=0, pady=10, sticky="")
            self.choice1_correct = ctk.CTkCheckBox(self.create_widgets_frame, text="Correct?")
            self.choice1_correct.grid(row=2, column=1, padx=10)

            self.choice2_entry = ctk.CTkEntry(self.create_widgets_frame, placeholder_text="Choice 2")
            self.choice2_entry.grid(row=3, column=0, pady=10, sticky="")
            self.choice2_correct = ctk.CTkCheckBox(self.create_widgets_frame, text="Correct?")
            self.choice2_correct.grid(row=3, column=1, padx=10)

            self.choice3_entry = ctk.CTkEntry(self.create_widgets_frame, placeholder_text="Choice 3")
            self.choice3_entry.grid(row=4, column=0, pady=10, sticky="")
            self.choice3_correct = ctk.CTkCheckBox(self.create_widgets_frame, text="Correct?")
            self.choice3_correct.grid(row=4, column=1, padx=10)

            self.choice4_entry = ctk.CTkEntry(self.create_widgets_frame, placeholder_text="Choice 4")
            self.choice4_entry.grid(row=5, column=0, pady=10, sticky="")
            self.choice4_correct = ctk.CTkCheckBox(self.create_widgets_frame, text="Correct?")
            self.choice4_correct.grid(row=5, column=1, padx=10)

            self.add_button = ctk.CTkButton(self.create_widgets_frame, text="ADD", command=self.add)
            self.add_button.grid(row=6, column=0, padx=5, pady=15)

            self.finish_button = ctk.CTkButton(self.create_widgets_frame, text="FINISH", command=self.home)
            self.finish_button.grid(row=6, column=1, padx=5, pady=15)

    def show_test_results(self):
        pass
    
    def log_out(self):
        self.master.user_id = None
        self.master.show_frame("login")
    
    def home(self):
        self.master.show_frame("home")
    
    def add(self):
        self.db_manager.add_question(self.test_id, self.question_entry.get(), [self.choice1_entry.get(), self.choice2_entry.get(), self.choice3_entry.get(), self.choice4_entry.get()], [self.choice1_correct.get(), self.choice2_correct.get(), self.choice3_correct.get(), self.choice4_correct.get()])
        self.curr_question_id += 1
        self.update_question()