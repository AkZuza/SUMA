import tkinter as tk
import common
import class_sql, course_sql, student_sql
from datetime import datetime

class AddStudentMarkPage(tk.Frame):
    def __init__(self, parent, controller):
        self.c = controller
        tk.Frame.__init__(self, parent)
        common.back_and_home(self, controller)

        labelfont = ("Arial", 16)


        self.classes_options = ['']
        tid = -1
        if common.logged_in_user != None:
            tid = int(common.logged_in_user)
            self.classes_options.pop()
        for i in class_sql.fetch_all():
            if tid == i[-1]:
                self.classes_options.append(i[1])

        self.classes = tk.StringVar(self)
        self.class_menu = tk.OptionMenu(self, self.classes, *self.classes_options)
        self.class_menu.place(anchor='nw', relx=0.11, rely=0.1)
        tk.Label(self, text='Class', font=labelfont).place(anchor='ne', relx = 0.1, rely=0.1)

        
        self.students_choice = tk.StringVar(self)
        self.students_options = ['']
        self.students_menu = tk.OptionMenu(self, self.students_choice, *self.students_options)
        self.students_menu.place(anchor='nw', relx=0.11, rely=0.16)

        terms_menu = ['Term 1', 'Term 2', 'Term 3']
        self.terms = tk.StringVar(self)
        self.term_menu = tk.OptionMenu(self, self.terms, *terms_menu)
        self.term_menu.place(anchor='nw', relx = 0.11, rely=0.22)
        tk.Label(self, font=labelfont, text='Term').place(anchor='ne', relx=0.1, rely=0.22)

    def get_students(self, val):
        classname = val
        cid = -1
        coid = 0
        for i in class_sql.fetch_all():
            if classname == i[1]:
                cid = i[0]
                coid = i[2]

        self.students = []
        for i in student_sql.fetch_all():
            if i[2] == cid:
                self.students.append(i)

        self.students_options = []
        for i in self.students:
            self.students_options.append(f"{i[0]}. {i[1]}")
        self.students_menu = tk.OptionMenu(self, self.students_choice, *self.students_options)
        self.students_menu.place(anchor='nw', relx=0.11, rely=0.16)
        labelfont = ("Arial", 16)
        tk.Label(self, font=labelfont, text="Student").place(anchor='ne', relx=0.1, rely=0.16)
        
        subjects = course_sql.get_sujects(coid)
        rely = 0.28
        self.marks = {}
        for sub in subjects:
            i = sub[0]
            tk.Label(self, font=labelfont, text=i).place(anchor='ne', relx=0.2, rely = rely)
            self.marks[i] = tk.Entry(self, font=labelfont, width=5)
            self.marks[i].place(anchor='nw', relx=0.21, rely=rely)
            rely += 0.06

        tk.Button(self, font=labelfont, text='Add Marks', command=lambda: self.add_marks()).place(anchor='nw', relx=0.21, rely=rely)

    def redraw(self):
        tid = int(common.logged_in_user)
        self.classes_options = ['']
        tid = -1
        
        if common.logged_in_user != None:
            tid = int(common.logged_in_user)
            self.classes_options.pop()
        for i in class_sql.fetch_all():
            if tid == i[-1]:
                self.classes_options.append(i[1])
        self.class_menu = tk.OptionMenu(self, self.classes, *self.classes_options, command=self.get_students)
        self.class_menu.place(anchor='nw', relx=0.11, rely=0.1)
        self.tid = tid

    def add_marks(self):
        for i in self.marks:
            sid = int(self.students_choice.get().partition('.')[0])
            term = self.terms.get()
            sub = i
            mark = int(self.marks[i].get())
            entered = datetime.today().strftime('%Y-%m-%d')
            year = entered.partition('-')[0]

            s = (sid, term, sub, mark, entered,year, self.tid)
            import marks_sql
            marks_sql.add(s)

        self.c.back_frame()

        