# ANS 1- In Python, a closure is a function object that remembers values in its enclosing scope even if they are no longer present in memory. 
# It is a combination of a function and the environment in which it was defined.
# To create a closure in Python, you typically define a nested function within another function and have the inner function access variables from the outer function.
# def output_decorator(operation):
#     def decorator(func):
#         def wrapper(x, y):
#             result = func(x, y)
#             print(f"Two number {operation} is {result}")
#         return wrapper
#     return decorator
# @output_decorator("addition")
# def addition(x, y):
#     return x + y
# @output_decorator("subtraction")
# def subtraction(x, y):
#     return x - y
# @output_decorator("multiplication")
# def multiplication(x, y):
#     return x * y
# addition(8, 3)
# subtraction(9, 4)
# multiplication(4, 6)

# ANS 2(A)-

# matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# print(transposed_matrix)

# # ANS 2(B)
# days = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
# temp_c = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]

# my_dict = {days: temp_c for days, temp_c in zip(days, temp_c)}

# print(my_dict)

# # ANS 3
# from tkinter import*
# import openpyxl
# from openpyxl import workbook
# root=Tk()
# root.geometry("900x900+50+150")
# root.resizable(0,0)
# root.title("registration form")
# root.config(bg="grey")
# lbl=Label(root,text="ADMISSION ENQUIRY FORM",font=("Ariel",20,'bold'),fg='white',bg="royalblue")
# lbl.place(x='250',y='5')
# lbl1=Label(root,text="NAME",font=("Ariel",20,'bold'),fg='white',bg="royalblue")
# lbl1.place(x='20',y='80')
# lbl2=Label(root,text="FATHER'S NAME",font=("Ariel",20,'bold'),fg='white',bg="royalblue")
# lbl2.place(x='20',y='140')
# # lbl3=Label(root,text="ERP ID",font=("Ariel",20,'bold'),fg='white',bg="royalblue")
# # lbl3.place(x='50',y='200')
# a=StringVar()
# ent1=Entry(root,font=('Ariel',20),fg='black',bg='white',textvariable=a)
# ent1.place(x=250,y=80,width=140)
# b=StringVar()
# ent2=Entry(root,font=('Ariel',20),fg='black',bg='white',textvariable=b)
# ent2.place(x=250,y=140,width=140)
# c=StringVar()
# ent3=Entry(root,font=('Ariel',20),fg='black',bg='white',textvariable=c)
# ent3.place(x=250,y=200,width=140)
# lbl6=Label(root,text="your gender",font=("Ariel",20,'bold'),fg='white',bg="royalblue")
# lbl6.place(x="400",y="80")
# def show():
#     if x.get()==1:
#         m="male"
#         lbl4=Label(root,text="My option is:"+m)
#         lbl4.place(x=400,y=200)
#     if x.get()==2:
        
#         f="female"
#         lbl5=Label(root,text="My option is:"+f)
#         lbl5.place(x=400,y=200)
    
    
# x=IntVar()
# rad1=Radiobutton(root,text="Male",value=1,command=show,variable=x)
# rad1.place(x=400,y=120)
# rad2=Radiobutton(root,text="Female",value=2,command=show,variable=x)
# rad2.place(x=400,y=160)
# lbl7=Label(root,text="your identity proof",font=("Ariel",20,'bold'),fg='white',bg="royalblue")
# lbl7.place(x='600',y='80')
# def show1():
#     st=" "
#     if p.get()==1:
#         print(x.get())
#         st+="DO YOU HAVE AADHAR CARD"
#     if q.get()==1:
#         st+="DO YOU HAVE PAN CARD"
#     if r.get()==1:
#         st+="DO YOU HAVE DRIVING LICENSE"

#     d.set(st)
# p=IntVar()
# q=IntVar()
# r=IntVar()
# d=StringVar()
# p.set(0)
# q.set(0)
# r.set(0)
# ent5=Entry(root,textvariable=d)
# ent5.place(x=600,y=120)
# chk=Checkbutton(root,text="DO YOU HAVE AADHAR CARD",variable=p)
# chk.place(x=600,y=160)
# chk1=Checkbutton(root,text="DO YOU HAVE PAN CARD",variable=q)
# chk1.place(x=600,y=200)
# chk2=Checkbutton(root,text="DO YOU HAVE DRIVING LICENSE",variable=r)
# chk2.place(x=600,y=240)
# but=Button(root,text="click",command=show1)
# but.place(x=650,y=300)
# def login():
#     s=a.get()
#     t=b.get()
#     u=c.get()
#     g=d.get()

#     lst1=[s,t,u,g]
#     sheet.append(lst1)
#     wb.save("C:\\Users\\agnih\\OneDrive\\student.xlsx")
# b1=Button(root,font=("ariel",20),bg="grey",fg="white",text="Login",activeforeground="red",activebackground="green",command=login)
# b1.place(x=400,y=400,width=100,height=50)
# wb=openpyxl.load_workbook("C:\\Users\\agnih\\OneDrive\\student.xlsx")
# sheet=wb.active
# root.mainloop()


# # ANS 4(A)-



# from tkinter import*
# from tkinter import ttk
# root=Tk()
# root.geometry("400x400")
# root.resizable(0,0)
# root.title("menu box")
# root.config(bg="black")
# dmenu=Menu(root)
# sub1=Menu(dmenu,tearoff=0)
# sub2=Menu(dmenu,tearoff=0)
# sub3=Menu(dmenu,tearoff=0)
# sub1.add_command(label="Notebook")
# sub1.add_separator()
# sub1.add_command(label="open")
# sub1.add_command(label="save")
# dmenu.add_cascade(label="file",menu=sub1)
# sub2.add_command(label="undo")
# sub2.add_command(label="redo")
# sub2.add_command(label="copy")
# sub2.add_command(label="paste")
# dmenu.add_cascade(label="edit",menu=sub2)
# sub3.add_command(label="show")
# sub3.add_command(label="hide")
# dmenu.add_cascade(label="view",menu=sub3)
# root.config(menu=dmenu)

# root.mainloop()

# # ANS 4(B)-

# import tkinter as tk

# conversion_factors = {
#     "Meters": 1.0,
#     "Feet": 3.28084,
#     "Inches": 39.3701,
#     "Centimeters": 100.0,
#     "Yards": 1.09361,
# }

# def convert_length():
#     input_value = float(entry.get())
#     from_unit = from_var.get()
#     to_unit = to_var.get()

    
#     meters = input_value / conversion_factors[from_unit]

    
#     converted_value = meters * conversion_factors[to_unit]

#     result_label["text"] = f"{input_value} {from_unit} = {converted_value} {to_unit}"


# window = tk.Tk()
# window.title("Length Converter")
# window.geometry("400x400")


# entry = tk.Entry(window, width=10)
# entry.pack()


# from_var = tk.StringVar(window)
# from_var.set("Meters")  
# from_menu = tk.OptionMenu(window, from_var, *conversion_factors.keys())
# from_menu.pack()


# to_var = tk.StringVar(window)
# to_var.set("Feet")  
# to_menu = tk.OptionMenu(window, to_var, *conversion_factors.keys())
# to_menu.pack()


# convert_button = tk.Button(window, text="Convert", command=convert_length)
# convert_button.pack()


# result_label = tk.Label(window)
# result_label.pack()


# window.mainloop()

# # ANS 5-
# import pandas as pd

# data1 = {'Admission_No': [101, 102, 103, 104],
#          'Name': ['John', 'Alice', 'Bob', 'Emma'],
#          'Branch': ['CSE', 'IT', 'ECE', 'Mech']}
# df1 = pd.DataFrame(data1)

# data2 = {'Admission_No': [101, 102, 104, 105],
#          'Marks': [90, 95, 88, 92]}
# df2 = pd.DataFrame(data2)


# inner_merge = pd.merge(df1, df2, on='Admission_No', how='inner')
# print("Inner Merge:")
# print(inner_merge)


# outer_merge = pd.merge(df1, df2, on='Admission_No', how='outer')
# print("\nOuter Merge:")
# print(outer_merge)

# # ANS 6

import numpy as np
import pandas as py
arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
v_a=arr*3
print(v_a)