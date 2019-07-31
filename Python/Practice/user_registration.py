# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:03:25 2019

@author: CL
"""


userNames = []

def myfunc():
    name = str(input("What is your name?\n"))
    userNames.append(name)
    choice = str(input("Press 'Y' to Continue and 'N' to Exit.\n"))
    if(choice == 'Y'):
        myfunc()
    elif(choice == 'y'):
        myfunc()
    elif(choice == 'N'):
        exit
    elif(choice == 'n'):
        exit
    else:
        print("No choice made. Exiting")
            
myfunc()

print(userNames[0:])