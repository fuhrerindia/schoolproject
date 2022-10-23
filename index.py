import mysql.connector as x
from constant import *
from signin import signinprompt
from mainmenu import rootmenu

"""
    HI THERE!
"""
conn = x.connect(host=server, user=user, password=password, database=db)

if (conn.is_connected()):
    # do stuff
    name, uid = signinprompt(conn)
    print("\n\n")
    print("Hi "+name.split()[0]+", ")
    print("Hope you are doing well, \nWelcome to "+appname)
    rootmenu(conn)
else:
    # showing error to user
    print("Bhai yaar! Connect nahi horha mysql, kuch kar.")