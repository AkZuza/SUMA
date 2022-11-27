import mysql.connector as mys

def fetch_all():
    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()

    cursor.execute(f'select * from Marks')
    s = cursor.fetchall()
    return s
        
def add(s):
    sid, term, subject, mark, entered_date, year, tid = s
    connection = mys.connect(user="root", passwd="root", host="localhost", database='SUMA')
    cursor = connection.cursor()
    
    # cursor.execute('delete from Marks where student_id={sid} and Term ="{term}"')

    q="insert into Marks values({},'{}','{}',{}, '{}', '{}', {})".format(sid, term, subject, mark, entered_date, year, tid)
    cursor.execute(q)
    connection.commit()
    return "Created"