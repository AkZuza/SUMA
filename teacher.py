import tkinter as tk
from tkinter import messagebox, ttk
import teacher_sql, marks, absentee
import marks_sql, student_sql, class_sql, absentice_sql

from common import back_and_home, loginheadingfont
import common
import report

# generate a csv file for student report
def generate_report_class():
    pass

def generate_report_student(id):
    pass

class CreateTeacherPage(tk.Frame):
    def __init__(self, parent, controller):
        self.c = controller
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
        code = teacher_sql.add(t)
        if code == "Exists":
            common.info_box('Teacher already exists')
        else:
            common.info_box('Added Teacher')
            self.c.back_frame()


class EditTeacherPage(tk.Frame):
    def __init__(self, parent, controller):
        self.c = controller
        tk.Frame.__init__(self, parent)
        back_and_home(self, controller)

        labelfont = ("Arial", 16)

        tk.Label(self, text="Teacher ID", font=labelfont).place(anchor="ne", relx=0.14, rely=0.1)
        self.teacherid = tk.Entry(self, font=labelfont, width=7)
        self.teacherid.place(anchor="nw", relx=0.16, rely=0.102)
        tk.Button(self, text="Search", font=("Arial", 12), command=lambda: self.search_update()).place(anchor="nw", relx=0.26, rely=0.102)

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

        tk.Button(self, text='Update Teacher', font=labelfont, command= lambda : self.update_teacher()).place(anchor='center', relx= 0.16, rely=0.356)

    def search_update(self):
        t = teacher_sql.fetch(int(self.teacherid.get()))
        if t == None:
            common.info_box('Such a teacher does not exist')

        id, name, pa, st =t 

        self.name.delete(0, tk.END)
        self.name.insert(0, name)

        self.password.delete(0, tk.END)
        self.password.insert(0, pa)

        self.status_clicked.set(st)

    def update_teacher(self):
        tid = int(self.teacherid.get())
        tname = self.name.get()
        passw = self.password.get()
        status = self.status_clicked.get()

        t = (tid, tname, passw, status)
        code = teacher_sql.add(t)
        if code == "Exists":
            teacher_sql.update(t)
            common.info_box('Updated Teacher')
            self.c.back_frame()
        else:
            common.info_box('Such a teache does not exist')


class TeacherPage(tk.Frame):
    def __init__(self, parent, controller):
        self.c = controller
        tk.Frame.__init__(self, parent)
        back_and_home(self, controller)
        
        menu_options = [
            'Student Marks', 'Absentees'
        ]
        self.clicked = tk.StringVar(self)
        self.clicked.set(menu_options[0])

        drop = tk.OptionMenu(self, self.clicked, *menu_options)
        drop.place(anchor='center', relx=0.1, rely=0.1, width=160)

        self.tree = ttk.Treeview(self)

        # buttons
        AddButton = tk.Button(self, text="Add", width=6, command= lambda : self.add_button())
        AddButton.place(anchor='center', relx=0.2, rely=0.1)
        DelButton = tk.Button(self, text="Delete", command= lambda: self.delete_thing())
        DelButton.place(anchor='center', relx=0.25, rely=0.1)
        ShowButton = tk.Button(self, text="Show", command=lambda: self.load_view_tree())
        ShowButton.place(anchor='center', relx=0.30, rely=0.1)
        AbsentButton = tk.Button(self, text="Mark Absent", command=lambda: self.c.show_frame(absentee.AbsenteePage))
        AbsentButton.place(anchor='center', relx=0.37, rely=0.1)

        gButton = tk.Button(self, text="Generate Report", command=lambda: report.generate_report())
        gButton.place(anchor='center', relx=0.45, rely=0.1)

        self.classes = ['']
        self.tid = int(common.logged_in_user) if common.logged_in_user != None else -1
        for i in class_sql.fetch_all():
            if i[3] == self.tid:
                self.classes.append(f'{i[0]}. {i[1]}')
        self.classes_choice = tk.StringVar(self)
        self.classes_menu = tk.OptionMenu(self, self.classes_choice, *self.classes)
        self.classes_menu.place(anchor='nw', relx= 0.1, rely=0.16)
        tk.Label(self, text='Class', font=("Arial", 12)).place(anchor='ne', relx = 0.1, rely = 0.16)

        tk.Label(self, font=("Arial", 12), text='Term').place(anchor='ne', relx= 0.25, rely=0.16)
        terms = ['Term 1', 'Term 2', 'Term 3']
        self.term_choice = tk.StringVar(self)
        self.term_menu = tk.OptionMenu(self, self.term_choice, *terms)
        self.term_menu.place(anchor='nw', relx=0.26, rely=0.16)
        self.term_choice.set('Term 1')

        # tk.Label(self, font=("Arial", 12), text='Student').place(anchor='ne', relx= 0.17, rely=0.16)
        # students = ['']
        # self.studen_choice = tk.StringVar(self)
        # self.studen_menu = tk.OptionMenu(self, self.studen_choice, *students)
        # self.studen_menu.place(anchor='nw', relx=0.18, rely=0.16)


    def delete_thing(self):
        pass
     
    def add_button(self):
        if self.clicked.get() == 'Student Marks':
            self.c.show_frame(marks.AddStudentMarkPage)

    def load_student_tree(self):
        columns = ()

        self.tree = ttk.Treeview(self, columns=('c1', 'c2', 'c3', 'c4'), show="headings", height=8)

        self.tree.column('# 1', anchor='center', width=5)
        self.tree.heading('# 1', text='Student')
        
        self.tree.column('# 2', anchor='center')
        self.tree.heading('# 2', text = 'Term')

        self.tree.column('# 3', anchor='center')
        self.tree.heading('# 3', text = 'Subject')

        self.tree.column('# 4', anchor='center')
        self.tree.heading('# 4', text = 'Marks')

        i = 1
        for tup in marks_sql.fetch_all():
            id, term, sub, mark, entered, year, tid = tup
            t = self.term_choice.get() 
            scid = student_sql.fetch_student(id)[2]
            cid = int(self.classes_choice.get().partition('.')[0])
            if term != t or scid != cid:
                continue

            sname = student_sql.fetch_student(id)[1]
            tname = teacher_sql.fetch(tid)[1]
            self.tree.insert('', 'end', text=str(i), values=(sname, term, sub, mark))
            i += 1

        self.tree.place(anchor='nw', relx=0.05, rely=0.21, relwidth=0.9)
            
    def load_absentee_tree(self):
        self.tree = ttk.Treeview(self, columns=('c1', 'c2'), show="headings", height=8)
        self.tree.column('# 1', anchor='center', width=5)
        self.tree.heading('# 1', text='Student')
        
        self.tree.column('# 2', anchor='center')
        self.tree.heading('# 2', text = 'Remarks')

        i = 1
        for tup in absentice_sql.fetch_all():
            id, rem = tup
            sname = student_sql.fetch_student(id)[1]
            self.tree.insert('', 'end', text=str(i), values=(sname, rem))
            i += 1

    def load_class(self):
        self.classes = []
        self.tid = int(common.logged_in_user)
        for i in class_sql.fetch_all():
            if i[3] == self.tid:
                self.classes.append(f'{i[0]}. {i[1]}')
        self.classes_choice = tk.StringVar(self)
        self.classes_menu = tk.OptionMenu(self, self.classes_choice, *self.classes)
        self.classes_menu.place(anchor='nw', relx= 0.1, rely=0.16)
        #tk.Label(self, text='Class', font=("Arial", 12)).place('ne', relx = 0.1, rely = 0.16)

        # students = ['']



        # self.studen_choice = tk.StringVar(self)
        # self.studen_menu = tk.OptionMenu(self, self.studen_choice, *students)
        # self.studen_menu.place(anchor='nw', relx=0.18, rely=0.16)

        pass

    def load_view_tree(self, val = None):
        # report.generate_report()
        if self.clicked.get() == 'Student Marks':
            self.load_student_tree()
        elif self.clicked.get() == 'Absentees':
            self.load_absentee_tree()
