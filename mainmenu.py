from constant import menuheading
from patient import newpatient, discharge_patient
def rootmenu():
    def patientmenu():
       while True:
           print(menuheading)
           print("""
            1. New Patient
            2. Discharge Patient
            3. Update Patient Details
            4. See Patient Details
            5. Go Back
           """)
           option = input("Your choice (1,2,3,4,5): ")
           if (option == "1"):
               newpatient()
           elif(option =="2"):
               discharge_patient()
           elif(option=="3"):
               print("Update patient")
           elif(option=="4"):
               print("patient details")
           else:
               break
            
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
    mainmenu()