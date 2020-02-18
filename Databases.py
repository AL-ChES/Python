from tkinter import *
import mysql.connector

mainwin = Tk()
mainwin.geometry("200x200")

mydb = mysql.connector.connect(host="localhost",user="aslan123",password="123",database="testdb")
mycursor = mydb.cursor()

def showmsg():
    from_entry = E1.get()
    mycursor.execute("insert into myemp(emp_id,emp_name,emp_phone) values(3,'%s',123456789)" % from_entry)
    mydb.commit()

L1 = Label(mainwin,text="Welcome To ASLAN")
L1.place(x=50,y=0)
B1 = Button(mainwin,text="Submit",command=showmsg)
B1.pack(side=BOTTOM)
E1 = Entry(mainwin,bd=2)
E1.place(x=50,y=20)




