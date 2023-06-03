import mysql.connector as mc


conn = mc.connect(host='localhost', user='root', password='YU_oppdivide!20', database='menagerie')
cursor = conn.cursor()
select_pet = """ 
SELECT owner, COUNT(*) AS pet_count
FROM pet
GROUP BY owner;
"""
cursor.execute(select_pet)
rows = cursor.fetchall()
for row in rows:
    owner, pet_count = row
    print(f"Owner: {owner}, Pets Owned: {pet_count}")
cursor.close()
conn.close()
