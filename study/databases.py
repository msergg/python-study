import sqlite3


con = sqlite3.connect('db.sqlite')

# con.execute("insert into t (a, b) values (?, ?);", (3000, 'OLOLO'))


# con.commit()

c = con.execute("select * from t;")
# print c.fetchone()
# print c.fetchall()


fields = ('a', 'b')
zip(fields, row)
dict(zip(fields, row))

for row in c:
    print row


    # ORM
    # SQLALCHEMY
    # PEEWEE