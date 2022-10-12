from cProfile import label
from distutils.command.config import config
from email.mime import image
import imp
from tkinter import*
from tkinter.font import BOLD
from turtle import heading
#from Registro import paginaregistro
#import pagregister

class paginaregistro():
    def __init__(controller):

        #Raiz
        ventana=Tk()
        ventana.title("Scrum")
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













class paginalogin():
    def __init__(controller):

        #Raiz
        ventana2=Tk()
        ventana2.title("Scrum")
        ventana2.resizable(False, False)
        ventana2.geometry("900x500")
        #ventana.iconbitmap("Scrum.ico")



        #Frame verde
        cuadroverde = Frame()
        cuadroverde.place(x = 510, y = 70)
        cuadroverde.config(bg = "#00A75E", width = 350, height = 350)

        textoiniciosesion=Label(ventana2, text = "INICIA SESIÓN", font = ("Times New Roman", 20), bg = "#00A75E").place(x = 603, y = 100)



        #Usuario y contraseña
        usuariotexto=Label(ventana2, text = "Usuario: ", font = ("Times New Roman", 13), bg = "#00A75E").place(x = 540, y = 160)
        usuariocuadro=Entry(ventana2, font = ("Times New Roman", 10), width = 48, bd = 0).place(x = 540, y = 185)

        clavetexto=Label(ventana2, text = "Contraseña: ", font = ("Times New Roman", 13), bg = "#00A75E").place(x = 540, y = 230)
        clavecuadro=Entry(ventana2, font = ("Times New Roman", 10,), width = 48, show = "*", bd = 0).place(x = 540, y = 255)



        def destroy_1():
            ventana2.destroy()
            paginaregistro ()

        #Bontones
        botoniniciar=Button(ventana2, text = "ENTRAR", font = ("Times New Roman", 13), bg = "white", bd = 0, width = 15).place(x = 620, y = 315)

        botonregistrar=Button(ventana2, text = "Si no tienes cuenta, dale click aquí", font = ("Times New Roman", 11, BOLD), bg = "#00A75E", fg = "white", bd = 0, command= destroy_1).place(x = 567, y = 355)



        #Decoración
        #textopublicidad=Label(ventana, text = , font = ("Times New Roman", 14)).place(x = 50, y = 310)

        #imagenscrum = PhotoImage(file="5.png")
        #fondo = Label(ventana, image = imagenscrum).place(x = 50, y = 80)

        ventana2.mainloop()

paginalogin()