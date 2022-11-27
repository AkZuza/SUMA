import tkinter as tk
from tkinter import messagebox

import sql_interface as si
from admin import AdminPage
from teacher import TeacherPage
from student import CreateStudentPage
from absentee import AbsenteePage
from marks import DisplayStudentMarksPage
from common import loginheadingfont

    

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.title(" Suma")
        container.pack(side="top", fill="both", expand=True)

        # initialize sql
        si.init()

        self.frame_history = []

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (DisplayStudentMarksPage, AbsenteePage, LoginPage,AdminPage, TeacherPage, CreateStudentPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")

        # login page open karo
        self.current_frame = CreateStudentPage
        self.show_frame(self.current_frame)
    
    # shows new frame
    def show_frame(self, cont):
        self.frame_history.append(self.current_frame)
        self.current_frame = cont
        frame = self.frames[cont]
        frame.tkraise()

    def back_frame(self):
        self.show_frame(self.frame_history.pop())

    def logout(self):
        self.show_frame(LoginPage)


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label2= tk.Label(self, text="Making managing students easier ✨✨", font=("Segoe UI", 15))
        label2.place(anchor="center", relx=0.5, rely=0.29)

        label = tk.Label(self, text="SUMA", font = loginheadingfont, pady=0)
        label.place(anchor="center", relx=0.5, rely=0.15)

        # text box and button for login
        username_x = 0.42
        tk.Label(self, text="User", font=("Segoe UI", 23)).place(anchor="e", relx=username_x, rely=0.52)
        username = tk.Entry(self, bd=3, font=("Segoe UI", 22), width=15)
        username.place(anchor="w", relx=username_x+0.01, rely=0.52)

        password_x = 0.42
        tk.Label(self, text="Password", font=("Segoe UI", 23)).place(anchor="e", relx=password_x, rely=0.6)
        password = tk.Entry(self, bd=3, font=("Segoe UI", 22), width=15, show="*")
        password.place(anchor="w", relx=password_x+0.01, rely=0.6)

        # login and exit button
        loginButton = tk.Button(self, text="Login",font=("Segoe UI", 19), width=5, command=lambda: self.login_button_click(username=username.get(), password=password.get(), cont=controller))
        loginButton.place(anchor="e", relx=0.49, rely=0.7)
        exitButton = tk.Button(self, text="Exit",font=("Segoe UI", 19), width=5, command=lambda: controller.quit())
        exitButton.place(anchor="w", relx=0.49, rely=0.7)



    """called when the login button is pressed
    it will retrieve all available users and check if credentials are correct
    admin account is special tho"""
    def login_button_click(self, username, password, cont):

        # request for login data

            # oh oh, this is admin.....
        if username == "admin":
            if password == "admin":
                cont.show_frame(AdminPage)
                return "Admin"
            else:
                messagebox.showinfo(title="Login Error", message="The username\\password you've entered is incorrect")
                return "Fail"

            # teacher ids are integers soooo
        if not username.isdigit():
            messagebox.showinfo(title="Login Error", message="The username\\password you've entered is incorrect")
            return "Fail"

            # create table just in case
        si.cursor.execute('''create table if not exists Teacher(Teacher_ID Int Primary Key,
        Teacher_Name varchar(25) NOT NULL, Password varchar(25) NOT NULL, Status varchar(10) )''')

            # request for the data
        si.cursor.execute(f"select Password from Teacher where Teacher_ID = {username} ")
        t_password = si.cursor.fetchone()[0]

            # if t_password is None the well she or he doesnt exist (or some rando entered wrong password)
        if t_password == None or t_password != password:
            messagebox.showinfo(title="Login Error", message="The username\\password you've entered is incorrect")
            return "Fail"

           # yay teacher exist not admin phew
        cont.show_frame(TeacherPage)

