from tkinter import*

root=Tk()

root.geometry("600x400")
a=Label(root,text="Username").place(x=30,y=50)
e1=Entry(root).place(x=100,y=50)
b=Label(root,text="First name").place(x=30,y=90)
e2=Entry(root).place(x=100,y=90)
c=Label(root,text="Last name").place(x=30,y=130)
e3=Entry(root).place(x=100,y=130)
d=Label(root,text="Password").place(x=30,y=170)
e4=Entry(root).place(x=100,y=170)
f=Label(root,text="Confirm password").place(x=30,y=210)
e5=Entry(root).place(x=100,y=210)
g=Label(root,text="Email").place(x=30,y=250)
e6=Entry(root).place(x=100,y=250)
h=Button(root,text="Register").place(x=50,y=290)


root.mainloop()



