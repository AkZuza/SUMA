import mysql.connector as mys

def fetch(id):
    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()
    cursor.execute(f'select * from teacher where teacher_ID={id}')
    s = cursor.fetchone()
    return s

def fetch_all():
    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()
    cursor.execute(f'select * from teacher')
    s = cursor.fetchall()
    return s

def update(s):
    TID=s[0]
    TNAME=s[1]
    PASSWD=s[2]
    STATUS=s[3]
    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()
    q="select * from teacher where Teacher_id={}".format(TID)
    cursor.execute(q)
    data=cursor.fetchone()
    if data==None:
        print("record not found")
        return False
    else:
        q="update teacher set teacher_Name='{}',password='{}',status='{}' where teacher_id = {} ".format(TNAME,PASSWD,STATUS, TID)
        cursor.execute(q)
        connection.commit()
        print(cursor.rowcount,"Record updated")
        
def add(s):
    TID=s[0]
    TNAME=s[1]
    PASSWD=s[2]
    STATUS=s[3]

    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()
    teacher = fetch(TID)

    if teacher!= None:
        print('Teacher already exists with the same teacher ID')
        return "Exists"
    
    q="insert into teacher values({},'{}','{}','{}')".format(TID,TNAME,PASSWD,STATUS)
    cursor.execute(q)
    connection.commit()
    return "Created"
