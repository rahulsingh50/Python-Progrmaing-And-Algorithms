import sqlite3
import pandas as pd


# Connection's Object
connection_obj = sqlite3.connect(":memory:")

# Object of cursor
cursor_obj = connection_obj.cursor()
# Saving format of table
# It will be written as an SQLite command
create_table = "CREATE TABLE STUDENT(RollNo int, FirstName varchar(20), LastName varchar(20), Branch varchar(3))"
# Lets execute
cursor_obj.execute(create_table)
cursor_obj.execute("select * from SQLite_master where type=\"table\"")


# Lets print the tables--
print("Table availables (in-memory database):")

tables = cursor_obj.fetchall()

print("Tables list from SQLite Master:")

for table in tables:
    print("Data Base Object Name: %s"%(table[0]))
    print("Name database object: %s"%(table[1]))
    print("Table Name: %s"%(table[2]))
    print("Root page: %s"%(table[3]))
    print("SQL statement: %s"%(table[4]))

data = [
        (1,'Foo', 'Cool','ME'),
        (3,'Bar', 'Hot','CSE'),
        (5,'Moo', 'Zoo','IT')]

# Inserting the data--
try:
  sql = '''INSERT INTO STUDENT (RollNo, FirstName, LastName, Branch) VALUES(?,?,?,?)'''
  cursor_obj.executemany(sql, data)

except sqlite3.IntegrityError as e:
  print('sqlite error: ', e.args[0]) # column name is not unique
  
# Commiting the above changes--
connection_obj.commit()

# To view any particular entry--
cursor_obj.execute("SELECT * FROM STUDENT WHERE Branch='IT';")
print(cursor_obj.fetchall())

# Converting it to Flat File--
table = pd.read_sql_query("SELECT * from STUDENT", connection_obj)
table.to_csv("Student_Table" + '.csv', index_label='index')

# Getting all the table names--
res = cursor_obj.execute("SELECT name FROM sqlite_master WHERE type='table';")
for name in res:
    print (name[0])
    

# Safely Closing the SQL Data Base
connection_obj.close