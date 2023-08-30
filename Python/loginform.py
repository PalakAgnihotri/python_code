from tkinter import*
# import openpyxl
# from openpyxl import workbook
root=Tk()
root.geometry("700x700")
root.resizable(0,0)
root.title("Login Form")
root.config(bg="white")
# def show():
#     x=a.get()
a=StringVar()
b=StringVar()
lbl=Label(root,text="LOGIN FORM",font=("Ariel",20,'bold'),fg='white',bg="black")
lbl.place(x=260,y=4)
lbl=Label(root,text="USER NAME",font=("Ariel",20,'bold'),fg='black',bg="white")
lbl.place(x=45,y=150)
lbl=Label(root,text="PASSWORD",font=("Ariel",20,'bold'),fg='black',bg="white")
lbl.place(x=45,y=300)
a=StringVar()
e1=Entry(root,font=('calibri',20),fg='black',bg='white',textvariable=a)
e1.place(x=500,y=150,width=160,height=45)
b=StringVar()
e2=Entry(root,font=('calibri',20),fg='black',bg='white',textvariable=b,show="*")
e2.place(x=500,y=300,width=160,height=45)
def login():
    x=a.get()
    y=b.get()
    lst1=[x,y]
    # sheet.append(lst1)
    
    # wb.save("C:\\Users\\agnih\\OneDrive\\first.xlsx")
b1=Button(root,font=("ariel",20),bg="grey",fg="white",text="Login",activeforeground="red",activebackground="green",command=login)
b1.place(x=280,y=400,width=100,height=50)
# wb=openpyxl.load_workbook("C:\\Users\\agnih\\OneDrive\\first.xlsx")
# sheet=wb.active
# lst=["ran",456]
# sheet.append(lst) 
root.mainloop()