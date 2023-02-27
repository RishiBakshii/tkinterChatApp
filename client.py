import socket
import threading
from tkinter import *


client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
nickname=input("choose your nickname")

ip_address="127.0.0.1"
port=8000
client.connect((ip_address,port))


class GUI:
    def __init__(self):
        self.window=Tk()
        self.window.withdraw()

        self.login=Toplevel()
        self.login.title("Login")

        self.login.resizable(width=False,height=False)
        self.login.configure(width=400,height=300)
        self.pls=Label(self.login,text="Please Login to continue")
        self.pls.place(relx=0.2,rely=0.1,relheight=0.2)

        self.labelname=Label(self.login,text="Name: ")
        self.labelname.place(relx=0.2,rely=0.4,relheight=0.2)
        self.entryname=Entry(self.login)
        self.entryname.place(relwidth=0.4,relheight=0.1,relx=0.4,rely=0.4)

        self.loginbtn=Button(self.login,text="Login",command=lambda: self.gotoMainScreen(self.entryname.get()))
        self.loginbtn.place(relx=0.4,rely=0.7)


        self.window.mainloop()

    def gotoMainScreen(self,name):
        self.login.destroy()
        self.name=name
        recv=threading.Thread(target=self.receive)
        recv.start()
    
    def receive(self):
        while True:
            try:
                msg=client.recv(2048).decode("utf-8")
                if msg=="NICKNAME":
                    client.send(nickname.encode("utf-8"))
                else:
                    pass
            except:
                print("an error occured!")
                client.close()
                break



root=GUI()
