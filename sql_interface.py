'''module to interface sql in a cleaner way'''
import mysql.connector as mys

# variables to hold all important mysql stuff
connection = None
cursor = None

def init():
    global cursor,connection
    connection = mys.connect(user="root", passwd="root", host="localhost")
    cursor = connection.cursor()

    # for our purposes select SUMA database
    cursor.execute("create database if not exists SUMA")
    cursor.execute("use SUMA")


    # create student table
    cursor.execute('''create table if not exists Student(student_id INT PRIMARY KEY,
    student_name VARCHAR(30) NOT NULL, 
    class_id INT NOT NULL,
    gender VARCHAR(8) NOT NULL,
    address VARCHAR(100),
    contact_no INT,
    email_id VARCHAR(60),
    emergency_no INT)''')

    print("SQL interface initialized") 