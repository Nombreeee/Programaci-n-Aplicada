# main form
import tkinter as tk
from tkinter import *
from tkinter import ttk
import psycopg2

w = 1310
h = 720



class mainform1:
    
    def __init__(self, master):
        self.master = master
        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- HEADER ------------- #
        
        headerframe = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow', highlightthickness=2, bg='#f2cb00', width=w+60, height=70)
        titleframe = tk.Frame(headerframe, bg='#f2cb00', padx=1, pady=1)
        title_label = tk.Label(titleframe, text='VJ Scrum', padx=15, pady=5, bg='#f2cb00', fg='black', font=('Italiana',24), width=8)
        

        headerframe.pack()
        titleframe.pack()
        title_label.pack()
        
        titleframe.place(y=32, relx=0.5, anchor=CENTER)

    

        

        # ----------- END HEADER ------------- #

        # ----------- MENU ------------- #

        self.frame = tk.Frame(self.master)
        self.menubar = Menu(self.frame)
        self.products = Menu(self.menubar)
        self.products.add_command(label="Inicio")
        self.products.add_command(label="Avances")
        self.products.add_command(label="Tareas")

        self.menubar.add_cascade(menu=self.products, label="Paginas")

        self.categories = Menu(self.menubar)
        self.categories.add_command(label="Añadir")
        self.categories.add_command(label="Editar")
        self.categories.add_command(label="Remover")

        self.menubar.add_cascade(menu=self.categories, label="Category")

        self.frame.pack()

        # ------------------------------ #

        # Aqui creo la caja gris que se encuentra al lateral del programa"
        # Esta caja contiene los botones para navegar entre las ventanas del programa"
    
        

        cajalateral = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow', highlightthickness=2, bg='#D9D9D9', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Scrum Board', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1) #command = lambda : controller.show_frame(Scrum_board))

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

        #titulo5.pack()
        #titulo5_label.pack()
        #titulo5.place(y = 550, x= 150)

        # -------------------------------------------- #
        self.master.config(menu=self.menubar, bg="#ffe291")
        self.lbl = tk.Label(self.master, text='Bienvenido a la pagina de Scrum', font=('verdana',17, 'italic', 'bold'), fg='#2A2C2B',bg="#ffe291")
        self.lbl.place(y=90, x=1120, anchor=CENTER)

        

        self.boton1 = tk.Button(self.master, text="Proyecto 1", width=20, height=10, anchor =CENTER)
        self.boton1.place(y=350, x=570, anchor=CENTER)

        self.boton2 = tk.Button(self.master, text="Proyecto 2", width=20, height=10, anchor =CENTER)
        self.boton2.place(y=350, x=1000, anchor=CENTER)

        #titulo5img = tk.PhotoImage(file="log_out.png", height = 10)
        #titulo5 = ttk.Button(self.master, image=titulo5img, width= 50, xwi)
        #titulo5.place(x=50, y=50)
        
        img_boton = tk.PhotoImage(file="log_out.png")
        boton = ttk.Button(self.master, image=img_boton)
        boton.place(x=271, y=648)
        boton.image = img_boton








class mainform2: # clase se va a llamar ScrumBoard
    
    def __init__(self, Scrumboard):
        self.master = Scrumboard

        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- HEADER ------------- #
        
        headerframe = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow', highlightthickness=2, bg='#f2cb00', width=w+60, height=70)
        titleframe = tk.Frame(headerframe, bg='#f2cb00', padx=1, pady=1)
        title_label = tk.Label(titleframe, text='Scrum Board', padx=15, pady=5, bg='#f2cb00', fg='black', font=('Italiana',24), width=8)
        

        headerframe.pack()
        titleframe.pack()
        title_label.pack()
        
        titleframe.place(y=32, relx=0.5, anchor=CENTER)

    

        

        # ----------- END HEADER ------------- #

        # ----------- MENU ------------- #

        self.frame = tk.Frame(self.master)
        self.menubar = Menu(self.frame)
        self.products = Menu(self.menubar)
        self.products.add_command(label="Inicio")
        self.products.add_command(label="Avances")
        self.products.add_command(label="Tareas")

        self.menubar.add_cascade(menu=self.products, label="Paginas")

        self.categories = Menu(self.menubar)
        self.categories.add_command(label="Añadir")
        self.categories.add_command(label="Editar")
        self.categories.add_command(label="Remover")

        self.menubar.add_cascade(menu=self.categories, label="Category")

        self.frame.pack()

        # ------------------------------    

        cajalateral = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow', highlightthickness=2, bg='#D9D9D9', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Inicio', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1) #command = lambda : controller.show_frame(Scrum_board))

        titulo2 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo2_label = tk.Button(titulo2, text='In Progress', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)

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
        titulo2.place(y=190, x=65)

        titulo3.pack()
        titulo3_label.pack()
        titulo3.place(y=340, x=92)

        titulo4.pack()
        titulo4_label.pack()
        titulo4.place(y=500, x=92)

        img_boton = tk.PhotoImage(file="log_out.png")
        boton = ttk.Button(self.master, image=img_boton)
        boton.place(x=271, y=648)
        boton.image = img_boton


        # -------------------------------------------- #

        self.master.config(menu=self.menubar, bg="#ffe291")

        self.label1 = tk.Label(self.master, text="To Do",  font=('Italiana',24), bg = "#ffe291")
        self.label1.place(y=100, x=440, anchor=CENTER)
        self.label11 = tk.Label(self.master,  font=('Italiana',24), bg = "#D9D9D9", height= 14, width=10)
        self.label11.place(y=400, x=440, anchor=CENTER)
        self.label12 = tk.Button(self.master, text="Ir a To Do",  font=('Italiana',15), bg = "#ffe291")
        self.label12.place(y=620, x=440, anchor=CENTER)

        self.label2 = tk.Label(self.master, text="In Progress", font=('Italiana',24), bg = "#ffe291")
        self.label2.place(y=100, x=800, anchor=CENTER)
        self.label21 = tk.Label(self.master,  font=('Italiana',24), bg = "#D9D9D9", height= 14, width=10)
        self.label21.place(y=400, x=800, anchor=CENTER)
        self.label22 = tk.Button(self.master, text="Ir a In Progress",  font=('Italiana',15), bg = "#ffe291")
        self.label22.place(y=620, x=800, anchor=CENTER)

        self.label3 = tk.Label(self.master, text="Done", font=('Italiana',24), bg = "#ffe291")
        self.label3.place(y=100, x=1170, anchor=CENTER)
        self.label31 = tk.Label(self.master,  font=('Italiana',24), bg = "#D9D9D9", height= 14, width=10)
        self.label31.place(y=400, x=1170, anchor=CENTER)
        self.label32 = tk.Button(self.master, text="Ir a Done",  font=('Italiana',15), bg = "#ffe291")
        self.label32.place(y=620, x=1175, anchor=CENTER)

        #title_label = tk.Label(titleframe, text='Scrum Board', padx=15, pady=5, bg='#f2cb00', fg='black', font=('Italiana',24), width=8)














class mainform3: # clase se va a llamar To Do
    
    def __init__(self, Scrumboard):
        self.master = Scrumboard

        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- HEADER ------------- #
        
        headerframe = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow', highlightthickness=2, bg='#f2cb00', width=w+60, height=70)
        titleframe = tk.Frame(headerframe, bg='#f2cb00', padx=1, pady=1)
        title_label = tk.Label(titleframe, text='To Do', padx=15, pady=5, bg='#f2cb00', fg='black', font=('Italiana',24), width=8)
        

        headerframe.pack()
        titleframe.pack()
        title_label.pack()
        
        titleframe.place(y=32, relx=0.5, anchor=CENTER)

    

        

        # ----------- END HEADER ------------- #

        # ----------- MENU ------------- #

        self.frame = tk.Frame(self.master)
        self.menubar = Menu(self.frame)
        self.products = Menu(self.menubar)
        self.products.add_command(label="Inicio")
        self.products.add_command(label="Avances")
        self.products.add_command(label="Tareas")

        self.menubar.add_cascade(menu=self.products, label="Paginas")

        self.categories = Menu(self.menubar)
        self.categories.add_command(label="Añadir")
        self.categories.add_command(label="Editar")
        self.categories.add_command(label="Remover")

        self.menubar.add_cascade(menu=self.categories, label="Category")

        self.frame.pack()

        # ------------------------------    

        cajalateral = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow', highlightthickness=2, bg='#D9D9D9', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Inicio', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1) #command = lambda : controller.show_frame(Scrum_board))

        titulo2 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo2_label = tk.Button(titulo2, text='In Progress', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)

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
        titulo2.place(y=190, x=65)

        titulo3.pack()
        titulo3_label.pack()
        titulo3.place(y=340, x=92)

        titulo4.pack()
        titulo4_label.pack()
        titulo4.place(y=500, x=92)

        img_boton = tk.PhotoImage(file="log_out.png")
        boton = ttk.Button(self.master, image=img_boton)
        boton.place(x=271, y=648)
        boton.image = img_boton


        # -------------------------------------------- #
        self.master.config(menu=self.menubar, bg="#ffe291")
        self.lbl = tk.Label(self.master, text='Lista de tareas en espera a ser realizadas:', font=('verdana',17, 'italic', 'bold'), fg='#2A2C2B',bg="#ffe291")
        self.lbl.place(y=105, x=585, anchor=CENTER)













class mainform4: # clase se va a llamar In Progress
    
    def __init__(self, Scrumboard):
        self.master = Scrumboard

        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- HEADER ------------- #
        
        headerframe = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow', highlightthickness=2, bg='#f2cb00', width=w+60, height=70)
        titleframe = tk.Frame(headerframe, bg='#f2cb00', padx=1, pady=1)
        title_label = tk.Label(titleframe, text='In Progress', padx=15, pady=5, bg='#f2cb00', fg='black', font=('Italiana',24), width=8)
        

        headerframe.pack()
        titleframe.pack()
        title_label.pack()
        
        titleframe.place(y=32, relx=0.5, anchor=CENTER)

    

        

        # ----------- END HEADER ------------- #

        # ----------- MENU ------------- #

        self.frame = tk.Frame(self.master)
        self.menubar = Menu(self.frame)
        self.products = Menu(self.menubar)
        self.products.add_command(label="Inicio")
        self.products.add_command(label="Avances")
        self.products.add_command(label="Tareas")

        self.menubar.add_cascade(menu=self.products, label="Paginas")

        self.categories = Menu(self.menubar)
        self.categories.add_command(label="Añadir")
        self.categories.add_command(label="Editar")
        self.categories.add_command(label="Remover")

        self.menubar.add_cascade(menu=self.categories, label="Category")

        self.frame.pack()

        # ------------------------------    

        cajalateral = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow', highlightthickness=2, bg='#D9D9D9', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Inicio', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1) #command = lambda : controller.show_frame(Scrum_board))

        titulo2 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo2_label = tk.Button(titulo2, text='In Progress', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)

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
        titulo2.place(y=190, x=65)

        titulo3.pack()
        titulo3_label.pack()
        titulo3.place(y=340, x=92)

        titulo4.pack()
        titulo4_label.pack()
        titulo4.place(y=500, x=92)

        img_boton = tk.PhotoImage(file="log_out.png")
        boton = ttk.Button(self.master, image=img_boton)
        boton.place(x=271, y=648)
        boton.image = img_boton


        # -------------------------------------------- #
        self.master.config(menu=self.menubar, bg="#ffe291")
        self.lbl = tk.Label(self.master, text='Lista de tareas que están siendo realizadas:', font=('verdana',17, 'italic', 'bold'), fg='#2A2C2B',bg="#ffe291")
        self.lbl.place(y=107, x=590, anchor=CENTER)














class mainform: # clase se va a llamar Done
    
    def __init__(self, Scrumboard):
        self.master = Scrumboard

        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- HEADER ------------- #
        
        headerframe = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow', highlightthickness=2, bg='#f2cb00', width=w+60, height=70)
        titleframe = tk.Frame(headerframe, bg='#f2cb00', padx=1, pady=1)
        title_label = tk.Label(titleframe, text='Done', padx=15, pady=5, bg='#f2cb00', fg='black', font=('Italiana',24), width=8)
        

        headerframe.pack()
        titleframe.pack()
        title_label.pack()
        
        titleframe.place(y=32, relx=0.5, anchor=CENTER)

    

        

        # ----------- END HEADER ------------- #

        # ----------- MENU ------------- #

        self.frame = tk.Frame(self.master)
        self.menubar = Menu(self.frame)
        self.products = Menu(self.menubar)
        self.products.add_command(label="Inicio")
        self.products.add_command(label="Avances")
        self.products.add_command(label="Tareas")

        self.menubar.add_cascade(menu=self.products, label="Paginas")

        self.categories = Menu(self.menubar)
        self.categories.add_command(label="Añadir")
        self.categories.add_command(label="Editar")
        self.categories.add_command(label="Remover")

        self.menubar.add_cascade(menu=self.categories, label="Category")

        self.frame.pack()

        # ------------------------------    

        cajalateral = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow', highlightthickness=2, bg='#D9D9D9', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Inicio', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1) #command = lambda : controller.show_frame(Scrum_board))

        titulo2 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo2_label = tk.Button(titulo2, text='In Progress', padx=15, pady=5, bg='#D9D9D9', fg='black', font=('Italiana',18, 'italic'), height= 1)

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
        titulo2.place(y=190, x=65)

        titulo3.pack()
        titulo3_label.pack()
        titulo3.place(y=340, x=92)

        titulo4.pack()
        titulo4_label.pack()
        titulo4.place(y=500, x=92)

        img_boton = tk.PhotoImage(file="log_out.png")
        boton = ttk.Button(self.master, image=img_boton)
        boton.place(x=271, y=648)
        boton.image = img_boton


        # -------------------------------------------- #
        self.master.config(menu=self.menubar, bg="#ffe291")
        self.lbl = tk.Label(self.master, text='Lista de tareas que ya han sido realizadas:', font=('verdana',17, 'italic', 'bold'), fg='#2A2C2B',bg="#ffe291")
        self.lbl.place(y=100, x=590, anchor=CENTER)