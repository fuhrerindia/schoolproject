from constant import *
from tabulate import tabulate

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
            updatepatient()
        elif(option=="4"):
            seedetails()
        else:
            break


def printdata(data):
    header = ["Patient Id", "Name", "Disease", "Appointed Doctor", "Admission On", "Medicines Prescribed", "Known Diseases", "Medicines In Dosage", "Billed Amount", "Admission Amount", "Is Admission Amount Paid?", "Room Type", "Bed Number"]
    vals = []
    index = 0
    for i in header:
        val_tp = data[0][index]
        if (data[0][index] == "" or data[0][index] == None or data[0][index] == "None"):
            val_tp = "Not Applicable"
        else:
            val_tp = data[0][index]
        if (index == 10):
            if (val_tp == 'y'):
                val_tp = 'Yes'
            else:
                val_tp = 'No'
        vals.append([header[index], val_tp])
        index = index+1
    print(tabulate(vals))
def get_record_from_id(id):
    con = connect()
    sql = "SELECT * FROM patient WHERE id='"+id+"'"
    cur = con.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    return data
def find_empyt_bed():
    valid_type = []
    for key in limit: 
        valid_type.append(key)
    b_type = input("Preferred Room Type (A/S/I): ").upper()
    if (b_type in valid_type):
        con = connect()
        cur = con.cursor()
        btp = b_type.lower()
        cur.execute("SELECT bed_n FROM patient WHERE r_type='"+btp+"';")
        data = cur.fetchall()
        res_beds = []
        for rec in data:
            res_beds.append(rec[0])
        free_beds = find_free(res_beds, limit[b_type])
        if (len(free_beds)>0):
            return free_beds[0], b_type
        else:
            return None, None
    else:
        print("Invalid Input")
        return None, None
def seedetails():
    """
    SEARCH AND SEE PATIENT
    """
    while True:
        print("""
            Please select an option from below.
            1. Search from Patient ID
            2. Search from patient name
            3. Get info from bed number
            4. Go back
        """)
        opt = input("Please enter valid input (1,2, 3, 4): ")
        if (opt == "1"):
            pid = input("Enter Patient ID: ")
            data = get_record_from_id(pid)
            if (len(data)>0):
                printdata(data)
            else:
                print("No Patient Found")
        elif(opt == "2"):
            pname = input("Enter patient name: ")
            sql = "SELECT id, name FROM patient WHERE name LIKE '%"+pname+"%';"
            con = connect()
            cur = con.cursor()
            cur.execute(sql)
            data = cur.fetchall()
            con.close()
            data = [["Patient Id", "Patient Name"]] + data
            if (len(data) > 0):
                print()
                print(tabulate(data, headers="firstrow"))
                pid = input("Select required Patient ID from above: ")
                data = get_record_from_id(pid)
                if (len(data)>0):
                    printdata(data)
                else:
                    print("No Patient Found")
            else:
                print("No Patient Found")
        elif(opt=="3"):
            pref = input("Input Room Type (A/S/I): ").upper()
            bdn = input("Input bed number of patient: ")
            sql = "SELECT * FROM patient WHERE r_type='"+pref+"' AND bed_n='"+bdn+"'"
            con = connect()
            cur = con.cursor()
            cur.execute(sql)
            data = cur.fetchall()
            if (len(data) > 0):
                printdata(data)
            else:
                print("No Patient found on this bed.")
        else:
            break
def newpatient():
    """
    CREATES NEW PATIENT IN DATABASE
    """
    print()
    print("-"*15)
    conn = connect()
    res_bed, b_type = find_empyt_bed()
    if (res_bed != None):
        p_name = input("Patient Name (`'` will be removed): ").replace("'", "")
        p_dis = input("Known Disease(s) separate with comma: ").replace("'", "")
        meds = input("Medicines in Dosage: ").replace("'", "")
        doc = input("Appointed Doctor id number(s) [Separate with commas]: ")
        initial_amount = input("Initial Admission Amount (press Enter for 15000): ")
        admn = input("Admission amount paid? (y/n): ")
        
        if (admn != "y"):
            admn = "n"

        if (initial_amount == ""):
            initial_amount = '15000'
        

        if (len(p_name) > 250):
            print("Please check the length of Patient Name(250)")
            newpatient()
        else:
            sql = "INSERT INTO patient (name, medicines_in_dosage, known_diseases, doctor, initial_amount, init_paid, r_type, bed_n) VALUES('"+p_name+"', '"+meds+"', '"+p_dis+"', '"+doc+"', "+initial_amount+", '"+admn+"', '"+b_type+"', '"+str(res_bed)+"');"
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
        conn.close()
        con = connect()
        cur = con.cursor()
        sql = "select id from patient order by id desc limit 0,1;"
        cur.execute(sql)
        data = cur.fetchone()
        print("-"*15)
        print("Patient Name", p_name, sep="\t")
        print("Patient ID", data[0], sep="\t")
        print("Room Type", b_type, sep="\t")
        print("Bed Number", res_bed, sep="\t")
        print("Bed Alloted", b_type + str(res_bed), sep="\t")
        print()
    else:
        print("Bed is not empty for this preference. Look for another preference.")
    conn.close()
def nonets(val):
    if val == None:
        return ""
    else:
        return str(val)
def discharge_patient():
    conn = connect()
    pat_id = input("Enter Patient Admitted ID: ")
    sql = "SELECT * FROM patient WHERE id='"+pat_id+"';"
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    conn.close()
    if (len(data) > 0):
        pt_name = data[0][1]
        conf = input("Are you sure to discharge "+pt_name+"? (y/n): ").lower()
        if (conf == 'y'):
            con = connect()
            bed_l = data[0][11] + str(data[0][12])
            usr = data[0]
            ts = usr[4].strftime("%Y-%m-%d %H:%M:%S")
            sql = "INSERT INTO ex_patient (id, name, disease, doctor, admission_on, medicines, known_diseases, medicines_in_dosage, billed, initital_amount, bed) VALUES('"+str(usr[0])+"', '"+nonets(usr[1])+"', '"+nonets(usr[2])+"', '"+nonets(usr[3])+"', '"+ts+"', '"+nonets(usr[5])+"', '"+str(usr[6])+"', '"+str(usr[7])+"', '"+str(usr[8])+"', '"+str(usr[9])+"', '"+bed_l+"')"
            cur = con.cursor()
            cur.execute(sql)
            cur.execute("DELETE FROM patient WHERE id='"+pat_id+"'")
            con.commit()
            con.close()
            print("Patient can be discharged now.")
            if (usr[10] == 'y'):
                print("Please collect Rs."+str(usr[8])+" from the patient.")
            else:
                print("Please collect Rs."+str(usr[8]+usr[9])+" from the patient.")
        else:
            print("Skipped Discharging.")
    else:
        print("Patient with provided ID can't be found, please try again.")
        discharge_patient()

def pre_detal_editing(data):
    new_name = input("Enter name to update ["+data[1]+"]: ")
    if (new_name == ""):
        new_name = data[1]
    print("Known diseases are listed below")
    i = 0
    for disease in data[6].split(", "):
        i = i+1
        print(str(i)+".", disease, sep=" ")
    known_disease = input("Update Known diseases: ")
    if (known_disease == ""):
        known_disease = data[6]
    print("Prescribed meds are listed below")
    i = 0
    for meds in data[7].split(", "):
        i = i+1
        print(str(i)+".", meds, sep=" ")
    known_meds = input("Update Known Medicines: ")
    if (known_meds == ""):
        known_meds = data[7]
    sql = "UPDATE patient SET name='"+new_name+"', medicines_in_dosage='"+known_meds+"', known_diseases='"+known_disease+"' WHERE id='"+str(data[0])+"';"
    if (call_sql(sql)):
        print("Updated Record")
    else:
        print("Error Occured")
def strong_edit(data):
    p_meds = input("Enter Prescribed Medicines to update: ")
    if (p_meds == ""):
        p_meds = data[5]
    docs = input("Update Doctors: ")
    if (docs == ""):
        docs = data[3]
    update_bed = input("Update Bed? (y/n): ")
    if (update_bed == "y"):
        bn, bt = find_empyt_bed()
    else:
        bt = data[11]
        bn = data[12]
    sql = "UPDATE patient SET medicines='"+p_meds+"', doctor='"+str(docs)+"', r_type='"+bt+"', bed_n='"+str(bn)+"' WHERE id='"+str(data[0])+"';"
    if (call_sql(sql)):
        print("Updated Record")
    else:
        print("Error Occured")
def alter_detail(data):
    p_meds = input("Enter Prescribed Medicines to add: ")
    docs = input("Add Doctors: ")
    d_dis = input("Add disease: ")
    if (p_meds != ""):
        if (data[5] != ""):
            p_meds = data[5] + ", " + p_meds
    else:
        p_meds = data[5]
    if (docs != ""):
        if (data[3] != ""):
            docs = data[3] + ", " + docs
    else:
        docs = data[3]
    if (d_dis != ""):
        if (data[2] != ""):
            if (data[2] != None):
                d_dis = data[2] + ", " + d_dis
    else:
        d_dis = data[2]

    sql = "UPDATE patient SET medicines='"+p_meds+"', doctor='"+str(docs)+"', disease='"+d_dis+"' WHERE id='"+str(data[0])+"';"
    if (call_sql(sql)):
        print("Updated Record")
    else:
        print("Error Occured")
def change_billing(data):
    print("""
    1. Initial Bill Paid detail
    2. Add new amount to bill
    3. Edit bill amount
    4. Edit Admission Charges
    """)
    option = input("Select option: ")
    if (option == "1"):
        is_paid = input("Is initital admission charges paid? (y/n): ")
        if (is_paid == "y"):
            vl = "y"
        else:
            vl = "n"
        sql = "UPDATE patient SET init_paid='"+vl+"' WHERE id='"+str(data[0])+"';"
        call_sql(sql)
        print("Updated Amount")
    elif (option == "2"):
        new_amount = int(input("Enter Amount to add: "))
        new_amount = data[8] + new_amount
        new_amount = str(new_amount)
        sql = "UPDATE patient SET billed='"+new_amount+"' WHERE id='"+str(data[0])+"';"
        call_sql(sql)
        print("Updated Bill")
    elif (option == "3"):
        amount = input("Enter Bill Amount (Rs. "+str(data[8])+"): ")
        sql = "UPDATE patient SET billed='"+amount+"' WHERE id='"+str(data[0])+"';"
        call_sql(sql)
        print("Changed Billed Amount to Rs.", amount)
    elif(option == "4"):
        new_admsn = input("Change Admission Charges (Rs."+str(data[9])+"): ")
        sql = "UPDATE patient SET initial_amount='"+new_admsn+"' WHERE id='"+str(data[0])+"';"
        call_sql(sql)
        print("Updated Admission Charges.")

def updatepatient():
    pid = input("Enter Patient ID: ")
    data = call_sql("SELECT * FROM patient WHERE id='"+pid+"';")
    if (len(data) > 0):
        while True:
            print("""
            Select appropriate option from below.
            1. Edit patient's early details [Name, Past Meds, Past Known Disease]
            2. Edit Prescribed Medicines, Doctor, Room Type, Bed Number
            3. Alter Prescribed Medicines, Doctor, Diagnosed Disease
            4. Change Billing
            5. Go Back
            """)
            option = input("Select Option (1,2,3): ")
            if (option == "1"):
                pre_detal_editing(data[0])
            elif(option == "2"):
                strong_edit(data[0])
            elif(option == "3"):
                alter_detail(data[0])
            elif(option == "4"):
                change_billing(data[0])
            else:
                break
    else:
        print("Can't Find this patient")