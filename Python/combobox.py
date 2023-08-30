from tkinter import*
from tkinter import ttk
root=Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("combo box")
root.config(bg="white")
lst=["sun","mon","tue","wed","thu","fri","sat"]
comb=ttk.Combobox(root,value=lst)
comb.set("please enter day")
comb.pack()
root.mainloop()