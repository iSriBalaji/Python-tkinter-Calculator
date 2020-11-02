from tkinter import *
import os

di=os.path.dirname(__file__)

root=Tk()
root.title("CalX")
root.configure(background="#ffffff")
#root.resizable(0,0)          #disables the maximize button

ph=PhotoImage(file=os.path.join(di,"ico.png"))
root.iconphoto(False,ph)


def equal():
    a=e.get()
    e.delete(0,END)
    try:
        e.insert(0,eval(a))
    except SyntaxError as s:
        e.insert(0,"Error")

def enter(s):
    a=e.get()
    e.delete(0,END)
    e.insert(0,a+s)

def clear():
    e.delete(0,END)




e=Entry(root,borderwidth=5,fg="#ffffff",bg="#000000",width=20,font=('Ubuntu',22))

b1=Button(root,text="1",fg="#ffffff",bg="#000000",font=('Ubuntu',14,"bold"),command=lambda:enter("1"),bd=0,padx=30,pady=25)
b2=Button(root,text="2",fg="#ffffff",bg="#000000",font=('Ubuntu',14,"bold"),command=lambda:enter("2"),bd=0,padx=30,pady=25)
b3=Button(root,text="3",fg="#ffffff",bg="#000000",font=('Ubuntu',14,"bold"),command=lambda:enter("3"),bd=0,padx=30,pady=25)
b4=Button(root,text="4",fg="#ffffff",bg="#000000",font=('Ubuntu',14,"bold"),command=lambda:enter("4"),bd=0,padx=30,pady=25)
b5=Button(root,text="5",fg="#ffffff",bg="#000000",font=('Ubuntu',14,"bold"),command=lambda:enter("5"),bd=0,padx=30,pady=25)
b6=Button(root,text="6",fg="#ffffff",bg="#000000",font=('Ubuntu',14,"bold"),command=lambda:enter("6"),bd=0,padx=30,pady=25)
b7=Button(root,text="7",fg="#ffffff",bg="#000000",font=('Ubuntu',14,"bold"),command=lambda:enter("7"),bd=0,padx=30,pady=25)
b8=Button(root,text="8",fg="#ffffff",bg="#000000",font=('Ubuntu',14,"bold"),command=lambda:enter("8"),bd=0,padx=30,pady=25)
b9=Button(root,text="9",fg="#ffffff",bg="#000000",font=('Ubuntu',14,"bold"),command=lambda:enter("9"),bd=0,padx=30,pady=25)
b0=Button(root,text="0",fg="#ffffff",bg="#000000",font=('Ubuntu',14,"bold"),command=lambda:enter("0"),bd=0,padx=30,pady=25)


e.grid(row=0,column=0,columnspan=4,sticky=W+E+N+S)

b1.grid(row=1,column=0,sticky=W+E+N+S)
b2.grid(row=1,column=1,sticky=W+E+N+S)
b3.grid(row=1,column=2,sticky=W+E+N+S)
b4.grid(row=2,column=0,sticky=W+E+N+S)
b5.grid(row=2,column=1,sticky=W+E+N+S)
b6.grid(row=2,column=2,sticky=W+E+N+S)
b7.grid(row=3,column=0,sticky=W+E+N+S)
b8.grid(row=3,column=1,sticky=W+E+N+S)
b9.grid(row=3,column=2,sticky=W+E+N+S)
b0.grid(row=4,column=1,sticky=W+E+N+S)

be=Button(root,text="=",fg="#ffffff",bg="#000000",font=('Ubuntu',14,"bold"),command=equal,bd=0,padx=30,pady=25)
ba=Button(root,text="+",fg="#ffffff",bg="#212121",font=('Ubuntu',14,"bold"),command=lambda:enter("+"),bd=0,padx=30,pady=25)
bs=Button(root,text="-",fg="#ffffff",bg="#212121",font=('Ubuntu',14,"bold"),command=lambda:enter("-"),bd=0,padx=30,pady=25)
bd=Button(root,text="/",fg="#ffffff",bg="#212121",font=('Ubuntu',14,"bold"),command=lambda:enter("/"),bd=0,padx=30,pady=25)
bm=Button(root,text="*",fg="#ffffff",bg="#212121",font=('Ubuntu',14,"bold"),command=lambda:enter("*"),bd=0,padx=30,pady=25)
bclear=Button(root,text="CLR",fg="#ffffff",bg="#c41212",font=('Ubuntu',12,"bold"),command=clear,bd=0,padx=25,pady=27)

be.grid(row=4,column=2,sticky=W+E+N+S)
ba.grid(row=4,column=3,sticky=W+E+N+S)
bs.grid(row=3,column=3,sticky=W+E+N+S)
bd.grid(row=1,column=3,sticky=W+E+N+S)
bm.grid(row=2,column=3,sticky=W+E+N+S)
bclear.grid(row=4,column=0,sticky=W+E+N+S)

root.mainloop()
