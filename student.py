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
        admnno = tk.Entry(self, font=labelfont, width=7)
        admnno.place(anchor="nw", relx=0.16, rely=0.102)

        tk.Label(self, text="Name", font=labelfont).place(anchor="ne", relx=0.14, rely=0.15)
        name = tk.Entry(self, font=labelfont)
        name.place(anchor="nw", relx=0.16, rely=0.153)

        tk.Label(self, text="Class", font=labelfont).place(anchor="ne", relx=0.14, rely=0.2)
        classid = tk.Entry(self, font=labelfont)
        classid.place(anchor="nw", relx=0.16, rely=0.204)

        tk.Label(self, text="Gender", font=labelfont).place(anchor="ne", relx=0.14, rely=0.25)
        menu_options_gender = [
            'Male', 'Female', 'LGBTQ+'
        ]
        gender_clicked = tk.StringVar(self)
        gender_clicked.set(menu_options_gender[0])

        gender_drop = tk.OptionMenu(self, gender_clicked, *menu_options_gender)
        gender_drop.place(anchor='nw', relx=0.16, rely=0.255)

        tk.Label(self, text="Address", font=labelfont).place(anchor="ne", relx=0.14, rely=0.3)
        address = tk.Entry(self, font=labelfont)
        address.place(anchor="nw", relx=0.16, rely=0.306)

        tk.Label(self, text="Contact No:", font=labelfont).place(anchor="ne", relx=0.14, rely=0.35)
        contact = tk.Entry(self, font=labelfont)
        contact.place(anchor="nw", relx=0.16, rely=0.357)

        tk.Label(self, text="Email ID", font=labelfont).place(anchor="ne", relx=0.14, rely=0.4)
        email = tk.Entry(self, font=labelfont)
        email.place(anchor="nw", relx=0.16, rely=0.408)

        tk.Label(self, text="Emergency No:", font=labelfont).place(anchor="ne", relx=0.14, rely=0.459)
        emerg = tk.Entry(self, font=labelfont)
        emerg.place(anchor="nw", relx=0.16, rely=0.459)

        s = ()
    


    



