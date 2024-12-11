from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
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

l1=Label(f1,text="EMPLOYEE MANAGEMENT SYSTEM",bg="#2C3E57",fg="white",font=("times",25,"bold"),pady=20)
l1.grid(row=0,columnspan=2,padx=20, pady=20)



## INPUTS

##NAME
name=StringVar()
l2=Label(f1,text="NAME",font=("times",20),fg="white",bg="#2C3E57",width=10)
l2.grid(row=1,column=0)
e2=Entry(f1,font=("times",20),width=30,textvariable=name)
e2.grid(row=1,column=1,padx=5,pady=5)

##AGE
age=StringVar()
l3=Label(f1,text="AGE",font=("times",20),fg="white",bg="#2C3E57",width=10)
l3.grid(row=1,column=2)
e3=Entry(f1,font=("times",20),width=30, textvariable=age)
e3.grid(row=1,column=3,padx=5,pady=5)

##DOB
dob=StringVar()
l4=Label(f1,text="DOB",font=("times",20),fg="white",bg="#2C3E57",width=10)
l4.grid(row=2,column=0)
e4=Entry(f1,font=("times",20),width=30,textvariable=dob)
e4.grid(row=2,column=1,padx=5,pady=5)

##EMAIL
email=StringVar()
l5=Label(f1,text="EMAIL",font=("times",20),fg="white",bg="#2C3E57",width=10)
l5.grid(row=2,column=2)
e5=Entry(f1,font=("times",20),width=30,textvariable=email)
e5.grid(row=2,column=3,padx=5,pady=5)

##GENDER
gender=StringVar()
l6=Label(f1,text="GENDER",font=("times",20),fg="white",bg="#2C3E57",width=10)
l6.grid(row=3,column=0,padx=5,pady=5)
combo_gender=ttk.Combobox(f1,font=("times",20),width=29,textvariable=gender,state="readonly")
combo_gender["values"]=("MALE","FEMALE","OTHERS")
combo_gender.grid(row=3,column=1)

##CONTACT
contact=StringVar()
l7=Label(f1,text="CONTACT",font=("times",20),fg="white",bg="#2C3E57",width=10)
l7.grid(row=3,column=2)
e7=Entry(f1,font=("times",20),width=30,textvariable=contact)
e7.grid(row=3,column=3,padx=5,pady=5)


##ADDRESS
address=StringVar()
l8=Label(f1,text="ADDRESS",font=("times",20),fg="white",bg="#2C3E57",width=10)
l8.grid(row=4,column=0,padx=5,pady=5)
e8=Text(f1,font=("times",20),width=48,height=2)
e8.grid(row=4,column=1,columnspan=3,sticky=W,padx=12,pady=5)


## BUTTON FRAME

def getdata(event):
    selected=mytree.focus()
    data=mytree.item(selected)
    global  infos
    infos=data["values"]
    ##  SHOW FIELDS
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
    if(e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="" or combo_gender.get()=="" or e7.get()==""
        or e8.get(1.0,END)==""):
        messagebox.showerror("ERROR","PLEASE FILL ALL FIELDS")
        return
    db.insert(e2.get(),e3.get(),e4.get(),e5.get(),combo_gender.get(),e7.get(),e8.get(1.0,END))
    messagebox.showinfo("SUCCESS","DATAS UPDATED")
    clear()
    displayall()

def select():
    pass

def update():
    if ( e2.get() == "" or e3.get() == "" or e4.get() == "" or e5.get() == "" or combo_gender.get() == "" or e7.get() == ""
            or e8.get(1.0, END) == ""):
        messagebox.showerror("ERROR", "PLEASE FILL ALL FIELDS")
        return
    db.update(infos[0],e2.get(), e3.get(), e4.get(), e5.get(), combo_gender.get(), e7.get(), e8.get(1.0, END))
    messagebox.showinfo("SUCCESS", "DATAS UPDATED")
    clear()
    displayall()



def delete():
    db.delete(infos[0])
    clear()
    displayall()

def deletemany():
    pass

def clear():
    name.set("")
    age.set("")
    dob.set("")
    email.set("")
    gender.set("")
    contact.set("")
    e8.delete(1.0,END)




f2=Frame(f1,bg="#2C3E50",padx=10,pady=10)
f2.grid(row=5,column=0,columnspan=4,padx=5,pady=5,sticky=W)

## BUTTOND(ADD,UPDATE,DELETE,CLEAR)

b1=Button(f2,command=add,text="ADD",font=("calibri",10,"bold"),bg="green",fg="white",padx=10,pady=10,width=20)
b1.grid(row=0,column=0,padx=10,pady=10)

b2=Button(f2,command=select,text="SELECT",font=("calibri",10,"bold"),bg="green",fg="white",padx=10,pady=10,width=20)
b2.grid(row=0,column=1,padx=10,pady=10)

b3=Button(f2,command=update,text="UPDATE",font=("calibri",10,"bold"),bg="green",fg="white",padx=10,pady=10,width=20)
b3.grid(row=0,column=2,padx=10,pady=10)

b4=Button(f2,command=delete,text="DELETE",font=("calibri",10,"bold"),bg="green",fg="white",padx=10,pady=10,width=20)
b4.grid(row=0,column=3,padx=10,pady=10)

b5=Button(f2,command=deletemany,text="DELETE MANY",font=("calibri",10,"bold"),bg="green",fg="white",padx=10,pady=10,width=20)
b5.grid(row=0,column=4,padx=10,pady=10)

b6=Button(f2,command=clear,text="CLEAR",font=("calibri",10,"bold"),bg="red",fg="white",padx=10,pady=10,width=20)
b6.grid(row=0,column=5,padx=10,pady=10)




## TREE FRAME

f3=Frame(w,bg="white")
f3.place(x=0,y=420,width=1366,height=300)                       ## 1366x768

## STYLING OF HEADING AND TREEVIEW TABLE
mystyle=ttk.Style()
mystyle.configure("mystyle.Treeview.Heading",font=("family",15,"bold"))
mystyle.configure("mystyle.Treeview",font=("claibiri",15),rowheight=25)

## TREEVIEW
mytree=ttk.Treeview(f3,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")




##HEADINg
mytree.heading("1",text="ID")
mytree.column("1",width=50)
mytree.heading("2",text="NAME")
mytree.heading("3",text="AGE")
mytree.column("3",width=100)
mytree.heading("4",text="D.O.B")
mytree.column("4",width=100)
mytree.heading("5",text="E-MAIL")
mytree.column("5",width=300)
mytree.heading("6",text="GENDER")
mytree.column("6",width=100)
mytree.heading("7",text="CONATCT")
mytree.column("7",width=150)
mytree.heading("8",text="ADDRESS")
mytree["show"]="headings"
mytree.bind("<ButtonRelease-1>",getdata)

mytree.pack(fill=X)



displayall()

w.mainloop()
