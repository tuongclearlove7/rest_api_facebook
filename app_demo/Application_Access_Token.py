from time import sleep
import facebook as fb
from PIL import ImageTk,Image
from threading import *
from tkinter import *
import os
import tkinter as tk
                                                
readMode = ['r+','a+','a','x','r','+','b','U','w','t']
AppStart = [True,False]
file_key_global = open('C:\\Users\\clearlove7\\Documents\\GitHub\\App\\text data\\Application.txt',mode=readMode[0],encoding="utf-8")
data = file_key_global.read()

class MyApp:
    def Api_Acess_Token():
        App = Tk()
        App.geometry("470x170")
        App.title("Tool API Post Status Facebook")
        App.iconbitmap("C:\\Users\\clearlove7\\Documents\\GitHub\\App\\image\\logo.ico")
        App.configure(background="#099D9D")
        img = PhotoImage(file = "C:\\Users\\clearlove7\\Documents\\GitHub\\App\\image\\background.png")
        img1 = img.subsample(3,3)
        token_var=tk.StringVar()
        content_var=tk.StringVar()
        
        def Run_API(My_access_token,My_msg):
            try:
                api = fb.GraphAPI(My_access_token)
                api.put_object('me','feed',message = My_msg)
                succes = [Label(App,text="Successfully✅",bg="green",font=('calibre',10, 'bold'),width=15).place(x=135,y=120),"Successfully"]
                print(succes[1])
            except Exception as error:
                err = [Label(App,text="Error ❌",bg="red",font=('calibre',10, 'bold'),width=15).place(x=135,y=120),"Error"]
                print(f"Error ❌: {str(error)}")

        def Handle_token():
            global get_token,get_content
            get_token=token_var.get()
            get_content=content_var.get()
            Run_API(get_token,get_content)
            str_token_content = str("token : "+get_token+"\n"+"content : "+get_content+"\n")
            write_token = open("C:\\Users\\clearlove7\\Documents\\GitHub\\App\\text data\\token.txt",readMode[1],encoding="utf-8")
            H_data = write_token.write(str_token_content)
            write_token.close() 
            content_var.set('')

        def multiple_threading():
            multi=Thread(target=Handle_token)
            multi.start()

        def F_Token(msg_token):
            file_token = open('C:\\Users\\clearlove7\\Documents\\GitHub\\App\\text data\\token.txt',mode=readMode[0],encoding="utf-8")
            F_data = file_token.read()
            print(msg_token+F_data)
        
        Labeltoken = Label(App,text='nhập token',bg="#099D9D",font=('calibre',10, 'bold')).place(x=10,y=10)
        Labelcontent = Label(App,text='nhập nội dung',bg="#099D9D",font=('calibre',10, 'bold')).place(x=10,y=40)
        token = Entry(App,textvariable=token_var,width=30).place(x=110,y=10)
        content = Entry(App,textvariable=content_var,width=30).place(x=110,y=40)
        Button_started = Button(App,text="POST",font=('calibre',10, 'bold'), command=multiple_threading)
        Button_started.place(x=180,y=80)
        Label_dev= Label(App,text='© By Clearlove7',fg='white',bg="#099D9D").place(x=0,y=150)
        Label_dev= Label(App,text='. Access Token Application',bg="#099D9D",fg='white').place(x=87,y=150)
        image = Label(App, image = img1).place(x=300,y=0)
        Button_exit = Button(App,text="exit",font=('calibre',10, 'bold'), command=exit)
        #Button_exit.place(x=10,y=80)

        App.mainloop()

while AppStart[0]:
       password = input("nhap pass : ")
       if password ==  data:
            MyApp.Api_Acess_Token()
            break;
       elif password !=  data:
            print("You were inputing wrong fields, please! re-enter")




















