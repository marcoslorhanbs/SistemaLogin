#Importar as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

#Criar Nossa Janela
jan = Tk()
jan.title("DP Systems - Acess Panel")
jan.geometry("600x330")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="icons/LogoIcon.ico")

#====== Carregando Imagens
logo = PhotoImage(file="icons/logo.png")

#===== Widgets ==================
LeftFrame = Frame(jan, width=200, height=400, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=400, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show="•")
PassEntry.place(x=150, y=160)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users 
    WHERE (User = ? and Password = ?)
    """, (User, Pass))
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado. Bem Vindo!")
    except:
        messagebox.showinfo(title="Login Info", message="Acesso Negado. Verifique se esta cadastro no sistema!")

#Botoes
LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=100, y=225)

def Register():
    #Removendo Widgets de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #Inserindo Widgets de Cadastro
    NomeLabel = Label(RightFrame, text="Name:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=39)
    NomeEntry.place(x=100, y=16)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=39)
    EmailEntry.place(x=100, y=66)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (Name == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="Register Error", message="Nao Deixe Nenhum Campo Vazio. Preencha Todos os Campos")
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Conta Criada Com Sucesso")

    Register = ttk.Button(RightFrame, text="Register", width=30, command=RegisterToDataBase)
    Register.place(x=100, y=225)

    def BackToLogin():
        #Removendo Widgets de Cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        #Trazendo de volta os Widgets de Login
        LoginButton.place(x=100)
        RegisterButton.place(x=125)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=125, y=260)



RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=125, y=260)

EsqueceuSenhaLabel = Label(RightFrame, text="Esqueceu a senha?", bg="MIDNIGHTBLUE", fg="white", bd=0, font=("Verdana", 12))
EsqueceuSenhaLabel.place(x=50, y=305)

def RecuperaSenha():
    #Removendo os widgets de senha
    PassLabel.place(x=5000)
    PassEntry.place(x=5000)
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    EsqueceuSenhaLabel.place(x=5000)
    EsqueceuSenhaButton.place(x=5000)
    #Adicionando o widget de email
    EmailRecuperationLabel.place(x=5)
    EmailRecuperationButton.place(x=150)
    RecuperaSenhaTitulo.place(x=5)
    RecuperaSenhaButton.place(x=100)
    BackLogin.place(x=125)
    

EsqueceuSenhaButton = Button(RightFrame, text="Recupere Aqui!", bg="MIDNIGHTBLUE", fg="LIGHTBLUE", bd=0, font=("Verdana", 12), command=RecuperaSenha)
EsqueceuSenhaButton.place(x=210, y=302)

EmailRecuperationLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
EmailRecuperationLabel.place(x=5000, y=150)

EmailRecuperationButton = ttk.Entry(RightFrame, width=30)
EmailRecuperationButton.place(x=5000, y=160)

RecuperaSenhaTitulo = Label(RightFrame, text="Recuperar Senha \n Preencha os campos abaixo!", font=("Century Gothic", 18), bg="MIDNIGHTBLUE", fg="White")
RecuperaSenhaTitulo.place(x=5000, y=5)

def GetSenha():
    NewUser = UserEntry.get()
    NewEmail = EmailRecuperationButton.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users 
    WHERE (User = ? and Email = ?)
    """, (NewUser, NewEmail))
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()
    DataBaser.cursor.execute("""
    SELECT Password FROM Users
    WHERE User = ? and Email = ?
    """, (NewUser, NewEmail))
    MostraSenha = DataBaser.cursor.fetchone()
    if (NewUser in VerifyLogin and NewEmail in VerifyLogin):
        messagebox.showinfo(title="Aviso", message=("Senha:", MostraSenha))
    else:
        messagebox.showinfo(title="Aviso", message="Dados Invalidos")


RecuperaSenhaButton = ttk.Button(RightFrame, text="Recuperar Senha", width=30, command=GetSenha)
RecuperaSenhaButton.place(x=5000, y=225)#x=100

def BackToLogin2():
    #Removendo Widgets de Cadastro
    EmailRecuperationLabel.place(x=5000)
    EmailRecuperationButton.place(x=5000)
    BackLogin.place(x=5000)
    RecuperaSenhaButton.place(x=5000)
    RecuperaSenhaTitulo.place(x=5000)
    #Trazendo de volta os Widgets de Login
    LoginButton.place(x=100)
    RegisterButton.place(x=125)
    PassLabel.place(x=5)
    PassEntry.place(x=150)
    EsqueceuSenhaLabel.place(x=50)
    EsqueceuSenhaButton.place(x=210)


BackLogin = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin2)
BackLogin.place(x=5000, y=260)#x=125

jan.mainloop()
