from tkinter import *
import json
from tkinter import messagebox
from PIL import ImageTk, Image
root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

def signin():
    username=user.get()
    password=code.get()
    file_path = 'data.json'
    with open(file_path, 'r') as file:
        loaded_dict = json.load(file)
    if username=='admin' and password=='1234':
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200') 
        screen.config(bg="white") 
        Label(screen, text='Hello Everyone!',bg='#fff',font=('Calibri (Body)', 50, 'bold')).pack(expand=True)
        screen.mainloop()




def signup():
    root=Tk()
    root.title('Sign up')
    root.geometry('925x500+300+200')
    root.configure(bg="#fff")
    root.resizable(False, False)
    frame = Frame(root, width=350,height=400,bg="White") 
    frame.place(x=290,y=70)
    heading = Label(frame, text='Sign Up', fg='#57a1f8',bg='white', font=('Microsoft YaHei UI Light', 23, 'bold')) 
    heading.place(x=100,y=5)

    def save_info():
        user_info = user1.get()
        password_info = password.get()

        userlist = {}
        userlist.update({user_info:password_info})
        print(userlist)

        file_path = 'data.json'
        with open(file_path, 'w') as file:
            json.dump(userlist, file)
           



    def on_enter(e):
        user1.delete(0, 'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0, "Enter Username")
    user1 = Entry(frame, width=25,fg='black', border=0,bg="white", font=('Microsoft YaHei UI Light',11))
    user1.place(x=30,y=80)
    user1.insert(0, 'Enter Username')
    user1.bind('<FocusIn>', on_enter)
    user1.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2,bg='black').place(x=25,y=107)
    def on_enter(e):
        email.delete(0, 'end')
    def on_leave(e):
        name=email.get()
        if name=='':
            email.insert(0, "Email ID")
    email = Entry(frame, width=25,fg='black', border=0,bg="white", font=('Microsoft YaHel UI Light',11))
    email.place(x=30,y=150) 
    email.insert(0, "Email ID")
    email.bind('<FocusIn>', on_enter)
    email.bind('<FocusOut>', on_leave)
    Frame(frame,width=295, height=2,bg='black').place(x=25,y=177)
    def on_enter(e):
        number.delete(0, 'end')
    def on_leave(e):
        name=number.get()
        if name=='':
            number.insert(0, "Phone Number")
    number = Entry(frame, width=25,fg='black', border=0,bg="white", font=('Microsoft YaHel UI Light',11))
    number.place(x=30,y=220) 
    number.insert(0, "Phone Number")
    number.bind('<FocusIn>', on_enter)
    number.bind('<FocusOut>', on_leave)
    Frame(frame,width=295, height=2,bg='black').place(x=25,y=247)
    def on_enter(e):
        password.delete(0, 'end')
    def on_leave(e):
        name=password.get()
        if name=='':
            number.insert(0, "Create Password")
    password = Entry(frame, width=25,fg='black', border=0,bg="white", font=('Microsoft YaHel UI Light',11))
    password.place(x=30,y=290) 
    password.insert(0, "Create Password")
    password.bind('<FocusIn>', on_enter)
    password.bind('<FocusOut>', on_leave)
    Frame(frame,width=295, height=2,bg='black').place(x=25,y=317)

    Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg="white", border=0,command=save_info).place(x=35,y=350)
    


img = Image.open("D:\\sumedh\\Internship\\login authentication\\attachment.png")
resized = img.resize((350,300), Image.ADAPTIVE)
img = ImageTk.PhotoImage(resized)
my_lable = Label(root,image=img,bg='white').place(x=50,y=100)

frame = Frame(root, width=350,height=350,bg="White") 
frame.place(x=480,y=70)
heading = Label(frame, text='Sign in', fg='#57a1f8',bg='white', font=('Microsoft YaHei UI Light', 23, 'bold')) 
heading.place(x=100,y=5)


def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, "Username")

user = Entry(frame, width=25,fg='black', border=0,bg="white", font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2,bg='black').place(x=25,y=107)


def on_enter(e):
    code.delete(0, 'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0, "Password")

code = Entry(frame, width=25,fg='black', border=0,bg="white", font=('Microsoft YaHel UI Light',11))
code.place(x=30,y=150) 
code.insert(0, "Password")
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame,width=295, height=2,bg='black').place(x=25,y=177)


Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg="white", border=0,command=signin).place(x=35,y=204)
label = Label(frame, text="Don't have an account?",fg='black', bg='white', font=('Microsoft YaHei UI Light',9)) 
label.place(x=75,y=270)
sign_up = Button(frame, width=6,text='Sign up', border=0,bg='white', cursor='hand2',fg='#57a1f8',command=signup) 
sign_up.place(x=215,y=270)




root.mainloop()