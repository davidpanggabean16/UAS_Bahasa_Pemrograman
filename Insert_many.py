import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="Toko_Komputer"
)

cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
values = [
  ("Doni", "Jakarta"),
  ("Ella", "Tangerang"),
  ("Fani", "Bekasi"),
  ("Galih", "Depok"),
  ("Dava", "Bogor"),
]

for val in values:
  cursor.execute(sql, val)
  db.commit()

print("{} data ditambahkan".format(len(values)))