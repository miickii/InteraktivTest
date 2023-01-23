import tkinter as tk
import customtkinter as ctk
ctk.set_appearance_mode("Dark")

root = ctk.CTk()

root.title("Grid layout test")

main_frame = ctk.CTkFrame(root, width=250, height=250, fg_color="#3A3845")
main_frame.grid(row=0, column=0)

frame2 = ctk.CTkFrame(root, width=200, height=200, fg_color="#f7ccac")
frame2.grid(row=1, column=0, sticky="WESN")

frame3 = ctk.CTkFrame(root, width=250, height=250, fg_color="#ffd93d")
frame3.grid(row=0, column=1)

frame4 = ctk.CTkFrame(root, width=150, height=100, fg_color="#6bcb77")
frame4.grid(row=1, column=1, sticky="NSEW")

horizontal = ctk.CTkFrame(root, height=100, width=500, fg_color="#4d96ff")
horizontal.grid(row=2, column=0, columnspan=2, sticky="NSEW")

vertical = ctk.CTkFrame(root, width=100, height=350, fg_color="#ff6b6b")
vertical.grid(row=0, column=2, rowspan=3, sticky="NSEW")

if __name__ == "__main__":
    root.mainloop()


