import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
VALUES(1,'EMOBILIS',7,'WESTLANDS',27000.00)");
conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
VALUES(2,'Safaricom',7,'WESTLANDS',27000.00)");
conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
VALUES(3,'Oracles',7,'WESTLANDS',27000.00)");
conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
VALUES(4,'Microsoft',7,'WESTLANDS',27000.00)");

# save values
conn.commit()
print("Records created successfully")
conn.close()