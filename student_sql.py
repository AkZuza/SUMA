import sql_interface as si

si.init()
def update(s):
    SID=s[0]
    SNAME=s[1]
    CID=s[2]
    GENDER=s[3]
    ADD=s[4]
    CONNO=s[5]
    MID=s[6]
    EMER=s[7]
    q="select * from student where SID={}".format(SID)
    si.cursor.execute(q)
    data=si.cursor.fetchone()
    if data==None:
        print("record not found")
        return False
    else:
        q="update student set Student_ID={},Student_Name='{}',Class_Id={},Gender='{}',Address='{}',Contact_No={},Email_Id='{}',Emergency={}".format(SID,SNAME,CID,GENDER,ADD,CONNO,MID,EMER)
        si.cursor.execute(q)
        si.connection.commit()
        print(si.cursor.rowcount,"Record updated")
        
si.cursor.exe