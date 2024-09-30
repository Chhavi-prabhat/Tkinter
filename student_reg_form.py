from tkinter import *
from tkinter import messagebox
import sqlite3 

def create_table():
    conn=sqlite3.connect('registration.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Registration(
    Name TEXT,
    Dob TEXT,
    Phno TEXT)''')
    conn.commit()
    conn.close()

def submit_registration():
    # Get values from entry fields
    Name = lbl2_enty.get()
    Dob = lbl3_enty.get()
    Phno = lbl4_enty.get()

    conn=sqlite3.connect('registration.db')
    c=conn.cursor()
    c.execute('''INSERT INTO Registration(Name, Dob, Phno) VALUES(?,?,?)''',(Name, Dob, Phno))
    conn.commit()
    conn.close()
    
    # Display confirmation message
    messagebox.showinfo("Registration Confirmation")

win = Tk()
win.maxsize(width=600, height=400)
win.minsize(width=600, height=400)
win.title("Student_Registration_form")

head_lbl = Label(win, text="STUDENT REGISTRATION FORM!", bg="blue", fg="white", font="arial")
head_lbl.place(x=120, y=2)

lbl2 = Label(win, text="Name", bg="black", fg="white", font="arial")
lbl2.place(x=15, y=35)
lbl2_enty = Entry(win, font="arial", width=50)
lbl2_enty.place(x=70, y=35)

lbl3 = Label(win, text="DOB", bg="black", fg="white", font="arial")
lbl3.place(x=15, y=65)
lbl3_enty = Entry(win, font="arial", width=50)
lbl3_enty.place(x=70, y=65)

lbl4 = Label(win, text="Phone", bg="black", fg="white", font="arial")
lbl4.place(x=15, y=95)
lbl4_enty = Entry(win, font="arial", width=50)
lbl4_enty.place(x=70, y=95)

btn = Button(win, text='Submit', bg="green", fg="white", font="arial", bd=3, command=submit_registration)
btn.place(x=210, y=170)

clr_btn = Button(win, text='Clear', bg="blue", fg="white", font="arial", bd=3)
clr_btn.place(x=290, y=170)
create_table()

win.mainloop()
