import sqlite3
from sqlite3 import Error

def showall():
    conn = sqlite3.connect('pass.db')
    c = conn.cursor()
 
    c.execute("SELECT * FROM PASSDB") 

    rows = c.fetchall()
    for row in rows:
        print(row)

    conn.commit()
    c.close()
    conn.close()


def add():
    conn = sqlite3.connect('pass.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS PASSDB(acc TEXT, url TEXT, uid TEXT, passwd TEXT)')
    
    acc = input('Account Name: ')
    url = input("Enter The Login URL: ")
    uid = input('Enter Username: ')
    passwd = input('Enter Password: ')
    c.execute('INSERT INTO PASSDB(acc, url, uid, passwd) VALUES(?, ?, ?, ?)', (acc, url, uid, passwd))
    conn.commit()

    c.close()
    conn.close() 


def find():
    conn = sqlite3.connect('pass.db')
    c = conn.cursor()

    acc = input('Enter The Account Name: ')
 
    c.execute("SELECT * FROM PASSDB WHERE acc=?", (acc,)) 

    rows = c.fetchall()
    for row in rows:
        print(row)

    conn.commit()
    c.close()
    conn.close()


def update():
    conn = sqlite3.connect('pass.db')
    c = conn.cursor()

    acc = input("Enter The Account Name: ")
    url = input("Provide Login URL: ")
    uid = input("Enter Login ID: ")
    passwd = input("Enter Login Password: ")

    c.execute("UPDATE PASSDB SET url=?, uid=?, passwd=? WHERE acc=?,", (url, uid, passwd, acc,))

    conn.commit()
    c.close()
    conn.close()

def delete():
    conn = sqlite3.connect('pass.db')
    c= conn.cursor

    acc = input('Enter Account Name:')

    c.execute('DELETE FROM PASSDB WHERE acc=?,', (acc,)) #problem with deleting records

    print("Entered Account Deleted. Printing Table....")

    showall()

    conn.commit()
    c.close()
    conn.close()


#test site
#add()
delete()
#find()
#showall()
#update()