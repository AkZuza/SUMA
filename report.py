import csv
import class_sql, course_sql, student_sql, marks_sql, common

def get_subjects(cid):
    su = course_sql.get_sujects(cid)
    subs = []
    for i in su:
        subs.append(i[0])
    return subs

def get_student_row(class_id, term, cid):
    dic = {}
    for s in student_sql.fetch_all():
        dic[s[0]] = {}

    for sid, ter, sub, mar, e, y, t in marks_sql.fetch_all():
        if ter == term and student_sql.fetch_student(sid)[2] == class_id:
            dic[sid][sub] = mar   

    rows = []
    for sid in dic:
        subs = get_subjects(cid)
        sname = student_sql.fetch_student(sid)[1]
        t = (sname,)  
        for i in sorted(subs):
            t += (dic[sid][i],)
        rows.append(i)
    return rows

def generate_report():
    classes = class_sql.fetch_all()
    
    for class_id, class_name, cid, tid in classes:
        subs = get_subjects(cid)
        for term in ['Term 1', 'Term 2', 'Term 3']:
            # row = get_student_row(class_id, term, cid)
            with open(class_name + '_' + term.replace(" ", "_") + ".csv", "w", newline="") as f:
                writer = csv.writer(f)
                for i in marks_sql.fetch_all():
                    if student_sql.fetch_student(i[0])[2] == class_id and term == i[1]:
                        sname = student_sql.fetch_student(i[0])[1]
                        writer.writerow((sname, class_name, i[1], i[2], i[3]))
                # writer.writerows(row)

    common.info_box('Generated Student and Absentee Reports')

    with open('absentees.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        import absentice_sql
        lol = absentice_sql.fetch_all()
        writer.writerows(lol)
                
