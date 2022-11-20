import tkinter as tk
from tkinter import messagebox

loginheadingfont = ("Segoe UI", 75)

def back_and_home(frame, controller):
    back = tk.Button(frame, text="Back", command= lambda: controller.back_frame())
    back.place(anchor="se", relx=0.99, rely=0.99)
    home = tk.Button(frame, text="Logout", command = lambda: controller.logout())
    home.place(anchor="se", relx=0.95, rely=0.99)

def info_box(text):
    messagebox.showinfo(title="Suma", text=text)
