import mysql.connector as mys

def fetch(id):
    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()
    cursor.execute(f'select * from course_master natural join course_details where course_id={id}')
    s = cursor.fetchone()
    return s

def get_sujects(courseid):
    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()

    cursor.execute('select subject from course_details where course_id = ' + str(courseid))
    result = cursor.fetchall()
    return result
    
def fetch_m(id):
    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()
    cursor.execute(f'select * from course_master where course_id={id}')
    s = cursor.fetchone()
    return s

def fetch_all():
    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()
    cursor.execute(f'select * from course_master natural join course_details')
    s = cursor.fetchall()
    return s

def fetch_m_all():
    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()
    cursor.execute(f'select * from course_master')
    s = cursor.fetchall()
    return s

def fetch_d_all():
    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()
    cursor.execute(f'select * from course_details')
    s = cursor.fetchall()
    return s

def update_master(s):
    id, name = s
    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()
    q="select * from course_master where course_id={}".format(id)
    cursor.execute(q)
    data=cursor.fetchone()
    if data==None:
        print("record not found")
        return False
    else:
        q="update course_master where course_id = {} set course_Name='{}'".format(id,name)
        cursor.execute(q)
        connection.commit()
        print(cursor.rowcount,"Record updated")

def update_details(s):
    pass
        
def add_master(s):
    id, name = s

    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()
    course = fetch(id)

    if course!= None:
        print('Course already exists')
        return "Exists"
    
    q="insert into course_master values({},'{}')".format(id, name)
    cursor.execute(q)
    connection.commit()
    return "Created"

def add_details(s):
    id, sub = s

    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()
    course = fetch(id)

    if course!= None:
        print('Course detail already exists')
        return "Exists"
    
    q="insert into course_details values({},'{}')".format(id, sub)
    cursor.execute(q)
    connection.commit()
    return "Created"