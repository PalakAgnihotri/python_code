from tkinter import*
root=Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("Radio button")
root.config(bg="white")
def show():
    if a.get()==1:
        m="male"
        #st=st+a.get()
        lbl=Label(root,text="My option is:"+m)
        lbl.pack()
    if a.get()==2:
        #st=st+a.get()
        f="female"
        lbl1=Label(root,text="My option is:"+f)
        lbl1.pack()
    # y=a.get()
    
a=IntVar()
rad1=Radiobutton(root,text="Male",value=1,command=show,variable=a)
rad1.pack()
rad2=Radiobutton(root,text="Female",value=2,command=show,variable=a)
rad2.pack()
root.mainloop()