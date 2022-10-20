import tkinter as tk
from tkinter import *
from tkinter import ttk
from cProfile import label
from distutils.command.config import config
from tkinter import *
from email.mime import image #
from tkinter.font import BOLD
from turtle import heading
from ScrumBoard import ScrumBoard1

#import paglogin

w = 1320
h = 680

class InProgress():
    def __init__(controller):

        #Raiz
        ventana2=Tk()
        ventana2.title("In Progress")
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
        title_label = tk.Label(titleframe, text='In Progress', padx=15, pady=5, bg='#f2cb00', fg='black', font=('Italiana',24), width=8)
        

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

        # ---------------- FUNCIONES DE DESPLAZAMIENTO ---------------- #

       # def Ir_Scrum():
        #    ScrumBoard1()  
        #   ventana2.destroy()
            


        # ----------------- CAJA LATERAL ---------------- #


        cajalateral = tk.Frame(ventana2, highlightbackgroun='yellow', highlightcolor='yellow', highlightthickness=2, bg='#F2CB00', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Inicio', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='Scrum Board', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1 ) #, command = Ir_Scrum)

        titulo3 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo3_label = tk.Button(titulo3, text='To Do', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)
        
        titulo4 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo4_label = tk.Button(titulo4, text='Done', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)



        cajalateral.pack(side = LEFT)
        cajalateral.config(cursor='heart')
        titulo1.pack()
        titulo1_label.pack()
        titulo1.place(y=30, x=100)

        titulo2.pack()
        titulo2_label.pack()
        titulo2.place(y=190, x=55)

        titulo3.pack()
        titulo3_label.pack()
        titulo3.place(y=340, x=92)

        titulo4.pack()
        titulo4_label.pack()
        titulo4.place(y=500, x=92)

        img_boton = tk.PhotoImage(file="log_out.png")
        boton = ttk.Button(ventana2, image=img_boton )
        boton.place(x=271, y=650)
        boton.image = img_boton

        

        # -----------------------FIN DE LA BARRA LATERAL ----------------------- #

        ventana2.config(menu=menubar, bg="#D9D9D9")
        lbl = tk.Label(ventana2, text='Lista de tareas que están siendo realizadas:', font=('verdana',17, 'italic', 'bold'), fg='#2A2C2B',bg="#D9D9D9")
        lbl.place(y=107, x=590, anchor=CENTER)

        blanca = tk.Frame (ventana2, width=900, height=450).place(x = 360, y =170)
        # blanca.pack()