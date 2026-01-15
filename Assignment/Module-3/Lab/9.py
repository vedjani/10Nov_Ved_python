# Write a Python program to connect to an SQLite3 database, create a table, insert data, and fetch data.
import sqlite3

try:
    db=sqlite3.connect("school.db")
    print("database connected!")
except Exception as e:
    print(e)

#table cerate
tbl_create="create table studinfo(id integer primary key autoincrement, name varchar(20), city varchar(20))"

try:
    db.execute(tbl_create)
    print("table createed")
except Exception as e:
    print(e)

#insert data
ins_data="insert into studinfo(name,city) values('ved','morbi'),('harsh','rajkot')"

try:
    db.execute(ins_data)
    db.commit()
    print("data added")
except Exception as e:
    print(e)

#fetch data

fetch="select * from studinfo"
try:
    cr=db.cursor()
    cr.execute(fetch)
    data=cr.fetchall()
    # print(data)
    for i in data:
        print(i)
except Exception as e:
    print(e)