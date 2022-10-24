import mysql.connector as x
user = 'root'
password = 'shrihari'
server = 'localhost'
db = 'hospital'
appname = 'GALI KA ASPATAL'
menuheading = "\nPlease enter serial number for respective functionality."
limit = {
    'A': 50, # 50 Beds for AC
    'S': 80, # 80 Beds for Standar Rooms (Non-Ac)
    'I': 20, # 20 ICU Beds
}

def connect():
    conn = x.connect(host=server, user=user, password=password, database=db)
    return conn

def find_free(list, limit):
    unexisted = []
    for num in range(1, limit+1):
        if (num not in list):
            unexisted.append(num) 
    return unexisted