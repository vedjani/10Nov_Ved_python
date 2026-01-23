# 22) Write a Python program to insert data into an SQLite3 database and fetch it
import sqlite3

try:
    db=sqlite3.connect("databash_12.db")
    print("database connected")
except Exception as e:
    print(e)

ins_data="insert into empinfo(name,city) values('ved','morbi')"
try:
    db.execute(ins_data)
    print("data add")
    db.commit()
except Exception as e:
    print(e)

try:
    cr=db.cursor()
    cr.execute("select * from empinfo")
    data=cr.fetchall()
    for i in data:
        print(i)
except Exception as e:
    print(e)
    