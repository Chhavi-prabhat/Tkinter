from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
def create_table():
    conn=sqlite3.connect('contacts.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts(
    name TEXT,
    phone NUMBER,
    email TEXT
    )''')
    conn.commit()
    conn.close()

win=Tk()
win.title("Form window")
win.maxsize(width=1000, height=600)
win.minsize(width=1000, height=600)
my_menu=Menu(win)
win.config(menu=my_menu)
file_menu=Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
nm=StringVar()
phn=StringVar()
eml=StringVar()
tt=StringVar()
def submit():
    name=nm.get()
    phone=phn.get()
    email=eml.get()
    conn=sqlite3.connect('Contacts.db')
    c=conn.cursor()
    c.execute('''INSERT INTO contacts (name, phone,email) VALUES(?,?,?)''',(name, phone,email))
    conn.commit()
    conn.close()
    msg=f"{name} is registered"
    messagebox.showinfo("Registered",msg)

def show_contacts():
    win2 = Tk()
    win2.title("Your Contacts")
    win2.maxsize(width=1200, height=400)
    win2.minsize(width=1200, height=400)
    del_btn = Button(win2, text="Delete", font=('Arial', 20, 'bold'), bg='red', fg='white', bd=3,command=deletion)
    edit_btn = Button(win2, text="Edit", font=('Arial', 20, 'bold'), bg='blue', fg='white', bd=3)
    del_btn.pack(side=BOTTOM, padx=10, pady=10)
    edit_btn.pack(side=BOTTOM, padx=10, pady=10)
    global text_area
    text_area=Text(win2, wrap=None,font=('Arial', 20))
    text_area.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar=Scrollbar(win2, orient=VERTICAL, command=text_area.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    text_area.configure(yscrollcommand=scrollbar.set)
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM contacts''')
    record = c.fetchall()
    for i, records in enumerate(record, start=1):
        text_area.insert(END, f"Name-{records[0]}\t Phone-{records[1]}\t Email-{records[2]}")
        text_area.insert(END,"\n")
def deletion():
    global text_area
    # Get the index of the currently selected text
    start_index = text_area.index("sel.first")
    end_index = text_area.index("sel.last")
    selected_contact = text_area.get(start_index, end_index).split("\n")[0]  # Extract only the first line
    print("Selected contact:", selected_contact)
    if selected_contact:
        confirmed = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete {selected_contact}?")
        if confirmed:
            try:
                conn = sqlite3.connect('contacts.db')
                c = conn.cursor()
                c.execute('''DELETE FROM contacts WHERE name = ?''', (selected_contact))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", f"{selected_contact} deleted successfully.")
                show_contacts()
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"SQLite error: {e}")
    else:
        messagebox.showerror("Error", "No contact selected.")

head_lbl=Label(win, text="Create new contact here!", fg="blue", font=('arial',24,'bold'))
head_lbl.place(x=500, y=40)
page_image=PhotoImage(file="form_img.png")
size_image=page_image.subsample(3,3)
Img_lbl=Label(win, image=size_image)
Img_lbl.place(x=10, y=100)

title=Label(win, text="Select Title", font=('arial', 16)).place(x=470, y=150)
enty=ttk.Combobox(win, width=28, textvariable=tt,font=('arial',14))
enty['values']= ('Ms.','Mr.','Mrs.')
enty.current(0)
enty.place(x=600, y=150)

name=Label(win, text="Enter name", font=('arial', 16),pady=25).place(x=470, y=190)
name_enty=Entry(win, width=30, font=('arial',14),bd=2, fg='grey', textvariable=nm).place(x=600, y=215)

phone=Label(win, text="Phone number", font=('arial', 16),pady=35).place(x=470, y=240)
phone_enty=Entry(win, textvariable=phn, width=28, font=('arial',14),bd=2, fg='grey').place(x=620, y=275)

email=Label(win, text="Enter email", font=('arial', 16), pady=25).place(x=470, y=310)
email_enty=Entry(win, width=30, font=('arial',14),bd=2, fg='grey',textvariable=eml).place(x=600, y=332)

create_btn=Button(win, text="Create contact", font=('arial', 16, 'bold'), bg='blue', fg='white',command=submit).place(x=520, y=400)
show_btn=Button(win, text="Show contacts", font=('arial', 16, 'bold'), bg='blue', fg='white',command=show_contacts).place(x=700, y=400)

create_table()
win.mainloop()