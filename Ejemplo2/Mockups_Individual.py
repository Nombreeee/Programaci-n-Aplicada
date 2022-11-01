# Mockups_Individual
import tkinter as tk
from tkinter import *
from tkinter import ttk
from cProfile import label
from distutils.command.config import config
from email.mime import image
# import imp
from tkinter import*
from tkinter.font import BOLD
from turtle import heading

w = 1320
h = 680

ventana2=Tk()


#Raiz

ventana2.title("Scrum Inicio")


# ----------- CENTRAR ------------- #
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

# ----------------- Funciones de Movimiento ---------------- #

def cerrar():
    ventana2.withdraw()
    




# ----------------- Funciones de Moviemiento end ---------------- #

# ----------------- CAJA LATERAL ---------------- #


cajalateral = tk.Frame(ventana2, highlightbackgroun='yellow', highlightcolor='yellow', highlightthickness=2, bg='#F2CB00', width=300, height=700)
titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
titulo1_label = tk.Button(titulo1, text='Scrum Board', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)#, command = Ir_Scrum)

titulo2 = tk.Frame(cajalateral)
titulo2_label = tk.Button(titulo2, text='In Progress', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)#, command= Ir_Progress)

titulo3 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
titulo3_label = tk.Button(titulo3, text='To Do', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)#, command = Ir_ToDo)

titulo4 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
titulo4_label = tk.Button(titulo4, text='Done', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)#, command = Ir_Done)



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





img_Proye1 = tk.PhotoImage(file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Ejemplo2/Proyecto1.png")
boton = ttk.Button(ventana2, image=img_Proye1)#, command= Ir_Scrum)
boton.place(x=475, y=240)
boton.image = img_Proye1
lbl_Proy1 = tk.Label(ventana2, text = "Proyecto 1", font = ("Times New Roman", 13), bg = "#D9D9D9").place(x = 545, y = 455)

img_Proye2 = tk.PhotoImage(file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Ejemplo2/Proyecto2.png")
boton2 = ttk.Button(ventana2, image=img_Proye2)#, command= Ir_Progress)
boton2.place(x=940, y=240)
boton2.image = img_Proye2
lbl_Proy2 = tk.Label(ventana2, text = "Proyecto 2", font = ("Times New Roman", 13), bg = "#D9D9D9").place(x = 1010, y = 455)


    

img_boton = tk.PhotoImage(file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Ejemplo2/log_out.png")
boton = ttk.Button(ventana2, image=img_boton, command =  cerrar)
boton.place(x=271, y=650)
boton.image = img_boton


def ir_Done ():
    ventana2.withdraw()
    Donee ()
    tk.Toplevel()
    
    
    


titulo4_label['command'] = ir_Done














class ScrumBoard1():
    def __init__(controller):

        #Raiz
        
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

        
        # ----------------- Funciones de Movimiento ---------------- #

        def cerrar():
            ventana2.destroy()


        # ----------------- Funciones de Movimiento end ---------------- #

        # ----------------- CAJA LATERAL ---------------- #


        cajalateral = tk.Frame(ventana2, highlightbackgroun='yellow', highlightcolor='yellow', highlightthickness=2, bg='#F2CB00', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Inicio', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1) #command = mainform1)

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='In Progress', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)#, command = Ir_Progress)

        titulo3 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo3_label = tk.Button(titulo3, text='To Do', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)#, command = Ir_ToDo)
        
        titulo4 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo4_label = tk.Button(titulo4, text='Done', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)#, command = Ir_Done)



        cajalateral.pack(side = LEFT)
        cajalateral.config(cursor='heart')
        titulo1.pack()
        titulo1_label.pack()
        titulo1.place(y=30, x=100)

        titulo2.pack()
        titulo2_label.pack()
        titulo2.place(y=190, x=65)

        titulo3.pack()
        titulo3_label.pack()
        titulo3.place(y=340, x=92)

        titulo4.pack()
        titulo4_label.pack()
        titulo4.place(y=500, x=92)

        
             

        img_boton = tk.PhotoImage(file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Ejemplo2/log_out.png")
        boton = ttk.Button(ventana2, image=img_boton, command = cerrar )
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

        




























class ToDo():
    def __init__(controller):

        #Raiz
        
        ventana2.title("Scrum To Do")
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

        
        # ----------------- Funciones de Movimiento ---------------- #

        def cerrar():
            ventana2.destroy()
                     

        # ----------------- Funciones de Movimiento end ---------------- #

        # ----------------- CAJA LATERAL ---------------- #


        cajalateral = tk.Frame(ventana2, highlightbackgroun='yellow', highlightcolor='yellow', highlightthickness=2, bg='#F2CB00', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Scrum Board', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1) #command = mainform1)

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='In Progress', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)#, command = Ir_Progress)

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

        


        img_boton = tk.PhotoImage(file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Ejemplo2/log_out.png")
        boton = ttk.Button(ventana2, image=img_boton, command = cerrar )
        boton.place(x=271, y=650)
        boton.image = img_boton

        

        # -----------------------FIN DE LA BARRA LATERAL ----------------------- #

        

        ventana2.config(menu=menubar, bg="#D9D9D9")

        ventana2.config(menu=menubar, bg="#D9D9D9")
        lbl = tk.Label(ventana2, text='Lista de tareas a realizar:', font=('verdana',17, 'italic', 'bold'), fg='#2A2C2B',bg="#D9D9D9")
        lbl.place(y=107, x=590, anchor=CENTER)

        blanca = tk.Frame (ventana2, width=900, height=450).place(x = 360, y =170)

        


































class InProgress():
    def __init__(controller):

        #Raiz
        ventana2= Tk()
        ventana2.title("In Progress")
        


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

        def cerrar():
            ventana2.destroy()
            

        # ----------------- CAJA LATERAL ---------------- #


        cajalateral = tk.Frame(ventana2, highlightbackgroun='yellow', highlightcolor='yellow', highlightthickness=2, bg='#F2CB00', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Inicio', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)#, command = Ir_Inicio)

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='Scrum Board', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)#, command = Ir_Scrum)

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


        img_boton = tk.PhotoImage(file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Ejemplo2/log_out.png")
        boton = ttk.Button(ventana2, image=img_boton, command = cerrar )
        boton.place(x=271, y=650)
        boton.image = img_boton

        

        # -----------------------FIN DE LA BARRA LATERAL ----------------------- #

        ventana2.config(menu=menubar, bg="#D9D9D9")
        lbl = tk.Label(ventana2, text='Lista de tareas que están siendo realizadas:', font=('verdana',17, 'italic', 'bold'), fg='#2A2C2B',bg="#D9D9D9")
        lbl.place(y=107, x=590, anchor=CENTER)

        blanca = tk.Frame (ventana2, width=900, height=450).place(x = 360, y =170)
        
        



















class Donee():
    def __init__(controller):

        #Raiz
        
        ventana2.title("Scrum Done")
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

        def cerrar():
            ventana2.destroy()


                     

        # ----------------- Funciones de Moviemiento end ---------------- #

        # ----------------- CAJA LATERAL ---------------- #


        cajalateral = tk.Frame(ventana2, highlightbackgroun='yellow', highlightcolor='yellow', highlightthickness=2, bg='#F2CB00', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Scrum Board', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1) #command = mainform1)

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='In Progress', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)#, command = Ir_Progress)

        titulo3 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo3_label = tk.Button(titulo3, text='To Do', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)
        
        titulo4 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo4_label = tk.Button(titulo4, text='Inicio', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)



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

    


        img_boton = tk.PhotoImage(file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Ejemplo2/log_out.png")
        boton = ttk.Button(ventana2, image=img_boton, command = cerrar )
        boton.place(x=271, y=650)
        boton.image = img_boton

        

        # -----------------------FIN DE LA BARRA LATERAL ----------------------- #

        

        ventana2.config(menu=menubar, bg="#D9D9D9")

        ventana2.config(menu=menubar, bg="#D9D9D9")
        lbl = tk.Label(ventana2, text='Lista de tareas Completadas:', font=('verdana',17, 'italic', 'bold'), fg='#2A2C2B',bg="#D9D9D9")
        lbl.place(y=107, x=590, anchor=CENTER)

        blanca = tk.Frame (ventana2, width=900, height=450).place(x = 360, y =170)

        

        
ventana2.mainloop()

