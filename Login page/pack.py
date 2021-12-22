from tkinter import*

pro= Tk()

a=Label(pro,text="Username").pack()
e1=Entry().pack()
b=Label(pro,text="Password").pack()
e2=Entry().pack()
c=Button(pro,text="LOGIN").pack()
d=Label(pro,text="Forget password?").pack()
f=Label(pro,text="Don't have an account,Sign up").pack()


pro.mainloop()