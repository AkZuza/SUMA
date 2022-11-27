import tkinter as tk
import common
import student_sql

class AbsenteePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        common.back_and_home(self, controller)
        # retrieve student data for their absentee data

        tk.Label(self, text="Student: ", font=("Arial", 17)).place(anchor="ne", relx=0.15, rely=0.05)

        absentee_students = ['']
        for i in student_sql.fetch_all():
            absentee_students.append(f'{i[0]}. "{i[1]}"')

        self.as_clicked = tk.StringVar(self)
        drop_menu = tk.OptionMenu(self, self.as_clicked, *absentee_students)
        drop_menu.place(anchor='nw', relx = 0.16, rely=0.05)
        
        tk.Label(self, font=("Arial", 17), text="Remarks").place(anchor='ne', relx=0.15, rely=0.11)
        self.remarks = tk.Entry(self, font=("Arial", 17))
        self.remarks.place(anchor='nw', relx=0.17, rely=0.11)

        tk.Button(self, font=("Arial", 17), text="Mark Absent", command= lambda: self.mark_absent()).place(anchor='center', relx = 0.08, rely=0.25)

    def mark_absent(self):
        sid = int(self.as_clicked.get().partition('.')[0])
        from datetime import datetime
        enter = datetime.today().strftime('%Y-%m-%d')
        remark = self.remarks.get()

        import absentice_sql
        absentice_sql.add_student((enter, sid, remark))
