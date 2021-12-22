from tkinter import*

root= Tk()

a=Label(root,text="Username")
e1=Entry(root)
b=Label(root,text="First name")
e2=Entry(root)
c=Label(root,text="Last name")
e3=Entry(root)
d=Label(root,text="Password")
e4=Entry(root)
f=Label(root,text="Confirm Password")
e5=Entry(root)
g=Label(root,text="Email")
e6=Entry(root)
h=Button(root,text="Register")

a.grid(row =0,column=0)
e1.grid(row=0,column=1)
b.grid(row=1,column=0)
e2.grid(row=1,column=1)
c.grid(row=2,column=0)
e3.grid(row=2,column=1)
d.grid(row=3,column=0)
e4.grid(row=3,column=1)
f.grid(row=4,column=0)
e5.grid(row=4,column=1)
g.grid(row=5,column=0)
e6.grid(row=6,column=1)
h.grid(row=7,column=1)

root.mainloop()

  