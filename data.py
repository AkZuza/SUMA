import mysql.connector as mys
import sql_interface as si
si.init()

connection = mys.connect(user="root", passwd="root", host="localhost")
cursor = connection.cursor()

cursor.execute('insert into course_master values(10, "CS")')
cursor.execute('insert into course_master values(11, "Bio")')
cursor.execute('insert into course_details values(10, "Maths")')
cursor.execute('insert into course_details values(10, "English")')
cursor.execute('insert into course_details values(10, "Chemistry")')
cursor.execute('insert into course_details values(10, "Physics")')
cursor.execute('insert into course_details values(10, "Computer Science")')

cursor.execute('insert into course_details values(11, "Maths")')
cursor.execute('insert into course_details values(11, "English")')
cursor.execute('insert into course_details values(11, "Chemistry")')
cursor.execute('insert into course_details values(11, "Physics")')
cursor.execute('insert into course_details values(11, "Biology")')