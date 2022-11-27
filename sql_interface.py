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
    emergency INT)''')

    # create teacher table
    cursor.execute('''create table if not exists Class(Class_ID INT PRIMARY KEY,
    Class_Name varchar(15) NOT NULL, Course_ID int not null, Teacher_id int not null)''')

    # create course table
    cursor.execute('''create table if not exists Course_Master(Course_ID int primary key, course_name varchar(20) not null)''')
    cursor.execute('''create table if not exists Course_Details(Course_ID int not null, Subject varchar(15) not null)''')
    
    # create teacher table
    cursor.execute('''create table if not exists Teacher(Teacher_ID int primary key, teacher_name varchar(30) not null, password varchar(20), status varchar(10))''')

    # create absence data
    cursor.execute('''create table if not exists Absence(Absence_Date Date Not Null, Student_ID int not null, Remarks varchar(30))''')

    # create mark table
    cursor.execute('''create table if not exists Marks(Student_Id int not null, term varchar(10) not null, subject varchar(20) not null,
    mark int not null, Entered_date Date not null, year varchar(10) not null, teacher_id int not null)''')

    print("SQL interface initialized") 