import random, sqlite3 as db
from models import *

db_connection = db.connect("database.sqlite", check_same_thread=False)
cursor = db_connection.cursor()

def generateRandomNumberOfSize(n):
  _min = pow(10, n-1)
  _max = pow(10, n) - 1
  return str(random.randint(_min, _max))

def validateAccountNumber(account_no):
  cursor.execute(f"""
    SELECT AccountNo from accounts 
    WHERE AccountNo='{account_no}'
  """)
  data = cursor.fetchall()
  return len(data) == 1

def validateCheque(cheque: cheque):
  cursor.execute(f"""
    SELECT * from cheques_issued 
    WHERE AccountNo='{cheque.payer_ac}' 
    AND Amount={cheque.amount} 
    AND ChequeNo='{cheque.cheque_no}'
  """)
  data = cursor.fetchall()
  return len(data) == 1

def validateCard(card: card, pin):
  cursor.execute(f"""
    SELECT CardNo from cards 
    WHERE CardNo='{card.card_no}' AND Pin='{pin}';
  """)
  data = cursor.fetchall()
  return len(data) == 1

def getAccountNumber(card: card):
  cursor.execute(f"""
    SELECT AccountNo from cards 
    WHERE CardNo='{card.card_no}'
  """)
  data = cursor.fetchall()
  return data[0][0]

def getAccountBalance(account_no):
  cursor.execute(f"""
    SELECT balance from accounts 
    WHERE AccountNo='{account_no}'
  """)
  data = cursor.fetchall()
  return data[0][0]

def validateTransactionAmount(account_no, amount):
  cursor.execute(f"""
    SELECT balance from accounts 
    WHERE AccountNo='{account_no}'
  """)
  balance = cursor.fetchall()[0][0]
  return float(balance) >= float(amount)

def validateUserCredentials(account_no, accountholders_name, card: card):
  cursor.execute(f"""
    SELECT * from accounts 
    WHERE AccountNo='{account_no}' AND Name='{accountholders_name}';
  """)
  accounts = cursor.fetchall()
  cursor.execute(f"""
    SELECT * from cards 
    WHERE AccountNo='{account_no}' AND CardNo='{card.card_no}';
  """)
  cards = cursor.fetchall()
  return (len(accounts) == 1 and len(cards) == 1)
