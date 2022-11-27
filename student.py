import student_sql
import sql_interface as si
import class_sql
import common
import tkinter as tk


class CreateStudentPage(tk.Frame):
    def __init__(self, parent, controller):
        self.c = controller
        tk.Frame.__init__(self, parent)
        common.back_and_home(self, controller)

        # textbox and input box
        labelfont = ("Arial", 16)

        tk.Label(self, text="Admin No:", font=labelfont).place(anchor="ne", relx=0.14, rely=0.1)
        self.admnno = tk.Entry(self, font=labelfont, width=7)
        self.admnno.place(anchor="nw", relx=0.16, rely=0.102)

        tk.Label(self, text="Name", font=labelfont).place(anchor="ne", relx=0.14, rely=0.155)
        self.name = tk.Entry(self, font=labelfont)
        self.name.place(anchor="nw", relx=0.16, rely=0.155)

        tk.Label(self, text="Class", font=labelfont).place(anchor="ne", relx=0.14, rely=0.208)
        self.classname = tk.Entry(self, font=labelfont)
        self.classname.place(anchor="nw", relx=0.16, rely=0.208)

        tk.Label(self, text="Gender", font=labelfont).place(anchor="ne", relx=0.14, rely=0.261)
        menu_options_gender = [
            'Male', 'Female', 'LGBTQ+'
        ]
        self.gender_clicked = tk.StringVar(self)
        self.gender_clicked.set(menu_options_gender[0])

        self.gender_drop = tk.OptionMenu(self, self.gender_clicked, *menu_options_gender)
        self.gender_drop.place(anchor='nw', relx=0.16, rely=0.261)

        tk.Label(self, text="Address", font=labelfont).place(anchor="ne", relx=0.14, rely=0.314)
        self.address = tk.Entry(self, font=labelfont)
        self.address.place(anchor="nw", relx=0.16, rely=0.314)

        tk.Label(self, text="Contact No:", font=labelfont).place(anchor="ne", relx=0.14, rely=0.367)
        self.contact = tk.Entry(self, font=labelfont)
        self.contact.place(anchor="nw", relx=0.16, rely=0.367)

        tk.Label(self, text="Email ID", font=labelfont).place(anchor="ne", relx=0.14, rely=0.420)
        self.email = tk.Entry(self, font=labelfont)
        self.email.place(anchor="nw", relx=0.16, rely=0.420)

        tk.Label(self, text="Emergency No:", font=labelfont).place(anchor="ne", relx=0.14, rely=0.473)
        self.emerg = tk.Entry(self, font=labelfont)
        self.emerg.place(anchor="nw", relx=0.16, rely=0.473)

        tk.Button(self, text='Add Student', font=labelfont, command= lambda : self.add_student()).place(anchor='ne', relx= 0.24, rely=0.525)

    def add_student(self):
        sid = int(self.admnno.get())
        sname = self.name.get()
        classname = self.classname.get()
        classid = -1

        classes = class_sql.fetch_all()
        for i in classes:
            if i[1].lower() == classname.lower():
                classid = i[0]


        if classid == -1:
            common.info_box('Such a class does not exist')
            return
        
        gender = self.gender_clicked.get()
        address = self.address.get()
        contact = int(self.contact.get())
        email = self.email.get()
        eme = int(self.emerg.get())

        s = (sid, sname, classid, gender, address, contact, email, eme)
        code = student_sql.add_student(s)
        if code == "Exists":
            common.info_box('Student with same admission number exists')
        else:
            common.info_box('Added Student')
            self.c.back_frame()


class EditStudentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        common.back_and_home(self, controller)

        # textbox and input box
        labelfont = ("Arial", 16)

        tk.Label(self, text="Admin No:", font=labelfont).place(anchor="ne", relx=0.14, rely=0.1)
        self.admnno = tk.Entry(self, font=labelfont, width=7)
        self.admnno.place(anchor="nw", relx=0.16, rely=0.102)
        tk.Button(self, text="Search", font=("Arial", 12), command=lambda: self.search_update()).place(anchor="nw", relx=0.26, rely=0.102)

        tk.Label(self, text="Name", font=labelfont).place(anchor="ne", relx=0.14, rely=0.155)
        self.name = tk.Entry(self, font=labelfont)
        self.name.place(anchor="nw", relx=0.16, rely=0.155)

        tk.Label(self, text="Class", font=labelfont).place(anchor="ne", relx=0.14, rely=0.208)
        self.classname = tk.Entry(self, font=labelfont)
        self.classname.place(anchor="nw", relx=0.16, rely=0.208)

        tk.Label(self, text="Gender", font=labelfont).place(anchor="ne", relx=0.14, rely=0.261)
        menu_options_gender = [
            'Male', 'Female', 'LGBTQ+'
        ]
        self.gender_clicked = tk.StringVar(self)
        self.gender_clicked.set(menu_options_gender[0])

        self.gender_drop = tk.OptionMenu(self, self.gender_clicked, *menu_options_gender)
        self.gender_drop.place(anchor='nw', relx=0.16, rely=0.261)

        tk.Label(self, text="Address", font=labelfont).place(anchor="ne", relx=0.14, rely=0.314)
        self.address = tk.Entry(self, font=labelfont)
        self.address.place(anchor="nw", relx=0.16, rely=0.314)

        tk.Label(self, text="Contact No:", font=labelfont).place(anchor="ne", relx=0.14, rely=0.367)
        self.contact = tk.Entry(self, font=labelfont)
        self.contact.place(anchor="nw", relx=0.16, rely=0.367)

        tk.Label(self, text="Email ID", font=labelfont).place(anchor="ne", relx=0.14, rely=0.420)
        self.email = tk.Entry(self, font=labelfont)
        self.email.place(anchor="nw", relx=0.16, rely=0.420)

        tk.Label(self, text="Emergency No:", font=labelfont).place(anchor="ne", relx=0.14, rely=0.473)
        self.emerg = tk.Entry(self, font=labelfont)
        self.emerg.place(anchor="nw", relx=0.16, rely=0.473)

        tk.Button(self, text='Add Student', font=labelfont, command= lambda : self.add_student()).place(anchor='ne', relx= 0.24, rely=0.525)

    def search_update(self):
        s = student_sql.fetch_student(int(self.admnno.get()))

        if s == None:
            common.info_box('Such a student does not exist within me')
            return

        SID=s[0]
        SNAME=s[1]
        CID=s[2]
        GENDER=s[3]
        ADD=s[4]
        CONNO=s[5]
        MID=s[6]
        EMER=s[7]
        
        classname = class_sql.fetch(CID)
        if classname == None:
            common.info_box('Such a class does not exist')
            return
    
        self.name.delete(0, tk.END)
        self.name.insert(0, SNAME)

        # retrieve class info
        
        self.classname.delete(0, tk.END)
        self.classname.insert(0, classname[1])

        self.gender_clicked.set(GENDER)

        self.address.delete(0, tk.END)
        self.address.insert(0, ADD)

        self.contact.delete(0, tk.END)
        self.contact.insert(0, str(CONNO))

        self.email.delete(0, tk.END)
        self.email.insert(0, MID)

        self.emerg.delete(0, tk.END)
        self.emerg.insert(0, str(EMER))

    def commit_update(self):
        sid = int(self.admnno.get())
        sname = self.name.get()
        classname = self.classname.get()
        classid = 1234
        gender = self.gender_clicked.get()
        address = self.address.get()
        contact = int(self.contact.get())
        email = self.email.get()
        eme = int(self.emerg.get())

        s = (sid, sname, classid, gender, address, contact, email, eme)
        code = student_sql.update(s)
        if code == "Exists":
            common.info_box('Student with same admission number exists')
        else:
            common.info_box('Updated Student')
            self.c.back_frame()



    


    



