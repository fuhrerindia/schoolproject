import mysql.connector as x
user = 'root'
password = 'shrihari'
server = 'localhost'
db = 'hospital'
appname = 'GALI KA ASPATAL'
menuheading = "\nPlease enter serial number for respective functionality."
limit = {
    'A': 8, # 50 Beds for AC
    'S': 10, # 80 Beds for Standar Rooms (Non-Ac)
    'I': 2, # 20 ICU Beds
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
def show_options(options, heading=menuheading, ):
    """
    CREATES MENU, GETS INPUT AND DO RESPECTIVE TASKS
    Parameter 1: Options of menu (array) with option as dictionary
    In dictionary 'f' parameter as function and 'm' as option text.
    Parameter 2: Heading of the menu (optional)
    """
    print(heading)
    for option in range(len(options)):
        print(str(option+1) + ". " + str(options[option]['m']))
    v_op = "("
    opt = []
    for i in range(1, len(options)+1):
        opt.append(i)
        if (i == len(options)):
            v_op = v_op + str(i)
        else:
            v_op = v_op + str(i) + "|"
    v_op = v_op + ")"
    inpt = int(input("Please select your choice " + v_op + ": "))
    if inpt in opt:
        f = options[inpt-1]['f']
        f()
    else:
        print("Unknown Choice")