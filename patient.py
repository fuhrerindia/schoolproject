from constant import *
def newpatient(conn):
    """
    CREATES NEW PATIENT IN DATABASE
    """
    print()
    print("-"*15)
    p_name = input("Patient Name (`'` will be removed): ").replace("'", "")
    p_dis = input("Known Disease(s) separate with comma: ").replace("'", "")
    meds = input("Medicines in Dosage: ").replace("'", "")
    bed = input("Bed Number (press Enter if not provided): ")
    doc = input("Appointed Doctor id number(s) [Separate with commas]: ")
    initial_amount = input("Initial Admission Amount (press Enter for 15000): ")
    admn = input("Admission amount paid? (y/n): ")
    
    if (admn != "y"):
        admn = "n"

    if (initial_amount == ""):
        initial_amount = '15000'
    

    if (len(p_name) > 250 or len(bed) > 12):
        print("Please check the length of Patient Name(250) and Bed(12).")
        newpatient()
    else:
        if (bed == ""):
            bed = "NULL"
        else:
            bed = "'"+bed+"'"
        sql = "INSERT INTO patient (name, medicines_in_dosage, known_diseases, bed, doctor, initial_amount, init_paid) VALUES('"+p_name+"', '"+meds+"', '"+p_dis+"', "+bed+", '"+doc+"', "+initial_amount+", '"+admn+"');"
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    print("-"*15)
    print()