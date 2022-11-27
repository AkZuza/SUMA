import sql_interface as si

def fetch_absentice(id):
    si.cursor.execute(f'select * from absence where Student_Id={id}')
    s = si.cursor.fetchone()
    return s

def fetch_all():
    si.cursor.execute(f'select * from absence')
    s = si.cursor.fetchall()
    return s

def update(s):
    AB_DATE=s[0]
    SID=s[1]
    REMARK=s[2]
    q="select * from absence where SID={}".format(SID)
    si.cursor.execute(q)
    data=si.cursor.fetchone()
    if data==None:
        print("record not found")
        return False
    else:
        q="update absence set absence_date={},student_id='{}',remark={},".format(AB_DATE,SID,REMARK)
        si.cursor.execute(q)
        si.connection.commit()
        print(si.cursor.rowcount,"Record updated")
        
def add_student(s):
    AB_DATE=s[0]
    SID=s[1]
    REMARK=s[2]
    
    q="insert into absence values('{}',{},'{}')".format(AB_DATE,SID,REMARK)
    si.cursor.execute(q)
    si.connection.commit()
    return "Created"
