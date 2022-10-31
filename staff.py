from tabulate import tabulate
from constant import *

def Add_Employ():
	conn = connect()
	username = input("Create Username: ")
	sql = "SELECT * FROM user WHERE username = '"+username+"';"
	cur = conn.cursor()
	cur.execute(sql)
	data_caught = cur.fetchall()
	conn.close()
	if (len(data_caught) > 0):
		print("Username Already Exists")
		Add_Employ()
	else:
		Name = input("Enter Staff Name : ")
		Post = input("Enter Staff Post : ")
		Salary = input("Enter Staff Income : ")
		Sex   = input("Enter Staff Sex : ")
		passw = input("Create New Password: ")
		conf_passw = input("Confirm Password: ")
		if (passw == conf_passw):
			sql = "INSERT INTO user (name, username, password, salary, post, sex) VALUES('"+Name+"', '"+username+"', '"+passw+"', '"+Salary+"', '"+Post+"', '"+Sex+"');"
			conn = connect()
			c = conn.cursor()
			c.execute(sql)
			conn.commit()
			conn.close()
		else:
			print("Entered Passwords Do not match.")
		print("Employee Added Successfully ")
		menu()

def check_staff(id):
	sql = "SELECT name FROM user WHERE username='"+id+"';"
	con = connect()
	cur = con.cursor()
	cur.execute(sql)
	data = cur.fetchall()
	con.close()
	if (len(data) > 0):
		return True
	else:
		return False
# Function to Remove Employee with given Id
def Remove_Employ():
	Id = input("Enter Username: ")

	if(check_staff(Id) == False):
		print("Employee does not exists")
		menu()
	
	else:
		sql = "DELETE FROM user where username='"+Id+"';"
		conn = connect()
		c = conn.cursor()
		c.execute(sql)
		conn.commit()
		conn.close()
		print("="*10)
		print("Employee Removed")
		print("="*10)
		menu()
# Function to Display All Employees

def Display_Employees():
	
	sql = 'SELECT * FROM user;'
	conn = connect()
	c = conn.cursor()
	c.execute(sql)
	r = c.fetchall()
	conn.close()
	top_row = ["ID", "NAME", "USERNAME", "POST", "SALARY", "SEX"]
	data = []
	data.append(top_row)
	for i in r:
		row = list(i)
		del(row[3])
		data.append(row)
	print(tabulate(data))
	print()
	menu()
# menu function to display the menu
def display_emp_id():
	id = input("Username of Employee: ")
	sql = "SELECT id, name, username, salary, post, sex FROM user WHERE username='"+id+"'"
	conn = connect()
	cur = conn.cursor()
	cur.execute(sql)
	row = cur.fetchone()
	conn.close()
	print()
	print("ID", row[0], sep="\t")
	print("NAME", row[1], sep="\t")
	print("USERNAME", row[2], sep="\t")
	print("SALARY", row[3], sep="\t")
	print("POST", row[4], sep="\t")
	print("SEX", row[5], sep="\t")
	print()
def menu():
	while True:
		print("Welcome to Staff Management")
		print("Press ")
		print("1 to Add Employee")
		print("2 to Remove Employee ")
		print("3 to Display All Employees")
		print("4 Display Employee with ID")
		print("5 to Go Back")
		
		ch = input("Enter your Choice: ")
		if ch == "1":
			Add_Employ()
			
		elif ch == "2":
			Remove_Employ()
			
		elif ch == "3":
			Display_Employees()
		elif ch=="4":
			display_emp_id()
		elif ch == "5":
			break
		else:
			print("Invalid Choice")
			menu()
