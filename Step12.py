import mysql.connector as mc


conn = mc.connect(host='localhost', user='root', password='YU_oppdivide!20', database='menagerie')
cursor = conn.cursor()
cursor.execute("DESCRIBE pet")
table = cursor.fetchall()
for column in table:
    print(column[0], column[1], column[2], column[3], column[4])
cursor.close()
conn.close()
