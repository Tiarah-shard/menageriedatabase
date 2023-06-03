import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='YU_oppdivide!20')
cursor = conn.cursor()
cursor.close()
conn.close()

