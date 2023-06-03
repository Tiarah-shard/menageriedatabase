import mysql.connector as mc


conn = mc.connect(host='localhost', user='root', password='YU_oppdivide!20', database='menagerie')
cursor = conn.cursor()
select_pet = "SELECT * FROM pet WHERE species = 'dog' AND sex = 'f'"
cursor.execute(select_pet)
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
conn.close()
