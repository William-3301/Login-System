#Importing
from tkinter import *
from tkinter import messagebox
import DataBase

#Creating Window
window = Tk()
window.title('Acess Panel')
window.geometry("600x600")
window.configure(background = "white")
window.resizable(width = False, height = False)
window.attributes("-alpha",0.9)
window.iconbitmap(default = "original.ico")

#Widgets
LeftFrame = Frame(window, width = 250, height = 600, background = "#3F7A63")
LeftFrame.pack(side = LEFT)

RightFrame = Frame(window, width = 325, height = 600, background = "#F29089")
RightFrame.pack(side = RIGHT)

#Images

logo = PhotoImage(file = "original.png")

#Labels

LogoLabel = Label(LeftFrame, image = logo, bg= "#3F7A63")
LogoLabel.place(x = 75, y = 250)

UserLabel = Label(RightFrame, text = "Username:", font = ("Century Gothic",20),bg = "#F29089", fg = "white")
UserLabel.place(x = 10, y = 200)

UserEntry = Entry(RightFrame, width = 25)
UserEntry.place(x = 160, y = 213)

PasswordLabel = Label(RightFrame, text = "Password:", font = ("Century Gothic",20),bg = "#F29089", fg = "white")
PasswordLabel.place(x = 10, y = 250)

PasswordEntry = Entry(RightFrame, width = 27)
PasswordEntry.place(x = 149, y = 263)


#Buttons

def Register():
    #Removing Login Widgets
    LoginButton.place(x = 1000)
    RegisterButton.place(x = 1000)
    
    #Adding Register Widgets
    NameLabel = Label(RightFrame, text = "Name:", font = ("Century Gothic",20), bg = "#F29089", fg = "white")
    NameLabel.place(x = 10, y = 100)
    NameEntry = Entry(RightFrame, width = 30)
    NameEntry.place(x =110, y= 113)
    
    EmailLabel = Label(RightFrame, text = "Email:", font = ("Century Gothic",20), bg = "#F29089", fg = "white")
    EmailLabel.place(x = 10, y = 150)
    EmailEntry = Entry(RightFrame, width = 30)
    EmailEntry.place(x =105, y= 163)

    def DataBaseConnection():
        Name = NameEntry.get()
        Email = EmailEntry.get()
        Username = UserEntry.get()
        Password = PasswordEntry.get()  
        
        if(Name == "" or Email == "" or Username == "" or Password == ""):
            messagebox.showerror(title = "Register Erro", message = "Complete All Columns" )
        
        else:
            DataBase.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?,?,?,?)
            """, (Name,Email,Username,Password))
            DataBase.conn.commit()
            messagebox.showinfo(title= "Register Info" ,message = "Register Successful")

    Register = Button(RightFrame,text= "Register", width = 30,command = DataBaseConnection)
    Register.place(x = 66, y = 310)

    def Back():
        
        #Removing Widgets
        NameLabel.place(x = 1000)
        NameEntry.place(x = 1000)
        EmailLabel.place(x = 1000)
        EmailEntry.place (x = 1000)
        Register.place(x = 1000)
        BackButton.place(x = 1000)
        
        #Adding Widgets
        
        LoginButton.place(x = 65, y = 310)
        
        RegisterButton.place(x = 96, y = 350)
        
    BackButton = Button(RightFrame,text= "Back", width = 20, command = Back)
    BackButton.place(x = 96, y = 350)



def Login():
    Username = UserEntry.get()
    Password = PasswordEntry.get()    
    DataBase.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ?) 
    """, (Username,Password))
    
    VerifyLogin = DataBase.cursor.fetchone()
    try:
        if (Username in VerifyLogin and Password in VerifyLogin):
            messagebox.showinfo(title= "Login Info", message="Acess Confirmed")
    except:
        messagebox.showerror(title= "Login Error", message="Acess Denied")


LoginButton = Button(RightFrame,text= "Login", width = 30,command = Login)
LoginButton.place(x = 65, y = 310)

RegisterButton = Button(RightFrame,text= "Register", width = 20, command=Register)
RegisterButton.place(x = 96, y = 350)


window.mainloop() 



