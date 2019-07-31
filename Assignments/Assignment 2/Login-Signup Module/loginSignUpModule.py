# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 00:31:44 2019

@author: CL
"""

import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",       # mysql username
    password = "abc123", # mysql pass
    database = "users"  # target database
)
 
mycursor = db.cursor()    # hold all data of database

#TABLE CREATED
# =============================================================================
# mycursor.execute('''CREATE TABLE userData (
# id INT AUTO_INCREMENT PRIMARY KEY,
# uName VARCHAR(255) NOT NULL,
# pass VARCHAR(255) NOT NULL        
# )''')
# =============================================================================

print("LOGIN")

def dataInsertion():
    userName = str(input("Please Enter Your Name: "))
    userPass = str(input("Please Enter Your Password: "))
    userCpass = str(input("Confirm Password: "))

    if(userName == '' and userPass == '' and userCpass == ''):
        print("All Fields are Required")
        dataInsertion()
    elif(userPass != userCpass):
        print("Password Doesn't Matched")
        dataInsertion()
    else:
        query = ('''
        INSERT INTO userData (uName,pass)
        VALUES(%s,%s)                
        ''')        # %s is a placeholder
        
        userValues = (userName,userPass)
        mycursor.execute(query,userValues)
        db.commit()
        print("Record Insert Successfully.")

dataInsertion()



