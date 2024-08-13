from tkinter import*
from tkinter import ttk
win=Tk()
win.title("list")
win.geometry("1920x1080")
win.config(bg="#040720")
def total():
    MARK_1=int(e1.get())
    MARK_2=int(e2.get())
    MARK_3=int(e3.get())
    a=MARK_1+MARK_2+MARK_3
    e4.delete(0,END)
    e4.insert(0,a)
    b=a/3
    e5.delete(0,END)
    e5.insert(0,b)

    if MARK_1>35 and MARK_2>35 and MARK_3>35:
        result="pass"

    else:
        result="fail"
    e6.delete(0,END)
    e6.insert(0,result)
    if b>=90 and b<=100:
        grade="A"
    elif b>=80 and b<90:
        grade="B"
    elif b>=70 and b<80:
        grade="C"
    else:
        grade="D"
    e7.delete(0,END)
    e7.insert(0,grade)
f1=Frame(win,bg="#040720")
f1.pack(side=TOP,fill=X)
l1=Label(f1,text="STUDENT MARK LIST",font=("times",18,"bold"))
l1.grid(row=0,columnspan=2,padx=10,pady=10,sticky="w")
l2=Label(f1,text="MARK_1",font=("times",14,"bold"))
l2.grid(row=1,column=0,padx=10,pady=10,sticky="w")
e1=Entry(f1,width=30)
e1.grid(row=1,column=1,padx=10,pady=10,sticky="w")
l3=Label(f1,text="MARK_2",font=("times",14,"bold"))
l3.grid(row=1,column=2,padx=10,pady=10,sticky="w")
e2=Entry(f1,width=30)
e2.grid(row=1,column=3,padx=10,pady=10,sticky="w")
l4=Label(f1,text="MARK_3",font=("times",14,"bold"))
l4.grid(row=2,column=0,padx=10,pady=10,sticky="w")
e3=Entry(f1,width=30)
e3.grid(row=2,column=1,padx=10,pady=10,sticky="w")
l5=Label(f1,text="Total",font=("times",14,"bold"))
l5.grid(row=2,column=2,padx=10,pady=10,sticky="w")
e4=Entry(f1,width=30)
e4.grid(row=2,column=3,padx=10,pady=10,sticky="w")
l6=Label(f1,text="Average",font=("times",14,"bold"))
l6.grid(row=3,column=0,padx=10,pady=10,sticky="w")
e5=Entry(f1,width=30)
e5.grid(row=3,column=1,padx=10,pady=10,sticky="w")
l7=Label(f1,text="Result",font=("times",14,"bold"))
l7.grid(row=3,column=2,padx=10,pady=10,sticky="w")
e6=Entry(f1,width=30)
e6.grid(row=3,column=3,padx=10,pady=10,sticky="w")

l8=Label(f1,text="Grade",font=("times",14,"bold"))
l8.grid(row=4,column=0,padx=10,pady=10,sticky="w")

e7=Entry(f1,width=30)
e7.grid(row=4,column=1,padx=10,pady=10,sticky="w")

f2=Frame(f1,bg="#000fff")
f2.grid(row=5,columnspan=1,padx=10,pady=10)

b1=Button(f2,text="calculate",command=total)
b1.grid(row=5,column=1,padx=10,pady=10)

win.mainloop(0)