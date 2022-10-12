from email.mime import image
from tkinter import*
from tkinter.font import BOLD
from turtle import heading
#import paglogin


class paginaregistro1():
    def __init__(controller):

        #Raiz
        ventana=Tk()
        ventana.title("Scrum")
        ventana.resizable(False, False)
        ventana.geometry("900x500")
        ventana.iconbitmap("Scrum.ico")



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
