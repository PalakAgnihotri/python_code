from tkinter import*
# import openpyxl
# from openpyxl import workbook
root=Tk()
root.geometry("900x900+50+150")
root.resizable(0,0)
root.title("registration form")
root.config(bg="grey")
lbl=Label(root,text="STUDENT",font=("Ariel",20,'bold'),fg='white',bg="royalblue")
lbl.place(x='400',y='5')
lbl1=Label(root,text="NAME",font=("Ariel",20,'bold'),fg='white',bg="royalblue")
lbl1.place(x='50',y='80')
lbl2=Label(root,text="ROLL NO.",font=("Ariel",20,'bold'),fg='white',bg="royalblue")
lbl2.place(x='50',y='140')
lbl3=Label(root,text="ERP ID",font=("Ariel",20,'bold'),fg='white',bg="royalblue")
lbl3.place(x='50',y='200')
a=StringVar()
ent1=Entry(root,font=('Ariel',20),fg='black',bg='white',textvariable=a)
ent1.place(x=250,y=80,width=140)
b=StringVar()
ent2=Entry(root,font=('Ariel',20),fg='black',bg='white',textvariable=b)
ent2.place(x=250,y=140,width=140)
c=StringVar()
ent3=Entry(root,font=('Ariel',20),fg='black',bg='white',textvariable=c)
ent3.place(x=250,y=200,width=140)
lbl6=Label(root,text="your gender",font=("Ariel",20,'bold'),fg='white',bg="royalblue")
lbl6.place(x="400",y="80")
def show():
    if x.get()==1:
        m="male"
        lbl4=Label(root,text="My option is:"+m)
        lbl4.place(x=400,y=200)
    if x.get()==2:
        
        f="female"
        lbl5=Label(root,text="My option is:"+f)
        lbl5.place(x=400,y=200)
    
    
x=IntVar()
rad1=Radiobutton(root,text="Male",value=1,command=show,variable=x)
rad1.place(x=400,y=120)
rad2=Radiobutton(root,text="Female",value=2,command=show,variable=x)
rad2.place(x=400,y=160)
lbl7=Label(root,text="Select your Language",font=("Ariel",20,'bold'),fg='white',bg="royalblue")
lbl7.place(x='600',y='80')
def show1():
    st=" "
    if p.get()==1:
        # print(x.get())
        st+="GERMAN"
    if q.get()==1:
        st+="FRENCH"
    if r.get()==1:
        st+="JAPANEESE"

    d.set(st)
p=IntVar()
q=IntVar()
r=IntVar()
d=StringVar()
p.set(0)
q.set(0)
r.set(0)
ent5=Entry(root,textvariable=d)
ent5.place(x=600,y=120)
chk=Checkbutton(root,text="GERMAN",variable=p)
chk.place(x=600,y=160)
chk1=Checkbutton(root,text="FRENCH",variable=q)
chk1.place(x=680,y=160)
chk2=Checkbutton(root,text="JAPANEESE",variable=r)
chk2.place(x=758,y=160)
but=Button(root,text="click",command=show1)
but.place(x=700,y=200)
def login():
    s=a.get()
    t=b.get()
    u=c.get()
    g=d.get()

    # lst1=[s,t,u,g]
    # sheet.append(lst1)
    # wb.save("C:\\Users\\agnih\\OneDrive\\student.xlsx")
b1=Button(root,font=("ariel",20),bg="grey",fg="white",text="Login",activeforeground="red",activebackground="green",command=login)
b1.place(x=280,y=400,width=100,height=50)
# wb=openpyxl.load_workbook("C:\\Users\\agnih\\OneDrive\\student.xlsx")
# sheet=wb.active
root.mainloop()