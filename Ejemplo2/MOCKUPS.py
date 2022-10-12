# MOCKUPS

import tkinter as tk
from tkinter import *
from tkinter import ttk
from cProfile import label
from distutils.command.config import config
from email.mime import image
import imp
from tkinter import*
from tkinter.font import BOLD
from turtle import heading
from Registro import *
#import pagregister


w = 1320
h = 680






class Inicio():
    def __init__(controller):

        #Raiz
        ventana2=Tk()
        ventana2.title("Scrum")
        ventana2.resizable(False, False)
        #ventana2.geometry("900x500")
        #ventana.iconbitmap("Scrum.ico")


        # ----------- CENTER FORM ------------- #
        ws = ventana2.winfo_screenwidth()
        hs = ventana2.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        ventana2.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- HEADER ------------- #
        
        headerframe = tk.Frame(ventana2, highlightbackgroun='yellow', highlightcolor='yellow', highlightthickness=2, bg='#f2cb00', width=w+60, height=70)
        titleframe = tk.Frame(headerframe, bg='#f2cb00', padx=1, pady=1)
        title_label = tk.Label(titleframe, text='VJ Scrum', padx=15, pady=5, bg='#f2cb00', fg='black', font=('Italiana',24), width=8)
        

        headerframe.pack()
        titleframe.pack()
        title_label.pack()
        
        titleframe.place(y=32, relx=0.5, anchor=CENTER)

         # ----------- END HEADER ------------- #

         # ----------- MENU ------------- #

        freim = tk.Frame(ventana2)
        menubar = Menu(freim)
        products = Menu(menubar)
        products.add_command(label="Inicio")
        products.add_command(label="Avances")
        products.add_command(label="Tareas")

        menubar.add_cascade(menu=products, label="Paginas")

        categories = Menu(menubar)
        categories.add_command(label="Añadir")
        categories.add_command(label="Editar")
        categories.add_command(label="Remover")

        menubar.add_cascade(menu=categories, label="Category")

        freim.pack()

        # ----------------- CAJA LATERAL ---------------- #


        cajalateral = tk.Frame(ventana2, highlightbackgroun='yellow', highlightcolor='yellow', highlightthickness=2, bg='#F2CB00', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Scrum Board', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1) #command = mainform1)

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='In Progress', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)

        titulo3 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo3_label = tk.Button(titulo3, text='To Do', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)
        
        titulo4 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo4_label = tk.Button(titulo4, text='Done', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)



        cajalateral.pack(side = LEFT)
        cajalateral.config(cursor='heart')
        titulo1.pack()
        titulo1_label.pack()
        titulo1.place(y=30, relx=0.2)

        titulo2.pack()
        titulo2_label.pack()
        titulo2.place(y=190, x=65)

        titulo3.pack()
        titulo3_label.pack()
        titulo3.place(y=340, x=92)

        titulo4.pack()
        titulo4_label.pack()
        titulo4.place(y=500, x=92)

        

        # -----------------------FIN DE LA BARRA LATERAL ----------------------- #

        

        ventana2.config(menu=menubar, bg="#D9D9D9")

        lbl = tk.Label(ventana2, text='Bienvenido a la pagina de Scrum', font=('verdana',17, 'italic', 'bold'), fg='#2A2C2B',bg="#D9D9D9")
        lbl.place(y=90, x=1050, anchor=CENTER)

        #def destroy_1():
         #   ventana2.destroy()
          #  paginaregistro ()        

        def destroy_1():
            Pagregistro = tk.Toplevel()
            app = paginaregistro1(Pagregistro)
            ventana2.withdraw()
            Pagregistro.protocol("WM_DELETE_WINDOW", ventana2.destroy) 

        img_Proye1 = tk.PhotoImage(file="Proyecto1.png")
        boton = ttk.Button(ventana2, image=img_Proye1)
        boton.place(x=475, y=240)
        boton.image = img_Proye1
        lbl_Proy1 = tk.Label(ventana2, text = "Proyecto 1", font = ("Times New Roman", 13), bg = "#D9D9D9").place(x = 545, y = 455)

        img_Proye2 = tk.PhotoImage(file="Proyecto2.png")
        boton2 = ttk.Button(ventana2, image=img_Proye2, command= destroy_1  )
        boton2.place(x=940, y=240)
        boton2.image = img_Proye2
        lbl_Proy2 = tk.Label(ventana2, text = "Proyecto 2", font = ("Times New Roman", 13), bg = "#D9D9D9").place(x = 1010, y = 455)
        
        
        img_boton = tk.PhotoImage(file="log_out.png")
        boton = ttk.Button(ventana2, image=img_boton )
        boton.place(x=271, y=650)
        boton.image = img_boton
        


        

        #Bontones
        botoniniciar=Button(ventana2, text = "ENTRAR", font = ("Times New Roman", 13), bg = "white", bd = 0, width = 15).place(x = 620, y = 520)

        botonregistrar=Button(ventana2, text = "Si no tienes cuenta, dale click aquí", font = ("Times New Roman", 11, BOLD), bg = "#00A75E", fg = "white", bd = 0, command= destroy_1).place(x = 567, y = 600)



        #Decoración
        #textopublicidad=Label(ventana, text = , font = ("Times New Roman", 14)).place(x = 50, y = 310)

        #imagenscrum = PhotoImage(file="5.png")
        #fondo = Label(ventana, image = imagenscrum).place(x = 50, y = 80)

        ventana2.mainloop()

Inicio()