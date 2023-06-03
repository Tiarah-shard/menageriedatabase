import mysql.connector as mc


conn = mc.connect(host='localhost', user='root', password='YU_oppdivide!20', database='menagerie')
cursor = conn.cursor()
select_pet = "SELECT name, birth FROM pet;"
cursor.execute(select_pet)
rows = cursor.fetchall()
for row in rows:
    name, birth = row
    print(f"Name: {name}, Birth: {birth}")
cursor.close()
conn.close()
