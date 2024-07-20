#database Management Banking

import mysql.connector as sql


mydb = sql.connect(
    host ='localhost',
    user = 'root',
    passwd='root',
    database='BANK'
)

cursor = mydb.cursor()

def db_query(str):
    return cursor.execute(str)
mydb.commit()

if __name__== "__main__":
    createcustomertable()