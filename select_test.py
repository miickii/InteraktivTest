import customtkinter as ctk

class SelectTest(ctk.CTkFrame):
    def __init__(self, master, db_manager):
        super().__init__(master)
        self.master = master
        self.db_manager = db_manager
    
    def create(self):
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

        self.create_test_button = ctk.CTkButton(self.topbar_buttons_frame, text="Create test", command=self.create_test)
        self.create_test_button.grid(row=0, column=0, padx=15)

        self.test_results_button = ctk.CTkButton(self.topbar_buttons_frame, text="Test results", command=self.show_test_results)
        self.test_results_button.grid(row=0, column=1, padx=15)

        self.logout_button = ctk.CTkButton(self.topbar_buttons_frame, text="Log out", command=self.log_out)
        self.logout_button.grid(row=0, column=3, padx=15)

        self.content = ctk.CTkFrame(self.container, width=400)
        self.content.grid(row=1, column=0, sticky="nsew")
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_rowconfigure(0, weight=1)

        self.select_frame = ctk.CTkFrame(self.content, width=400, height=300, fg_color="#3A3845")
        self.select_frame.grid(row=0, column=0, sticky="")

        self.widgets_frame = ctk.CTkFrame(self.select_frame, width=400, height=300, fg_color="#3A3845")
        self.widgets_frame.grid(row=0, column=0, sticky="", padx=50, pady=(10, 50))

        row = 0
        for test in self.db_manager.get_all_tests():
            test_button = ctk.CTkButton(self.widgets_frame, text=test[1], command=lambda: self.start_test(test[0]))
            test_button.grid(row=row, column=0, pady=15)
            row += 1
    
    def destroy_widgets(self):
        self.container.destroy()
    
    def create_test(self):
        self.master.show_frame("create_test")

    def show_test_results(self):
        pass
    
    def log_out(self):
        self.master.user_id = None
        self.master.show_frame("login")
    
    def start_test(self, test_id):
        self.master.selected_test_id = test_id
        self.master.show_frame("test")