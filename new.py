import tkinter as tk
import pymysql
from tkinter import *

from main import Username, password


class Musiclly:


    def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    newWindow.title( "Options" )

    # sets the geometry of toplevel
    newWindow.geometry( "300x300" )
    submitbtn1 = tk.Button( newWindow, text="Add",
                            bg='light blue', command=openNewWindow )
    submitbtn1.place( x=10, y=15, width=55 )

    submitbtn2 = tk.Button( newWindow, text="Update",
                            bg='light blue', command=openNewWindow )
    submitbtn2.place( x=10, y=15, width=55 )

    Label( newWindow, font="Calibri, 12" ).pack()
    x = root.winfo_x()
    y = root.winfo_y()
    newWindow.geometry( "+%d+%d" % (x, y) )

    # Keep the toplevel window in front of the root window
    newWindow.wm_transient( root )
    root.mainloop()

    Username=""
    password=""


    def __init__(self,user,passw):
        self.user=Username.get()
        self.passw=password.get()

        root = tk.Tk()
        root.geometry( "300x300" )
        root.title( "Database Connection Page" )
        root.eval( 'tk::PlaceWindow . center' )

        # Defining the first row
        lblfrstrow = tk.Label( root, text="Username -", )
        lblfrstrow.place( x=50, y=20 )

        Username = tk.Entry( root, width=35 )
        Username.place( x=150, y=20, width=100 )

        lblsecrow = tk.Label( root, text="Password -" )
        lblsecrow.place( x=50, y=50 )

        password = tk.Entry( root, show="*", width=35 )
        password.place( x=150, y=50, width=100 )

        '''
        submitbtn = tk.Button( root, text="Login",
                               bg='light blue', command=submitact )
        submitbtn.place( x=150, y=135, width=55 )

        '''

        submitbtn = tk.Button( root, text="Connect to DataBase",
                               bg='light blue', command=openNewWindow )
        submitbtn.place( x=90, y=135, width=150 )
