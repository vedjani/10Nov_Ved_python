# 21) Write a Python program to create a database and a table using SQLite3.
import sqlite3

try:
    db=sqlite3.connect("databash_12.db")
    print("databash connected")
except Exception as e:
    print(e)

tbl_crt="create table empinfo(id integer primary key autoincrement, name varchar(20), city varchar(20)) "
try:
    db.execute(tbl_crt)
    print("table created")
except Exception as e:
    print(e)