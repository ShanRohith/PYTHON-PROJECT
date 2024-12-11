import tkinter
from tkinter import *
from tkinter import  ttk
from tkinter import messagebox
from db import Database

db=Database("Employee.db")


w=Tk()
w.title("EMPLOYEE MANAGEMENT SYSTEM")
w.geometry("1366x768")
w.config(bg="#2C3E50")
w.state("zoomed")


## LABEL AND ENTRY FRAME
f1=Frame(w,bg="#2C3E50")
f1.pack(side=TOP,fill=X)

l1=Label(f1,text="EMPLOYEE MANAGEMENT SYSTEM",bg="#2C3E57",fg="gold",font=("times",30,"italic"),padx=10,pady=10)
l1.grid(row=0,columnspan=2,padx=10, pady=10)



## INPUTS

##NAME
name=StringVar()
l2=Label(f1,text="NAME",font=("times",20),fg="white",bg="#2C3E57",width=5)
l2.grid(row=1,column=0)
e2=Entry(f1,font=("times",15),width=30,textvariable=name)
e2.grid(row=1,column=1,padx=10,pady=10,sticky=W)

##AGE
age=StringVar()
l3=Label(f1,text="AGE",font=("times",20),fg="white",bg="#2C3E57",width=5)
l3.grid(row=1,column=2)
e3=Entry(f1,font=("times",15),width=30,textvariable=age)
e3.grid(row=1,column=3,padx=10,pady=10,sticky=W)

##DOB
dob=StringVar()
l4=Label(f1,text="DOB",font=("times",20),fg="white",bg="#2C3E57",width=5)
l4.grid(row=2,column=0)
e4=Entry(f1,font=("times",15),width=30,textvariable=dob)
e4.grid(row=2,column=1,padx=10,pady=10,sticky=W)

##EMAIL
email=StringVar()
l5=Label(f1,text="EMAIL",font=("times",20),fg="white",bg="#2C3E57",width=10)
l5.grid(row=2,column=2)
e5=Entry(f1,font=("times",15),width=30,textvariable=email)
e5.grid(row=2,column=3,padx=10,pady=10,sticky=W)

##GENDER
gender=StringVar()
l6=Label(f1,text="GENDER",font=("times",20),fg="white",bg="#2C3E57",width=10)
l6.grid(row=3,column=0,padx=10,pady=10)
combo_gender=ttk.Combobox(f1,font=("times",15),width=29,textvariable=gender,state="readonly")
combo_gender["values"]=("MALE","FEMALE","OTHERS")
combo_gender.grid(row=3,column=1,sticky=W,padx=8)

##CONTACT
contact=StringVar()
l7=Label(f1,text="CONTACT",font=("times",20),fg="white",bg="#2C3E57",width=10)
l7.grid(row=3,column=2)
e7=Entry(f1,font=("times",15),width=30,textvariable=contact)
e7.grid(row=3,column=3,padx=10,pady=10,sticky=W)


##ADDRESS
address=StringVar()
l8=Label(f1,text="ADDRESS",font=("times",20),fg="white",bg="#2C3E57",width=10)
l8.grid(row=4,column=0)
e8=Text(f1,font=("times",15),width=92,height=2)
e8.grid(row=4,column=1,columnspan=3,padx=10,pady=10,sticky=W)


## FUNCTION DEFIINITION FOR BUTTTONS

def getdata(event):
    selected=mytree.focus()
    data=mytree.item(selected)
    global infos
    infos=data["values"]
    ## SHIW FIELDS
    name.set(infos[1])
    age.set(infos[2])
    dob.set(infos[3])
    email.set(infos[4])
    gender.set(infos[5])
    contact.set(infos[6])
    e8.delete(1.0,END)
    e8.insert(END,infos[7])


def displayall():
    mytree.delete(*mytree.get_children())
    for info in db.fetch():
        mytree.insert("",END,values=info)


def add():
    if (e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="" or combo_gender.get()==""  or  e7.get()==""
        or e8.get(1.0,END)==""):
        messagebox.showerror("ERROR","PLS FILL ALL FIELDS")
    db.insert(e2.get(),e3.get(),e4.get(),e5.get(),combo_gender.get(),e7.get(),e8.get(1.0,END))
    messagebox.showinfo("SUCCESS","RECOREDS ADDEd")
    clear()
    displayall()

def update():
    if (e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="" or combo_gender.get()==""  or  e7.get()==""
        or e8.get(1.0,END)==""):
        messagebox.showerror("ERROR","PLS FILL ALL FIELDS")
        return
    db.update(infos[0],e2.get(),e3.get(),e4.get(),e5.get(),combo_gender.get(),e7.get(),e8.get(1.0,END))
    messagebox.showinfo("SUCCESS","RECOREDS UPDATED")
    clear()
    displayall()


def remove():
    db.delete(infos[0])
    clear()
    displayall()


def clear():
    name.set("")
    age.set("")
    dob.set("")
    email.set("")
    gender.set("")
    contact.set("")
    e8.delete(1.0,END)



f2=Frame(f1,bg="#2C3E50",padx=55,pady=10)
f2.grid(row=5,column=0,columnspan=4,padx=5,pady=5,sticky=W)


## BUTTOND(ADD,UPDATE,DELETE,CLEAR)

b1=Button(f2,command=add,text="ADD",font=("calibri",14,"bold"),bg="green",fg="white",padx=5,pady=5,width=25)
b1.grid(row=0,column=0,padx=5,pady=5)

b2=Button(f2,command=update,text="UPDATE",font=("calibri",14,"bold"),bg="green",fg="white",padx=5,pady=5,width=25)
b2.grid(row=0,column=1,padx=15,pady=5)

b3=Button(f2,command=remove,text="REMOVE",font=("calibri",14,"bold"),bg="green",fg="white",padx=5,pady=5,width=25)
b3.grid(row=0,column=2,padx=5,pady=5)

b4=Button(f2,command=clear,text="CLEAR",font=("calibri",14,"bold"),bg="red",fg="white",padx=5,pady=5,width=25)
b4.grid(row=0,column=3,padx=5,pady=5)



## TREEVIEW FRAMR
f3=Frame(w,bg="white")
f3.place(x=0,y=390,width=1366,height=550)

mystyle=ttk.Style()
mystyle.configure("mystyle.Treeview.Heading",font=("calibiri",15,"bold"),foreground="black")
mystyle.configure("mystyle.Treeview",font=("claibri",14),rowheight=25,background="white",foreground="black")

col=(1,2,3,4,5,6,7,8)
mytree=ttk.Treeview(f3,columns=col,show="headings",style="mystyle.Treeview")


mytree.heading(1,text="ID")
mytree.heading(2,text="NAME")
mytree.heading(3,text="AGE")
mytree.heading(4,text="DOB")
mytree.heading(5,text="EMAIL")
mytree.heading(6,text="GENDER")
mytree.heading(7,text="CONTACT")
mytree.heading(8,text="ADDRESS")



mytree.column(1,width=50,anchor=tkinter.CENTER)
mytree.column(2,width=150,anchor=tkinter.CENTER)
mytree.column(3,width=50,anchor=tkinter.CENTER)
mytree.column(4,width=120,anchor=tkinter.CENTER)
mytree.column(4,width=200,anchor=tkinter.CENTER)
mytree.column(6,width=60,anchor=tkinter.CENTER)
mytree.column(7,width=100,anchor=tkinter.CENTER)
mytree.column(8,width=200,anchor=tkinter.CENTER)

mytree.bind("<ButtonRelease-1>",getdata)

mytree.pack(fill=X)









displayall()
w.mainloop()
