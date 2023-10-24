import sqlite3

conn = sqlite3.connect('example.db')
print("Opened db successfuly")

conn.execute("DELETE from COMPANY1 where id=2") #delete row
conn.commit() # save changes

cursor = conn.execute("SELECT id, name, age, address, salary from COMPANY1")
for row in cursor:
    print("ID =", row[0])
    print("NAME =", row[1])
    print("AGE=", row[2])
    print("ADDRESS =", row[3])
    print("SALARY=", row[4])
print("Operation created successfully")
conn.close()


