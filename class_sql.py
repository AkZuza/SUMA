import mysql.connector as mys

def fetch(id):
    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()
    cursor.execute(f'select * from Class where Class_ID={id}')
    s= cursor.fetchone()
    return s

def fetch_all():
    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()

    cursor.execute(f'select * from Class')
    s = cursor.fetchall()
    return s

def update(s):
    id, name, course, teacher = s

    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()

    q="select * from class where class_id={}".format(id)
    cursor.execute(q)
    data=cursor.fetchone()
    if data==None:
        print("record not found")
        return False
    else:
        q="update class set Class_Name='{}',Course_ID='{}',Teacher_ID='{}' where class_id = {}".format(name, course, teacher, id)
        cursor.execute(q)
        connection.commit()
        print(cursor.rowcount,"Record updated")
        
def add(s):
    id, name, course, teacher = s

    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()

    sclass = fetch(id)

    if sclass != None:
        print('Class already exists with the same admission number')
        return "Exists"
    
    q="insert into Class values({},'{}','{}','{}')".format(id, name, course, teacher)
    cursor.execute(q)
    connection.commit()
    return "Created"