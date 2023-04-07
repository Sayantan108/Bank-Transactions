from transactions import *

createAccountsTable()
db_connection.commit()

names = ["Philip Rodgers", "Lorenzo Kim", "Jair Cain", "Rodolfo Ritter", "Kevin Berry"]
address = ["Park Street, NY Upstate", "White House, Toronto", "Azerbaizan", "803, Adeilade", "London", "Denmark"]
gender = ["M", "F", "M", "M", "M"]


for i in zip(names, address, gender):
  insertInAccountsTable(i[0], i[1], i[2])
  db_connection.commit()

createCardsTable()
db_connection.commit()

cursor.execute("SELECT AccountNo FROM accounts;")
account_number = cursor.fetchall()
pins = ['4567', '1024', '4096', '3072', '6436']

for i in range(len(account_number)):
  insertInCardsTable(account_number[i][0], pins[i])
  db_connection.commit()

createChequesIssuedTable()
db_connection.commit()
