import tkinter as tk
from calendar import Calendar

import pymysql
from tkinter import *



def submitact():
        user = username
        passw = password

        print( f"The name entered by you is {user} {passw}" )

        logintodb( user, passw )


def logintodb(user, passw, db=None):
    # If password is enetered by the
    # user
    if passw:
        conn = pymysql.connect( host='localhost',
                                user=user,
                                password=passw,
                                db='musicly' )
        cursor = conn.cursor()

    # If no password is enetered by the
    # user
    else:
        conn = pymysql.connect( host='localhost',
                                user=user,
                                db='musicly' )
        cursor = conn.cursor()
        print("Connected to Database")
    # A Table in the database
    savequery = "select * from users"

    try:
        cursor.execute( savequery )
        myresult = cursor.fetchall()

        # Printing the result of the
        # query
        for x in myresult:
            print( x )
        print( "Query Executed successfully" )
    except:
        db.rollback()
        print( "Error occurred" )




# Insert in users table.



def userInfo():
    userInfo = Toplevel( root )
    userInfo.title("User Info")
    userInfo.geometry( "300x300" )


    lblsecrow = tk.Label( userInfo, text="Name -" )
    lblsecrow.place( x=50, y=50 )

    Username = tk.Entry( userInfo,  width=35 )
    Username.place( x=150, y=50, width=100 )


    lblsecrow = tk.Label( userInfo, text="Member -" )
    lblsecrow.place( x=50, y=80 )

    Member = tk.Entry( userInfo, width=35 )
    Member.place( x=150, y=80, width=100 )

    lblsecrow = tk.Label( userInfo, text="Password -" )
    lblsecrow.place( x=50, y=110 )

    Member = tk.Entry( userInfo, show="*", width=35 )
    Member.place( x=150, y=110, width=100 )

    lblsecrow = tk.Label( userInfo, text="DOB -" )
    lblsecrow.place( x=50, y=140 )

    Member = tk.Entry( userInfo, width=35 )
    Member.place( x=150, y=140, width=100 )


    lblsecrow = tk.Label( userInfo, text="Phone Num" )
    lblsecrow.place( x=50, y=170 )

    Member = tk.Entry( userInfo, width=35 )
    Member.place( x=150, y=170, width=100 )

    submitbtn5 = tk.Button( userInfo, text="Next",
                            bg='light blue', command=openNewWindow )
    submitbtn5.place( x=10, y=250, width=100 )
    submitbtn6 = tk.Button( userInfo, text="Exit",
                            bg='light blue', command=exit )
    submitbtn6.place( x=150, y=250, width=100 )

    Label( userInfo, font="Calibri, 12" ).pack()
    x = root.winfo_x()
    y = root.winfo_y()
    userInfo.geometry( "+%d+%d" % (x, y) )

    # Keep the toplevel window in front of the root window
    userInfo.wm_transient( root )


# New Window for Options

def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel( root )

    # sets the title of the
    # Toplevel widget
    newWindow.title( "Options" )

    # sets the geometry of toplevel
    newWindow.geometry( "300x300" )
    submitbtn1 = tk.Button( newWindow, text="Song Info",
                            bg='light blue', command=openNewWindow )
    submitbtn1.place( x=10, y=15, width=100 )

    submitbtn2 = tk.Button( newWindow, text="Artist Info",
                            bg='light blue', command=openNewWindow )
    submitbtn2.place( x=150, y=15, width=100 )
    submitbtn3 = tk.Button( newWindow, text="Add Song Review",
                            bg='light blue', command=openNewWindow )
    submitbtn3.place( x=10, y=75, width=100 )
    submitbtn4 = tk.Button( newWindow, text="Add Artist Review",
                            bg='light blue', command=openNewWindow )
    submitbtn4.place( x=150, y=75, width=100 )
    submitbtn5 = tk.Button( newWindow, text="Add Song Rating",
                            bg='light blue', command=openNewWindow )
    submitbtn5.place( x=10, y=135, width=100 )
    submitbtn6 = tk.Button( newWindow, text="Add Artist Rating",
                            bg='light blue', command=openNewWindow )
    submitbtn6.place( x=150, y=135, width=100 )

    submitbtn7 = tk.Button( newWindow, text="Exit",
                            bg='light blue', command=exit )
    submitbtn7.place( x=100, y=250, width=100 )


    Label( newWindow, font="Calibri, 12" ).pack()
    x = root.winfo_x()
    y = root.winfo_y()
    newWindow.geometry( "+%d+%d" % (x, y) )

    # Keep the toplevel window in front of the root window
    newWindow.wm_transient( root )


# Main Loop window
global username
global password
print( "Enter Username: " )
username = input()
print( "Enter Password: " )
password = input()

conn = pymysql.connect( host='localhost',
                                user=username,
                                password=password,
                                db='musicly' )
cursor = conn.cursor()



root = tk.Tk()
root.geometry( "300x300" )
root.title( "Database Connection Page" )
root.eval( 'tk::PlaceWindow . center' )


'''
submitbtn = tk.Button( root, text="Login",
                       bg='light blue', command=submitact )
submitbtn.place( x=150, y=135, width=55 )

'''

submitbtn = tk.Button( root, text="Connect to DataBase",
                       bg='light blue', command=lambda:[userInfo(), submitact()])
submitbtn.place( x=10, y=135, width=150 )

submitbtne = tk.Button( root, text="Exit",
                       bg='light blue', command=exit )
submitbtne.place( x=180, y=135, width=100 )


root.mainloop()
