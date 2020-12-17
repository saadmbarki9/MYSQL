from tkinter import *
from tkinter import ttk
import MySQLdb as mdb
from tkinter import messagebox as msg

DBNAME= 'sql9382682'
DBHOST = 'sql9.freemysqlhosting.net'
DBPASS = 'vee3VfyyuE'
DBUSER = 'sql9382682'

root= Tk()
root.title("first try")
root.geometry("600x360")

#hado label ze3ma lktba li ktkon 9bl la case li ghadi tapi fiha les données dyalk
Label(root , text = 'Full name:',font='arial 10 bold').grid(column = 0,row = 0 , padx = 10 , pady=10, sticky="w" )
Label(root , text = 'E-mail :',font='arial 10 bold').grid(column = 0,row = 1 , padx = 10 , pady=10,sticky="w" )
Label(root , text = 'Phone:',font='arial 10 bold').grid(column = 0,row = 2 , padx = 10 , pady=10,sticky="w" )

#hna creation dyal les cases li ghadi dkhel fihom data dyawlk
name=ttk.Entry(root, width=30, font='arial 15 bold')
name.grid(column=1,row=0,padx=10,pady=10)

email=ttk.Entry(root, width=30, font='arial 15 bold')
email.grid(column=1,row=1,padx=10,pady=10)

phone=ttk.Entry(root, width=30, font='arial 15 bold')
phone.grid(column=1,row=2,padx=10,pady=10)


#creation dyal boutton 
btn=ttk.Button(root, text="create account", command=lambda : ff(name.get(),email.get(),phone.get()))
btn.grid(column=1,row=3,padx=10,pady=10,)


#khasna fonction li ghadi t verifi lya wash pass1=pass2 o tsift lya data l hosting
def ff(name,email,phone):
    db=mdb.connect(DBHOST, DBUSER , DBPASS , DBNAME)
    cur=db.cursor()
    print('Done')
    insert = (
        "INSERT INTO data (name , email , phone)" 
        "VALUES (%s,%s,%s)"
    )
    vallues = (str(name) , str(email) , str(phone))
    cur.execute(insert ,vallues)
    db.commit()
    msg.showinfo('Data saved','Data saved sucsesully')
    db.close()

root.mainloop()