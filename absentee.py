import tkinter as tk
import common

class AbsenteePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        common.back_and_home(self, controller)
        # retrieve student data for their absentee data

        tk.Label(self, text="Student: ", font=("Arial", 17)).place(anchor="ne", relx=0.15, rely=0.05)

        absentee_students = ['student 1', 'student 2', 'student 3']
        as_clicked = tk.StringVar(self)
        drop_menu = tk.OptionMenu(self, as_clicked, *absentee_students)
        drop_menu.place(anchor='nw', relx = 0.16, rely=0.05)
        
        # create false data later
        