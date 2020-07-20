print("hola bienvenido vamos ha hacer calculos eletricos")
print()
import re
import os
import winsound
from tkinter import*
from io import open
dic={}
pu={}
pt=0
et=0
PT=0
ET=0
longitud_acometida_interna=0
longitud_acometida_externa=0
breaker_circuitos=0
potencia_panel_solar=0
potencia_inversor=0
tiempo_luz_solar_optimo_diario=0
texto1=0
def menu_1():
    global texto1
    
    ventana8=Tk()      #ventana
    ventana8.title("Electrodomesticos")      #titulo de la ventana
    #ventana8.iconbitmap("archivo.ico")      #icono de la ventana (la imagen se deve converitr a formato .ico)
    ventana8.resizable(False,False)      #redimencionar la ventana 
    #ventana8.geometry("1200x800")      #geometria de la ventana
    ventana8.config(bg="blue")      #color de fondo de la ventana
    
    

    frame=Frame()      #frame
    frame.pack()      #empaquetado de rame
    frame.config(bg="orange")      #color de fondo del frame 
    frame.config(width="1400", height="800")      #geometria del frame
    frame.config(bd=25)      #ancho de borde del frame 
    frame.config(relief="groove")      #tipo de borde del frame
    frame.config(cursor="hand2")      #tipo de cursor de frame

    imagen_1=PhotoImage(file="materiales.PNG")      #imagen 1 (conversor online PNG y de tamaño)
    Label(frame, image=imagen_1).place(x=800,y=200)  #imagen


    Label(frame, text="¿que desea realizar?", bg="orange", fg="purple", font=("Comic Sans MS", 28)).place(x=200,y=50)  #texto corto

    texto=StringVar()
    
    Label(frame, text="agregar mas electrodomesticos", bg="orange", fg="purple", font=("Comic Sans MS", 28)).place(x=200,y=200)  #texto corto
    def enviar1():
        texto.set("a")         
    boton1=Button(frame, text="a)", bg="white", command=enviar1, fg="purple", font=("Comic Sans MS", 18))  #boton
    boton1.place(x=130,y=200)
    
    
    Label(frame, text="cambiar datos de energia solar", bg="orange", fg="purple", font=("Comic Sans MS", 28)).place(x=200,y=270)  #texto corto
    def enviar2():
        texto.set("b")
    boton2=Button(frame, text="b)", bg="white", command=enviar2, fg="purple", font=("Comic Sans MS", 18))  #boton
    boton2.place(x=130,y=270)

    
    Label(frame, text="cerrar secion", bg="orange", fg="purple", font=("Comic Sans MS", 28)).place(x=200,y=340)  #texto corto
    def enviar3():
        texto.set("c")
    boton3=Button(frame, text="c)", bg="white", command=enviar3, fg="purple", font=("Comic Sans MS", 18))  #boton
    boton3.place(x=130,y=340)

    
    entrada=Entry(frame, width=3, textvariable=texto, bg="white", fg="purple", font=("Comic Sans MS", 28)) #entrada
    entrada.place(x=900,y=50)
    def enviar11():
        global texto1
        texto1=texto.get()
        ventana8.destroy()
    boton1=Button(frame, text="SIGUIENTE", bg="white", command=enviar11, fg="purple", font=("Comic Sans MS", 28))  #boton
    boton1.place(x=1050,y=30)

    texto1=texto.get()

    



    ventana8.mainloop()

    print(texto.get)

#CREAMOS VENTANA PRINCIPAL.
def ventana_inicio():
    global ventana_principal
    pestas_color="LightPink"
    ventana_principal=Tk()
    ventana_principal.geometry("600x550")#DIMENSIONES DE LA VENTANA
    ventana_principal.title("Login con tkinter")#TITULO DE LA VENTANA
    Label(text="¿Qué desea hacer?", bg="LightPink", width="600", height="8", font=("Cambria", 18)).pack()#ETIQUETA CON TEXTO
    Label(text="").pack()
    Button(text="Iniciar sesion", height="2", width="30", bg=pestas_color, command=login).pack() #BOTÓN "Acceder"
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", bg=pestas_color, command=registro).pack() #BOTÓN "Registrarse".
    Label(text="").pack()
    ventana_principal.mainloop()

#CREAMOS VENTANA PARA REGISTRO.
def registro():
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("500x450")
    ventana_registro.config(bg="LightGray")
 
    global nombre_usuario
    global clave
    global entrada_nombre
    global entrada_clave
    nombre_usuario = StringVar() 
    clave = StringVar() 
 
    Label(ventana_registro, text="Introduzca datos", bg="LightPink", width="500", height="3").pack()
    etiqueta_nombre = Label(ventana_registro, text="Nombre de usuario * ")
    etiqueta_nombre.pack()
    etiqueta_nombre.config(bg="LightGray")
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario) 
    entrada_nombre.pack()
    etiqueta_clave = Label(ventana_registro, text="Contraseña * ")
    etiqueta_clave.pack()
    etiqueta_clave.config(bg="LightGray")
    entrada_clave = Entry(ventana_registro, textvariable=clave, show='*') 
    entrada_clave.pack()
    Button(ventana_registro, text="Registrarse", width=10, height=1, bg="LightPink", command = registro_usuario).pack() #BOTÓN "Registrarse"

#CREAMOS VENTANA PARA LOGIN.

def login():
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("500x450")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña", bg="LightPink", width="500", height="3").pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nombre usuario * ").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña * ").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login).pack()

#VENTANA "VERIFICACION DE LOGIN".

def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END) 
    entrada_login_clave.delete(0, END)
    leer()
    global dic
    usuario1=dic.get(usuario1,False)
    print(dic)
    if usuario1 != False:
        def ingresoc():
            c1=0
            if usuario1 == clave1:
                exito_login(usuario1)
            elif c1<2:
                c1=c1+1
                winsound.Beep(100, 500)
                no_clave()
        ingresoc()
    else:
        winsound.Beep(100, 500)
        no_usuario() 


# VENTANA "Login finalizado con exito".
 
def exito_login(a):
    global ventana_exito
    ventana_exito = Toplevel(ventana_login)
    ventana_exito.title("Exito")
    ventana_exito.geometry("150x100")
    Label(ventana_exito, text="Login finalizado con exito").pack()
    Button(ventana_exito, text="OK", command=borrar_exito_login).pack()
    ventana_login.destroy()
    ventana_principal.destroy()
    prop(a)
 
#VENTANA DE "Contraseña incorrecta".
 
def no_clave():
    global ventana_no_clave
    ventana_no_clave = Toplevel(ventana_login)
    ventana_no_clave.title("ERROR")
    ventana_no_clave.geometry("150x100")
    Label(ventana_no_clave, text="Contraseña incorrecta ").pack()
    Button(ventana_no_clave, text="OK", command=borrar_no_clave).pack() 
 
#VENTANA DE "Usuario no encontrado".
 
def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("ERROR")
    ventana_no_usuario.geometry("150x100")
    Label(ventana_no_usuario, text="Usuario no encontrado").pack()
    Button(ventana_no_usuario, text="OK", command=borrar_no_usuario).pack() 

#CERRADO DE VENTANAS

def borrar_exito_login():
    ventana_exito.destroy()
 
 
def borrar_no_clave():
    ventana_no_clave.destroy()
 
 
def borrar_no_usuario():
    ventana_no_usuario.destroy()

#REGISTRO USUARIO
dic={}
def registro_usuario():
    global dic
    usuario_info = str(nombre_usuario.get())
    clave_info = str(clave.get())
    if dic.get(usuario_info,False) == False:
        if len(usuario_info)>=2:
            def registroc():
                c1=0
                c2=0
                for i in clave_info:
                    if re.search("[a-z]",i) or re.search("[A-Z]",i):
                        c1=c1+1
                    if re.search("[0-9]",i):
                        c2=c2+1
                if c1>=1 and c2>=1:
                    actualizar(usuario_info,clave_info)
                    Label(ventana_registro, text="Registro completado con éxito", fg="Green", bg="LightGray", font=("calibri", 11)).pack()  
                    leer()
                else:
                    winsound.Beep(100, 500)
                    l=Label(ventana_registro, text="La contraseña no cuenta con los parámetros establecidos, intente de nuevo",fg="Green", bg="LightGray", font=("calibri", 11)).pack()
                    l.destroy()
                    registroc()
                    entrada_nombre.delete(0, END)
                    entrada_clave.delete(0, END)
            registroc()
        else:
            winsound.Beep(100, 500)
            l=Label(ventana_registro, text="El nombre de usuario no cuenta con los parámetros establecidos, intente de nuevo",fg="Green", bg="LightGray", font=("calibri", 11)).pack()
            l.destroy()
            registro_usuario()
            entrada_nombre.delete(0, END)
            entrada_clave.delete(0, END)
 
#ACTUALIACIÓN DE DATOS:
def actualizar(a,b):
    registro=open("registro.txt","a")
    registro.write (a + ":" + b + "\n" )
#LECTURA DE DATOS
def leer():
    global registro
    global dic
    registro=open("registro.txt","r")
    iregistro=registro.read()
    registro.close()

    lregistro=iregistro.split()
    for i in lregistro:
        lc=i.split(":")
        dic[lc[0]]=lc[1]
 
 


def prop(nombre):
    archivo=f"{nombre} electrodomésticos.txt"
    ea=os.path.isfile(archivo)
    if ea==False:
        elec=open(f"{nombre} electrodomésticos.txt","w")
        ##elec.write("Electrodomestico:Potencia:Uso en horas al dia \n")
        elec.close
    def aelec():
        global pt
        global et
        global pu
        global ET
        global PT
        
       
        ventana2=Tk()      #ventana
        ventana2.title("Electrodomesticos")      #titulo de la ventana
        #ventana2.iconbitmap("archivo.ico")      #icono de la ventana (la imagen se deve converitr a formato .ico)
        ventana2.resizable(False,False)      #redimencionar la ventana 
        #ventana2.geometry("1200x800")      #geometria de la ventana
        ventana2.config(bg="blue")      #color de fondo de la ventana
        

        frame=Frame()      #frame
        frame.pack()      #empaquetado de rame
        frame.config(bg="orange")      #color de fondo del frame 
        frame.config(width="1400", height="800")      #geometria del frame
        frame.config(bd=0)      #ancho de borde del frame 
        frame.config(relief="groove")      #tipo de borde del frame
        frame.config(cursor="hand2")      #tipo de cursor de frame

        imagen_1=PhotoImage(file="electrodomesticos 0.PNG")      #imagen 1 (conversor online PNG y de tamaño)
        Label(frame, image=imagen_1).place(x=300,y=150)  #imagen

        texto_numero=StringVar()
        Label(frame, text="¿cuantos electrodomesticos vas a ingresar?", bg="orange", fg="purple", font=("Comic Sans MS", 28)).place(x=100,y=50)  #texto corto
        entrada_numero_electrodomesticos=Entry(frame, width=3, bg="white", fg="purple", font=("Comic Sans MS", 28)) #entrada
        entrada_numero_electrodomesticos.place(x=900,y=50)
        def enviar1():
            texto_numero.set(entrada_numero_electrodomesticos.get())
            ventana2.destroy()
        boton1=Button(frame, text="SIGUIENTE", bg="white", command=enviar1, fg="purple", font=("Comic Sans MS", 28))  #boton
        boton1.place(x=1050,y=30)
        ventana2.mainloop()
        ne=int(texto_numero.get())      
        for i in range(ne):
            ventana3=Tk()      #ventana
            ventana3.title("Electrodomesticos")      #titulo de la ventana
            #ventana3.iconbitmap("archivo.ico")      #icono de la ventana (la imagen se deve converitr a formato .ico)
            ventana3.resizable(False,False)      #redimencionar la ventana 
            #ventana3.geometry("1200x800")      #geometria de la ventana
            ventana3.config(bg="blue")      #color de fondo de la ventana

            frame=Frame()      #frame
            frame.pack()      #empaquetado de rame
            frame.config(bg="orange")      #color de fondo del frame 
            frame.config(width="1400", height="800")      #geometria del frame
            frame.config(bd=25)      #ancho de borde del frame 
            frame.config(relief="groove")      #tipo de borde del frame
            frame.config(cursor="hand2")      #tipo de cursor de frame

            imagen_1=PhotoImage(file="electrodomesticos.PNG")      #imagen 1 (conversor online PNG y de tamaño)
            Label(frame, image=imagen_1).place(x=15,y=15)  #imagen
            
            texto_electrodomesticos=StringVar()
            Label(frame, text="Electrodomestico:", bg="orange", fg="purple", font=("Comic Sans MS", 28)).place(x=10,y=540)  #texto corto
            entrada_electrodomesticos=Entry(frame, width=18, bg="white", fg="purple", font=("Comic Sans MS", 28)) #entrada
            entrada_electrodomesticos.place(x=330,y=540)
            def enviar2():
                texto_electrodomesticos.set(entrada_electrodomesticos.get())               
            salida_electrodomesticos=Entry(frame, width=18, textvariable=texto_electrodomesticos, bg="white", fg="purple", font=("Comic Sans MS", 28)) #entrada
            salida_electrodomesticos.place(x=920,y=540)
            boton2=Button(frame, text="Enviar", bg="white", command=enviar2, fg="purple", font=("Comic Sans MS", 16))  #boton
            boton2.place(x=780,y=540)
            
            texto_potencias=StringVar()
            Label(frame, text="Potencia (watts):", bg="orange", fg="purple", font=("Comic Sans MS", 28)).place(x=10,y=610)  #texto corto
            entrada_potencias=Entry(frame, width=9, bg="white", fg="purple", font=("Comic Sans MS", 28)) #entrada
            entrada_potencias.place(x=330,y=610)
            def enviar3():
                texto_potencias.set(entrada_potencias.get())
            salida_potencias=Entry(frame, width=9, textvariable=texto_potencias,bg="white", fg="purple", font=("Comic Sans MS", 28)) #entrada
            salida_potencias.place(x=920,y=610)
            boton3=Button(frame, text="Enviar", bg="white", command=enviar3, fg="purple", font=("Comic Sans MS", 16))  #boton
            boton3.place(x=780,y=610)
            
            texto_horas=StringVar()
            Label(frame, text="Uso diario (horas):", bg="orange", fg="purple", font=("Comic Sans MS", 28)).place(x=10,y=680)  #texto corto
            entrada_horas=Entry(frame, width=3, bg="white", fg="purple", font=("Comic Sans MS", 28)) #entrada
            entrada_horas.place(x=330,y=680)
            def enviar4():
                texto_horas.set(entrada_horas.get())
            salida_horas=Entry(frame, width=3, textvariable=texto_horas, bg="white", fg="purple", font=("Comic Sans MS", 28)) #entrada
            salida_horas.place(x=920,y=680)
            boton4=Button(frame, text="Enviar", bg="white", command=enviar4, fg="purple", font=("Comic Sans MS", 16))  #boton
            boton4.place(x=780,y=680)
            

            def enviar5():
                ventana3.destroy()
            boton5=Button(frame, text="SIGUIENTE", bg="white", command=enviar5, fg="purple", font=("Comic Sans MS", 28))  #boton
            boton5.place(x=1050,y=30)
            ventana3.mainloop()

            a=str(texto_electrodomesticos.get())
            b=int(texto_potencias.get())
            c=float(texto_horas.get())

            
            pu[a]=(b,c)
            l=(b,c)
            if i>=1:
                wt=wt+l[0]
                pt=pt+l[0]*l[1]
            else:
                wt=l[0]
                pt=l[0]*l[1]
            
            electrodomestico=list(pu.keys())
            voltaje_uso=list(pu.values())
        
            elec=open(f"{nombre} electrodomésticos.txt","a")
            elec.write(texto_electrodomesticos.get() + ":" + texto_potencias.get() + ":" + texto_horas.get() +"\n")
            elec.close()
            Elec=open(f"{nombre} Elec.txt","a")
            Elec.write(texto_electrodomesticos.get()+"\n")
            Elec.close()
            Pot=open(f"{nombre} Pot.txt","a")
            Pot.write( texto_potencias.get() +"\n")
            Pot.close()
            Hor=open(f"{nombre} Hor.txt","a")
            Hor.write(texto_horas.get() +"\n")
            Hor.close()
     

        if os.path.isfile(f"{nombre} potencias.txt"):
            pass
        else:
            txt=open(f"{nombre} potencias.txt","w")
            txt.close()



        ##Agregar informacion 
        potencias=open(f"{nombre} potencias.txt","a")
        potencias.write(str(wt)+"\n")
        potencias.close()



        ##Leer archivo
        potencias=open(f"{nombre} potencias.txt","r")
        informacion_potencias=potencias.read()
        potencias.close()
 

            
    
        archivo = f"{nombre} potencias"
        fh = open(f"{nombre} potencias.txt", 'r')
        lineas = fh.readlines()
        fh.close()
        p=list(map(lambda x:x.strip(),lineas))
        m= [int(x) for x in p]
        PT=sum(m)
            
    

        if os.path.isfile(f"{nombre} energias.txt"):
            pass
        else:
            txt=open(f"{nombre} energias.txt","w")
            txt.close()

        ##Agregar informacion 
        energias=open(f"{nombre} energias.txt","a")
        energias.write(str(pt)+"\n")
        energias.close()



        ##Leer archivo
        energias=open(f"{nombre} energias.txt","r")
        informacion_energias=energias.read()
        energias.close()
 

            
            
    
        archivo_e = f"{nombre} energias"
        fhl = open(f"{nombre} energias.txt", 'r')
        lineas_e = fhl.readlines()
        fhl.close()
        r=list(map(lambda x:x.strip(),lineas_e))
        n= [float(x) for x in r]
        ET=sum(n)
            


            
        elec=open(f"{nombre} electrodomésticos.txt","r")
        ielec=elec.read()
        elec.close()
        lelec=ielec.split()
        for f in lelec:
            lc=f.split(":")
            pu[lc[1]]=lc[2]
        ps=list(pu.keys())
        us=list(pu.values())
      

        
        print()
        print("electrodomésticos:potencia:uso diaro en horas")       
        print(ielec)
        print()
        print(f"Potencia total {wt}w")
        print(f"Energia total {pt}w/h")
        print()
        print("estas fueron las potencias registradas")
        print()
        print(informacion_potencias)
        print()
        print("esta es la potencia acumulada")
        print(PT)
        print()
        print()
        print("estas fueron las energias registradas")
        print()
        print(informacion_energias)
        print()
        print("esta es la energia acumulada")
        print(ET)
        print()
        print()

        ##Leer archivo
        Elec=open(f"{nombre} Elec.txt","r")
        IElec=Elec.read()
        Elec.close()

        ##Leer archivo
        Pot=open(f"{nombre} Pot.txt","r")
        IPot=Pot.read()
        Pot.close()

        ##Leer archivo
        Hor=open(f"{nombre} Hor.txt","r")
        IHor=Hor.read()
        Hor.close()


        print("estos son los electrodomesticos")
        print(IElec)
        print()
        print("estas son las potencia")
        print(IPot)
        print()
        print("estas son las horas")
        print(IHor)

        #ley de energia
        Energia_diaria_wh=ET #(watts-hora)
        Energia_diaria_kwh=Energia_diaria_wh/1000  #(kilowatts-hora)
        Energia_mensual_kwh=Energia_diaria_kwh*30  #(kilowatts-hora)
        

        ventana4=Tk()      #ventana
        ventana4.title("Electrodomesticos")      #titulo de la ventana
        #ventana4.iconbitmap("archivo.ico")      #icono de la ventana (la imagen se deve converitr a formato .ico)
        ventana4.resizable(False,False)      #redimencionar la ventana 
        #ventana4.geometry("1200x800")      #geometria de la ventana
        ventana4.config(bg="blue")      #color de fondo de la ventana

        frame=Frame()      #frame
        frame.pack()      #empaquetado de rame
        frame.config(bg="orange")      #color de fondo del frame 
        frame.config(width="1400", height="800")      #geometria del frame
        frame.config(bd=25)      #ancho de borde del frame 
        frame.config(relief="groove")      #tipo de borde del frame
        frame.config(cursor="hand2")      #tipo de cursor de frame

    
        Label(frame, text="Electrodomestico:", bg="orange", fg="purple", font=("Comic Sans MS", 28)).place(x=50,y=100)  #texto corto   
        electrodomesticos_t=Text(frame, width=20, height=9, bg="white", fg="purple", font=("Comic Sans MS", 28))  #texto largo
        electrodomesticos_t.place(x=50,y=160)
        barra_e=Scrollbar(frame, command=electrodomesticos_t.yview)
        barra_e.place(x=495,y=160)
        electrodomesticos_t.config(yscrollcommand=barra_e.set)
        electrodomesticos_t.insert(INSERT, IElec +"\n")
            
    
        Label(frame, text="Potencia (watts):", bg="orange", fg="purple", font=("Comic Sans MS", 28)).place(x=600,y=100)  #texto corto
        potencias_t=Text(frame, width=10, height=9, bg="white", fg="purple", font=("Comic Sans MS", 28))  #texto largo
        potencias_t.place(x=600,y=160)
        barra_e=Scrollbar(frame, command=potencias_t.yview)
        barra_e.place(x=815,y=160)
        potencias_t.config(yscrollcommand=barra_e.set)
        potencias_t.insert(INSERT, IPot +"\n")
            
    
        Label(frame, text="Uso diario (horas):", bg="orange", fg="purple", font=("Comic Sans MS", 28)).place(x=1000,y=100)  #texto corto
        horas_t=Text(frame, width=5, height=9, bg="white", fg="purple", font=("Comic Sans MS", 28))  #texto largo
        horas_t.place(x=1000,y=160)
        barra_e=Scrollbar(frame, command=horas_t.yview)
        barra_e.place(x=1100,y=160)
        horas_t.config(yscrollcommand=barra_e.set)
        horas_t.insert(INSERT, IHor +"\n")

        Label(frame, text="Potencia Total (watts):", bg="orange", fg="purple", font=("Comic Sans MS", 28)).place(x=50,y=680)  #texto corto
        Label(frame, text=PT, bg="white", fg="purple", font=("Comic Sans MS", 28)).place(x=450,y=680)  #texto corto
        

        Label(frame, text="Energia Total diaria (Kwh):", bg="orange", fg="purple", font=("Comic Sans MS", 28)).place(x=700,y=680)  #texto corto
        Label(frame, text=Energia_diaria_kwh, bg="white", fg="purple", font=("Comic Sans MS", 28)).place(x=1170,y=680)  #texto corto
       

        def enviar6():
            ventana4.destroy()
        boton6=Button(frame, text="SIGUIENTE", bg="white", command=enviar6, fg="purple", font=("Comic Sans MS", 28))  #boton
        boton6.place(x=1080,y=15)
        ventana4.mainloop()
        
       
 

    def entradas():
        global longitud_acometida_interna
        global longitud_acometida_externa
        global breaker_circuitos
        global potencia_panel_solar
        global potencia_inversor
        global tiempo_luz_solar_optimo_diario
        
        px=12
        py=12

        r=Tk()
        r.title("Electrodomesticos")      #titulo de la ventana
        #r.iconbitmap("archivo.ico")      #icono de la ventana (la imagen se deve converitr a formato .ico)
        r.resizable(False,False)      #redimencionar la ventana 
        #r.geometry("1200x800")      #geometria de la ventana
        r.config(bg="blue")      #color de fondo de la ventana
        e1=IntVar()
        e2=IntVar()
        e3=IntVar()
        e4=IntVar()
        e5=IntVar()
        e6=IntVar()
        mf=Frame()
        mf.pack()
        mf.config(bg="orange")      #color de fondo del frame 
        mf.config(width="1400", height="800")      #geometria del frame
        mf.config(bd=25)      #ancho de borde del frame 
        mf.config(relief="groove")      #tipo de borde del frame
        mf.config(cursor="hand2")      #tipo de cursor de frame

        lail=Label(mf, text="Ingrese la longitud de la acometida interna en metros:")
        lail.grid(row=0,column=0,sticky="w",padx=px,pady=py, columnspan=4)
        laie=Entry(mf,width=9, textvariable=e1)
        laie.grid(row=1,column=5,sticky="w",padx=px,pady=py)
        Radiobutton(mf,text="3m",variable=e1,value=3 ).grid(row=1,column=0,padx=px,pady=py)
        Radiobutton(mf,text="6m",variable=e1,value=6 ).grid(row=1,column=1,padx=px,pady=py)
        Radiobutton(mf,text="9m",variable=e1,value=9 ).grid(row=1,column=2,padx=px,pady=py)
        Radiobutton(mf,text="12m",variable=e1,value=12 ).grid(row=1,column=3,padx=px,pady=py)
        Radiobutton(mf,text="15m",variable=e1,value=15 ).grid(row=1,column=4,padx=px,pady=py)


        lael=Label(mf, text="Ingrese la longitud de la acometida externa en metros:")
        lael.grid(row=2,column=0,sticky="w",padx=px,pady=py,  columnspan=4)
        laee=Entry(mf,width=9, textvariable=e2)
        laee.grid(row=3,column=5,sticky="w",padx=px,pady=py)
        Radiobutton(mf,text="5m",variable=e2,value=5 ).grid(row=3,column=0,padx=px,pady=py)
        Radiobutton(mf,text="10m",variable=e2,value=10 ).grid(row=3,column=1,padx=px,pady=py)
        Radiobutton(mf,text="15m",variable=e2,value=15 ).grid(row=3,column=2,padx=px,pady=py)
        Radiobutton(mf,text="20m",variable=e2,value=20 ).grid(row=3,column=3,padx=px,pady=py)
        Radiobutton(mf,text="25m",variable=e2,value=25 ).grid(row=3,column=4,padx=px,pady=py)


        bc=Label(mf, text="Ingrese uno de estos valores en amperios para los breakers de los circuitos:")
        bc.grid(row=4,column=0,sticky="w",padx=px,pady=py , columnspan=5)
        Radiobutton(mf,text="10A",variable=e3,value=10 ).grid(row=5,column=0,padx=px,pady=py)
        Radiobutton(mf,text="15A",variable=e3,value=15 ).grid(row=5,column=1,padx=px,pady=py)
        Radiobutton(mf,text="20A",variable=e3,value=20 ).grid(row=5,column=2,padx=px,pady=py)
        Radiobutton(mf,text="25A",variable=e3,value=25 ).grid(row=5,column=3,padx=px,pady=py)
        Radiobutton(mf,text="30A",variable=e3,value=30 ).grid(row=5,column=4,padx=px,pady=py)


        pps=Label(mf, text="Ingrese uno de estos valores en watts para elejir el tipo de panel solar: ")
        pps.grid(row=6,column=0,sticky="w",padx=px,pady=py, columnspan=5)
        Radiobutton(mf,text="200w",variable=e4,value=200 ).grid(row=7,column=0,padx=px,pady=py)
        Radiobutton(mf,text="250w",variable=e4,value=250 ).grid(row=7,column=1,padx=px,pady=py)
        Radiobutton(mf,text="300w",variable=e4,value=300 ).grid(row=7,column=2,padx=px,pady=py)
        Radiobutton(mf,text="350w",variable=e4,value=350 ).grid(row=7,column=3,padx=px,pady=py)
        Radiobutton(mf,text="400w",variable=e4,value=400 ).grid(row=7,column=4,padx=px,pady=py)


        pi=Label(mf, text="Ingrese uno de estos valores en watts para elejir el tipo de inversor: ")
        pi.grid(row=8,column=0,sticky="w",padx=px,pady=py, columnspan=5)
        Radiobutton(mf,text="1000w",variable=e5,value=1000 ).grid(row=9,column=0,padx=px,pady=py)
        Radiobutton(mf,text="1500w",variable=e5,value=1500 ).grid(row=9,column=1,padx=px,pady=py)
        Radiobutton(mf,text="2000w",variable=e5,value=2000 ).grid(row=9,column=2,padx=px,pady=py)
        Radiobutton(mf,text="2500w",variable=e5,value=2500 ).grid(row=9,column=3,padx=px,pady=py)
        Radiobutton(mf,text="3000w",variable=e5,value=3000 ).grid(row=9,column=4,padx=px,pady=py)
        
        
        tll=Label(mf, text="Ingrese el promedio de tiempo de luz solar optima diario que hay en tu zona en horas:")
        tll.grid(row=10,column=0,sticky="w",padx=px,pady=py, columnspan=5)
        tle=Entry(mf,width=9, textvariable=e6)
        tle.grid(row=11,column=5,sticky="w",padx=px,pady=py)
        Radiobutton(mf,text="2h",variable=e6,value=2 ).grid(row=11,column=0,padx=px,pady=py)
        Radiobutton(mf,text="4h",variable=e6,value=4 ).grid(row=11,column=1,padx=px,pady=py)
        Radiobutton(mf,text="6h",variable=e6,value=6 ).grid(row=11,column=2,padx=px,pady=py)
        Radiobutton(mf,text="8h",variable=e6,value=8 ).grid(row=11,column=3,padx=px,pady=py)
        Radiobutton(mf,text="10h",variable=e6,value=10 ).grid(row=11,column=4,padx=px,pady=py)
        
        def env():
            global longitud_acometida_interna
            global longitud_acometida_externa
            global breaker_circuitos
            global potencia_panel_solar
            global potencia_inversor
            global tiempo_luz_solar_optimo_diario
            
            longitud_acometida_interna=e1.get()
            longitud_acometida_externa=e2.get()                              
            breaker_circuitos=e3.get()
            potencia_panel_solar=e4.get()
            potencia_inversor=e5.get()
            tiempo_luz_solar_optimo_diario=e6.get()
            r.destroy()
        Button(mf, text="ENVIAR", command=env ).grid(row=12,column=0,padx=20,pady=20,columnspan=5)
        r.mainloop()
        print()
        print()
    def formulas():
        #FORMULAS

        #LEYES

        #ley de energia
        energia_diaria_wh=ET #(watts-hora)
        energia_diaria_kwh=energia_diaria_wh/1000  #(kilowatts-hora)
        energia_mensual_kwh=energia_diaria_kwh*30  #(kilowatts-hora)
 
        #ley de watt
        import math
        potencia_total=PT #(watts)
        voltaje=120  #voltios
        corriente_total=potencia_total/voltaje #(amperios)
        numero_circuitos=math.ceil(corriente_total/breaker_circuitos) #

        #ley de caida de voltaje
        resistividad_cobre=0.000000017   #(ohmios*metro)
        longitud_acometida=longitud_acometida_interna+longitud_acometida_externa  #(metros)
        voltaje_poste=127             #(voltios)
        caida_voltaje=voltaje_poste*(3/100)  #(voltios)
        area_acometida=2*1000000*corriente_total*resistividad_cobre*longitud_acometida/caida_voltaje #(milimetros cuadrados)

        #ley de paneles
        longitud_circuitos_paneles_d=4*(potencia_panel_solar/200)**(0.5) #(metros)
        longitud_circuitos_paneles=float("{:.2f}".format(longitud_circuitos_paneles_d))  #(metros)
        numero_paneles=math.ceil(energia_diaria_wh/(tiempo_luz_solar_optimo_diario*potencia_panel_solar)) #
        potencia_total_paneles=numero_paneles*potencia_panel_solar #(watts)

        #ley de inversores
        numero_inversores=math.ceil(potencia_total_paneles/potencia_inversor) #
        corriente_inversor=potencia_inversor/voltaje #(amperios)
        corriente_total_inversores=numero_inversores*corriente_inversor  #(amperios)
        area_acometida_paneles=2*1000000*longitud_acometida_externa*resistividad_cobre*corriente_total_inversores/caida_voltaje  #(milimetros cuadrados)

        #CATALOGO PRECIOS

        #tablero de distribucion
        corriente_tablero_1=40  #(amperios)
        corriente_tablero_2=80  #(amperios)
        corriente_tablero_3=110 #(amperios)
        corriente_tablero_4=150 #(amperios)
        corriente_tablero_5=200 #(amperios)
        costo_tablero_1=25000  #(pesos)
        costo_tablero_2=37000  #(pesos)
        costo_tablero_3=70000  #(pesos)
        costo_tablero_4=120000 #(pesos)
        costo_tablero_5=147000 #(pesos)
        if corriente_total<corriente_tablero_1:
            corriente_tablero=corriente_tablero_1
            costo_tablero=costo_tablero_1
        elif corriente_tablero_1<=corriente_total<corriente_tablero_2:
            corriente_tablero=corriente_tablero_2
            costo_tablero=costo_tablero_2
        elif corriente_tablero_2<=corriente_total<corriente_tablero_3:
            corriente_tablero=corriente_tablero_3
            costo_tablero=costo_tablero_3
        elif corriente_tablero_3<=corriente_total<corriente_tablero_4:
            corriente_tablero=corriente_tablero_4
            costo_tablero=costo_tablero_4
        elif corriente_tablero_4<=corriente_total:
            corriente_tablero=corriente_tablero_5
            costo_tablero=costo_tablero_5

        #medidor
        potencia_medidor_1=4800   #(watts)
        potencia_medidor_2=9600   #(watts)
        potencia_medidor_3=13200  #(watts)
        potencia_medidor_4=18000  #(watts)
        potencia_medidor_5=24000  #(watts)
        costo_medidor_1=56000    #(pesos)
        costo_medidor_2=123000   #(pesos)
        costo_medidor_3=210000   #(pesos)
        costo_medidor_4=480000   #(pesos)
        costo_medidor_5=670000   #(pesos)
        if potencia_total<potencia_medidor_1:
            potencia_medidor=potencia_medidor_1
            costo_medidor=costo_medidor_1
        elif potencia_medidor_1<=potencia_total<potencia_medidor_2:
            potencia_medidor=potencia_medidor_2
            costo_medidor=costo_medidor_2
        elif potencia_medidor_2<=potencia_total<potencia_medidor_3:
            potencia_medidor=potencia_medidor_3
            costo_medidor=costo_medidor_3
        elif potencia_medidor_3<=potencia_total<potencia_medidor_4:
            potencia_medidor=potencia_medidor_4
            costo_medidor=costo_medidor_4
        elif potencia_medidor_4<=potencia_total:
            potencia_medidor=potencia_medidor_5
            costo_medidor=costo_medidor_5

        #breakers
        corriente_breaker_1=10   #(amperios)
        corriente_breaker_2=15   #(amperios)
        corriente_breaker_3=20   #(amperios)
        corriente_breaker_4=25   #(amperios)
        corriente_breaker_5=30   #(amperios)
        corriente_breaker_6=40   #(amperios)
        corriente_breaker_7=80   #(amperios)
        corriente_breaker_8=110  #(amperios)
        corriente_breaker_9=150  #(amperios)
        corriente_breaker_10=200 #(amperios)
        costo_breaker_1=11000   #(pesos)
        costo_breaker_2=16000   #(pesos)
        costo_breaker_3=17500   #(pesos)
        costo_breaker_4=19000   #(pesos)
        costo_breaker_5=22000   #(pesos)
        costo_breaker_6=45000   #(pesos)
        costo_breaker_7=65000   #(pesos)
        costo_breaker_8=83000   #(pesos)
        costo_breaker_9=110000  #(pesos)
        costo_breaker_10=137000 #(pesos)
        if corriente_total<corriente_breaker_1:    #(breaker-medidor)
            breaker_medidor=corriente_breaker_1
            costo_breaker_medidor=costo_breaker_1
        elif corriente_breaker_1<=corriente_total<corriente_breaker_2:
            breaker_medidor=corriente_breaker_2
            costo_breaker_medidor=costo_breaker_2
        elif corriente_breaker_2<=corriente_total<corriente_breaker_3:
            breaker_medidor=corriente_breaker_3
            costo_breaker_medidor=costo_breaker_3
        elif corriente_breaker_3<=corriente_total<corriente_breaker_4:
            breaker_medidor=corriente_breaker_4
            costo_breaker_medidor=costo_breaker_4
        elif corriente_breaker_4<=corriente_total<corriente_breaker_5:
            breaker_medidor=corriente_breaker_5
            costo_breaker_medidor=costo_breaker_5
        elif corriente_breaker_5<=corriente_total<corriente_breaker_6:
            breaker_medidor=corriente_breaker_6
            costo_breaker_medidor=costo_breaker_6
        elif corriente_breaker_6<=corriente_total<corriente_breaker_7:
            breaker_medidor=corriente_breaker_7
            costo_breaker_medidor=costo_breaker_7
        elif corriente_breaker_7<=corriente_total<corriente_breaker_8:
            breaker_medidor=corriente_breaker_8
            costo_breaker_medidor=costo_breaker_8
        elif corriente_breaker_8<=corriente_total<corriente_breaker_9:
            breaker_medidor=corriente_breaker_9
            costo_breaker_medidor=costo_breaker_9
        elif corriente_breaker_9<=corriente_total:
            breaker_medidor=corriente_breaker_10
            costo_breaker_medidor=costo_breaker_10
        if breaker_circuitos==corriente_breaker_1:           #(breaker-circuitos)
            costo_breaker_circuitos=costo_breaker_1
        elif breaker_circuitos==corriente_breaker_2:
            costo_breaker_circuitos=costo_breaker_2
        elif breaker_circuitos==corriente_breaker_3:
            costo_breaker_circuitos=costo_breaker_3
        elif breaker_circuitos==corriente_breaker_4:
            costo_breaker_circuitos=costo_breaker_4
        elif breaker_circuitos==corriente_breaker_5:
            costo_breaker_circuitos=costo_breaker_5
        if corriente_inversor<corriente_breaker_1:            #(breaker-inversor)                      
            breaker_inversor=corriente_breaker_1
            costo_breaker_inversor=costo_breaker_1
        elif corriente_breaker_1<=corriente_inversor<corriente_breaker_2:
            breaker_inversor=corriente_breaker_2
            costo_breaker_inversor=costo_breaker_2
        elif corriente_breaker_2<=corriente_inversor<corriente_breaker_3:
            breaker_inversor=corriente_breaker_3
            costo_breaker_inversor=costo_breaker_3
        elif corriente_breaker_3<=corriente_inversor<corriente_breaker_4:
            breaker_inversor=corriente_breaker_4
            costo_breaker_inversor=costo_breaker_4
        elif corriente_breaker_4<=corriente_inversor<corriente_breaker_5:
            breaker_inversor=corriente_breaker_5
            costo_breaker_inversor=costo_breaker_5
        elif corriente_breaker_5<=corriente_inversor<corriente_breaker_6:
            breaker_inversor=corriente_breaker_6
            costo_breaker_inversor=costo_breaker_6
        elif corriente_breaker_6<=corriente_inversor<corriente_breaker_7:
            breaker_inversor=corriente_breaker_7
            costo_breaker_inversor=costo_breaker_7
        elif corriente_breaker_7<=corriente_inversor<corriente_breaker_8:
            breaker_inversor=corriente_breaker_8
            costo_breaker_inversor=costo_breaker_8
        elif corriente_breaker_8<=corriente_inversor<corriente_breaker_9:
            breaker_inversor=corriente_breaker_9
            costo_breaker_inversor=costo_breaker_9
        elif corriente_breaker_9<=corriente_inversor:
            breaker_inversor=corriente_breaker_10
            costo_breaker_inversor=costo_breaker_10   
        #condcutores
        area_1=0.82              #(milimetros cuadrados)
        area_2=1.31              #(milimetros cuadrados)
        area_3=2.08              #(milimetros cuadrados)
        area_4=3.31              #(milimetros cuadrados)
        area_5=5.26              #(milimetros cuadrados)
        area_6=8.37              #(milimetros cuadrados)
        area_7=13.3              #(milimetros cuadrados)
        area_8=21.2              #(milimetros cuadrados)
        area_9=33.6              #(milimetros cuadrados)
        area_10=53.5             #(milimetros cuadrados)
        calibre_1=18              #
        calibre_2=16              #
        calibre_3=14              #
        calibre_4=12              #
        calibre_5=10              #
        calibre_6=8               #
        calibre_7=6               #
        calibre_8=4               #
        calibre_9=2               #
        calibre_10=0              #
        costo_calibre_1=500     #(pesos)
        costo_calibre_2=600     #(pesos)
        costo_calibre_3=1000    #(pesos)
        costo_calibre_4=1600    #(pesos)
        costo_calibre_5=2700    #(pesos)
        costo_calibre_6=5000    #(pesos)
        costo_calibre_7=6700    #(pesos)
        costo_calibre_8=9600    #(pesos)
        costo_calibre_9=140000  #(pesos)
        costo_calibre_10=225000 #(pesos)
        if area_acometida<area_1:      #(acometida)
            calibre_acometida=calibre_1
            costo_conductor_acometida=costo_calibre_1
        elif area_1<=area_acometida<area_2:
            calibre_acometida=calibre_2
            costo_conductor_acometida=costo_calibre_2
        elif area_2<=area_acometida<area_3:
            calibre_acometida=calibre_3
            costo_conductor_acometida=costo_calibre_3
        elif area_3<=area_acometida<area_4:
            calibre_acometida=calibre_4
            costo_conductor_acometida=costo_calibre_4
        elif area_4<=area_acometida<area_5:
            calibre_acometida=calibre_5
            costo_conductor_acometida=costo_calibre_5
        elif area_5<=area_acometida<area_6:
            calibre_acometida=calibre_6
            costo_conductor_acometida=costo_calibre_6
        elif area_6<=area_acometida<area_7:
            calibre_acometida=calibre_7
            costo_conductor_acometida=costo_calibre_7
        elif area_7<=area_acometida<area_8:
            calibre_acometida=calibre_8
            costo_conductor_acometida=costo_calibre_8
        elif area_8<=area_acometida<area_9:
            calibre_acometida=calibre_9
            costo_conductor_acometida=costo_calibre_9
        elif area_9<=area_acometida:
            calibre_acometida=calibre_10
            costo_conductor_acometida=costo_calibre_10
        if area_acometida_paneles<area_1:                     #(acometida-paneles)
            calibre_acometida_paneles=calibre_1
            costo_conductor_acometida_paneles=costo_calibre_1
        elif area_1<=area_acometida_paneles<area_2:
            calibre_acometida_paneles=calibre_2
            costo_conductor_acometida_paneles=costo_calibre_2
        elif area_2<=area_acometida_paneles<area_3:
            calibre_acometida_paneles=calibre_3
            costo_conductor_acometida_paneles=costo_calibre_3
        elif area_3<=area_acometida_paneles<area_4:
            calibre_acometida_paneles=calibre_4
            costo_conductor_acometida_paneles=costo_calibre_4
        elif area_4<=area_acometida_paneles<area_5:
            calibre_acometida_paneles=calibre_5
            costo_conductor_acometida_paneles=costo_calibre_5
        elif area_5<=area_acometida_paneles<area_6:
            calibre_acometida_paneles=calibre_6
            costo_conductor_acometida_paneles=costo_calibre_6
        elif area_6<=area_acometida_paneles<area_7:
            calibre_acometida_paneles=calibre_7
            costo_conductor_acometida_paneles=costo_calibre_7
        elif area_7<=area_acometida_paneles<area_8:
            calibre_acometida_paneles=calibre_8
            costo_conductor_acometida_paneles=costo_calibre_8
        elif area_8<=area_acometida_paneles<area_9:
            calibre_acometida_paneles=calibre_9
            costo_conductor_acometida_paneles=costo_calibre_9
        elif area_9<=area_acometida_paneles:
            calibre_acometida_paneles=calibre_10
            costo_conductor_acometida_paneles=costo_calibre_10
        calibre_circuitos_paneles=calibre_acometida_paneles+2
        if calibre_circuitos_paneles>=calibre_1:            #(conductor-circuitos-paneles)
            costo_conductor_circuitos_paneles=costo_calibre_1
        elif calibre_circuitos_paneles==calibre_2:
            costo_conductor_circuitos_paneles=costo_calibre_2
        elif calibre_circuitos_paneles==calibre_3:
            costo_conductor_circuitos_paneles=costo_calibre_3
        elif calibre_circuitos_paneles==calibre_4:
            costo_conductor_circuitos_paneles=costo_calibre_4
        elif calibre_circuitos_paneles==calibre_5:
            costo_conductor_circuitos_paneles=costo_calibre_5
        elif calibre_circuitos_paneles==calibre_6:
            costo_conductor_circuitos_paneles=costo_calibre_6
        elif calibre_circuitos_paneles==calibre_7:
            costo_conductor_circuitos_paneles=costo_calibre_7
        elif calibre_circuitos_paneles==calibre_8:
            costo_conductor_circuitos_paneles=costo_calibre_8
        elif calibre_circuitos_paneles==calibre_9:
            costo_conductor_circuitos_paneles=costo_calibre_9
        elif calibre_circuitos_paneles==calibre_10:
            costo_conductor_circuitos_paneles=costo_calibre_10
        calibre_tierra=calibre_acometida+2
        if calibre_tierra>=calibre_1:                 #(conductor-tierra)
            costo_conductor_tierra=costo_calibre_1
        elif calibre_tierra==calibre_2:
            costo_conductor_tierra=costo_calibre_2
        elif calibre_tierra==calibre_3:
            costo_conductor_tierra=costo_calibre_3
        elif calibre_tierra==calibre_4:
            costo_conductor_tierra=costo_calibre_4
        elif calibre_tierra==calibre_5:
            costo_conductor_tierra=costo_calibre_5
        elif calibre_tierra==calibre_6:
            costo_conductor_tierra=costo_calibre_6
        elif calibre_tierra==calibre_7:
            costo_conductor_tierra=costo_calibre_7
        elif calibre_tierra==calibre_8:
            costo_conductor_tierra=costo_calibre_8
        elif calibre_tierra==calibre_9:
            costo_conductor_tierra=costo_calibre_9
        elif calibre_tierra==calibre_10:
            costo_conductor_tierra=costo_calibre_10

        #paneles solares
        potencia_panel_1=200    #(watss)
        potencia_panel_2=250    #(watss)
        potencia_panel_3=300    #(watss)
        potencia_panel_4=350    #(watss)
        potencia_panel_5=400    #(watss)
        costo_panel_1=280000   #(pesos)
        costo_panel_2=370000   #(pesos)
        costo_panel_3=440000   #(pesos)
        costo_panel_4=520000   #(pesos)
        costo_panel_5=650000   #(pesos)
        if potencia_panel_solar==potencia_panel_1:
            costo_panel_solar=costo_panel_1
        elif potencia_panel_solar==potencia_panel_2:
            costo_panel_solar=costo_panel_2
        elif potencia_panel_solar==potencia_panel_3:
            costo_panel_solar=costo_panel_3
        elif potencia_panel_solar==potencia_panel_4:
            costo_panel_solar=costo_panel_4
        elif potencia_panel_solar==potencia_panel_5:
            costo_panel_solar=costo_panel_5

        #inversores
        potencia_inversor_1=1000     #(watss)
        potencia_inversor_2=1500     #(watss)
        potencia_inversor_3=2000     #(watss)
        potencia_inversor_4=2500     #(watss)
        potencia_inversor_5=3000     #(watss)
        costo_inversor_1=1150000    #(pesos)
        costo_inversor_2=1800000    #(pesos)
        costo_inversor_3=2700000    #(pesos)
        costo_inversor_4=3650000    #(pesos)
        costo_inversor_5=4535000    #(pesos)
        if potencia_inversor==potencia_inversor_1:
            costo_inversor=costo_inversor_1
        elif potencia_inversor==potencia_inversor_2:
            costo_inversor=costo_inversor_2
        elif potencia_inversor==potencia_inversor_3:
            costo_inversor=costo_inversor_3
        elif potencia_inversor==potencia_inversor_4:
            costo_inversor=costo_inversor_4
        elif potencia_inversor==potencia_inversor_5:
            costo_inversor=costo_inversor_5

        #otros
        costo_tuberia_galvanizada=13500       #(pesos)
        costo_tuberia_pvc=1800                #(pesos
        costo_varilla_coperwell=56000         #(pesos)
        costo_interruptor_diferencial=87500   #(pesos)

        #CALCULO COSTOS

        total_tablero=costo_tablero
        total_medidor=costo_medidor
        total_breakers_circuitos=costo_breaker_circuitos*numero_circuitos
        total_breaker_medidor=costo_breaker_medidor
        total_conductor_acometida=costo_conductor_acometida*longitud_acometida
        total_tuberia_galvanizada=costo_tuberia_galvanizada*longitud_acometida
        total_energia_red=total_tablero+total_medidor+total_breakers_circuitos+total_breaker_medidor+2*(total_conductor_acometida)+total_tuberia_galvanizada

        total_paneles_solares=costo_panel_solar*numero_paneles
        total_inversores=costo_inversor*numero_inversores
        total_breakers_inversores=costo_breaker_inversor*numero_inversores
        total_conductor_circuitos_paneles=float("{:.2f}".format(costo_conductor_circuitos_paneles*longitud_circuitos_paneles))
        total_conductor_acometida_paneles=costo_conductor_acometida_paneles*longitud_acometida_externa
        total_tuberia_pvc=float("{:.2f}".format(costo_tuberia_pvc*longitud_circuitos_paneles))
        total_tuberia_galvanizada_paneles=costo_tuberia_galvanizada*longitud_acometida_externa
        total_energia_paneles=total_paneles_solares+total_inversores+total_breakers_inversores+2*(total_conductor_circuitos_paneles)+2*(total_conductor_acometida_paneles)+total_tuberia_pvc+total_tuberia_galvanizada_paneles

        total_varilla_coperwell=costo_varilla_coperwell
        total_conductor_tierra=costo_conductor_tierra*longitud_acometida_interna
        total_interruptor_diferencial=costo_interruptor_diferencial
        total_puesta_tierra=total_varilla_coperwell+total_conductor_tierra+total_interruptor_diferencial

        presupuesto_total=total_energia_red+total_energia_paneles+total_puesta_tierra


        ventana7=Tk()      #ventana
        ventana7.title("Electrodomesticos")      #titulo de la ventana
        #ventana7.iconbitmap("archivo.ico")      #icono de la ventana (la imagen se deve converitr a formato .ico)
        ventana7.resizable(False,False)      #redimencionar la ventana 
        #ventana7.geometry("1200x800")      #geometria de la ventana
        ventana7.config(bg="blue")      #color de fondo de la ventana

        frame=Frame()      #frame
        frame.pack()      #empaquetado de rame
        frame.config(bg="orange")      #color de fondo del frame 
        frame.config(width="1400", height="800")      #geometria del frame
        frame.config(bd=25)      #ancho de borde del frame 
        frame.config(relief="groove")      #tipo de borde del frame
        frame.config(cursor="hand2")      #tipo de cursor de frame

        Label(frame, text="Proceso de calculo", bg="orange", fg="purple", font=("Comic Sans MS", 28)).place(x=200,y=30)  #texto corto

        imagen_1=PhotoImage(file="ecuaciones.PNG")      #imagen 1 (conversor online PNG y de tamaño)
        Label(frame, image=imagen_1).place(x=100,y=130)  #imagen

        def enviar3():
            ventana7.destroy()
        boton3=Button(frame, text="SIGUIENTE", bg="white", command=enviar3, fg="purple", font=("Comic Sans MS", 28))  #boton
        boton3.place(x=1080,y=20)


        ventana7.mainloop()


                                    #SALIDAS

        #sistema
        print("PRESUPUESTO")
        print()
        print("Tablero de distribución de: ", corriente_tablero, "amperios.", " Costo unitario de: ", costo_tablero, " Cantidad: 1", " Total: ", total_tablero)
        print("Medidor de: ", potencia_medidor, "watts.", " Costo unitario de: ", costo_medidor, " Cantidad: 1", " Total: ", total_medidor)
        print("Breaker de: ", breaker_circuitos, "amperios.", " Costo unitario de: ", costo_breaker_circuitos, " Cantidad: ", numero_circuitos, " Total: ", total_breakers_circuitos)
        print("Breaker (medidor) de: ", breaker_medidor, "amperios.", " Costo unitario de: ", costo_breaker_medidor, " Cantidad: 1", " Total: ", total_breaker_medidor)
        print("Conductor de: ", calibre_acometida, "awg negro (metros).", " Costo unitario de: ", costo_conductor_acometida, " Cantidad: ", longitud_acometida, " Total: ", total_conductor_acometida) 
        print("Conductor de: ", calibre_acometida, "awg blanco (metros).", " Costo unitario de: ", costo_conductor_acometida, " Cantidad: ", longitud_acometida, " Total: ", total_conductor_acometida)
        print("Tubería 3/4'' galvanizada (metros): ", " Costo unitario de: ", costo_tuberia_galvanizada, " Cantidad: ", longitud_acometida, " Total: ", total_tuberia_galvanizada)
        print("Total de materiales para distribución de energía por red: ", total_energia_red)
        print()
        print("Panel solar de: ", potencia_panel_solar, "watts con soporte.", " Costo unitario de: ", costo_panel_solar, " Cantidad: ", numero_paneles, " Total: ", total_paneles_solares)
        print("Inversor de: ", potencia_inversor, "watts.", " Costo unitario de: ", costo_inversor, " Cantidad: ", numero_inversores, " Total: ", total_inversores)
        print("Breaker (inversores) de: ", breaker_inversor, "amperios.", " Costo unitario de: ", costo_breaker_inversor, " Cantidad: ", numero_inversores, " Total: ", total_breakers_inversores)
        print("Conductor (circuitos de paneles) de: ", calibre_circuitos_paneles, "awg negro (metros).", " Costo unitario de: ", costo_conductor_circuitos_paneles, " Cantidad: ", longitud_circuitos_paneles, " Total: ", total_conductor_circuitos_paneles)
        print("Conductor (circuitos de paneles) de: ", calibre_circuitos_paneles, "awg blanco (metros).", " Costo unitario de: ", costo_conductor_circuitos_paneles, " Cantidad: ", longitud_circuitos_paneles, " Total: ", total_conductor_circuitos_paneles)
        print("Conductor (acometida paneles) de: ", calibre_acometida_paneles, "awg negro (metros).", " Costo unitario de: ", costo_conductor_acometida_paneles, " Cantidad: ", longitud_acometida_externa, " Total: ", total_conductor_acometida_paneles)
        print("Conductor (acometida paneles) de: ", calibre_acometida_paneles, "awg blanco (metros).", " Costo unitario de: ", costo_conductor_acometida_paneles, " Cantidad: ", longitud_acometida_externa, " Total: ", total_conductor_acometida_paneles)
        print("Tubería 1/2'' pvc recubierta (metros)", " Costo unitario de: ", costo_tuberia_pvc, " Cantidad: ", longitud_circuitos_paneles, " Total: ", total_tuberia_pvc)
        print("Tubería 3/4'' galvanizada (metros). ", "Costo unitario de: ", costo_tuberia_galvanizada, " Cantidad: ", longitud_acometida_externa, " Total: ", total_tuberia_galvanizada_paneles)
        print("Total de materiales para distribución de energía por paneles:", total_energia_paneles)
        print()
        print("Varilla coperwell 1/2'' 1.5 metros. ", "Costo unitario de: ", costo_varilla_coperwell, " Cantidad: 1 ", " Total: ", total_varilla_coperwell)
        print("Conductor (puesta a tierra) de: ", calibre_tierra, "awg verde (metros).", " Costo unitario de: ", costo_conductor_tierra, " Cantidad: ", longitud_acometida_interna, " Total: ", total_conductor_tierra)
        print("Interruptor diferencial",  "Costo unitario de: ", costo_interruptor_diferencial, " Cantidad: 1", " Total: ", total_interruptor_diferencial)
        print("Total de materiales para el sistema de puesto a tierra: ", total_puesta_tierra)
        print()
        print("Presupuesto total: ", presupuesto_total)
        print()
        
        print(longitud_acometida_interna)
        print(longitud_acometida_externa)
        print(breaker_circuitos)
        print(potencia_panel_solar)
        print(potencia_inversor)
        print(tiempo_luz_solar_optimo_diario)

        presupuesto=open(f"{nombre} presupuesto.txt","w")
        presupuesto.write("PRESUPUESTO"+"\n")
        presupuesto.write("  "+"\n")
        presupuesto.write("materiales de distribucion de energia por red"+"\n")
        presupuesto.write("Tablero de distribución de "+str(corriente_tablero)+" amperios."+"   Costo unitario:"+str(costo_tablero)+"  Cantidad:1"+"  Total:"+str(total_tablero)+"\n")
        presupuesto.write("Medidor de "+str(potencia_medidor)+" watts."+"   Costo unitario:"+str(costo_medidor)+"  Cantidad:1"+"  Total:"+str(total_medidor)+"\n")
        presupuesto.write("Breaker de "+str(breaker_circuitos)+" amperios."+"   Costo unitario:"+str(costo_breaker_circuitos)+"  Cantidad:"+str(numero_circuitos)+"  Total:"+str(total_breakers_circuitos)+"\n")
        presupuesto.write("Breaker (medidor) de "+str(breaker_medidor)+" amperios."+"   Costo unitario:"+str(costo_breaker_medidor)+"  Cantidad:1"+"  Total:"+str(total_breaker_medidor)+"\n")
        presupuesto.write("Conductor "+str(calibre_acometida)+" awg negro (metros)."+"   Costo unitario:"+str(costo_conductor_acometida)+"  Cantidad:"+str(longitud_acometida)+"  Total:"+str(total_conductor_acometida)+"\n")
        presupuesto.write("Conductor "+str(calibre_acometida)+" awg blanco (metros)."+"   Costo unitario:"+str(costo_conductor_acometida)+"  Cantidad:"+str(longitud_acometida)+"  Total:"+str(total_conductor_acometida)+"\n")
        presupuesto.write("Tubería 3/4'' galvanizada (metros)."+"   Costo unitario:"+str(costo_tuberia_galvanizada)+"  Cantidad:"+str(longitud_acometida)+"  Total:"+str(total_tuberia_galvanizada)+"\n")
        presupuesto.write("Total de materiales para distribución de energía por red:"+str(total_energia_red)+"\n")
        presupuesto.write("  "+"\n")
        presupuesto.write("materiales de distribucion de energia solar"+"\n")
        presupuesto.write("Panel solar de "+str(potencia_panel_solar)+" watts con soporte."+"   Costo unitario:"+str(costo_panel_solar)+"  Cantidad:"+str(numero_paneles)+"  Total:"+str(total_paneles_solares)+"\n")
        presupuesto.write("Inversor de "+str(potencia_inversor)+" watts."+"   Costo unitario de:"+str(costo_inversor)+"  Cantidad:"+str(numero_inversores)+"  Total:"+str(total_inversores)+"\n")
        presupuesto.write("Breaker (inversores) de "+str(breaker_inversor)+" amperios."+"   Costo unitario de:"+str(costo_breaker_inversor)+"  Cantidad:"+str(numero_inversores)+"  Total:"+str(total_breakers_inversores)+"\n")
        presupuesto.write("Conductor (circuitos de paneles) de "+str(calibre_circuitos_paneles)+" awg negro (metros)."+"   Costo unitario:"+str(costo_conductor_circuitos_paneles)+"  Cantidad:"+str(longitud_circuitos_paneles)+"  Total:"+str(total_conductor_circuitos_paneles)+"\n")
        presupuesto.write("Conductor (circuitos de paneles) de "+str(calibre_circuitos_paneles)+" awg blanco (metros)."+"   Costo unitario:"+str(costo_conductor_circuitos_paneles)+"  Cantidad:"+str(longitud_circuitos_paneles)+"  Total:"+str(total_conductor_circuitos_paneles)+"\n")
        presupuesto.write("Conductor (acometida paneles) de "+str(calibre_acometida_paneles)+" awg negro (metros)."+"   Costo unitario:"+str(costo_conductor_acometida_paneles)+"  Cantidad:"+str(longitud_acometida_externa)+"  Total:"+str(total_conductor_acometida_paneles)+"\n")
        presupuesto.write("Conductor (acometida paneles) de "+str(calibre_acometida_paneles)+" awg blanco (metros)."+"   Costo unitario:"+str(costo_conductor_acometida_paneles)+"  Cantidad:"+str(longitud_acometida_externa)+"  Total:"+str(total_conductor_acometida_paneles)+"\n")
        presupuesto.write("Tubería 1/2'' pvc recubierta (metros)."+"   Costo unitario:"+str(costo_tuberia_pvc)+"  Cantidad:"+str(longitud_circuitos_paneles)+"  Total:"+str(total_tuberia_pvc)+"\n")
        presupuesto.write("Tubería 3/4'' galvanizada (metros)."+"   Costo unitario:"+str(costo_tuberia_galvanizada)+"  Cantidad:"+str(longitud_acometida_externa)+"  Total:"+str(total_tuberia_galvanizada_paneles)+"\n")
        presupuesto.write("Total de materiales para distribución de energía solar.:"+str(total_energia_paneles)+"\n")
        presupuesto.write("  "+"\n")
        presupuesto.write("materiales de puesta a tierra"+"\n")
        presupuesto.write("Varilla coperwell 1/2'' 1.5 metros. "+"   Costo unitario"+str(costo_varilla_coperwell)+"  Cantidad:1"+"  Total:"+str(total_varilla_coperwell)+"\n")
        presupuesto.write("Conductor (puesta a tierra) "+str(calibre_tierra)+" awg verde (metros)."+"   Costo unitario:"+str(costo_conductor_tierra)+"  Cantidad:"+str(longitud_acometida_interna)+"  Total:"+str(total_conductor_tierra)+"\n")
        presupuesto.write("Interruptor diferencial."+"   Costo unitario:"+str(costo_interruptor_diferencial)+"  Cantidad:1"+"  Total:"+str(total_interruptor_diferencial)+"\n")
        presupuesto.write("Total de materiales de puesto a tierra:"+str(total_puesta_tierra)+"\n")
        presupuesto.write("  "+"\n")
        presupuesto.write("Presupuesto total: "+str(presupuesto_total)+"\n")
        presupuesto.close

        


        ventana=Tk()
        ventana.title("presupuesto")
        #ventana.geometry("1200x800")
        ventana.resizable(0,0)
        ventana.config(bg="blue")

        miframe=Frame()
        miframe.pack()
        miframe.config(bg="orange")
        miframe.config(width="1400", height="800")
        miframe.config(bd=25)
        miframe.config(relief="groove")

        Label(miframe, text="PRESUPUESTO", bg="white", fg="purple", font=("Comic Sans MS", 28)).place(x=500,y=10)

        #SISTEMA
        Label(miframe, text="SISTEMA", bg="white", fg="purple", font=("Comic Sans MS", 16)).place(x=10,y=100)
        Label(miframe, text="tablero", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=10,y=200)
        Label(miframe, text="medidor", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=10,y=220)
        Label(miframe, text="acometida", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=10,y=240)
        Label(miframe, text="acometida", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=10,y=260)
        Label(miframe, text="inversores", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=10,y=400)
        Label(miframe, text="circuito paneles", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=10,y=420)
        Label(miframe, text="circuito paneles", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=10,y=440)
        Label(miframe, text="acometida paneles", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=10,y=460)
        Label(miframe, text="acometida paneles", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=10,y=480)
        Label(miframe, text="circuito paneles", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=10,y=500)
        Label(miframe, text="acometida paneles", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=10,y=520)
        Label(miframe, text="puesta a tierra", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=10,y=620)
       
        #MATERIALES
        Label(miframe, text="MATERIALES", bg="white", fg="purple", font=("Comic Sans MS", 16)).place(x=160,y=100)
        Label(miframe, text="energia por red", bg="light coral", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=140)
        Label(miframe, text="tablero de distribucion", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=160)
        Label(miframe, text="medidor", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=180)
        Label(miframe, text="breaker", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=200)
        Label(miframe, text="breaker", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=220)
        Label(miframe, text="conductor negro (metros)", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=240)
        Label(miframe, text="conductor blanco(metros)", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=260)
        Label(miframe, text="tuberia 3/4 galvanizada (metros)", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=280)
        Label(miframe, text="total materiales energia por red", bg="light coral", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=300)
        Label(miframe, text="energia solar", bg="light blue", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=340)
        Label(miframe, text="panel solar con soporte", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=360)
        Label(miframe, text="inversor", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=380)
        Label(miframe, text="breaker", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=400)
        Label(miframe, text="conductor negro (metros)", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=420)
        Label(miframe, text="conductor blanco (metros)", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=440)
        Label(miframe, text="conductor negro (metros)", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=460)
        Label(miframe, text="conductor blanco (metros)", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=480)
        Label(miframe, text="tuberia 1/2 pvc recubierta (metros)", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=500)
        Label(miframe, text="tuberia 3/4 galvanizada (metros)", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=520)
        Label(miframe, text="total materiales energia solar", bg="light blue", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=540)
        Label(miframe, text="puesta a tierra", bg="light green", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=580)
        Label(miframe, text="varilla coperwell 1/2 1.5 metros", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=600)
        Label(miframe, text="conductor verde (metros)", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=620)
        Label(miframe, text="interruptor diferencial", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=640)
        Label(miframe, text="total materiles puesta a tierra", bg="light green", fg="black", font=("Comic Sans MS", 10)).place(x=160,y=660)
        
        #CALIBRES
        Label(miframe, text="AWG", bg="white", fg="purple", font=("Comic Sans MS", 16)).place(x=400,y=100)
        Label(miframe, text=calibre_acometida, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=400,y=240)
        Label(miframe, text=calibre_acometida, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=400,y=260)
        Label(miframe, text=calibre_circuitos_paneles, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=400,y=420)
        Label(miframe, text=calibre_circuitos_paneles, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=400,y=440)
        Label(miframe, text=calibre_acometida_paneles, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=400,y=460)
        Label(miframe, text=calibre_acometida_paneles, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=400,y=480)
        Label(miframe, text=calibre_tierra, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=400,y=620)
        
        #POTENCIAS
        Label(miframe, text="WATTS", bg="white", fg="purple", font=("Comic Sans MS", 16)).place(x=490,y=100)
        Label(miframe, text=potencia_medidor, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=490,y=180)
        Label(miframe, text=potencia_panel_solar, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=490,y=360)
        Label(miframe, text=potencia_inversor, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=490,y=380)
        
        #CORRIENTES
        Label(miframe, text="AMPS", fg="purple", font=("Comic Sans MS", 16)).place(x=600,y=100)
        Label(miframe, text=corriente_tablero, fg="black", font=("Comic Sans MS", 10)).place(x=600,y=160)
        Label(miframe, text=breaker_circuitos, fg="black", font=("Comic Sans MS", 10)).place(x=600,y=200)
        Label(miframe, text=breaker_medidor, fg="black", font=("Comic Sans MS", 10)).place(x=600,y=220)
        Label(miframe, text=breaker_inversor, fg="black", font=("Comic Sans MS", 10)).place(x=600,y=400)
        
        #COSTOS UNITARIOS
        Label(miframe, text="COSTO UNITARIO", bg="white", fg="purple", font=("Comic Sans MS", 16)).place(x=720,y=100)
        Label(miframe, text=costo_tablero, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=720,y=160)
        Label(miframe, text=costo_medidor, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=720,y=180)
        Label(miframe, text=costo_breaker_circuitos, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=720,y=200)
        Label(miframe, text=costo_breaker_medidor, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=720,y=220)
        Label(miframe, text=costo_conductor_acometida, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=720,y=240)
        Label(miframe, text=costo_conductor_acometida, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=720,y=260)
        Label(miframe, text=costo_tuberia_galvanizada, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=720,y=280)
        Label(miframe, text=costo_panel_solar, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=720,y=360)
        Label(miframe, text=costo_inversor, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=720,y=380)
        Label(miframe, text=costo_breaker_inversor, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=720,y=400)
        Label(miframe, text=costo_conductor_circuitos_paneles, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=720,y=420)
        Label(miframe, text=costo_conductor_circuitos_paneles, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=720,y=440)
        Label(miframe, text=costo_conductor_acometida_paneles, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=720,y=460)
        Label(miframe, text=costo_conductor_acometida_paneles, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=720,y=480)
        Label(miframe, text=costo_tuberia_pvc, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=720,y=500)
        Label(miframe, text=costo_tuberia_galvanizada, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=720,y=520)
        Label(miframe, text=costo_varilla_coperwell, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=720,y=600)
        Label(miframe, text=costo_conductor_tierra, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=720,y=620)
        Label(miframe, text=costo_interruptor_diferencial, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=720,y=640)
        
        #CANTIDADES
        Label(miframe, text="CANTIDAD", bg="white", fg="purple", font=("Comic Sans MS", 16)).place(x=990,y=100)
        Label(miframe, text="1", fg="black", bg="white", font=("Comic Sans MS", 10)).place(x=990,y=160)
        Label(miframe, text="1", fg="black", bg="white", font=("Comic Sans MS", 10)).place(x=990,y=180)
        Label(miframe, text=numero_circuitos, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=990,y=200)
        Label(miframe, text="1", fg="black", bg="white", font=("Comic Sans MS", 10)).place(x=990,y=220)
        Label(miframe, text=longitud_acometida, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=990,y=240)
        Label(miframe, text=longitud_acometida, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=990,y=260)
        Label(miframe, text=longitud_acometida, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=990,y=280)
        Label(miframe, text=numero_paneles, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=990,y=360)
        Label(miframe, text=numero_inversores, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=990,y=380)
        Label(miframe, text=numero_inversores, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=990,y=400)
        Label(miframe, text=longitud_circuitos_paneles, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=990,y=420)
        Label(miframe, text=longitud_circuitos_paneles, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=990,y=440)
        Label(miframe, text=longitud_acometida_externa, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=990,y=460)
        Label(miframe, text=longitud_acometida_externa, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=990,y=480)
        Label(miframe, text=longitud_circuitos_paneles, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=990,y=500)
        Label(miframe, text=longitud_acometida_externa, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=990,y=520)
        Label(miframe, text="1", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=990,y=600)
        Label(miframe, text=longitud_acometida_interna, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=990,y=620)
        Label(miframe, text="1", bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=990,y=640)
        
        #COSTOS TOTALES
        Label(miframe, text="COSTO TOTAL", bg="white", fg="purple", font=("Comic Sans MS", 16)).place(x=1170,y=100)
        Label(miframe, text=total_tablero, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=160)
        Label(miframe, text=total_medidor, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=180)
        Label(miframe, text=total_breakers_circuitos, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=200)
        Label(miframe, text=total_breaker_medidor, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=220)
        Label(miframe, text=total_conductor_acometida, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=240)
        Label(miframe, text=total_conductor_acometida, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=260)
        Label(miframe, text=total_tuberia_galvanizada, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=280)
        Label(miframe, text=total_energia_red, bg="light coral", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=300)
        Label(miframe, text=total_paneles_solares, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=360)
        Label(miframe, text=total_inversores, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=380)
        Label(miframe, text=total_breakers_inversores, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=400)
        Label(miframe, text=total_conductor_circuitos_paneles, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=420)
        Label(miframe, text=total_conductor_circuitos_paneles, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=440)
        Label(miframe, text=total_conductor_acometida_paneles, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=460)
        Label(miframe, text=total_conductor_acometida_paneles, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=480)
        Label(miframe, text=total_tuberia_pvc, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=500)
        Label(miframe, text=total_tuberia_galvanizada_paneles, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=520)
        Label(miframe, text=total_energia_paneles, bg="light blue", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=540)
        Label(miframe, text=total_varilla_coperwell, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=600)
        Label(miframe, text=total_conductor_tierra, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=620)
        Label(miframe, text=total_interruptor_diferencial, bg="white", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=640)
        Label(miframe, text=total_puesta_tierra, bg="light green", fg="black", font=("Comic Sans MS", 10)).place(x=1170,y=660)
        
        #presupuesto
        Label(miframe, text="PRESUPUESTO TOTAL", bg="white", fg="purple", font=("Comic Sans MS", 16)).place(x=160,y=700)
        Label(miframe, text=total_puesta_tierra+total_energia_paneles+total_energia_red, bg="white", fg="purple", font=("Comic Sans MS", 16)).place(x=1170,y=700)

        

        def enviar5():
            ventana.destroy()
        boton1=Button(miframe, text="SIGUIENTE", bg="white", command=enviar5, fg="purple", font=("Comic Sans MS", 22))  #boton
        boton1.place(x=1140,y=10)
                        
        ventana.mainloop()
                          


    aelec()
    entradas()
    formulas()
    def menu():
        menu_1()
        d=texto1
        print(d)
        if d=="a":
            aelec()
            formulas()
            menu()
        elif d=="b":
            entradas()
            formulas()
            menu()

    menu()
ventana_inicio() 
    
            
        
    
    


