import tkinter as tk
from tkinter import messagebox

from common import back_and_home
import student

class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        back_and_home(self, controller)

        # tk.Label(self, text="Admin", font=loginheadingfont).place(anchor="center", relx=0.5, rely=0.5)

        # create drop down menu
        menu_options = [
            'Student Details', 'Class Details', 'Teacher Details'
        ]
        self.clicked = tk.StringVar(self)
        self.clicked.set(menu_options[0])

        drop = tk.OptionMenu(self, self.clicked, *menu_options)
        drop.place(anchor='center', relx=0.1, rely=0.1, width=160)


        # buttons
        AddButton = tk.Button(self, text="Add", width=6, command= lambda : self.add_button(controller))
        AddButton.place(anchor='center', relx=0.2, rely=0.1)
        EditButton = tk.Button(self, text="Edit", width=6)
        EditButton.place(anchor='center', relx=0.25, rely=0.1)
        DelButton = tk.Button(self, text="Delete")
        DelButton.place(anchor='center', relx=0.30, rely=0.1)


        # the list view
        self.list_to_view = []


    def add_button(self, controller):
        if self.clicked.get() == "Student Details":
            controller.show_frame(student.CreateStudentPage)