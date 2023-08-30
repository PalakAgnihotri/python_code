# from tkinter import*
# root=Tk()
# root.geometry("400x400")
# root.resizable()
# root.config(bg="green")
# root.title("my calci")
# def close_window():
#     root.destroy()
# root.after(10000, close_window)
# def show(op):
#     a.set(a.get()+op)
# def eql(exp):
#     a.set(eval(exp))
# def clear():
#     a.set(" ")

# e1=Entry(root,font=("ariel",23),justify="right",textvariable=a)
# e1.place(x=0,y=0,height=250,width=50)
# b1=Button(root,font=("ariel",23),bg='blue',fg='pink',text='1',command=show)
# b1.config(command=lambda:show("1"))
# b1.place(x=5,y=55,height=55,width=100)

# def see():
#     if a.get()==1:
#         m="male"
#         lbl=Label(root,text="my option is:"+m)
#         lbl.pack()
#     if a.get()==2:
#         f="female"
#         lbl2=Label(root,text="my option is:"+f)
#         lbl2.pack()

# a=IntVar()
# rad1=Radiobutton(root,text='male',value=1,command=see,variable=a)
# rad1.pack()
# rad2=Radiobutton(root,text='female',value=2,command=see,variable=a)
# rad2.pack()

# def show():
#     c=''
#     if x.get()==1:
#         c+="java"
#     if y.get()==1:
#         c+="c"
#     if z.get()==1:
#         c+="c++"
#     d.set(c)
# x=IntVar()
# y=IntVar()
# z=IntVar()
# d=StringVar()
# e=Entry(root,textvariable=d)
# e.pack()
# chk1=Checkbutton(root,text='java',variable=x)
# chk1.pack()
# chk2=Checkbutton(root,text='c',variable=y)
# chk2.pack()
# chk3=Checkbutton(root,text='c++',variable=z)
# chk3.pack()
# but=Button(root,text="click",command=show)
# but.pack()
# dmenu=Menu(root)
# sub1=Menu(dmenu,tearoff=0)
# sub2=Menu(dmenu,tearoff=0)
# sub3=Menu(dmenu,tearoff=0)
# dmenu.add_cascade(label='files',menu=sub1)
# sub1.add_command(label='hii')
# sub1.add_separator()
# sub1.add_command(label='j')
# dmenu.add_cascade(label='edit',menu=sub2)
# sub2.add_command(label='g')
# sub2.add_separator()
# sub2.add_command(label='k')
# dmenu.add_cascade(label='run',menu=sub3)
# sub3.add_command(label='k')
# sub3.add_separator()
# sub3.add_command(label='j')
# root.config(menu=dmenu)
# can=Canvas(root,width=300,height=200,bg='yellow')
# can.pack()
# can.create_rectangle(50,70,90,50,fill='red')
# root.mainloop()

import numpy as np
a=np.arange(12).reshape(3,4)
print(a[0:2,1::2])