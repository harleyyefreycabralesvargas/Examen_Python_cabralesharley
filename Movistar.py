import json
def abrirJSON():
    dicFinal={}
    with open("./BaseDeDatos.Json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal
def guardarJSON(dic):
    with open("./BaseDeDatos.Json",'w') as outFile:
        json.dump(dic,outFile)
d={}

zzz=False
while zzz==False:
 d=abrirJSON()
 print("Bienvenido a movistar ")
 print(len(d["clientes"]))
 acceso=False
 persona1=int(input("Para iniciar sesion cual eres 1.Usuario, 2.operador"))
 if persona1==1:
     identificacion1=int(input("Dame tu ID: "))
     contraseña1=int(input("Dame tu contraseña: "))
     for i in range(len(d["clientes"])):
         f=str(i)
         if identificacion1==d["clientes"][f]["id"]:
             a=f
     if contraseña1==d["clientes"][a]["contraseña"]:
         acceso=True
         z1=True
     while z1==True:
      if acceso==True:
          print("Menu")
          print("0. Cerrar sesion")
          print("1. ver tu informacion")
          print("2. Presentar una queja")
          print("3. Ver y compar servicios")
          opcion1=int(input("Cual deseas hacer"))
          if opcion1==0:
              z1=False

          if opcion1==1:
               idd1=d["clientes"][f]["id"]
               con1=d["clientes"][f]["contraseña"]
               nom1=d["clientes"][f]["nombre"]
               apl1=d["clientes"][f]["apellidos"]
               dir1=d["clientes"][f]["direccion"]
               tel1=d["clientes"][f]["telefono"]
               cat1=d["clientes"][f]["categoria"]
               ser1=d["clientes"][f]["servicio"]
               que1=d["clientes"][f]["quejas"]
               tie1=d["clientes"][f]["tiempo"]
               print("ID: ",idd1," Contraseña: ",con1," Nombre: ",nom1," Apellidos: ",apl1," Direccion: ",dir1," Telefono: ",tel1,"Categoria: ",cat1," Servicio: ",ser1," Quejas: ",que1," Tiempo: ",tie1)
          if opcion1==2:
              queja1=input("Cual es la queja que tienes")
              d["clientes"][f]["quejas"]=queja1
              guardarJSON(d)
          if d["clientes"][f]["categoria"]=="cliente regular":
              precio=precio*0.95
              
              
          if opcion1==3:
              print(d["servicios"])
              s=input("Cual servicio quieres comprar")
              cu1=d["servicios"][s]["adquirido"]
              d["servicios"][s]["adquirido"]=cu1+1
              d["clientes"][a]["servicio"]=d["servicios"][s]
              guardarJSON(d)

          if acceso==False:
             print("contraseña o usuario incorretco")
      
 if persona1==2:
   identificacion1=int(input("Dame tu ID: "))
   contraseña1=int(input("Dame tu contraseña: "))
   for i in range(len(d["operador"])):
       f=str(i)
       if identificacion1==d["operador"][f]["id"]:
           a=f
   if contraseña1==d["operador"][a]["contraseña"]:
       acceso=True
       z1=True
   while z1==True:
    if acceso==True:
        print("Menu")
        print("0. cerrar sesion")
        print("1. ver tu infotmacion")
        print("2. añadir servicios")    
        print("3. añadir clientes")    
        opcion2=int(input("Cual opcion quieres hacer"))  
        if opcion2==0:
            z1=False
 
        if opcion2==1:
              idd1=d["operador"][f]["id"]
              con1=d["operador"][f]["contraseña"]
              nom1=d["operador"][f]["nombre"]
              apl1=d["operador"][f]["apellidos"]
              print("ID: ",idd1," Contraseña: ",con1," Nombre: ",nom1," Apellidos: ",apl1)
        if opcion2==2:
            s=str(len(d["servicios"]))
            servicio1=input("cual es el nuevo servicio: ")
            precio1=int(input("Cual es el precio: "))
            d["servicios"][s]={
                "servicio":servicio1,
                "precio":precio1,
                "adquirido":0
            }
            guardarJSON(d) 
        if opcion2==3:
            s=len(d["clientes"])
            print("la ID nueva es ",s)
            d["clientes"][s]={
             "id":s,
             "contraseña":int(input("cual es la cpntraseña a asignar")),
             "nombre":input("cual es el nombre de nuevo cliente"),
             "apellidos":input("cuales son los apellidos del nuevo cliente"),
             "direccion":input("cual es la direccion de nuevo cliente"),
             "telefono":input("cual es el telefono de nuevo cliente"),
             "categoria":"cliente nuevo",
             "servicio":"",
             "quejas":"",
             "tiempo":"0"
             }
            guardarJSON(d)
            
            

              
   if acceso==False:
       print("contraseña o usuario incorretco")
   
  #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