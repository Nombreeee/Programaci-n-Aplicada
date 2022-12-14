import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
#import mysql.connector
import psycopg2
#import proyectos

cedula = 1000972264
idproyecto2 = 3
selecproyecto = 0


username2 = "e"
root = Tk()
#connection = mysql.connector.connect(host='localhost', user='root', port='3306', password='', database='py_lg_rg_db')
#conexion = psycopg2.connect(host='localhost',database='aplicada', user='postgresql', password='Martin123')
connection = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='admin',
    database='nueva'  # antes aplicada
)

root.title('Scrum Iniciar Sesión')
c = connection.cursor()

w = 1310
h = 720
bgcolor = "#bdc3c7"
gris = "#D9D9D9"

# ----------- CENTER FORM ------------- #
# root.overrideredirect(1) # remove border
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws-w)/2
y = (hs-h)/2
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

# ----------- HEADER ------------- #

headerframe = tk.Frame(root, highlightbackgroun='yellow', highlightcolor='yellow',
                       highlightthickness=2, bg='#f2cb00', width=w, height=70)
titleframe = tk.Frame(headerframe, bg='#f2cb00', padx=1, pady=1)
title_label = tk.Label(titleframe, text='VJ Scrum', padx=15, pady=5,
                       bg='#f2cb00', fg='black', font=('Italiana', 24), width=8)
close_button = tk.Button(headerframe, text='X',
                         borderwidth=1, relief='solid', font=('Verdana', 12))

headerframe.pack()
titleframe.pack()
title_label.pack()
close_button.pack()

titleframe.place(y=32, relx=0.5, anchor=CENTER)
close_button.place(x=1280, y=10)

# close window


def close_win():
    root.destroy()


close_button['command'] = close_win


# ----------- END HEADER ------------- #

mainframe = tk.Frame(root, width=w, height=h)

# ----------- Login Page ------------- #

loginframe = tk.Frame(mainframe, width=w, height=h)
login_contentframe = tk.Frame(loginframe, padx=475, pady=100, highlightbackgroun='yellow',
                              highlightcolor='yellow', highlightthickness=2, bg=bgcolor)

username_label = tk.Label(
    login_contentframe, text='Usuario  ', font=('Verdana', 16), bg=bgcolor)
password_label = tk.Label(
    login_contentframe, text='Contraseña  ', font=('Verdana', 16), bg=bgcolor)

username_entry = tk.Entry(login_contentframe, font=('Verdana', 16))
password_entry = tk.Entry(login_contentframe, font=('Verdana', 16), show='*')

login_button = tk.Button(login_contentframe, text="Login", font=(
    'Verdana', 16), bg='#2980b9', fg='#fff', padx=20, pady=10, width=25)

go_register_label = tk.Label(login_contentframe, text=">>  ¿No tienes cuenta? Crea una!  <<", font=(
    'Verdana', 10), bg=bgcolor, fg='red')

mainframe.pack(fill='both', expand=1)
loginframe.pack(fill='both', expand=1)
login_contentframe.pack(fill='both', expand=1)

username_label.grid(row=0, column=0, pady=10)
username_entry.grid(row=0, column=1)

password_label.grid(row=1, column=0, pady=10)
password_entry.grid(row=1, column=1)

login_button.grid(row=2, column=0, columnspan=2, pady=40)

go_register_label.grid(row=3, column=0, columnspan=2, pady=20)


# create a function to display the register frame


def go_to_register():
    loginframe.forget()
    registerframe.pack(fill="both", expand=1)
    title_label['text'] = ' REGISTRO '
    # title_label['bg'] = '#27ae60'


go_register_label.bind("<Button-1>", lambda page: go_to_register())


# create a function to make the user login
def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    vals = (username, password,)
    globals()['username2'] = username
    select_query = "SELECT * FROM usuarios WHERE username = %s and password = %s"  # antes users
    c.execute(select_query, vals)
    user = c.fetchone()
    if user is not None:
        # messagebox.showinfo('Test','Test')
        Iniciowin = tk.Toplevel()
        app = Inicio(Iniciowin)
        root.withdraw()  # hide the root
        Iniciowin.protocol("WM_DELETE_WINDOW", close_win)  # close the app

    else:
        messagebox.showwarning('Error', 'Usuario o contraseña errada')


login_button['command'] = login


# ----------- Register Page ------------- #

registerframe = tk.Frame(mainframe, width=w, height=h)
register_contentframe = tk.Frame(registerframe, padx=395, pady=105, highlightbackgroun='yellow',
                                 highlightcolor='yellow', highlightthickness=2, bg=bgcolor)

fullname_label_rg = tk.Label(
    register_contentframe, text='Nombre:', font=('Verdana', 14), bg=bgcolor)
surname_label_rg = tk.Label(
    register_contentframe, text='Apellido:', font=('Orbitron', 14), bg=bgcolor)
username_label_rg = tk.Label(
    register_contentframe, text='Usuario:', font=('Verdana', 14), bg=bgcolor)
password_label_rg = tk.Label(
    register_contentframe, text='Contraseña:', font=('Verdana', 14), bg=bgcolor)
phone_label_rg = tk.Label(register_contentframe,
                          text='Telefono:', font=('Verdana', 14), bg=bgcolor)
gender_label_rg = tk.Label(register_contentframe,
                           text='Genero:', font=('Verdana', 14), bg=bgcolor)
email_label_rg = tk.Label(register_contentframe,
                          text='Correo:', font=('Orbitron', 14), bg=bgcolor)
document_label_rg = tk.Label(
    register_contentframe, text='Documento:', font=('Orbitron', 14), bg=bgcolor)


fullname_entry_rg = tk.Entry(
    register_contentframe, font=('Verdana', 14), width=22)
surname_entry_rg = tk.Entry(register_contentframe,
                            font=('Verdana', 14), width=22)
username_entry_rg = tk.Entry(
    register_contentframe, font=('Verdana', 14), width=22)
password_entry_rg = tk.Entry(
    register_contentframe, font=('Verdana', 14), width=22, show='*')
phone_entry_rg = tk.Entry(register_contentframe,
                          font=('Verdana', 14), width=22)
email_entry_rg = tk.Entry(register_contentframe,
                          font=('Verdana', 14), width=22)
document_entry_rg = tk.Entry(
    register_contentframe, font=('Verdana', 14), width=22)


radiosframe = tk.Frame(register_contentframe)
gender = StringVar()
gender.set('Male')
male_radiobutton = tk.Radiobutton(radiosframe, text='Hombre', font=(
    'Orbitron', 14), bg=bgcolor, variable=gender, value='Male')
female_radiobutton = tk.Radiobutton(radiosframe, text='Mujer', font=(
    'Orbitron', 14), bg=bgcolor, variable=gender, value='Female')


register_button = tk.Button(register_contentframe, text="Registrarse", font=(
    'Verdana', 16), bg='#2980b9', fg='#fff', padx=25, pady=10, width=25)

go_login_label = tk.Label(register_contentframe, text=">>¿Ya tienes cuenta? Inicia sesión! <<", font=(
    'Verdana', 10), bg=bgcolor, fg='red')

#mainframe.pack(fill='both', expand=1)
#registerframe.pack(fill='both', expand=1)
register_contentframe.pack(fill='both', expand=1)


fullname_label_rg.grid(row=0, column=0, pady=5, sticky='e')
fullname_entry_rg.grid(row=0, column=1)

username_label_rg.grid(row=2, column=0, pady=5, sticky='e')
username_entry_rg.grid(row=2, column=1)

password_label_rg.grid(row=3, column=0, pady=5, sticky='e')
password_entry_rg.grid(row=3, column=1)

surname_label_rg.grid(row=1, column=0, pady=5, sticky='e')
surname_entry_rg.grid(row=1, column=1)

phone_label_rg.grid(row=4, column=0, pady=5, sticky='e')
phone_entry_rg.grid(row=4, column=1)

email_label_rg.grid(row=5, column=0, pady=5, sticky='e')
email_entry_rg.grid(row=5, column=1)

gender_label_rg.grid(row=7, column=0, pady=5, sticky='e')
radiosframe.grid(row=7, column=1)

document_label_rg.grid(row=6, column=0, pady=5, sticky='e')
document_entry_rg.grid(row=6, column=1)


register_button.grid(row=8, column=0, columnspan=2, pady=20)

go_login_label.grid(row=9, column=0, columnspan=2, pady=10)
male_radiobutton.grid(row=0, column=0)
female_radiobutton.grid(row=0, column=1)


# --------------------------------------- #


# create a function to display the login frame
def go_to_login():
    registerframe.forget()
    loginframe.pack(fill="both", expand=1)
    title_label['text'] = 'VJ Scrum'
    title_label['bg'] = '#f2cb00'


go_login_label.bind("<Button-1>", lambda page: go_to_login())
# --------------------------------------- #

# create a function to check if the username already exists


def check_username(username):
    username = username_entry_rg.get().strip()
    vals = (username,)
    select_query = "SELECT * FROM usuarios WHERE username = %s"
    c.execute(select_query, vals)
    user = c.fetchone()
    if user is not None:
        return True
    else:
        return False


# --------------------------------------- #


# create a function to register a new user
def register():

    fullname = fullname_entry_rg.get().strip()
    document = document_entry_rg.get().strip()
    username = username_entry_rg.get().strip()
    password = password_entry_rg.get().strip()
    surname = surname_entry_rg.get().strip()
    email = email_entry_rg.get().strip()
    phone = phone_entry_rg.get().strip()
    gdr = gender.get()

    if len(fullname) > 0 and len(username) > 0 and len(password) > 0 and len(phone) > 0:
        if check_username(username) == False:
            if password:
                vals = (document, fullname, username,
                        password, phone, surname, gdr, email)
                insert_query = "INSERT INTO usuarios(document,fullname, username, password, phone, surname, gender, email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                c.execute(insert_query, vals)
                connection.commit()
                messagebox.showinfo('Enhorabuena', 'Tu cuenta ha sido creada')
            else:
                messagebox.showwarning('Contraseña')
        else:
            messagebox.showwarning(
                'Usuario existente', 'Este usuario ya esta registrado, intente con otro')
    else:
        messagebox.showwarning('Información incompleta',
                               'Rellene todos los campos')


register_button['command'] = register

# --------------------------------------- #

# ----------0-------------------------------------------------------------- #


class Inicio():

    def __init__(self, master):
        ayudenme = 5
        # cur=py_login_register_form.connection.cursor()
        self.master = master
        self.master.title("Scrum Inicio")
        self.master.config(bg="#D9D9D9")

        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()+ 20
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- HEADER ------------- #
        headerframe = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#f2cb00', width=w+60, height=70)
        titleframe = tk.Frame(headerframe, bg='#f2cb00', padx=1, pady=1)
        title_label = tk.Label(titleframe, text='VJ Scrum', padx=15, pady=5,
                               bg='#f2cb00', fg='black', font=('Italiana', 24), width=8)

        headerframe.pack()
        titleframe.pack()
        title_label.pack()

        titleframe.place(y=32, relx=0.5, anchor=CENTER)

        # ----------------- Funciones de Movimiento ---------------- #

        def cerrarr():
            self.master.destroy()

        def ir_Done():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Done(scrumwindow)

        def ir_ToDo():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ToDo(scrumwindow)

        def ir_Progress():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = InProgress(scrumwindow)

        def ir_ScrumBoard1():
            ayudenme = 1
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ScrumBoard(scrumwindow)

        def ir_ScrumBoard2():
            ayudenme = 2
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ScrumBoard(scrumwindow)

        def ir_CreaHistoria ():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = nueva_Historia(scrumwindow)

        # ----------------- CAJA LATERAL ---------------- #

        cajalateral = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#F2CB00', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Scrum Board', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command = Ir_Scrum)
        titulo1_label['command'] = ir_ScrumBoard1

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='In Progress', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command= Ir_Progress)
        titulo2_label['command'] = ir_Progress

        titulo3 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo3_label = tk.Button(titulo3, text='To Do', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command = Ir_ToDo)
        titulo3_label['command'] = ir_ToDo

        titulo4 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo4_label = tk.Button(titulo4, text='Done', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command = Ir_Done)
        titulo4_label['command'] = ir_Done

        cajalateral.pack(side=LEFT)
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

        sql_select_query3 = "select document from usuarios where username = %s"
        c.execute(sql_select_query3, (username2,))
        record = c.fetchone()
        doc2 = record
        # print(record)

        sql_select_query4 = "select proyect from proyectos where document = %s"
        c.execute(sql_select_query4, (doc2,))
        record2 = c.fetchall()
        #print('record 2: ', record2)

        if (c.rowcount == 0):
            proye1 = ""
            proye2 = ""

        elif (c.rowcount == 1):
            proye1 = record2[0]
            proye2 = ""
            # print(proye1)

        elif (c.rowcount == 2):
            proye1 = record2[0]
            proye2 = record2[1]
            #print('proyecto 1: ', proye1)
            #print ('proyecto 2: ',proye2)

        lbl = tk.Label(self.master, text='Bienvenido a la pagina de Scrum', font=(
            'verdana', 17, 'italic', 'bold'), fg='#2A2C2B', bg="#D9D9D9")
        lbl.place(y=90, x=1070, anchor=CENTER)

        img_Proye1 = tk.PhotoImage(
            file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Scrum/Proyecto1.png")
        # , command= Ir_Scrum)
        boton = ttk.Button(self.master, image=img_Proye1)
        boton.place(x=475, y=240)
        boton.image = img_Proye1
        lbl_Proy1 = tk.Label(self.master, text='\n'.join(''.join(map(str, tup)) for tup in proye1), font=(
            "Times New Roman", 13), bg=gris, width= 28, wraplength= 200).place(x=450, y=455) #  anchor='w', justify=LEFT,  wraplength=900)
        boton['command'] = ir_ScrumBoard1

        img_Proye2 = tk.PhotoImage(
            file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Scrum/Proyecto2.png")
        # , command= Ir_Progress)
        boton2 = ttk.Button(self.master, image=img_Proye2)
        boton2.place(x=940, y=240)
        boton2.image = img_Proye2
        lbl_Proy2 = tk.Label(self.master, text='\n'.join(''.join(map(str, tup)) for tup in proye2), font=(
            "Times New Roman", 13), bg=gris, width = 28).place(x=915, y=455)
        boton2['command'] = ir_ScrumBoard2

        img_boton = tk.PhotoImage(
            file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Scrum/log_out.png")
        boton = ttk.Button(self.master, image=img_boton, command=cerrarr)
        boton.place(x=271, y=650)
        boton.image = img_boton

        boton = ttk.Button(self.master, text = 'Crear un Proyecto', command=ir_CreaHistoria)
        boton.place(x=1000, y=550)

        
        


class ScrumBoard ():
    a = selecproyecto
    

    def __init__(self, master):

        self.master = master
        self.master.title("Scrum Board Proyectos")
        self.master.config(bg="#D9D9D9")

        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- HEADER ------------- #

        headerframe = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#f2cb00', width=w+60, height=70)
        titleframe = tk.Frame(headerframe, bg='#f2cb00', padx=1, pady=1)
        title_label = tk.Label(titleframe, text='VJ Scrum', padx=15, pady=5,
                               bg='#f2cb00', fg='black', font=('Italiana', 24), width=8)

        headerframe.pack()
        titleframe.pack()
        title_label.pack()

        titleframe.place(y=32, relx=0.5, anchor=CENTER)

        # ----------- END HEADER ------------- #

        # ----------------- Funciones de Movimiento ---------------- #

        def cerrar():
            self.master.destroy()

        def ir_Inicio():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Inicio(scrumwindow)

        def ir_Done():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Done(scrumwindow)

        def ir_ToDo():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ToDo(scrumwindow)

        def ir_Progress():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = InProgress(scrumwindow)

        def ir_NuevoProyecto ():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Crear_Proyecto(scrumwindow)

        # ----------------- Funciones de Movimiento end ---------------- #

        # ----------------- CAJA LATERAL ---------------- #

        cajalateral = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#F2CB00', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Inicio', padx=15, pady=5, bg=gris, fg='black', font=(
            'Italiana', 18, 'italic'), height=1, )  # command = mainform1)
        titulo1_label['command'] = ir_Inicio

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='In Progress', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command = Ir_Progress)
        titulo2_label['command'] = ir_Progress

        titulo3 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo3_label = tk.Button(titulo3, text='To Do', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command = Ir_ToDo)
        titulo3_label['command'] = ir_ToDo

        titulo4 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo4_label = tk.Button(titulo4, text='Done', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command = Ir_Done)
        titulo4_label['command'] = ir_Done

        cajalateral.pack(side=LEFT)
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

        img_boton = tk.PhotoImage(
            file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Scrum/log_out.png")
        boton = ttk.Button(self.master, image=img_boton, command=cerrar)
        boton.place(x=271, y=650)
        boton.image = img_boton

        # -----------------------FIN DE LA BARRA LATERAL ----------------------- #

        sql_select_query3 = "select document from usuarios where username = %s"
        c.execute(sql_select_query3, (username2,))
        record = c.fetchone()
        doc2 = record
        print(doc2)

        dar_projectid = "select proyid from proyectos where document = %s"
        c.execute(dar_projectid, (doc2,))
        suprojid = c.fetchall()

        if (c.rowcount == 0):
            ir_NuevoProyecto()
        #if (selecproyecto == 1):
        #    proyectidd = suprojid[0]
        #elif (selecproyecto == 2):
        #    proyectidd = suprojid[1]
        #else:
        #    proyectidd = suprojid[0]
        proyectidd = suprojid [0]

        #print('El proyect Id es: ', proyectidd)

        ver_estado = "select historias from progreso where estado = %s and proyid = %s"
        c.execute(ver_estado, ('0', proyectidd,))
        ToDos = c.fetchall()
        #print('Los To do: ', ToDos)

        ver_estado2 = "select historias from progreso where estado = %s and proyid = %s"
        c.execute(ver_estado2, ('1', proyectidd,))
        InProgresses = c.fetchall()
        print('Los In Progress: ', InProgresses)

        ver_estado3 = "select historias from progreso where estado = %s and proyid = %s"
        c.execute(ver_estado3, ('2', proyectidd,))
        Dones = c.fetchall()
        #print('Los Done: ', Dones)

        label1 = tk.Label(self.master, text="To Do",
                          font=('Italiana', 24), bg="#ffe291")
        label1.place(y=100, x=440, anchor=CENTER)
        label11 = tk.Label(self.master,  font=('Italiana', 24),
                           bg="#D9D9D9", height=14, width=10)
        label11.place(y=400, x=440, anchor=CENTER)
        label12 = tk.Button(self.master, text="Ir a To Do",
                            font=('Italiana', 15), bg="#ffe291")
        label12.place(y=620, x=440, anchor=CENTER)
        label12['command'] = ir_ToDo
        label13 = tk.Label(self.master, text='\n•'.join(''.join(map(str, tup)) for tup in ToDos),
                           font=('Italiana', 15), bg=gris, width=21, wraplength=220, height=19, anchor='n')  # width= 20, anchor= 'n', justify = LEFT,  wraplength=900 )
        label13.place(y=370, x=440, anchor=CENTER)

        label2 = tk.Label(self.master, text="In Progress",
                          font=('Italiana', 24), bg="#ffe291")
        label2.place(y=100, x=800, anchor=CENTER)
        label21 = tk.Label(self.master,  font=('Italiana', 24),
                           bg="#D9D9D9", height=14, width=10)
        label21.place(y=400, x=800, anchor=CENTER)
        label22 = tk.Button(self.master, text="Ir a In Progress",
                            font=('Italiana', 15), bg="#ffe291")
        label22.place(y=620, x=800, anchor=CENTER)
        label22['command'] = ir_Progress
        label23 = tk.Label(self.master, text='\n•'.join(''.join(map(str, tup)) for tup in InProgresses),
                           font=('Italiana', 15), bg="#D9D9D9", width=21, wraplength=220, height=19, anchor='n')
        label23.place(y=370, x=800, anchor=CENTER)

        label3 = tk.Label(self.master, text="Done",
                          font=('Italiana', 24), bg="#ffe291")
        label3.place(y=100, x=1170, anchor=CENTER)
        label31 = tk.Label(self.master,  font=('Italiana', 24),
                           bg="#D9D9D9", height=14, width=10)
        label31.place(y=400, x=1170, anchor=CENTER)
        label32 = tk.Button(self.master, text="Ir a Done",
                            font=('Italiana', 15), bg="#ffe291")
        label32.place(y=620, x=1175, anchor=CENTER)
        label32['command'] = ir_Done
        label33 = tk.Label(self.master, text='\n•'.join(''.join(map(str, tup)) for tup in Dones),
                           font=('Italiana', 15), bg="#D9D9D9", width=21, wraplength=220, height=19, anchor='n')
        label33.place(y=370, x=1175, anchor=CENTER)


class ToDo():
    def __init__(self, master):

        self.master = master
        self.master.title("Scrum To Do")
        self.master.config(bg="#D9D9D9")

        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- HEADER ------------- #

        headerframe = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#f2cb00', width=w+60, height=70)
        titleframe = tk.Frame(headerframe, bg='#f2cb00', padx=1, pady=1)
        title_label = tk.Label(titleframe, text='VJ Scrum', padx=15, pady=5,
                               bg='#f2cb00', fg='black', font=('Italiana', 24), width=8)

        headerframe.pack()
        titleframe.pack()
        title_label.pack()

        titleframe.place(y=32, relx=0.5, anchor=CENTER)

        # ----------- END HEADER ------------- #


        

        # ----------------- Funciones de Movimiento ---------------- #

        def cerrar():
            self.master.destroy()

        def ir_Inicio():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Inicio(scrumwindow)

        def ir_Done():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Done(scrumwindow)

        def ir_ToDo():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ToDo(scrumwindow)

        def ir_Progress():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = InProgress(scrumwindow)

        def ir_ScrumBoard():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ScrumBoard(scrumwindow)

        def ir_CreaHistoria ():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Crear_Proyecto(scrumwindow)

        def ir_NuevoProyecto ():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Crear_Proyecto(scrumwindow)
        

        # ----------------- Funciones de Movimiento end ---------------- #

        sql_select_query3 = "select document from usuarios where username = %s"
        c.execute(sql_select_query3, (username2,))
        record = c.fetchone()
        doc2 = record
        print('documento del ususario: ', doc2)

        dar_projectid = "select proyid from proyectos where document = %s"
        c.execute(dar_projectid, (doc2,))
        suprojid = c.fetchone()
        proyectidd = suprojid
        print('El proyect Id es: ', proyectidd)

        ver_estado = "select historias from progreso where estado = %s and proyid = %s"
        c.execute(ver_estado, ('0', suprojid,))
        ToDos = c.fetchall()
        print('Los To do: ', ToDos)



        # ----------------- CAJA LATERAL ---------------- #

        cajalateral = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#F2CB00', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Inicio', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # command = mainform1)
        titulo1_label['command'] = ir_Inicio

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='Scrum Board', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command = Ir_Progress)
        titulo2_label['command'] = ir_ScrumBoard

        titulo3 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo3_label = tk.Button(titulo3, text='In Progress', padx=15, pady=5,
                                  bg='#D9D9D9', fg='black', font=('Italiana', 18, 'italic'), height=1)
        titulo3_label['command'] = ir_Progress

        titulo4 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo4_label = tk.Button(titulo4, text='Done', padx=15, pady=5,
                                  bg='#D9D9D9', fg='black', font=('Italiana', 18, 'italic'), height=1)
        titulo4_label['command'] = ir_Done

        cajalateral.pack(side=LEFT)
        cajalateral.config(cursor='heart')
        titulo1.pack()
        titulo1_label.pack()
        titulo1.place(y=30, x=100)

        titulo2.pack()
        titulo2_label.pack()
        titulo2.place(y=190, relx=0.2)

        titulo3.pack()
        titulo3_label.pack()
        titulo3.place(y=340, x=65)

        titulo4.pack()
        titulo4_label.pack()
        titulo4.place(y=500, x=92)

        img_boton = tk.PhotoImage(
            file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Scrum/log_out.png")
        boton = ttk.Button(self.master, image=img_boton, command=cerrar)
        boton.place(x=271, y=650)
        boton.image = img_boton

        # -----------------------FIN DE LA BARRA LATERAL ----------------------- #

        

        if (c.rowcount == 0):
            ir_NuevoProyecto()

        def show_selection():
        # Obtener la opción seleccionada.
            seleccion = cajita.get()
            #print('la variable de seleccion es:', type(seleccion))
            messagebox.showinfo(
                message=f"La opción seleccionada es: {seleccion}",
                title="Selección" )
            seleccion_modificada2 = seleccion.replace ('{','')
            seleccion_modificada3 = seleccion_modificada2.replace ('}','')
            datos = (seleccion_modificada3, proyectidd)
            actualiza_Progress = "UPDATE progreso SET  estado = '1' WHERE historias= %s and proyid=%s"
            print('soy los datos = ', datos)
            c.execute (actualiza_Progress, (seleccion_modificada3, proyectidd),) 
            connection.commit()
            

        cajita = ttk.Combobox(self.master, state="readonly", width=70,  font=('verdana', 13),
                              values=ToDos
                              )
        cajita.place(x=350, y=550)
        cajita.set("Seleccione la historia de Usuario")
        
        botonactualizar = tk.Button (self.master, width = 20, text = 'Actualizar',  font=('Italiana', 13), command=show_selection)
        botonactualizar.place (x = 1155, y = 545)

        lblpresent = tk.Label(self.master, text='Lista de tareas a realizar', font=(
            'verdana', 17, 'italic', 'bold'), fg='#2A2C2B', bg=bgcolor)
        lblpresent.place(y=107, x=480, anchor=CENTER)

        lbl = tk.Label(self.master, text='\n'.join(''.join(map(str, tup)) for tup in ToDos), font=(
            'verdana', 17, 'italic', 'bold'), fg='#2A2C2B', bg=gris, width=56, anchor='w', justify=LEFT,  wraplength=900)
        lbl.place(y=160, x=355)  # , anchor='e')

        boton = ttk.Button(self.master, text = 'Crear una Historia de Usuario', command=ir_CreaHistoria)
        boton.place(x=690, y=630)

        

        # blanca = tk.Frame(self.master, width=900,
        #                  height=450).place(x=360, y=170)


class InProgress():
    def __init__(self, master):

        self.master = master
        self.master.title("Scrum In Progress")
        self.master.config(bg="#D9D9D9")

        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- HEADER ------------- #

        headerframe = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#f2cb00', width=w+60, height=70)
        titleframe = tk.Frame(headerframe, bg='#f2cb00', padx=1, pady=1)
        title_label = tk.Label(titleframe, text='VJ Scrum', padx=15, pady=5,
                               bg='#f2cb00', fg='black', font=('Italiana', 24), width=8)

        headerframe.pack()
        titleframe.pack()
        title_label.pack()

        titleframe.place(y=32, relx=0.5, anchor=CENTER)

        # ----------- END HEADER ------------- #

        # ---------------- FUNCIONES DE DESPLAZAMIENTO ---------------- #

        def cerrar():
            self.master.destroy()

        def ir_Inicio():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Inicio(scrumwindow)

        def ir_Done():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Done(scrumwindow)

        def ir_ToDo():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ToDo(scrumwindow)

        def ir_ScrumBoard():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ScrumBoard(scrumwindow)

        def ir_NuevoProyecto ():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Crear_Proyecto(scrumwindow)

        # ----------------- CAJA LATERAL ---------------- #

        cajalateral = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#F2CB00', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Inicio', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command = Ir_Inicio)
        titulo1_label['command'] = ir_Inicio

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='Scrum Board', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command = Ir_Scrum)
        titulo2_label['command'] = ir_ScrumBoard

        titulo3 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo3_label = tk.Button(titulo3, text='To Do', padx=15, pady=5,
                                  bg='#D9D9D9', fg='black', font=('Italiana', 18, 'italic'), height=1)
        titulo3_label['command'] = ir_ToDo

        titulo4 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo4_label = tk.Button(titulo4, text='Done', padx=15, pady=5,
                                  bg='#D9D9D9', fg='black', font=('Italiana', 18, 'italic'), height=1)
        titulo4_label['command'] = ir_Done

        cajalateral.pack(side=LEFT)
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

        img_boton = tk.PhotoImage(
            file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Scrum/log_out.png")
        boton = ttk.Button(self.master, image=img_boton, command=cerrar)
        boton.place(x=271, y=650)
        boton.image = img_boton

        # -----------------------FIN DE LA BARRA LATERAL ----------------------- #

        sql_select_query3 = "select document from usuarios where username = %s"
        c.execute(sql_select_query3, (username2,))
        record = c.fetchone()
        doc2 = record

        dar_projectid = "select proyid from proyectos where document = %s"
        c.execute(dar_projectid, (doc2,))
        suprojid = c.fetchone()
        proyectidd = suprojid
        
        ver_estado = "select historias from progreso where estado = %s and proyid = %s"
        c.execute(ver_estado, ('1', suprojid,))
        InProgresses = c.fetchall()
        print('Los In Progress: ', InProgresses)

        def ir_NuevoProyecto ():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Crear_Proyecto(scrumwindow)

        def show_selection():
            seleccion = cajita.get()
            seleccion_modificada2 = seleccion.replace ('{','')
            seleccion_modificada3 = seleccion_modificada2.replace ('}','')
            datos = (seleccion_modificada3, proyectidd)
            actualiza_Progress = "UPDATE progreso SET  estado = '2' WHERE historias= %s and proyid=%s"
            print('soy los datos = ', datos)
            c.execute (actualiza_Progress, (seleccion_modificada3, proyectidd),) 
            connection.commit()

        cajita = ttk.Combobox(self.master, state="readonly", width=70,  font=('verdana', 13),
                              values=InProgresses
                              )
        botonactualizar = tk.Button (self.master, width = 20, text = 'Actualizar',  font=('Italiana', 13),command = show_selection)
        botonactualizar.place (x = 1200, y = 550)

        cajita.place(x=350, y=550)
        cajita.set("Seleccione la historia de Usuario")


        lbl = tk.Label(self.master, text='Lista de tareas que están siendo realizadas:', font=(
            'verdana', 17, 'italic', 'bold'), fg='#2A2C2B', bg="#D9D9D9")
        lbl.place(y=107, x=600, anchor=CENTER)

        lbltareas = tk.Label(self.master, text='\n'.join(''.join(map(str, tup)) for tup in InProgresses), font=(
            'verdana', 17, 'italic', 'bold'), fg='#2A2C2B', bg=gris, width=56, anchor='w', justify=LEFT,  wraplength=900)
        lbltareas.place(y=160, x=355)

        

        #blanca = tk.Frame(self.master, width=900,
        #                  height=450).place(x=360, y=170)


class Done():

    def __init__(self, master):

        self.master = master
        self.master.title("Scrum Done")
        self.master.config(bg="#D9D9D9")

        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- HEADER ------------- #

        headerframe = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#f2cb00', width=w+60, height=70)
        titleframe = tk.Frame(headerframe, bg='#f2cb00', padx=1, pady=1)
        title_label = tk.Label(titleframe, text='VJ Scrum', padx=15, pady=5,
                               bg='#f2cb00', fg='black', font=('Italiana', 24), width=8)

        headerframe.pack()
        titleframe.pack()
        title_label.pack()

        titleframe.place(y=32, relx=0.5, anchor=CENTER)

        # ----------- END HEADER ------------- #

        # ----------------- Funciones de Moviemiento ---------------- #

        def cerrar():
            self.master.destroy()

        def ir_Inicio():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Inicio(scrumwindow)

        def ir_ToDo():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ToDo(scrumwindow)

        def ir_Progress():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = InProgress(scrumwindow)

        def ir_ScrumBoard():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ScrumBoard(scrumwindow)
        
        def ir_NuevoProyecto ():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Crear_Proyecto(scrumwindow)

        # ----------------- Funciones de Moviemiento end ---------------- #

        # ----------------- CAJA LATERAL ---------------- #

        cajalateral = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#F2CB00', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Inicio', padx=15, pady=5,
                                  bg='#D9D9D9', fg='black', font=('Italiana', 18, 'italic'), height=1)
        titulo1_label['command'] = ir_Inicio

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='Scrum Board', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command = Ir_Progress)
        titulo2_label['command'] = ir_ScrumBoard

        titulo3 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo3_label = tk.Button(titulo3, text='In Progress', padx=15, pady=5,
                                  bg='#D9D9D9', fg='black', font=('Italiana', 18, 'italic'), height=1)
        titulo3_label['command'] = ir_Progress

        titulo4 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo4_label = tk.Button(titulo4, text='To Do', padx=15, pady=5,
                                  bg='#D9D9D9', fg='black', font=('Italiana', 18, 'italic'), height=1)
        titulo4_label['command'] = ir_ToDo

        cajalateral.pack(side=LEFT)
        cajalateral.config(cursor='heart')
        titulo1.pack()
        titulo1_label.pack()
        titulo1.place(y=30, x=92)

        titulo2.pack()
        titulo2_label.pack()
        titulo2.place(y=190, relx=0.2)

        titulo3.pack()
        titulo3_label.pack()
        titulo3.place(y=340, x=65)

        titulo4.pack()
        titulo4_label.pack()
        titulo4.place(y=500, x=92)

        img_boton = tk.PhotoImage(
            file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Scrum/log_out.png")
        boton = ttk.Button(self.master, image=img_boton, command=cerrar)
        boton.place(x=271, y=650)
        boton.image = img_boton

        # -----------------------FIN DE LA BARRA LATERAL ----------------------- #

        sql_select_query3 = "select document from usuarios where username = %s"
        c.execute(sql_select_query3, (username2,))
        record = c.fetchone()
        doc2 = record
        print('documento del ususario: ', doc2)

        dar_projectid = "select proyid from proyectos where document = %s"
        c.execute(dar_projectid, (doc2,))
        suprojid = c.fetchone()
        proyectidd = suprojid
        print('El proyect Id es: ', proyectidd)

        ver_estado = "select historias from progreso where estado = %s and proyid = %s"
        c.execute(ver_estado, ('2', suprojid,))
        Dones = c.fetchall()
        print('Los Done: ', Dones)

        def ir_NuevoProyecto ():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Crear_Proyecto(scrumwindow)

        lbltareas = tk.Label(self.master, text='\n'.join(''.join(map(str, tup)) for tup in Dones), font=(
            'verdana', 17, 'italic', 'bold'), fg='#2A2C2B', bg=gris, width=56, anchor='w', justify=LEFT,  wraplength=900)
        lbltareas.place(y=160, x=355)


        lbl = tk.Label(self.master, text='Lista de tareas Completadas:', font=(
            'verdana', 17, 'italic', 'bold'), fg='#2A2C2B', bg="#D9D9D9")
        lbl.place(y=107, x=505, anchor=CENTER)

        #blanca = tk.Frame(self.master, width=900,
        #                  height=450).place(x=360, y=170)

class Crear_Proyecto():
    def __init__(self, master):

        self.master = master
        self.master.title("Scrum To Do")
        self.master.config(bg="#D9D9D9")

        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- HEADER ------------- #

        headerframe = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#f2cb00', width=w+60, height=70)
        titleframe = tk.Frame(headerframe, bg='#f2cb00', padx=1, pady=1)
        title_label = tk.Label(titleframe, text='VJ Scrum', padx=15, pady=5,
                               bg='#f2cb00', fg='black', font=('Italiana', 24), width=8)

        headerframe.pack()
        titleframe.pack()
        title_label.pack()

        titleframe.place(y=32, relx=0.5, anchor=CENTER)

        # ----------- END HEADER ------------- #

        # ----------------- Funciones de Movimiento ---------------- #

        def cerrar():
            self.master.destroy()

        def ir_Inicio():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Inicio(scrumwindow)

        def ir_Done():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Done(scrumwindow)

        def ir_ToDo():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ToDo(scrumwindow)

        def ir_Progress():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = InProgress(scrumwindow)

        def ir_ScrumBoard():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ScrumBoard(scrumwindow)
        

        # ----------------- Funciones de Movimiento end ---------------- #

        # ----------------- CAJA LATERAL ---------------- #

        cajalateral = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#F2CB00', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Inicio', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # command = mainform1)
        titulo1_label['command'] = ir_Inicio

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='Scrum Board', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command = Ir_Progress)
        titulo2_label['command'] = ir_ScrumBoard

        titulo3 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo3_label = tk.Button(titulo3, text='In Progress', padx=15, pady=5,
                                  bg='#D9D9D9', fg='black', font=('Italiana', 18, 'italic'), height=1)
        titulo3_label['command'] = ir_Progress

        titulo4 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo4_label = tk.Button(titulo4, text='Done', padx=15, pady=5,
                                  bg='#D9D9D9', fg='black', font=('Italiana', 18, 'italic'), height=1)
        titulo4_label['command'] = ir_Done

        cajalateral.pack(side=LEFT)
        cajalateral.config(cursor='heart')
        titulo1.pack()
        titulo1_label.pack()
        titulo1.place(y=30, x=100)

        titulo2.pack()
        titulo2_label.pack()
        titulo2.place(y=190, relx=0.2)

        titulo3.pack()
        titulo3_label.pack()
        titulo3.place(y=340, x=65)

        titulo4.pack()
        titulo4_label.pack()
        titulo4.place(y=500, x=92)

        img_boton = tk.PhotoImage(
            file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Scrum/log_out.png")
        boton = ttk.Button(self.master, image=img_boton, command=cerrar)
        boton.place(x=271, y=650)
        boton.image = img_boton

        # -----------------------FIN DE LA BARRA LATERAL ----------------------- #

        def getText():
            historiaa=textou.get("1.0","end")
            proyidusuario = darlelproyid.get("1.0","2.0")
            proyidusuario = proyidusuario.replace('\n', '')
            proyidusuario = int(proyidusuario)
            datos = (doc2, historiaa, proyidusuario)
            print ('valor solo de la historia: ', historiaa)
            print ('valor de los datos: ', datos)
            insert_query = "INSERT INTO proyectos(document,proyect,proyid) VALUES (%s,%s,%s)"
            c.execute(insert_query, datos)
            connection.commit()

        sql_select_query3 = "select document from usuarios where username = %s"
        c.execute(sql_select_query3, (username2,))
        record = c.fetchone()
        doc2 = record
        print('documento del ususario: ', doc2)

        dar_projectid = "select proyid from proyectos where document = %s"
        c.execute(dar_projectid, (doc2,))
        suprojid = c.fetchone()
        proyectidd = suprojid
        print('El proyect Id es: ', proyectidd)

        ver_estado = "select historias from progreso where estado = %s and proyid = %s"
        c.execute(ver_estado, ('0', suprojid,))
        ToDos = c.fetchall()
        print('Los To do: ', ToDos)

        labelcrear = tk.Label (self.master, text = 'Página de creación de Proyectos' , font= ('verdana', 17, 'italic', 'bold'), bg = gris)
        labelcrear.place (y=107, x=530, anchor=CENTER)

        textou = tk.Text (self.master, bd = 10, font = ('Verdana', 14), height = 10, relief = GROOVE, width= 75)
        textou. place (y=300, x=810, anchor=CENTER)

        labeldarproyid = tk.Label (self.master, text = 'Da el Proyect ID' , font= ('verdana', 12, 'italic', 'bold'), bg = gris)
        labeldarproyid.place (y=462, x=440, anchor = CENTER)
        darlelproyid = tk.Text (self.master,font = ('Verdana', 14), height = 1, relief = GROOVE, width= 2)
        darlelproyid.place (x = 520, y = 450)

        botonaniadir = tk.Button (self.master, text= 'Crear Proyecto', font= ('verdana', 12, 'italic'), command =getText)
        botonaniadir.place (y=550, x=800, anchor=CENTER)


class nueva_Historia():
    def __init__(self, master):

        self.master = master
        self.master.title("Scrum To Do")
        self.master.config(bg="#D9D9D9")
        historiaa = 'a'

        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- HEADER ------------- #

        headerframe = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#f2cb00', width=w+60, height=70)
        titleframe = tk.Frame(headerframe, bg='#f2cb00', padx=1, pady=1)
        title_label = tk.Label(titleframe, text='VJ Scrum', padx=15, pady=5,
                               bg='#f2cb00', fg='black', font=('Italiana', 24), width=8)

        headerframe.pack()
        titleframe.pack()
        title_label.pack()

        titleframe.place(y=32, relx=0.5, anchor=CENTER)

        # ----------- END HEADER ------------- #

        # ----------------- Funciones de Movimiento ---------------- #

        def cerrar():
            self.master.destroy()

        def ir_Inicio():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Inicio(scrumwindow)

        def ir_Done():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Done(scrumwindow)

        def ir_ToDo():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ToDo(scrumwindow)

        def ir_Progress():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = InProgress(scrumwindow)

        def ir_ScrumBoard():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ScrumBoard(scrumwindow)

        # ----------------- Funciones de Movimiento end ---------------- #

        # ----------------- CAJA LATERAL ---------------- #

        cajalateral = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#F2CB00', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Inicio', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # command = mainform1)
        titulo1_label['command'] = ir_Inicio

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='Scrum Board', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command = Ir_Progress)
        titulo2_label['command'] = ir_ScrumBoard

        titulo3 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo3_label = tk.Button(titulo3, text='In Progress', padx=15, pady=5,
                                  bg='#D9D9D9', fg='black', font=('Italiana', 18, 'italic'), height=1)
        titulo3_label['command'] = ir_Progress

        titulo4 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo4_label = tk.Button(titulo4, text='Done', padx=15, pady=5,
                                  bg='#D9D9D9', fg='black', font=('Italiana', 18, 'italic'), height=1)
        titulo4_label['command'] = ir_Done

        cajalateral.pack(side=LEFT)
        cajalateral.config(cursor='heart')
        titulo1.pack()
        titulo1_label.pack()
        titulo1.place(y=30, x=100)

        titulo2.pack()
        titulo2_label.pack()
        titulo2.place(y=190, relx=0.2)

        titulo3.pack()
        titulo3_label.pack()
        titulo3.place(y=340, x=65)

        titulo4.pack()
        titulo4_label.pack()
        titulo4.place(y=500, x=92)

        img_boton = tk.PhotoImage(
            file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Scrum/log_out.png")
        boton = ttk.Button(self.master, image=img_boton, command=cerrar)
        boton.place(x=271, y=650)
        boton.image = img_boton

        # -----------------------FIN DE LA BARRA LATERAL ----------------------- #

        def getText():
            historiaa=textou.get("1.0","end")
            datos = (proyectidd, historiaa, '0')
            print ('valor solo de la historia: ', historiaa)
            print ('valor de los datos: ', datos)
            insert_query = "INSERT INTO progreso(proyid,historias,estado) VALUES (%s,%s,%s)"
            c.execute(insert_query, datos)
            connection.commit()
        

        labelcrear = tk.Label (self.master, text = 'Página para añadir Historias de Usuario' , font= ('verdana', 17, 'italic', 'bold'), bg = gris)
        labelcrear.place (y=107, x=565, anchor=CENTER)

        textou = tk.Text (self.master, bd = 10, font = ('Verdana', 14), height = 10, relief = GROOVE, width= 75)
        textou. place (y=300, x=810, anchor=CENTER)

        botonaniadir = tk.Button (self.master, text= 'Añadir Historia de Usuario', font= ('verdana', 12, 'italic'), command=getText)
        botonaniadir.place (y=550, x=800, anchor=CENTER)

        sql_select_query3 = "select document from usuarios where username = %s"
        c.execute(sql_select_query3, (username2,))
        record = c.fetchone()
        doc2 = record
        print('documento del ususario: ', doc2)

        dar_projectid = "select proyid from proyectos where document = %s"
        c.execute(dar_projectid, (doc2,))
        suprojid = c.fetchone()
        proyectidd = suprojid
        print('El proyect Id es: ', proyectidd)

        ver_estado = "select historias from progreso where estado = %s and proyid = %s"
        c.execute(ver_estado, ('0', suprojid,))
        ToDos = c.fetchall()
        print('Los To do: ', ToDos)

        
        
        
        #insert_query = "INSERT INTO progreso(proyid,historias,estado) VALUES (%s,%s,%s)"
        #c.execute(insert_query, vals)
        #connection.commit()



# ----------------------------------------------------------------------------------------------------------------------------------------------------
class ScrumBoard2 ():
    a = selecproyecto
    

    def __init__(self, master):

        self.master = master
        self.master.title("Scrum Board Proyectos")
        self.master.config(bg="#D9D9D9")

        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- HEADER ------------- #

        headerframe = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#f2cb00', width=w+60, height=70)
        titleframe = tk.Frame(headerframe, bg='#f2cb00', padx=1, pady=1)
        title_label = tk.Label(titleframe, text='VJ Scrum', padx=15, pady=5,
                               bg='#f2cb00', fg='black', font=('Italiana', 24), width=8)

        headerframe.pack()
        titleframe.pack()
        title_label.pack()

        titleframe.place(y=32, relx=0.5, anchor=CENTER)

        # ----------- END HEADER ------------- #

        # ----------------- Funciones de Movimiento ---------------- #

        def cerrar():
            self.master.destroy()

        def ir_Inicio():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Inicio(scrumwindow)

        def ir_Done():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Done(scrumwindow)

        def ir_ToDo():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ToDo(scrumwindow)

        def ir_Progress():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = InProgress(scrumwindow)

        def ir_NuevoProyecto ():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Crear_Proyecto(scrumwindow)

        # ----------------- Funciones de Movimiento end ---------------- #

        # ----------------- CAJA LATERAL ---------------- #

        cajalateral = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#F2CB00', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Inicio', padx=15, pady=5, bg=gris, fg='black', font=(
            'Italiana', 18, 'italic'), height=1, )  # command = mainform1)
        titulo1_label['command'] = ir_Inicio

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='In Progress', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command = Ir_Progress)
        titulo2_label['command'] = ir_Progress

        titulo3 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo3_label = tk.Button(titulo3, text='To Do', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command = Ir_ToDo)
        titulo3_label['command'] = ir_ToDo

        titulo4 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo4_label = tk.Button(titulo4, text='Done', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command = Ir_Done)
        titulo4_label['command'] = ir_Done

        cajalateral.pack(side=LEFT)
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

        img_boton = tk.PhotoImage(
            file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Scrum/log_out.png")
        boton = ttk.Button(self.master, image=img_boton, command=cerrar)
        boton.place(x=271, y=650)
        boton.image = img_boton

        # -----------------------FIN DE LA BARRA LATERAL ----------------------- #

        sql_select_query3 = "select document from usuarios where username = %s"
        c.execute(sql_select_query3, (username2,))
        record = c.fetchone()
        doc2 = record
        print(doc2)

        dar_projectid = "select proyid from proyectos where document = %s"
        c.execute(dar_projectid, (doc2,))
        suprojid = c.fetchall()

        if (c.rowcount == 0):
            ir_NuevoProyecto()
        #if (selecproyecto == 1):
        #    proyectidd = suprojid[0]
        #elif (selecproyecto == 2):
        #    proyectidd = suprojid[1]
        #else:
        #    proyectidd = suprojid[0]
        proyectidd = suprojid [0]

        #print('El proyect Id es: ', proyectidd)

        ver_estado = "select historias from progreso where estado = %s and proyid = %s"
        c.execute(ver_estado, ('0', proyectidd,))
        ToDos = c.fetchall()
        #print('Los To do: ', ToDos)

        ver_estado2 = "select historias from progreso where estado = %s and proyid = %s"
        c.execute(ver_estado2, ('1', proyectidd,))
        InProgresses = c.fetchall()
        print('Los In Progress: ', InProgresses)

        ver_estado3 = "select historias from progreso where estado = %s and proyid = %s"
        c.execute(ver_estado3, ('2', proyectidd,))
        Dones = c.fetchall()
        #print('Los Done: ', Dones)

        label1 = tk.Label(self.master, text="To Do",
                          font=('Italiana', 24), bg="#ffe291")
        label1.place(y=100, x=440, anchor=CENTER)
        label11 = tk.Label(self.master,  font=('Italiana', 24),
                           bg="#D9D9D9", height=14, width=10)
        label11.place(y=400, x=440, anchor=CENTER)
        label12 = tk.Button(self.master, text="Ir a To Do",
                            font=('Italiana', 15), bg="#ffe291")
        label12.place(y=620, x=440, anchor=CENTER)
        label12['command'] = ir_ToDo
        label13 = tk.Label(self.master, text='\n•'.join(''.join(map(str, tup)) for tup in ToDos),
                           font=('Italiana', 15), bg=gris, width=21, wraplength=220, height=19, anchor='n')  # width= 20, anchor= 'n', justify = LEFT,  wraplength=900 )
        label13.place(y=370, x=440, anchor=CENTER)

        label2 = tk.Label(self.master, text="In Progress",
                          font=('Italiana', 24), bg="#ffe291")
        label2.place(y=100, x=800, anchor=CENTER)
        label21 = tk.Label(self.master,  font=('Italiana', 24),
                           bg="#D9D9D9", height=14, width=10)
        label21.place(y=400, x=800, anchor=CENTER)
        label22 = tk.Button(self.master, text="Ir a In Progress",
                            font=('Italiana', 15), bg="#ffe291")
        label22.place(y=620, x=800, anchor=CENTER)
        label22['command'] = ir_Progress
        label23 = tk.Label(self.master, text='\n•'.join(''.join(map(str, tup)) for tup in InProgresses),
                           font=('Italiana', 15), bg="#D9D9D9", width=21, wraplength=220, height=19, anchor='n')
        label23.place(y=370, x=800, anchor=CENTER)

        label3 = tk.Label(self.master, text="Done",
                          font=('Italiana', 24), bg="#ffe291")
        label3.place(y=100, x=1170, anchor=CENTER)
        label31 = tk.Label(self.master,  font=('Italiana', 24),
                           bg="#D9D9D9", height=14, width=10)
        label31.place(y=400, x=1170, anchor=CENTER)
        label32 = tk.Button(self.master, text="Ir a Done",
                            font=('Italiana', 15), bg="#ffe291")
        label32.place(y=620, x=1175, anchor=CENTER)
        label32['command'] = ir_Done
        label33 = tk.Label(self.master, text='\n•'.join(''.join(map(str, tup)) for tup in Dones),
                           font=('Italiana', 15), bg="#D9D9D9", width=21, wraplength=220, height=19, anchor='n')
        label33.place(y=370, x=1175, anchor=CENTER)


class ToDo2():
    def __init__(self, master):

        self.master = master
        self.master.title("Scrum To Do")
        self.master.config(bg="#D9D9D9")

        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- HEADER ------------- #

        headerframe = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#f2cb00', width=w+60, height=70)
        titleframe = tk.Frame(headerframe, bg='#f2cb00', padx=1, pady=1)
        title_label = tk.Label(titleframe, text='VJ Scrum', padx=15, pady=5,
                               bg='#f2cb00', fg='black', font=('Italiana', 24), width=8)

        headerframe.pack()
        titleframe.pack()
        title_label.pack()

        titleframe.place(y=32, relx=0.5, anchor=CENTER)

        # ----------- END HEADER ------------- #


        

        # ----------------- Funciones de Movimiento ---------------- #

        def cerrar():
            self.master.destroy()

        def ir_Inicio():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Inicio(scrumwindow)

        def ir_Done():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Done(scrumwindow)

        def ir_ToDo():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ToDo(scrumwindow)

        def ir_Progress():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = InProgress(scrumwindow)

        def ir_ScrumBoard():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ScrumBoard(scrumwindow)

        def ir_CreaHistoria ():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Crear_Proyecto(scrumwindow)

        def ir_NuevoProyecto ():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Crear_Proyecto(scrumwindow)
        

        # ----------------- Funciones de Movimiento end ---------------- #

        sql_select_query3 = "select document from usuarios where username = %s"
        c.execute(sql_select_query3, (username2,))
        record = c.fetchone()
        doc2 = record
        print('documento del ususario: ', doc2)

        dar_projectid = "select proyid from proyectos where document = %s"
        c.execute(dar_projectid, (doc2,))
        suprojid = c.fetchone()
        proyectidd = suprojid
        print('El proyect Id es: ', proyectidd)

        ver_estado = "select historias from progreso where estado = %s and proyid = %s"
        c.execute(ver_estado, ('0', suprojid,))
        ToDos = c.fetchall()
        print('Los To do: ', ToDos)



        # ----------------- CAJA LATERAL ---------------- #

        cajalateral = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#F2CB00', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Inicio', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # command = mainform1)
        titulo1_label['command'] = ir_Inicio

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='Scrum Board', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command = Ir_Progress)
        titulo2_label['command'] = ir_ScrumBoard

        titulo3 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo3_label = tk.Button(titulo3, text='In Progress', padx=15, pady=5,
                                  bg='#D9D9D9', fg='black', font=('Italiana', 18, 'italic'), height=1)
        titulo3_label['command'] = ir_Progress

        titulo4 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo4_label = tk.Button(titulo4, text='Done', padx=15, pady=5,
                                  bg='#D9D9D9', fg='black', font=('Italiana', 18, 'italic'), height=1)
        titulo4_label['command'] = ir_Done

        cajalateral.pack(side=LEFT)
        cajalateral.config(cursor='heart')
        titulo1.pack()
        titulo1_label.pack()
        titulo1.place(y=30, x=100)

        titulo2.pack()
        titulo2_label.pack()
        titulo2.place(y=190, relx=0.2)

        titulo3.pack()
        titulo3_label.pack()
        titulo3.place(y=340, x=65)

        titulo4.pack()
        titulo4_label.pack()
        titulo4.place(y=500, x=92)

        img_boton = tk.PhotoImage(
            file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Scrum/log_out.png")
        boton = ttk.Button(self.master, image=img_boton, command=cerrar)
        boton.place(x=271, y=650)
        boton.image = img_boton

        # -----------------------FIN DE LA BARRA LATERAL ----------------------- #

        

        if (c.rowcount == 0):
            ir_NuevoProyecto()

        def show_selection():
        # Obtener la opción seleccionada.
            seleccion = cajita.get()
            #print('la variable de seleccion es:', type(seleccion))
            messagebox.showinfo(
                message=f"La opción seleccionada es: {seleccion}",
                title="Selección" )
            seleccion_modificada2 = seleccion.replace ('{','')
            seleccion_modificada3 = seleccion_modificada2.replace ('}','')
            datos = (seleccion_modificada3, proyectidd)
            actualiza_Progress = "UPDATE progreso SET  estado = '1' WHERE historias= %s and proyid=%s"
            print('soy los datos = ', datos)
            c.execute (actualiza_Progress, (seleccion_modificada3, proyectidd),) 
            connection.commit()
            

        cajita = ttk.Combobox(self.master, state="readonly", width=70,  font=('verdana', 13),
                              values=ToDos
                              )
        cajita.place(x=350, y=550)
        cajita.set("Seleccione la historia de Usuario")
        
        botonactualizar = tk.Button (self.master, width = 20, text = 'Actualizar',  font=('Italiana', 13), command=show_selection)
        botonactualizar.place (x = 1155, y = 545)

        lblpresent = tk.Label(self.master, text='Lista de tareas a realizar', font=(
            'verdana', 17, 'italic', 'bold'), fg='#2A2C2B', bg=bgcolor)
        lblpresent.place(y=107, x=480, anchor=CENTER)

        lbl = tk.Label(self.master, text='\n'.join(''.join(map(str, tup)) for tup in ToDos), font=(
            'verdana', 17, 'italic', 'bold'), fg='#2A2C2B', bg=gris, width=56, anchor='w', justify=LEFT,  wraplength=900)
        lbl.place(y=160, x=355)  # , anchor='e')

        boton = ttk.Button(self.master, text = 'Crear una Historia de Usuario', command=ir_CreaHistoria)
        boton.place(x=690, y=630)

        

        # blanca = tk.Frame(self.master, width=900,
        #                  height=450).place(x=360, y=170)


class InProgress2():
    def __init__(self, master):

        self.master = master
        self.master.title("Scrum In Progress")
        self.master.config(bg="#D9D9D9")

        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- HEADER ------------- #

        headerframe = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#f2cb00', width=w+60, height=70)
        titleframe = tk.Frame(headerframe, bg='#f2cb00', padx=1, pady=1)
        title_label = tk.Label(titleframe, text='VJ Scrum', padx=15, pady=5,
                               bg='#f2cb00', fg='black', font=('Italiana', 24), width=8)

        headerframe.pack()
        titleframe.pack()
        title_label.pack()

        titleframe.place(y=32, relx=0.5, anchor=CENTER)

        # ----------- END HEADER ------------- #

        # ---------------- FUNCIONES DE DESPLAZAMIENTO ---------------- #

        def cerrar():
            self.master.destroy()

        def ir_Inicio():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Inicio(scrumwindow)

        def ir_Done():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Done(scrumwindow)

        def ir_ToDo():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ToDo(scrumwindow)

        def ir_ScrumBoard():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ScrumBoard(scrumwindow)

        def ir_NuevoProyecto ():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Crear_Proyecto(scrumwindow)

        # ----------------- CAJA LATERAL ---------------- #

        cajalateral = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#F2CB00', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Inicio', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command = Ir_Inicio)
        titulo1_label['command'] = ir_Inicio

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='Scrum Board', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command = Ir_Scrum)
        titulo2_label['command'] = ir_ScrumBoard

        titulo3 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo3_label = tk.Button(titulo3, text='To Do', padx=15, pady=5,
                                  bg='#D9D9D9', fg='black', font=('Italiana', 18, 'italic'), height=1)
        titulo3_label['command'] = ir_ToDo

        titulo4 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo4_label = tk.Button(titulo4, text='Done', padx=15, pady=5,
                                  bg='#D9D9D9', fg='black', font=('Italiana', 18, 'italic'), height=1)
        titulo4_label['command'] = ir_Done

        cajalateral.pack(side=LEFT)
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

        img_boton = tk.PhotoImage(
            file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Scrum/log_out.png")
        boton = ttk.Button(self.master, image=img_boton, command=cerrar)
        boton.place(x=271, y=650)
        boton.image = img_boton

        # -----------------------FIN DE LA BARRA LATERAL ----------------------- #

        sql_select_query3 = "select document from usuarios where username = %s"
        c.execute(sql_select_query3, (username2,))
        record = c.fetchone()
        doc2 = record

        dar_projectid = "select proyid from proyectos where document = %s"
        c.execute(dar_projectid, (doc2,))
        suprojid = c.fetchone()
        proyectidd = suprojid
        
        ver_estado = "select historias from progreso where estado = %s and proyid = %s"
        c.execute(ver_estado, ('1', suprojid,))
        InProgresses = c.fetchall()
        print('Los In Progress: ', InProgresses)

        def ir_NuevoProyecto ():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Crear_Proyecto(scrumwindow)

        def show_selection():
            seleccion = cajita.get()
            seleccion_modificada2 = seleccion.replace ('{','')
            seleccion_modificada3 = seleccion_modificada2.replace ('}','')
            datos = (seleccion_modificada3, proyectidd)
            actualiza_Progress = "UPDATE progreso SET  estado = '2' WHERE historias= %s and proyid=%s"
            print('soy los datos = ', datos)
            c.execute (actualiza_Progress, (seleccion_modificada3, proyectidd),) 
            connection.commit()

        cajita = ttk.Combobox(self.master, state="readonly", width=70,  font=('verdana', 13),
                              values=InProgresses
                              )
        botonactualizar = tk.Button (self.master, width = 20, text = 'Actualizar',  font=('Italiana', 13),command = show_selection)
        botonactualizar.place (x = 1200, y = 550)

        cajita.place(x=350, y=550)
        cajita.set("Seleccione la historia de Usuario")


        lbl = tk.Label(self.master, text='Lista de tareas que están siendo realizadas:', font=(
            'verdana', 17, 'italic', 'bold'), fg='#2A2C2B', bg="#D9D9D9")
        lbl.place(y=107, x=600, anchor=CENTER)

        lbltareas = tk.Label(self.master, text='\n'.join(''.join(map(str, tup)) for tup in InProgresses), font=(
            'verdana', 17, 'italic', 'bold'), fg='#2A2C2B', bg=gris, width=56, anchor='w', justify=LEFT,  wraplength=900)
        lbltareas.place(y=160, x=355)

        

        #blanca = tk.Frame(self.master, width=900,
        #                  height=450).place(x=360, y=170)


class Done2():

    def __init__(self, master):

        self.master = master
        self.master.title("Scrum Done")
        self.master.config(bg="#D9D9D9")

        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- HEADER ------------- #

        headerframe = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#f2cb00', width=w+60, height=70)
        titleframe = tk.Frame(headerframe, bg='#f2cb00', padx=1, pady=1)
        title_label = tk.Label(titleframe, text='VJ Scrum', padx=15, pady=5,
                               bg='#f2cb00', fg='black', font=('Italiana', 24), width=8)

        headerframe.pack()
        titleframe.pack()
        title_label.pack()

        titleframe.place(y=32, relx=0.5, anchor=CENTER)

        # ----------- END HEADER ------------- #

        # ----------------- Funciones de Moviemiento ---------------- #

        def cerrar():
            self.master.destroy()

        def ir_Inicio():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Inicio(scrumwindow)

        def ir_ToDo():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ToDo(scrumwindow)

        def ir_Progress():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = InProgress(scrumwindow)

        def ir_ScrumBoard():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ScrumBoard(scrumwindow)
        
        def ir_NuevoProyecto ():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Crear_Proyecto(scrumwindow)

        # ----------------- Funciones de Moviemiento end ---------------- #

        # ----------------- CAJA LATERAL ---------------- #

        cajalateral = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#F2CB00', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Inicio', padx=15, pady=5,
                                  bg='#D9D9D9', fg='black', font=('Italiana', 18, 'italic'), height=1)
        titulo1_label['command'] = ir_Inicio

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='Scrum Board', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command = Ir_Progress)
        titulo2_label['command'] = ir_ScrumBoard

        titulo3 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo3_label = tk.Button(titulo3, text='In Progress', padx=15, pady=5,
                                  bg='#D9D9D9', fg='black', font=('Italiana', 18, 'italic'), height=1)
        titulo3_label['command'] = ir_Progress

        titulo4 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo4_label = tk.Button(titulo4, text='To Do', padx=15, pady=5,
                                  bg='#D9D9D9', fg='black', font=('Italiana', 18, 'italic'), height=1)
        titulo4_label['command'] = ir_ToDo

        cajalateral.pack(side=LEFT)
        cajalateral.config(cursor='heart')
        titulo1.pack()
        titulo1_label.pack()
        titulo1.place(y=30, x=92)

        titulo2.pack()
        titulo2_label.pack()
        titulo2.place(y=190, relx=0.2)

        titulo3.pack()
        titulo3_label.pack()
        titulo3.place(y=340, x=65)

        titulo4.pack()
        titulo4_label.pack()
        titulo4.place(y=500, x=92)

        img_boton = tk.PhotoImage(
            file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Scrum/log_out.png")
        boton = ttk.Button(self.master, image=img_boton, command=cerrar)
        boton.place(x=271, y=650)
        boton.image = img_boton

        # -----------------------FIN DE LA BARRA LATERAL ----------------------- #

        sql_select_query3 = "select document from usuarios where username = %s"
        c.execute(sql_select_query3, (username2,))
        record = c.fetchone()
        doc2 = record
        print('documento del ususario: ', doc2)

        dar_projectid = "select proyid from proyectos where document = %s"
        c.execute(dar_projectid, (doc2,))
        suprojid = c.fetchone()
        proyectidd = suprojid
        print('El proyect Id es: ', proyectidd)

        ver_estado = "select historias from progreso where estado = %s and proyid = %s"
        c.execute(ver_estado, ('2', suprojid,))
        Dones = c.fetchall()
        print('Los Done: ', Dones)

        def ir_NuevoProyecto ():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Crear_Proyecto(scrumwindow)

        lbltareas = tk.Label(self.master, text='\n'.join(''.join(map(str, tup)) for tup in Dones), font=(
            'verdana', 17, 'italic', 'bold'), fg='#2A2C2B', bg=gris, width=56, anchor='w', justify=LEFT,  wraplength=900)
        lbltareas.place(y=160, x=355)


        lbl = tk.Label(self.master, text='Lista de tareas Completadas:', font=(
            'verdana', 17, 'italic', 'bold'), fg='#2A2C2B', bg="#D9D9D9")
        lbl.place(y=107, x=505, anchor=CENTER)

        #blanca = tk.Frame(self.master, width=900,
        #                  height=450).place(x=360, y=170)

class nueva_Historia2():
    def __init__(self, master):

        self.master = master
        self.master.title("Scrum To Do")
        self.master.config(bg="#D9D9D9")
        historiaa = 'a'

        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- HEADER ------------- #

        headerframe = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#f2cb00', width=w+60, height=70)
        titleframe = tk.Frame(headerframe, bg='#f2cb00', padx=1, pady=1)
        title_label = tk.Label(titleframe, text='VJ Scrum', padx=15, pady=5,
                               bg='#f2cb00', fg='black', font=('Italiana', 24), width=8)

        headerframe.pack()
        titleframe.pack()
        title_label.pack()

        titleframe.place(y=32, relx=0.5, anchor=CENTER)

        # ----------- END HEADER ------------- #

        # ----------------- Funciones de Movimiento ---------------- #

        def cerrar():
            self.master.destroy()

        def ir_Inicio():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Inicio(scrumwindow)

        def ir_Done():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = Done(scrumwindow)

        def ir_ToDo():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ToDo(scrumwindow)

        def ir_Progress():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = InProgress(scrumwindow)

        def ir_ScrumBoard():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = ScrumBoard(scrumwindow)

        # ----------------- Funciones de Movimiento end ---------------- #

        # ----------------- CAJA LATERAL ---------------- #

        cajalateral = tk.Frame(self.master, highlightbackgroun='yellow', highlightcolor='yellow',
                               highlightthickness=2, bg='#F2CB00', width=300, height=700)
        titulo1 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo1_label = tk.Button(titulo1, text='Inicio', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # command = mainform1)
        titulo1_label['command'] = ir_Inicio

        titulo2 = tk.Frame(cajalateral)
        titulo2_label = tk.Button(titulo2, text='Scrum Board', padx=15, pady=5, bg='#D9D9D9', fg='black', font=(
            'Italiana', 18, 'italic'), height=1)  # , command = Ir_Progress)
        titulo2_label['command'] = ir_ScrumBoard

        titulo3 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo3_label = tk.Button(titulo3, text='In Progress', padx=15, pady=5,
                                  bg='#D9D9D9', fg='black', font=('Italiana', 18, 'italic'), height=1)
        titulo3_label['command'] = ir_Progress

        titulo4 = tk.Frame(cajalateral, bg='#f2cb00', padx=0.1, pady=1)
        titulo4_label = tk.Button(titulo4, text='Done', padx=15, pady=5,
                                  bg='#D9D9D9', fg='black', font=('Italiana', 18, 'italic'), height=1)
        titulo4_label['command'] = ir_Done

        cajalateral.pack(side=LEFT)
        cajalateral.config(cursor='heart')
        titulo1.pack()
        titulo1_label.pack()
        titulo1.place(y=30, x=100)

        titulo2.pack()
        titulo2_label.pack()
        titulo2.place(y=190, relx=0.2)

        titulo3.pack()
        titulo3_label.pack()
        titulo3.place(y=340, x=65)

        titulo4.pack()
        titulo4_label.pack()
        titulo4.place(y=500, x=92)

        img_boton = tk.PhotoImage(
            file="D:/Users/Jonathan/Desktop/Uni/4/Programación Aplicada/Scrum/log_out.png")
        boton = ttk.Button(self.master, image=img_boton, command=cerrar)
        boton.place(x=271, y=650)
        boton.image = img_boton

        # -----------------------FIN DE LA BARRA LATERAL ----------------------- #

        def getText():
            historiaa=textou.get("1.0","end")
            datos = (proyectidd, historiaa, '0')
            print ('valor solo de la historia: ', historiaa)
            print ('valor de los datos: ', datos)
            insert_query = "INSERT INTO progreso(proyid,historias,estado) VALUES (%s,%s,%s)"
            c.execute(insert_query, datos)
            connection.commit()
        

        labelcrear = tk.Label (self.master, text = 'Página para añadir Historias de Usuario' , font= ('verdana', 17, 'italic', 'bold'), bg = gris)
        labelcrear.place (y=107, x=565, anchor=CENTER)

        textou = tk.Text (self.master, bd = 10, font = ('Verdana', 14), height = 10, relief = GROOVE, width= 75)
        textou. place (y=300, x=810, anchor=CENTER)

        botonaniadir = tk.Button (self.master, text= 'Añadir Historia de Usuario', font= ('verdana', 12, 'italic'), command=getText)
        botonaniadir.place (y=550, x=800, anchor=CENTER)

        sql_select_query3 = "select document from usuarios where username = %s"
        c.execute(sql_select_query3, (username2,))
        record = c.fetchone()
        doc2 = record
        print('documento del ususario: ', doc2)

        dar_projectid = "select proyid from proyectos where document = %s"
        c.execute(dar_projectid, (doc2,))
        suprojid = c.fetchone()
        proyectidd = suprojid
        print('El proyect Id es: ', proyectidd)

        ver_estado = "select historias from progreso where estado = %s and proyid = %s"
        c.execute(ver_estado, ('0', suprojid,))
        ToDos = c.fetchall()
        print('Los To do: ', ToDos)

        
        
        
        #insert_query = "INSERT INTO progreso(proyid,historias,estado) VALUES (%s,%s,%s)"
        #c.execute(insert_query, vals)
        #connection.commit()


root.mainloop()
