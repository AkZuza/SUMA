import mysql.connector as mys

def fetch_student(id):
    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()
    cursor.execute(f'select * from Student where Student_Id={id}')
    s= cursor.fetchone()
    return s

def fetch_all():
    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()

    cursor.execute(f'select * from Student')
    s = cursor.fetchall()
    return s

def update(s):
    SID=s[0]
    SNAME=s[1]
    CID=s[2]
    GENDER=s[3]
    ADD=s[4]
    CONNO=s[5]
    MID=s[6]
    EMER=s[7]

    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()

    q="select * from student where SID={}".format(SID)
    cursor.execute(q)
    data=cursor.fetchone()
    if data==None:
        print("record not found")
        return False
    else:
        q="update student set Student_Name='{}',Class_Id={},Gender='{}',Address='{}',Contact_No={},Email_Id='{}',Emergency={} where Student_ID={} ".format(SNAME,CID,GENDER,ADD,CONNO,MID,EMER, SID)
        cursor.execute(q)
        connection.commit()
        print(cursor.rowcount,"Record updated")
        
def add_student(s):
    SID=s[0]
    SNAME=s[1]
    CID=s[2]
    GENDER=s[3]
    ADD=s[4]
    CONNO=s[5]
    MID=s[6]
    EMER=s[7]

    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()

    student = fetch_student(SID)

    if student != None:
        print('Student already exists with the same admission number')
        return "Exists"
    
    q="insert into Student values({},'{}',{},'{}','{}',{},'{}',{})".format(SID,SNAME,CID,GENDER,ADD,CONNO,MID,EMER)
    cursor.execute(q)
    connection.commit()
    return "Created"

