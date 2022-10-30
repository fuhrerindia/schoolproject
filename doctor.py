from constant import *
import mysql.connector as ms
from tabulate import tabulate
def doctormenu():
    cn=connect()
    cur = cn.cursor()
    if True:
        while(True):
            print("""
            1. Show all doctor details
            2. Add new doctor
            3. Fire a doctor
            4. Edit doctor details
            5. Go back to main menu
            """)
            a=int(input("Enter your choice:"))
            if a==1:
                cur.execute("select * from doctor")
                rec=cur.fetchall()
                if (len(rec) > 0):
                    k = ["Doctor ID", "Name", "speciality", "Age", "Mobile_no", "Fees"]
                    out = []
                    out.append(k)
                    for i in rec:
                        out.append(i)
                    print(tabulate(out))
                else:
                    print("!!!NO DOCTOR FOUND!!!")
            elif a==2:
                Name=input("Enter name of the doctor:")
                Speciality=input("Enter doctor speciality:")
                Age=input("Enter age:")
                Mobile_no=input("Enter mobile number:")
                Fees=input("Enter fees:")
                sql = "insert into doctor (name, speciality, mobile, age, fees) values('"+Name+"', '"+Speciality+"', '"+Mobile_no+"', '"+Age+"', '"+Fees+"');"
                cur.execute(sql)
                cn.commit()
                print("""
                ======================================
                New doctor has been added successfully
                ======================================
                """)
            elif a==3:
                id=input("Enter Doctor ID:")
                p=input("Are you sure? (y/n):")
                if p=="y":
                    cur.execute("delete from doctor where doctor_id='"+id+"'")
                    cn.commit()
                    print("***Doctor has been fired***")
                else:
                    print("!!!Error in deletion!!!")
            elif a==4:
                if True:
                    while(True):
                        print("""
                        1. Change Speciality
                        2. Change Mobile
                        3. Change Age
                        4. Change Fees
                        5. Go Back
                        """)
                        b=input("Enter your choice:")
                        if b=="1":
                            lm=input("Enter Doctor_ID:")
                            ml=input("Enter new Speciality:")
                            cur.execute("UPDATE doctor SET Speciality='"+ml+"' where Doctor_ID='"+lm+"'")
                            cn.commit()
                            print(" ||| Value has been updated ||| ")
                        elif b=="2":
                            ps=input("Enter doctor_ID:")
                            sp=input("Enter new Mobile number:")
                            cur.execute("UPDATE doctor SET Mobile='"+sp+"' where Doctor_ID='"+ps+"'")
                            cn.commit()
                            print(" ||| Value has been updated ||| ")
                        elif b=="3":
                            np=input("Enter Doctor_ID:")
                            pn=input("Enter new Age:")
                            cur.execute("UPDATE doctor SET age='"+pn+"' where Doctor_ID='"+np+"'")
                            cn.commit()
                            print(" ||| Value has been updated ||| ")
                        elif b=="4":
                            wz=input("Enter Doctor_ID:")
                            zw=input("Enter new Fees:")
                            cur.execute("UPDATE doctor SET fees='"+zw+"' where Doctor_ID='"+wz+"'")
                            cn.commit()
                            print(" ||| Value has been updated ||| ")
                        else:
                            break
            elif a==5:
                break