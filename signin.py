from constant import appname
def signinprompt(conn):
    """
        RETURNS name and user id together.
        Saves signed in user into storage.dat file
    """
    print("\nSIGN TO " + appname )
    print()
    username = input("Enter your registered username: ").replace("'", "")
    password = input("Enter you respective password: ").replace("'", "")
    query = "SELECT id, name FROM user WHERE username='"+username+"' AND password='"+password+"';"
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchone()
    if (data == None):
        print("Wrong username or password, please try again.")
        print()
        return signinprompt(conn)
    else:
        user_name = data[1]
        uid = data[0]
        return user_name, uid