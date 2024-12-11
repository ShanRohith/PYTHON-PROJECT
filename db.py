import sqlite3


class Database:
    ## creation of table
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        com = """CREATE TABLE IF NOT EXISTS employees(
               id INTEGER  Primary Key  ,
               name TEXT,
               age TEXT,
               dob TEXT,
               email TEXT,
               gender TEXT,
               contact TEXT,
               address TEXT)"""
        self.cur.execute(com)
        self.con.commit()

    # INSERT FUNCTION
    def insert(self,name, age, dob, email, gender, contact, address):
        self.cur.execute("INSERT INTO employees values (NULL,?,?,?,?,?,?,?)",(name,age,dob,email,gender,contact,address))
        self.con.commit()

    ## FECTCH ALL() DATA FROM DB
    def fetch(self):
        self.cur.execute("select * from employees")
        info = self.cur.fetchall()
        return info


    ## DROP DB
    def drop(self):
        self.cur.execute("DROP TABLE employees")
        self.con.commit()


    ## UPDATE VALUES IN DB
    def update(self,id,name, age, dob, email, gender, contact, address):
        self.cur.execute("UPDATE employees SET name=?, age=?, dob=?, email=?, gender=?, contact=?, address=? WHERE id=?",
                         (name, age, dob, email, gender, contact, address,id))
        self.con.commit()

    def delete(self,id):
        self.cur.execute("DELETE FROM employees  WHERE id=?",(id,))
        self.con.commit()



# o = Database("Employee.db")
#
# # o.drop()
# o.insert("shan","45","05-Apr-1970","shan@gmail.com","male","56565656","chennai")
# o.insert("rohith","23","01-Jul-2023","rohith2000dr@gmail.com","male","8428140832","chennai")
# o.insert("saran","22","01-Apr-2023","saranmech@gmail.com","male","8650385603","pallavaram")
# o.insert("ramesh","21","01-jan-2023","kumarramesh@gmail.com","male","9790351361","tambaram")
# o.insert("selva","24","01-Sep-2023","selvakumar45@gmail.com","male","7339283846","mount")
# o.insert("aravindhan","29","01-Dec-2023","arav56@gmail.com","male","8989898989","madurai")


# o.delete(5)



