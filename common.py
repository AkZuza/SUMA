import tkinter as tk
from tkinter import messagebox

loginheadingfont = ("Segoe UI", 75)

logged_in_user = None

def back_and_home(frame, controller):
    back = tk.Button(frame, text="Back", command= lambda: controller.back_frame())
    back.place(anchor="se", relx=0.99, rely=0.99)
    home = tk.Button(frame, text="Logout", command = lambda: controller.logout())
    home.place(anchor="se", relx=0.95, rely=0.99)

def info_box(text):
    messagebox.showinfo(title="Suma", message=text)

def find_id(tup, name):
    for i in tup:
        if i[1] == name:
            return i[0]
        
    return -1

def get_name(id, l):
    for i in l:
        if i[0] == id:
            return i[1]
