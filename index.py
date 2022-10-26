from constant import *
from signin import signinprompt
from mainmenu import rootmenu

"""
    HI THERE!
"""
if (test_mode):
    name, uid = appname, 1
else:
    name, uid = signinprompt()
print("\n\n")
print("Hi "+name.split()[0]+", ")
print("Hope you are doing well, \nWelcome to "+appname)
rootmenu()