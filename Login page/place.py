from tkinter import*

root=Tk()
root.geometry("400x400")
a=Label(root,text="Username").place(x=30,y=50)
e1=Entry(root).place(x=30,y=90)
b=Label(root,text="Password").place(x=30,y=130)
e2=Entry(root).place(x=30,y=180)
c=Button(root,text="LOGIN").place(x=100,y=210)
d=Label(root,text="Forget password?").place(x=100,y=260)
f=Label(root,text="Don't have an account,Sign up").place(x=100,y=280)


root.mainloop()
