import sql_interface as si
import common


# data in a student
# id, name, class_id, gender, address, contact, email, emergency_no

def add_student(student_data):
    id, name, c_id, g, addr, cont, email, emerg = student_data
    student_info = " values({id}, '{name}', {c_id}, '{addr}', {cont}, '{email}', {emerg})"
    
    si.cursor.execute("insert into Student" + student_info)
    common.info_box('Student added')

def get_student(id):
    si.cursor.execute(f"select * from Student where student_id={id}")



    



