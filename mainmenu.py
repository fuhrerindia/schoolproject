
from constant import menuheading
from patient import patientmenu
from authentication import logout

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
        else:
            logout()