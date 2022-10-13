import tkinter as tk
from tkinter import *
from tkinter import ttk
from cProfile import label
from distutils.command.config import config
# import imp
from tkinter import *
from email.mime import image #
from tkinter.font import BOLD
from turtle import heading
from In_Progress import *
from To_Do import *
from Done import *

#from MOCKUPS import Inicio
#import paglogin

w = 1320
h = 680

class paginaregistro1():
    def __init__(controller):

        #Raiz
        ventana=Tk()
        ventana.title("Srum Board")
        ventana.resizable(False, False)
        ventana.geometry("900x500")
        



        #Bordes verdes
        recverde=Frame()
        recverde.pack(side="left")
        recverde.config(bg="#00A75E", width=90, height=500)

        recverde2=Frame()
        recverde2.pack(side="right", anchor="n")
        recverde2.config(bg="#00A75E", width=810, height=80)



        #Datos usuario
        textoregistro=Label(ventana, text = "REGISTRATE", font = ("Times New Roman", 20)).place(x = 445, y = 100)

        nombretexto=Label(ventana, text = "Nombres: ", font = ("Times New Roman", 13)).place(x = 210, y = 180)
        nombrecuadro=Entry(ventana, font = ("Times New Roman", 10), width = 40, bd = 0, bg="#D6D6D6").place(x = 210, y = 205)

        apellidotexto=Label(ventana, text = "Apellidos: ", font = ("Times New Roman", 13)).place(x = 550, y = 180)
        apellidocuadro=Entry(ventana, font = ("Times New Roman", 10), width = 40, bd = 0, bg="#D6D6D6").place(x = 550, y = 205)

        correotexto=Label(ventana, text = "Correo: ", font = ("Times New Roman", 13)).place(x = 210, y = 245)
        correocuadro=Entry(ventana, font = ("Times New Roman", 10), width = 40, bd = 0, bg="#D6D6D6").place(x = 210, y = 270)

        direcciontexto=Label(ventana, text = "Dirección: ", font = ("Times New Roman", 13)).place(x = 550, y = 245)
        direccioncuadro=Entry(ventana, font = ("Times New Roman", 10), width = 40, bd = 0, bg="#D6D6D6").place(x = 550, y = 270)

        contraseñatexto=Label(ventana, text = "Contraseña: ", font = ("Times New Roman", 13)).place(x = 210, y = 310)
        contraseñacuadro=Entry(ventana, font = ("Times New Roman", 10), width = 40, bd = 0, bg="#D6D6D6", show = "*").place(x = 210, y = 335)

        confirmarcontratexto=Label(ventana, text = "Confirmar contraseña: ", font = ("Times New Roman", 13)).place(x = 550, y = 310)
        confirmarcontracuadro=Entry(ventana, font = ("Times New Roman", 10), width = 40, bd = 0, bg="#D6D6D6", show = "*").place(x = 550, y = 335)



        #Check box aceptar terminos y conidiciones
        terminos=Checkbutton(ventana, text="Aceptar terminos y condiciones", font = ("Times New Roman", 13), bd = 0).place(x = 390, y = 390)



        #Botones
        registrarboton=Button(ventana, text = "REGISTRAR", font = ("Times New Roman", 13), bg = "#D6D6D6", bd = 0, width = 15).place(x = 440, y = 435)

        volver=Button(ventana, text="Iniciar\nSesión", font = ("Times New Roman", 13, BOLD), bg = "#00A75E", bd = 0, width = 6, fg = "white").place(x = 12, y = 430)

       # ventana.mainloop()



















class ScrumBoard1():
    def __init__(controller):

        #Raiz
        ventana2=Tk()
        ventana2.title("Scrum Board")
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

        
        # ----------------- Funciones de Moviemiento ---------------- #

        def Ir_Progress():
            InProgress() 
            ventana2.destroy()

        def Ir_ToDo():
            ventana2.destroy()
            ToDo()  
        
        def Ir_Done():
            ventana2.destroy()
            Donee()


        # ----------------- Funciones de Moviemiento end ---------------- #

        # ----------------- CAJA LATERAL ---------------- #


        cajalateral = tk.Frame(ventana2, highlightbackgroun='yellow', highlightcolor='yellow', highlightthickness=2, bg='#F2CB00', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Inicio', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1) #command = mainform1)

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='In Progress', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1, command = Ir_Progress)

        titulo3 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo3_label = tk.Button(titulo3, text='To Do', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1, command = Ir_ToDo)
        
        titulo4 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo4_label = tk.Button(titulo4, text='Done', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1, command = Ir_Done)



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

        img_boton = tk.PhotoImage(file="log_out.png")
        boton = ttk.Button(ventana2, image=img_boton )
        boton.place(x=271, y=650)
        boton.image = img_boton

        

        # -----------------------FIN DE LA BARRA LATERAL ----------------------- #

        

        ventana2.config(menu=menubar, bg="#D9D9D9")

        label1 = tk.Label(ventana2, text="To Do",  font=('Italiana',24), bg = "#ffe291")
        label1.place(y=100, x=440, anchor=CENTER)
        label11 = tk.Label(ventana2,  font=('Italiana',24), bg = "#D9D9D9", height= 14, width=10)
        label11.place(y=400, x=440, anchor=CENTER)
        label12 = tk.Button(ventana2, text="Ir a To Do",  font=('Italiana',15), bg = "#ffe291")
        label12.place(y=620, x=440, anchor=CENTER)

        label2 = tk.Label(ventana2, text="In Progress", font=('Italiana',24), bg = "#ffe291")
        label2.place(y=100, x=800, anchor=CENTER)
        label21 = tk.Label(ventana2,  font=('Italiana',24), bg = "#D9D9D9", height= 14, width=10)
        label21.place(y=400, x=800, anchor=CENTER)
        label22 = tk.Button(ventana2, text="Ir a In Progress",  font=('Italiana',15), bg = "#ffe291")
        label22.place(y=620, x=800, anchor=CENTER)

        label3 = tk.Label(ventana2, text="Done", font=('Italiana',24), bg = "#ffe291")
        label3.place(y=100, x=1170, anchor=CENTER)
        label31 = tk.Label(ventana2,  font=('Italiana',24), bg = "#D9D9D9", height= 14, width=10)
        label31.place(y=400, x=1170, anchor=CENTER)
        label32 = tk.Button(ventana2, text="Ir a Done",  font=('Italiana',15), bg = "#ffe291")
        label32.place(y=620, x=1175, anchor=CENTER)
