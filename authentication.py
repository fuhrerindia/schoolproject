from constant import appname, connect

def logout():
    fh = open('storage.txt', 'w')
    fh.write("")
    exit()
def signinprompt():
    """
        RETURNS name and user id together.
        Saves signed in user into storage.dat file
    """
    fh = open('storage.txt', "r+")
    text = fh.read()
    if (len(text) > 0):
        text = text.split("[split]")
        usern = text[0]
        passw = text[1]
    else:
        usern = None
        passw = None
    conn = connect()
    if (usern == None):
        print("\nSIGN TO " + appname )
    print()
    if (usern != None):
        username = usern
        password = passw
    else:
        username = input("Enter your registered username: ").replace("'", "")
        password = input("Enter you respective password: ").replace("'", "")
    query = "SELECT id, name FROM user WHERE username='"+username+"' AND password='"+password+"';"
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchone()
    if (data == None):
        print("Wrong username or password, please try again.")
        fh.seek(0)
        fh.write("")
        fh.close()
        print()
        conn.close()
        return signinprompt()
    else:
        user_name = data[1]
        uid = data[0]
        fh.seek(0)
        towrite = username+"[split]"+password
        fh.write(towrite)
        fh.close()
        conn.close()
        return user_name, uid