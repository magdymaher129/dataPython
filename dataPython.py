import sqlite3
conn=sqlite3.connect('DB/hr.db')
if conn:
    print ('ok')
c=conn.cursor()

#c.execute("INSERT INTO COMPANY VALUES ('1','SAMY','LONDON')")
#c.execute("INSERT INTO COMPANY VALUES ('2','JAC','PARIS')")
#c.execute("INSERT INTO COMPANY VALUES ('3','MARK','BON')")
c.execute("update  company set name='mary' where id =3")
conn.commit()
c.execute("select * from COMPANY ")
print (c.fetchall())
conn.commit()
conn.close()
