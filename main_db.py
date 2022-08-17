import sqlite3

student_dict = {}
admin_dict = {}
tasks = []
st_tasks = []
one_task_student = []


def student_login():
    st_lst = []
    con = sqlite3.connect("project_db.db")
    cur = con.cursor()
    query = ("SELECT username, password FROM students")
    res = cur.execute(query)
    result = res.fetchall()
    for i in result:
        student_dict[str(i[0])] = str(i[1])
        st_lst.append(i)
    return st_lst

def check_login(user,passw):
    con = sqlite3.connect("project_db.db")
    cur = con.cursor()
    query = (f"SELECT username, password FROM students where username = '{user}'")
    res = cur.execute(query)
    result = res.fetchone()
    if passw == result[1]:
        return True
    return False





def student_register_db(values):
    con = sqlite3.connect("project_db.db")
    cur = con.cursor()
    cur.execute("INSERT INTO students(username, firstname, lastname, prolanguage, password) VALUES(?, ?, ?, ?, ?)", values)
    con.commit()
    cur.close()
    con.close()




def admin_login():
    con = sqlite3.connect("project_db.db")
    cur = con.cursor()
    query = ("SELECT username, password FROM admins")
    res = cur.execute(query)
    result = res.fetchall()
    for i in result:
        admin_dict[str(i[0])] = str(i[1])


admin_login()



def admin_register_db(values_1):
    con = sqlite3.connect("project_db.db")
    cur = con.cursor()
    cur.execute("INSERT INTO admins(username, firstname, lastname, prolanguage, password) VALUES(?, ?, ?, ?, ?)", values_1)
    con.commit()
    cur.close()
    con.close()



def tasks_done_db(values_2):
    con = sqlite3.connect("project_db.db")
    cur = con.cursor()
    cur.execute("INSERT INTO taskss(title, taskdone, assessment, content, username) VALUES(?, ?, ?, ?, ?)", values_2)
    con.commit()
    cur.close()
    con.close()



def tasks_db():
    con = sqlite3.connect("project_db.db")
    cur = con.cursor()
    query = ("SELECT id, title, taskdone, assessment, content, username FROM taskss")
    res = cur.execute(query)
    result = res.fetchall()
    for i in result:
        tasks.append(i)

tasks_db()

def student_tasks(username):
    st_tasks = []
    con = sqlite3.connect("project_db.db")
    cur = con.cursor()
    query = (f"SELECT id, title, taskdone, assessment, content, username FROM taskss WHERE username = '{username}'")
    res = cur.execute(query)
    result = res.fetchall()
    for i in result:
        st_tasks.append(i)
    return st_tasks


def student_task_sh(username, title):
    one_task_student = []
    con = sqlite3.connect("project_db.db")
    cur = con.cursor()
    query = (f"SELECT id, title, taskdone, assessment, content, username FROM taskss WHERE username = '{username}' and title = '{title}'")
    res = cur.execute(query)
    result = res.fetchall()
    for i in result:
        one_task_student.append(i)
    return one_task_student



def del_task(title, username):
    con = sqlite3.connect("project_db.db")
    cur = con.cursor()
    cur.execute(f"DELETE FROM taskss WHERE title = '{title}' and username = '{username}'")
    con.commit()
    cur.close()
    con.close()





def change_task(values):
    con = sqlite3.connect("project_db.db")
    cur = con.cursor()
    cur.execute(f"UPDATE taskss SET title = ?, taskdone = ?, assessment = ?, content = ?, username = ? WHERE username = ? and title= ?", values)
    con.commit()
    cur.close()
    con.close()

   

