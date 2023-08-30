from tkinter import*
root=Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("check button")
root.config(bg="white")
def show1():
    st=" "
    if x.get()==1:
        print(x.get())
        st+="JAVA"
    if y.get()==1:
        st+="PYTHON"
    if z.get()==1:
        st+="C++"

    c.set(st)
x=IntVar()
y=IntVar()
z=IntVar()
c=StringVar()
# x.set(0)
# y.set(0)
# z.set(0)
ent=Entry(root,textvariable=c)
ent.pack()
chk=Checkbutton(root,text="JAVA",variable=x)
chk.pack()
chk1=Checkbutton(root,text="PYTHON",variable=y)
chk1.pack()
chk2=Checkbutton(root,text="C++",variable=z)
chk2.pack()
but=Button(root,text="click",command=show1)
but.pack()
root.mainloop()