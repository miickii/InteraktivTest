import customtkinter as ctk
import math
import time

class Test(ctk.CTkFrame):
    def __init__(self, master, db_manager):
        super().__init__(master)
        self.master = master
        self.db_manager = db_manager
    
    def create(self):
        self.test_name, self.questions, self.choices = self.db_manager.get_test_data(self.master.selected_test_id)
        self.curr_question_id = 0
        self.curr_question = self.questions[0]
        self.curr_choices = self.choices[0]
        self.correct_answers = 0

        self.container = ctk.CTkFrame(self.master, width=400, height=100)
        self.container.grid(row=0, column=0, sticky="nsew")
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(1, weight=1)
    
        self.topbar = ctk.CTkFrame(self.container, width=400, height=100, fg_color="#3A3845")
        self.topbar.grid(row=0, column=0, sticky="nwe")
        self.topbar.grid_columnconfigure(0, weight=1)

        self.topbar_buttons_frame = ctk.CTkFrame(self.topbar, width=400, height=100, fg_color="#3A3845")
        self.topbar_buttons_frame.grid(row=0, column=0, sticky="", pady=10)
        self.topbar_buttons_frame.grid_columnconfigure(0, weight=1)

        self.home_button = ctk.CTkButton(self.topbar_buttons_frame, text="Home", command=lambda: self.master.show_frame("home"))
        self.home_button.grid(row=0, column=0, padx=15)

        self.create_test_button = ctk.CTkButton(self.topbar_buttons_frame, text="Create test", command=lambda: self.master.show_frame("create_test"))
        self.create_test_button.grid(row=0, column=1, padx=15)

        self.test_results_button = ctk.CTkButton(self.topbar_buttons_frame, text="Test results", command=lambda: self.master.show_frame("test_results"))
        self.test_results_button.grid(row=0, column=2, padx=15)

        self.logout_button = ctk.CTkButton(self.topbar_buttons_frame, text="Log out", command=self.log_out)
        self.logout_button.grid(row=0, column=3, padx=15)

        self.update_question()

    def update_question(self):
        self.content = ctk.CTkFrame(self.container, width=400)
        self.content.grid(row=1, column=0, sticky="nsew")
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_rowconfigure(0, weight=1)

        self.question_frame = ctk.CTkFrame(self.content, width=400, height=300, fg_color="#3A3845")
        self.question_frame.grid(row=0, column=0, sticky="")

        self.widgets_frame = ctk.CTkFrame(self.question_frame, width=400, height=300, fg_color="#3A3845")
        self.widgets_frame.grid(row=0, column=0, sticky="", padx=50, pady=(10, 50))

        self.question_label = ctk.CTkLabel(self.widgets_frame, text=self.curr_question[1], font=ctk.CTkFont(size=20, weight="bold"))
        self.question_label.grid(row=0, column=0, pady=(5, 20), sticky="n")

        choice1_button = ctk.CTkButton(self.widgets_frame, text=self.curr_choices[0][0], command=lambda: self.next_question(self.curr_choices[0][1]))
        choice1_button.grid(row=1, column=0, pady=10)

        choice2_button = ctk.CTkButton(self.widgets_frame, text=self.curr_choices[1][0], command=lambda: self.next_question(self.curr_choices[1][1]))
        choice2_button.grid(row=2, column=0, pady=10)

        choice3_button = ctk.CTkButton(self.widgets_frame, text=self.curr_choices[2][0], command=lambda: self.next_question(self.curr_choices[2][1]))
        choice3_button.grid(row=3, column=0, pady=10)

        choice4_button = ctk.CTkButton(self.widgets_frame, text=self.curr_choices[3][0], command=lambda: self.next_question(self.curr_choices[3][1]))
        choice4_button.grid(row=4, column=0, pady=10)
    
    def destroy_widgets(self):
        self.container.destroy()
    
    def create_test(self):
        self.master.show_frame("create_test")

    def show_test_results(self):
        self.content = ctk.CTkFrame(self.container, width=400)
        self.content.grid(row=1, column=0, sticky="nsew")
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_rowconfigure(0, weight=1)

        result = math.floor(self.correct_answers / len(self.questions) * 100)
        self.results_label = ctk.CTkLabel(self.content, text=str(result) + "%", font=ctk.CTkFont(size=20, weight="bold"))
        self.results_label.grid(row=0, column=0, sticky="")

        local_time = time.localtime() # get struct_time
        time_string = time.strftime("%m/%d/%Y, %H:%M:%S", local_time)
        date_time = [s.strip() for s in time_string.split(",")]

        self.db_manager.add_completed(self.test_name, result, date_time[0], date_time[1], self.master.user_id)
    
    def log_out(self):
        self.master.user_id = None
        self.master.show_frame("login")
    
    def next_question(self, correct):
        print(correct)
        if correct:
            self.correct_answers += 1
        
        self.curr_question_id += 1
        if self.curr_question_id >= len(self.questions):
            self.show_test_results()
        else:
            self.curr_question = self.questions[self.curr_question_id]
            self.curr_choices = self.choices[self.curr_question_id]
            self.update_question()
