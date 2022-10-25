from constant import *
import datetime 
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