import tkinter as tk
from tkinter import ttk

from common import back_and_home
import student, teacher, sclass

import mysql.connector as mys

import student_sql, class_sql, teacher_sql, course_sql

class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        back_and_home(self, controller)

        # tk.Label(self, text="Admin", font=loginheadingfont).place(anchor="center", relx=0.5, rely=0.5)

        # create drop down menu
        menu_options = [
            'Student Details', 'Class Details', 'Teacher Details', 'Course Master', 'Course Details',
        ]
        self.clicked = tk.StringVar(self)
        self.clicked.set(menu_options[0])

        drop = tk.OptionMenu(self, self.clicked, *menu_options)
        drop.place(anchor='center', relx=0.1, rely=0.1, width=160)

        # the tree view
        self.tree = ttk.Treeview(self)
        
        # buttons
        AddButton = tk.Button(self, text="Add", width=6, command= lambda : self.add_button(controller))
        AddButton.place(anchor='center', relx=0.2, rely=0.1)
        EditButton = tk.Button(self, text="Edit", width=6, command= lambda: self.edit_button(controller))
        EditButton.place(anchor='center', relx=0.25, rely=0.1)
        DelButton = tk.Button(self, text="Delete", command= lambda: self.delete_thing())
        DelButton.place(anchor='center', relx=0.30, rely=0.1)
        ShowButton = tk.Button(self, text="Show", command=lambda: self.load_tree_view())
        ShowButton.place(anchor='center', relx=0.35, rely=0.1)



    def add_button(self, controller):
        if self.clicked.get() == "Student Details":
            controller.show_frame(student.CreateStudentPage)
        if self.clicked.get() == 'Teacher Details':
            controller.show_frame(teacher.CreateTeacherPage)
        if self.clicked.get() == 'Class Details':
            controller.show_frame(sclass.CreateClassPage)

    def edit_button(self, controller):
        if self.clicked.get() == 'Student Details':
            controller.show_frame(student.EditStudentPage)
        if self.clicked.get() == 'Teacher Details':
            controller.show_frame(teacher.EditTeacherPage)
        if self.clicked.get() == 'Class Details':
            controller.show_frame(sclass.EditClassPage)
            
    def load_student_tree(self):
        self.tree = ttk.Treeview(self, columns=('c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7'), show="headings", height=8)

        self.tree.column('# 1', anchor='center', width=5)
        self.tree.heading('# 1', text='Admn No:')
        
        self.tree.column('# 2', anchor='center')
        self.tree.heading('# 2', text='Name')

        self.tree.column('# 3', anchor='center', width=6)
        self.tree.heading('# 3', text='Class')

        self.tree.column('# 4', anchor='center', width=6)
        self.tree.heading('# 4', text='Gender')

        self.tree.column('# 5', anchor='center',width=16)
        self.tree.heading('# 5', text='Contact No:')

        self.tree.column('# 6', anchor='center')
        self.tree.heading('# 6', text='Email')

        self.tree.column('# 7', anchor='center')
        self.tree.heading('# 7', text='Emergency')

        i = 1
        for s in student_sql.fetch_all():
            SID=s[0]
            SNAME=s[1]
            CID=s[2]
            GENDER=s[3]
            ADD=s[4]
            CONNO=s[5]
            MID=s[6]
            EMER=s[7]
            classname = class_sql.fetch(CID)[1]
            self.tree.insert('', 'end', text=str(i), values=(SID, SNAME, classname, GENDER, CONNO, MID, EMER))
            i +=1

        
    def load_class_view(self):
        self.tree = ttk.Treeview(self, columns=('c1', 'c2', 'c3', 'c4'), show="headings", height=8)
        self.tree.column('# 1', anchor='center', width=5)
        self.tree.heading('# 1', text='Class ID')
        
        self.tree.column('# 2', anchor='center')
        self.tree.heading('# 2', text='Class Name')

        self.tree.column('# 3', anchor='center', width=6)
        self.tree.heading('# 3', text='Teacher')

        self.tree.column('# 4', anchor='center', width=6)
        self.tree.heading('# 4', text='Course')

        classes = class_sql.fetch_all()
        i = 1
        for s in classes:
            teacher_id = s[3]
            teacher_name = ''
            for j in teacher_sql.fetch_all():
                if j[0] == teacher_id:
                    teacher_name = j[1]

            course_name = course_sql.fetch_m(s[2])[1]
            self.tree.insert('', 'end', text=str(i), values=(s[0], s[1], teacher_name, course_name))
            i +=1

    
    def load_teacher_view(self):
        self.tree = ttk.Treeview(self, columns=('c1', 'c2', 'c3', 'c4'), show="headings", height=8)
        self.tree.column('# 1', anchor='center', width=5)
        self.tree.heading('# 1', text='Teacher ID')
        
        self.tree.column('# 2', anchor='center')
        self.tree.heading('# 2', text='Teacher Name')

        self.tree.column('# 3', anchor='center', width=6)
        self.tree.heading('# 3', text='Password')

        self.tree.column('# 4', anchor='center', width=6)
        self.tree.heading('# 4', text='Status')

        i = 1
        for s in teacher_sql.fetch_all():
            self.tree.insert('', 'end', text=str(i), values=(s[0], s[1], s[2], s[3]))
            i +=1

    def load_course_m_view(self):
        self.tree = ttk.Treeview(self, columns=('c1', 'c2'), show="headings", height=8)
        self.tree.column('# 1', anchor='center', width=5)
        self.tree.heading('# 1', text='Course ID')
        
        self.tree.column('# 2', anchor='center')
        self.tree.heading('# 2', text='Course Name')

        i = 1
        for s in course_sql.fetch_m_all():
            self.tree.insert('', 'end', text=str(i), values=(s[0], s[1]))
            i +=1

    def load_course_d_view(self):
        self.tree = ttk.Treeview(self, columns=('c1', 'c2'), show="headings", height=8)
        self.tree.column('# 1', anchor='center', width=5)
        self.tree.heading('# 1', text='Course ID')
        self.tree.column('# 2', anchor='center')
        self.tree.heading('# 2', text='Subject')
        i = 1
        for s in course_sql.fetch_d_all():
            self.tree.insert('', 'end', text=str(i), values=(s[0], s[1]))
            i +=1


    def load_tree_view(self):
        selected = self.clicked.get()
        if selected == 'Student Details':
            self.load_student_tree()
        elif selected == 'Class Details':
            self.load_class_view()
        elif selected == 'Teacher Details':
            self.load_teacher_view()
        elif selected == 'Course Master':
            self.load_course_m_view()
        elif selected == 'Course Details':
            self.load_course_d_view()

        self.tree.place(anchor='nw', relx=0.05, rely=0.15, relwidth=0.90)

    def delete_thing(self):
        dic = self.tree.item(self.tree.focus())
        if dic == None:
            return
        
        items = dic['values']

        if items == '':
            return

        i = items[0]

        connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
        cursor = connection.cursor()

        selected = self.clicked.get()
        if selected == 'Student Details':
            cursor.execute('delete from Student where student_id = ' + str(i))
        elif selected == 'Class Details':
            cursor.execute('delete from Class where class_id = ' + str(i))
        elif selected == 'Teacher Details':
            cursor.execute('delete from Teacher where teacher_id = ' + str(i))

        connection.commit()