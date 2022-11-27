import mysql.connector as mys
import sql_interface as si

def insert_Data():
    si.init()

    si.cursor.execute('insert into course_master values(10, "CS")')
    si.cursor.execute('insert into course_master values(11, "Bio")')
    si.cursor.execute('insert into course_details values(10, "Maths")')
    si.cursor.execute('insert into course_details values(10, "English")')
    si.cursor.execute('insert into course_details values(10, "Chemistry")')
    si.cursor.execute('insert into course_details values(10, "Physics")')
    si.cursor.execute('insert into course_details values(10, "Computer Science")')

    si.cursor.execute('insert into course_details values(11, "Maths")')
    si.cursor.execute('insert into course_details values(11, "English")')
    si.cursor.execute('insert into course_details values(11, "Chemistry")')
    si.cursor.execute('insert into course_details values(11, "Physics")')
    si.cursor.execute('insert into course_details values(11, "Biology")')

    si.connection.commit()

insert_Data()