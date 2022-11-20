import tkinter as tk
from tkinter import messagebox

from common import back_and_home, loginheadingfont

# generate a csv file for student report
def generate_report_class():
    pass

def generate_report_student(id):
    pass






class TeacherPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        back_and_home(self, controller)
        

        # the actual gui lesgo

        menu_options = [
            'Student Marks', 'Attendance'
        ]
        clicked = tk.StringVar(self)
        clicked.set(menu_options[0])

        drop = tk.OptionMenu(self, clicked, *menu_options)
        drop.place(anchor='center', relx=0.1, rely=0.1, width=160)