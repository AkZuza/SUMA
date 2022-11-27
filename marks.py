import tkinter as tk
import common

class DisplayStudentMarksPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        common.back_and_home(self, controller)

        # identifier input box


        # display marks termwise
        terms = ['Pre Midterm', 'Post Midterm', 'Models', 'Finals']
        selected_term = tk.StringVar(self)
        term_menu = tk.OptionMenu(self, selected_term, *terms)
        term_menu.place(anchor='center', relx = 0.1, rely=0.1)
        # also add option to add delete or update marks

    def refresh_mark_view(self, term):
        pass