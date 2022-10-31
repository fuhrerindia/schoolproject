
from constant import menuheading
from patient import patientmenu
from authentication import logout
from doctor import doctormenu
from staff import menu

def mainmenu():
    while True:
        print(menuheading)
        print("""
            1. Patient Management
            2. Doctor Management
            3. Staff Management
            4. Logout
        """)
        selection = input("Your choice (1,2,3,4): ")
        if (selection == "1"):
            patientmenu()
        elif(selection == "2"):
            doctormenu()
        elif(selection == "3"):
            menu()
        else:
            logout()