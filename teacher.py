import tkinter as tk
from tkinter import messagebox

from common import back_and_home, loginheadingfont

# generate a csv file for student report
def generate_report_class():
    pass

def generate_report_student(id):
    pass



class CreateTeacherPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        back_and_home(self, controller)

        labelfont = ("Arial", 16)

        tk.Label(self, text="Teacher ID", font=labelfont).place(anchor="ne", relx=0.14, rely=0.1)
        self.teacherid = tk.Entry(self, font=labelfont, width=7)
        self.teacherid.place(anchor="nw", relx=0.16, rely=0.102)

        tk.Label(self, text="Name", font=labelfont).place(anchor="ne", relx=0.14, rely=0.15)
        self.name = tk.Entry(self, font=labelfont)
        self.name.place(anchor="nw", relx=0.16, rely=0.153)

        tk.Label(self, text="Password", font=labelfont).place(anchor="ne", relx=0.14, rely=0.2)
        self.password = tk.Entry(self, font=labelfont)
        self.password.place(anchor="nw", relx=0.16, rely=0.204)

        tk.Label(self, text="Status", font=labelfont).place(anchor="ne", relx=0.14, rely=0.25)
        menu_options_status = [
            'Active', 'Retired'
        ]
        self.status_clicked = tk.StringVar(self)
        self.status_clicked.set(menu_options_status[0])

        self.status_drop = tk.OptionMenu(self, self.status_clicked, *menu_options_status)
        self.status_drop.place(anchor='nw', relx=0.16, rely=0.255)

        tk.Button(self, text='Add Teacher', font=labelfont, command= lambda : self.add_teacher()).place(anchor='center', relx= 0.16, rely=0.356)

    def add_teacher(self):
        tid = int(self.teacherid.get())
        tname = self.name.get()
        passw = self.password.get()
        status = self.status_clicked.get()

        t = (tid, tname, passw, status)



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