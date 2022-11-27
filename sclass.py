import tkinter as tk
from tkinter import messagebox
import class_sql, teacher_sql, course_sql

from common import back_and_home, loginheadingfont
import common

# generate a csv file for student report
def generate_report_class():
    pass

def generate_report_student(id):
    pass

class CreateClassPage(tk.Frame):
    def __init__(self, parent, controller):
        self.c = controller
        tk.Frame.__init__(self, parent)
        back_and_home(self, controller)

        labelfont = ("Arial", 16)

        tk.Label(self, text="Class ID", font=labelfont).place(anchor="ne", relx=0.14, rely=0.1)
        self.classid = tk.Entry(self, font=labelfont, width=7)
        self.classid.place(anchor="nw", relx=0.16, rely=0.102)

        tk.Label(self, text="Class Name", font=labelfont).place(anchor="ne", relx=0.14, rely=0.15)
        self.name = tk.Entry(self, font=labelfont)
        self.name.place(anchor="nw", relx=0.16, rely=0.153)

        tk.Label(self, text="Teacher", font=labelfont).place(anchor="ne", relx=0.14, rely=0.2)
        self.teacher = tk.Entry(self, font=labelfont)
        self.teacher.place(anchor="nw", relx=0.16, rely=0.204)

        tk.Label(self, text="Course", font=labelfont).place(anchor="ne", relx=0.14, rely=0.25)
        self.course = tk.Entry(self, font=labelfont)
        self.course.place(anchor="nw", relx=0.16, rely=0.25)

        tk.Button(self, text='Add Class', font=labelfont, command= lambda : self.add_class()).place(anchor='center', relx= 0.16, rely=0.356)

    def add_class(self):
        tid = int(self.classid.get())
        tname = self.name.get()
        teacher = self.teacher.get()
        course = self.course.get()

        teacherid = common.find_id(teacher_sql.fetch_all(), teacher)
        courseid = common.find_id(course_sql.fetch_m_all(), course)

        if courseid == -1:
            common.info_box('Such a course does not exist')

        if teacherid == -1:
            common.info_box('Such a teacher does not exist')

        t = (tid, tname, courseid, teacherid)
        code = class_sql.add(t)
        if code == "Exists":
            common.info_box('class already exists')
        else:
            common.info_box('Added class')
            self.c.back_frame()


class EditClassPage(tk.Frame):
    def __init__(self, parent, controller):
        self.c = controller
        tk.Frame.__init__(self, parent)
        back_and_home(self, controller)

        labelfont = ("Arial", 16)

        tk.Button(self, text="Search", font=("Arial", 12), command=lambda: self.search_update()).place(anchor="nw", relx=0.26, rely=0.102)

        tk.Label(self, text="Class ID", font=labelfont).place(anchor="ne", relx=0.14, rely=0.1)
        self.classid = tk.Entry(self, font=labelfont, width=7)
        self.classid.place(anchor="nw", relx=0.16, rely=0.102)

        tk.Label(self, text="Class Name", font=labelfont).place(anchor="ne", relx=0.14, rely=0.15)
        self.name = tk.Entry(self, font=labelfont)
        self.name.place(anchor="nw", relx=0.16, rely=0.153)

        tk.Label(self, text="Teacher", font=labelfont).place(anchor="ne", relx=0.14, rely=0.2)
        self.teacher = tk.Entry(self, font=labelfont)
        self.teacher.place(anchor="nw", relx=0.16, rely=0.204)

        tk.Label(self, text="Course", font=labelfont).place(anchor="ne", relx=0.14, rely=0.25)
        self.course = tk.Entry(self, font=labelfont)
        self.course.place(anchor="nw", relx=0.16, rely=0.25)

        tk.Button(self, text='Update class', font=labelfont, command= lambda : self.update_class()).place(anchor='center', relx= 0.16, rely=0.356)

    def search_update(self):
        t = class_sql.fetch(int(self.classid.get()))
        if t == None:
            common.info_box('Such a class does not exist')

        id, name, c, st =t 

        self.name.delete(0, tk.END)
        self.name.insert(0, name)

        self.teacher.delete(0, tk.END)
        self.teacher.insert(0, teacher_sql.fetch(st)[1])

        self.course.delete(0, tk.END)
        self.course.insert(0, course_sql.fetch(c)[1])

    def update_class(self):
        tid = int(self.classid.get())
        tname = self.name.get()
        teacher = self.teacher.get()
        course = self.course.get()

        teacherid = common.find_id(teacher_sql.fetch_all(), teacher)
        courseid = common.find_id(course_sql.fetch_m_all(), course)

        t = (tid, tname, courseid, teacherid)
        code = class_sql.add(t)
        if code == "Exists":
            class_sql.update(t)
            common.info_box('Updated Class')
            self.c.back_frame()
        else:
            common.info_box('Such a Class does not exist')