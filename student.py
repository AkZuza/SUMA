import sql_interface as si
import common
import tkinter as tk


class CreateStudentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        common.back_and_home(self, controller)

        # textbox and input box
        labelfont = ("Arial", 16)

        tk.Label(self, text="Admin No:", font=labelfont).place(anchor="ne", relx=0.14, rely=0.1)
        self.admnno = tk.Entry(self, font=labelfont, width=7)
        self.admnno.place(anchor="nw", relx=0.16, rely=0.102)

        tk.Label(self, text="Name", font=labelfont).place(anchor="ne", relx=0.14, rely=0.15)
        self.name = tk.Entry(self, font=labelfont)
        self.name.place(anchor="nw", relx=0.16, rely=0.153)

        tk.Label(self, text="Class", font=labelfont).place(anchor="ne", relx=0.14, rely=0.2)
        self.classid = tk.Entry(self, font=labelfont)
        self.classid.place(anchor="nw", relx=0.16, rely=0.204)

        tk.Label(self, text="Gender", font=labelfont).place(anchor="ne", relx=0.14, rely=0.25)
        menu_options_gender = [
            'Male', 'Female', 'LGBTQ+'
        ]
        self.gender_clicked = tk.StringVar(self)
        self.gender_clicked.set(menu_options_gender[0])

        self.gender_drop = tk.OptionMenu(self, self.gender_clicked, *menu_options_gender)
        self.gender_drop.place(anchor='nw', relx=0.16, rely=0.255)

        tk.Label(self, text="Address", font=labelfont).place(anchor="ne", relx=0.14, rely=0.3)
        self.address = tk.Entry(self, font=labelfont)
        self.address.place(anchor="nw", relx=0.16, rely=0.306)

        tk.Label(self, text="Contact No:", font=labelfont).place(anchor="ne", relx=0.14, rely=0.35)
        self.contact = tk.Entry(self, font=labelfont)
        self.contact.place(anchor="nw", relx=0.16, rely=0.357)

        tk.Label(self, text="Email ID", font=labelfont).place(anchor="ne", relx=0.14, rely=0.4)
        self.email = tk.Entry(self, font=labelfont)
        self.email.place(anchor="nw", relx=0.16, rely=0.408)

        tk.Label(self, text="Emergency No:", font=labelfont).place(anchor="ne", relx=0.14, rely=0.459)
        self.emerg = tk.Entry(self, font=labelfont)
        self.emerg.place(anchor="nw", relx=0.16, rely=0.459)

    def add_student(self):
        pass
    


    



