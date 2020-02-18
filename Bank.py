from tkinter import *
import mysql.connector

root = Tk()
root.geometry("200x100")

mydata = mysql.connector.connect(host='localhost', user='aslan', password='123', database='bank_data')
mycursor = mydata.cursor()

def Sign_up():
    
    root.destroy()
    
    top = Tk()
    top.geometry("300x300")

    L1 = Label(top, text="Username:")
    L1.place(x=50,y=50)
    L2 = Label(top, text="password:")
    L2.place(x=50,y=80)
    L3 = Label(top, text="Email ID:")
    L3.place(x=50,y=110)
    L4 = Label(top, text="Address:")
    L4.place(x=50,y=140)
    L5 = Label(top, text="Amount:")
    L5.place(x=50,y=170)

    E1 = Entry(top)
    E1.place(x=120, y=50)
    E2 = Entry(top)
    E2.place(x=120, y=80)
    E3 = Entry(top)
    E3.place(x=120, y=110)
    E4 = Entry(top)
    E4.place(x=120, y=140)
    E5 = Entry(top)
    E5.place(x=120, y=170)

    def Add_Data():
    	userID = 104
    	username = E1.get()
    	password = E2.get()
    	email_id = E3.get()
    	address = E4.get()
    	amount = int(E5.get())

    	mycursor.execute("insert into customer_data (Cus_id, Cus_name, Cus_email, Cus_password, Cus_Add, Cus_Amount) values ('%d','%s','%s','%s','%s','%d')" %(userID,username,password,email_id,address,amount))
    	mydata.commit()   

    B1 = Button(top, text='Sing up', command=Add_Data)
    B1.place(x=140,y=200)

    top.mainloop()


B1 = Button(root, text='Log in')
B1.place(x=40,y=40)

B2 = Button(root, text='Sing up', command=Sign_up)
B2.place(x=120,y=40)


root.mainloop()
