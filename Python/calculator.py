from tkinter import*
root=Tk()
root.geometry("420x280")
root.resizable(0,0)
root.title("My Calculator")
root.config(bg="skyblue")
a=StringVar()
e1=Entry(root,font=('Ariel',25),justify="right",textvariable=a)
e1.place(x=0,y=0,width=425,height=50)
def show(op):
    a.set(a.get()+op)

def eql():
    exp=a.get()
    a.set(eval(exp))
def clear():
    a.set(" ")
b1=Button(root,font=("ariel",25),bg="grey",fg="white",text="1",activeforeground="red",activebackground="green",command=show)
b1.place(x=5,y=55,width=100,height=50)
b1.config(command=lambda:show("1"))
b2=Button(root,font=("ariel",25),bg="grey",fg="white",text="2",activeforeground="red",activebackground="green",command=show)
b2.place(x=110,y=55,width=100,height=50)
b2.config(command=lambda:show("2"))
b3=Button(root,font=("ariel",25),bg="grey",fg="white",text="3",activeforeground="red",activebackground="green",command=show)
b3.place(x=215,y=55,width=100,height=50)
b3.config(command=lambda:show("3"))
b4=Button(root,font=("ariel",25),bg="grey",fg="white",text="+",activeforeground="red",activebackground="green",command=show)
b4.place(x=320,y=55,width=100,height=50)
b4.config(command=lambda:show("+"))
b5=Button(root,font=("ariel",25),bg="grey",fg="white",text="4",activeforeground="red",activebackground="green",command=show)
b5.place(x=5,y=110,width=100,height=50)
b5.config(command=lambda:show("4"))
b6=Button(root,font=("ariel",25),bg="grey",fg="white",text="5",activeforeground="red",activebackground="green",command=show)
b6.place(x=110,y=110,width=100,height=50)
b6.config(command=lambda:show("5"))
b7=Button(root,font=("ariel",25),bg="grey",fg="white",text="6",activeforeground="red",activebackground="green",command=show)
b7.place(x=215,y=110,width=100,height=50)
b7.config(command=lambda:show("6"))
b8=Button(root,font=("ariel",25),bg="grey",fg="white",text="-",activeforeground="red",activebackground="green",command=show)
b8.place(x=320,y=110,width=100,height=50)
b8.config(command=lambda:show("-"))
b9=Button(root,font=("ariel",25),bg="grey",fg="white",text="7",activeforeground="red",activebackground="green",command=show)
b9.place(x=5,y=165,width=100,height=50)
b9.config(command=lambda:show("7"))
b10=Button(root,font=("ariel",25),bg="grey",fg="white",text="8",activeforeground="red",activebackground="green",command=show)
b10.place(x=110,y=165,width=100,height=50)
b10.config(command=lambda:show("8"))
b11=Button(root,font=("ariel",25),bg="grey",fg="white",text="9",activeforeground="red",activebackground="green",command=show)
b11.place(x=215,y=165,width=100,height=50)
b11.config(command=lambda:show("9"))
b12=Button(root,font=("ariel",25),bg="grey",fg="white",text="*",activeforeground="red",activebackground="green",command=show)
b12.place(x=320,y=165,width=100,height=50)
b12.config(command=lambda:show("*"))
b13=Button(root,font=("ariel",25),bg="grey",fg="white",text="c",activeforeground="red",activebackground="green",command=clear)
b13.place(x=5,y=220,width=100,height=50)
b13.config(command=clear)
b14=Button(root,font=("ariel",25),bg="grey",fg="white",text="0",activeforeground="red",activebackground="green",command=clear)
b14.place(x=110,y=220,width=100,height=50)
b14.config(command=lambda:show('0'))
b15=Button(root,font=("ariel",25),bg="grey",fg="white",text="=",activeforeground="red",activebackground="green",command=eql)
b15.place(x=215,y=220,width=100,height=50)
b15.config(command=eql)
b16=Button(root,font=("ariel",25),bg="grey",fg="white",text="/",activeforeground="red",activebackground="green",command=show)
b16.place(x=320,y=220,width=100,height=50)
b16.config(command=lambda:show("/"))

root.mainloop()
