print("hola bienvenido vamos ha hacer calculos eletricos")
print()
import re
import os
import winsound
from io import open
dic={}
pu={}
pt=0
et=0
longitud_acometida_interna=0
longitud_acometida_externa=0
breaker_circuitos=0
potencia_panel_solar=0
potencia_inversor=0
tiempo_luz_solar_optimo_diario=0

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
def actualizar(a,b):
    registro=open("registro.txt","a")
    registro.write (a + ":" + b + "\n" )
    

def borrar():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
   
def registrar():
    global dic
    print("El usuario que registre debera tener mas de 2 caracteres.")
    a=input("Ingrese el nombre de usuario con el que quiere ser registrado: ")
    if dic.get(a,False) == False:
        if len(a)>=2:
            def registroc():
                print("La contaseña que registre debera tener almenos una letra y un numero.")
                b=input("Ingrese la contraseña con que quiere ser registrado: ")
                c1=0
                c2=0
                for i in b:
                    if re.search("[a-z]",i) or re.search("[A-Z]",i):
                        c1=c1+1
                    if re.search("[0-9]",i):
                        c2=c2+1
                if c1>=1 and c2>=1:
                    actualizar(a,b)
                    print("Registro exitoso.")
                    c=input("Si dessea salir del programa ingrese (a) si quiere volver al inicio presione enter: ")
                    borrar()
                    if c == "a":
                        salir()
                    
                    
                else:
                    winsound.Beep(100, 500)
                    print("La contraseña no cuenta con los parametros establecidos, oprima enter para intentarlo otra vez")
                    input()
                    borrar()
                    registroc()
            registroc()
        else:
            winsound.Beep(100, 500)
            print("El nombre de usuario no cuenta con los parametros establecidos, oprima enter para intentarlo otra vez")
            input()
            borrar()
            registrar()

    else:
        winsound.Beep(100, 500)
        print("Este nombre de usuario ya se encuentra registrado, use otro, oprima enter para intentarlo otra vez")
        input()
        borrar()
        registrar()
        
def ingreso():
    global dic
    a=input("Ingrese su nombre de usuario: ")
    b=dic.get(a,False)
    if b != False:
        def ingresoc():
            c1=0
            c=input("Ingrese su contraseña: ")
            if b == c:
                print("Felicitaciones ingreso exitoso.")
                prop(a)
                ca=input("Si dessea salir del programa ingrese (a) si quiere volver al inicio presione enter: ")
                borrar()
                if ca == "a":
                    salir()
            elif c1<2:
                c1=c1+1
                winsound.Beep(100, 500)
                d = input(f"Contraseña incorrecta {c1} veces (si falla 3 veces sera devuelto al inicio),si desea intentarlo otra vez ingrese (a) si quiere volver al inicio oprima enter: ")
                if d == "a":
                    borrar()
                    ingresoc()
        ingresoc()
    else:
        winsound.Beep(100, 500)
        e=input("Usuario no registrado, si desea intentarlo otra vez ingrese (a) si quiere volver al inicio oprima enter: ")
        if e == "a":
            borrar()
            ingreso()
def salir():
    global vc
    vc=False

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
        ne=int(input("Escriba cuantos electrodomesticos va a ingresar: "))
        for i in range(ne):
            a=input("Electrodomestico: ")
            b=int(input("Potencia en w: "))
            c=float(input("Uso en horas al dia: "))
            elec=open(f"{nombre} electrodomésticos.txt","a")
            elec.write(a + ":" + str(b) + ":" + str(c)+"\n")
            elec.close()
        global pu
        elec=open(f"{nombre} electrodomésticos.txt","r")
        ielec=elec.read()
        elec.close()
        lelec=ielec.split()
        for f in lelec:
            lc=f.split(":")
            pu[lc[1]]=lc[2]
        ps=list(pu.keys())
        us=list(pu.values())
        for x in range(len(ps)):
            if x>=1:
                pt=pt+int(ps[x])
                et=et+float(us[x])*int(ps[x])
            else:
                pt=int(ps[x])
                et=float(us[x])*int(ps[x])

        
        print()
        print("electrodomésticos:potencia:uso diaro en horas")       
        print(ielec)
        print(f"Potencia total {pt}w")
        print(f"Energia total {et}w/h")
        print()

        

    def entradas():
        global longitud_acometida_interna
        global longitud_acometida_externa
        global breaker_circuitos
        global potencia_panel_solar
        global potencia_inversor
        global tiempo_luz_solar_optimo_diario
        longitud_acometida_interna=int(input("ingrese la longitud de la acometida interna en metros: "))
        longitud_acometida_externa=int(input("ingrese la longitud de la acometida externa en metros: "))
        breaker_circuitos=int(input("ingrese uno de estos valores 10,15,20,25,30 en amperios para los breakers de los circuitos: "))
        potencia_panel_solar=int(input("ingrese uno de estos valores 200,250,300,350,400 en watts para elejir el tipo de panel solar: "))
        potencia_inversor=int(input("ingrese uno de estos valores 1000,1500,2000,2500,3000 en watts para elejir el tipo de inversor: "))
        tiempo_luz_solar_optimo_diario=int(input("ingrese el promedio de tiempo de luz solar optima diario que hay en tu zona en horas: "))
        print()
        print()
    def formulas():
        #FORMULAS

        #LEYES

        #ley de energia
        energia_diaria_wh=et #(watts-hora)
        energia_diaria_kwh=energia_diaria_wh/1000  #(kilowatts-hora)
        energia_mensual_kwh=energia_diaria_kwh*30  #(kilowatts-hora)
 
        #ley de watt
        import math
        potencia_total=pt #(watts)
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
        total_conductor_circuitos_paneles=costo_conductor_circuitos_paneles*longitud_circuitos_paneles
        total_conductor_acometida_paneles=costo_conductor_acometida_paneles*longitud_acometida_externa
        total_tuberia_pvc=costo_tuberia_pvc*longitud_circuitos_paneles
        total_tuberia_galvanizada_paneles=costo_tuberia_galvanizada*longitud_acometida_externa
        total_energia_paneles=total_paneles_solares+total_inversores+total_breakers_inversores+2*(total_conductor_circuitos_paneles)+2*(total_conductor_acometida_paneles)+total_tuberia_pvc+total_tuberia_galvanizada_paneles

        total_varilla_coperwell=costo_varilla_coperwell
        total_conductor_tierra=costo_conductor_tierra*longitud_acometida_interna
        total_interruptor_diferencial=costo_interruptor_diferencial
        total_puesta_tierra=total_varilla_coperwell+total_conductor_tierra+total_interruptor_diferencial

        presupuesto_total=total_energia_red+total_energia_paneles+total_puesta_tierra
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

        print("Conductor de: ", calibre_acometida, "awg negro (metros).", " Costo unitario de: ", costo_conductor_acometida, " Cantidad: ", longitud_acometida, " Total: ", total_conductor_acometida)

        print("Tubería 3/4'' galvanizada (metros). ", "Costo unitario de: ", costo_tuberia_galvanizada, " Cantidad: ", longitud_acometida_externa, " Total: ", total_tuberia_galvanizada_paneles)

        print("Total de materiales para distribución de energía por paneles:", total_energia_paneles)
        print()
        print("Conductor de: ", calibre_acometida, "awg negro (metros).", " Costo unitario de: ", costo_conductor_acometida, " Cantidad: ", longitud_acometida, " Total: ", total_conductor_acometida)

        print("Varilla coperwell 1/2'' 1.5 metros. ", "Costo unitario de: ", costo_varilla_coperwell, " Cantidad: 1 ", " Total: ", total_varilla_coperwell)

        print("Conductor (puesta a tierra) de: ", calibre_tierra, "awg verde (metros).", " Costo unitario de: ", costo_conductor_tierra, " Cantidad: ", longitud_acometida_interna, " Total: ", total_conductor_tierra)

        print("Interruptor diferencial",  "Costo unitario de: ", costo_interruptor_diferencial, " Cantidad: 1", " Total: ", total_interruptor_diferencial)

        print("Total de materiales para el sistema de puesto a tierra: ", total_puesta_tierra)

        print()
        print("Presupuesto total: ", presupuesto_total)
        print()


    aelec()
    entradas()
    formulas()
    def menu():
        d=input("Si desea agregar mas electrodomesticos ingrese (a), si desea ingresar otros datos electricos perione (b), si no oprima enter: ")
        borrar()
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
     
            
        
    
    
vc = True
ex=os.path.isfile("registro.txt")
if ex != True:
    registro=open("registro.txt","w") 
    registro.close
while vc:
    leer()
    print("Bienvenido \n a.Registrarse \n b.Ingresar \n c.Salir")
    a=input("Ingrese (a), (b) o (c) segun lo que quiera hacer: ")
    if a == "a":
        registrar()
    elif a == "b":
        ingreso()
    elif a == "c":
        salir()
    else:
        print("Caracter no valido, solo (a), (b) o (c) oprima enter para intentarlo otra vez.")
        winsound.Beep(100, 500)
        input()
        borrar()
input("Hasta la proximaaaaa, presione enter para cerrar el programa.")
