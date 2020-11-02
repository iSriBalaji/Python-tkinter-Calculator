#Code - Sri Balaji Muruganandam
from tkinter import *
import os

di=os.path.dirname(__file__)

root=Tk()
root.title("CalX")
root.configure(background="#232232")
root.resizable(0,0)          #disables the maximize button

ph=PhotoImage(file=os.path.join(di,"ico.png"))
root.iconphoto(False,ph)


def equal():
    a=e.get()
    e.delete(0,END)
    try:
        e.insert(0,eval(a))
    except SyntaxError as s:
        e.insert(0,"Invalid")

def enter(s):
    a=e.get()
    e.delete(0,END)
    e.insert(0,a+s)

def clear():
    e.delete(0,END)




e=Entry(root,borderwidth=5,fg="#232232",bg="#fdfae5",width=20,font=('Ubuntu',22))

b1=Button(root,text="1",padx=30,pady=25,fg="#232232",bg="#f5ea92",font=('Ubuntu',14,"bold"),command=lambda:enter("1"))
b2=Button(root,text="2",padx=30,pady=25,fg="#232232",bg="#f5ea92",font=('Ubuntu',14,"bold"),command=lambda:enter("2"))
b3=Button(root,text="3",padx=30,pady=25,fg="#232232",bg="#f5ea92",font=('Ubuntu',14,"bold"),command=lambda:enter("3"))
b4=Button(root,text="4",padx=30,pady=25,fg="#232232",bg="#f5ea92",font=('Ubuntu',14,"bold"),command=lambda:enter("4"))
b5=Button(root,text="5",padx=30,pady=25,fg="#232232",bg="#f5ea92",font=('Ubuntu',14,"bold"),command=lambda:enter("5"))
b6=Button(root,text="6",padx=30,pady=25,fg="#232232",bg="#f5ea92",font=('Ubuntu',14,"bold"),command=lambda:enter("6"))
b7=Button(root,text="7",padx=30,pady=25,fg="#232232",bg="#f5ea92",font=('Ubuntu',14,"bold"),command=lambda:enter("7"))
b8=Button(root,text="8",padx=30,pady=25,fg="#232232",bg="#f5ea92",font=('Ubuntu',14,"bold"),command=lambda:enter("8"))
b9=Button(root,text="9",padx=30,pady=25,fg="#232232",bg="#f5ea92",font=('Ubuntu',14,"bold"),command=lambda:enter("9"))
b0=Button(root,text="0",padx=30,pady=25,fg="#232232",bg="#f5ea92",font=('Ubuntu',14,"bold"),command=lambda:enter("0"))


e.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

b1.grid(row=1,column=0,padx=5,pady=5)
b2.grid(row=1,column=1,padx=5,pady=5)
b3.grid(row=1,column=2,padx=5,pady=5)
b4.grid(row=2,column=0,padx=5,pady=5)
b5.grid(row=2,column=1,padx=5,pady=5)
b6.grid(row=2,column=2,padx=5,pady=5)
b7.grid(row=3,column=0,padx=5,pady=5)
b8.grid(row=3,column=1,padx=5,pady=5)
b9.grid(row=3,column=2,padx=5,pady=5)
b0.grid(row=4,column=1,padx=5,pady=5)

be=Button(root,text="=",padx=30,pady=25,fg="#232232",bg="#f5ea92",font=('Ubuntu',14,"bold"),command=equal)
ba=Button(root,text="+",padx=30,pady=25,fg="#232232",bg="#f5ea92",font=('Ubuntu',14,"bold"),command=lambda:enter("+"))
bs=Button(root,text="-",padx=30,pady=25,fg="#232232",bg="#f5ea92",font=('Ubuntu',14,"bold"),command=lambda:enter("-"))
bd=Button(root,text="/",padx=30,pady=25,fg="#232232",bg="#f5ea92",font=('Ubuntu',14,"bold"),command=lambda:enter("/"))
bm=Button(root,text="*",padx=30,pady=25,fg="#232232",bg="#f5ea92",font=('Ubuntu',14,"bold"),command=lambda:enter("*"))
bclear=Button(root,text="CLR",padx=25,pady=27,fg="#232232",bg="#f5ea92",font=('Ubuntu',12,"bold"),command=clear)

be.grid(row=4,column=2,padx=5,pady=5)
ba.grid(row=4,column=3,padx=5,pady=5)
bs.grid(row=3,column=3,padx=5,pady=5)
bd.grid(row=1,column=3,padx=5,pady=5)
bm.grid(row=2,column=3,padx=5,pady=5)
bclear.grid(row=4,column=0,padx=5,pady=5)

root.mainloop()
