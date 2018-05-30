from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
 
db = GraphDatabase("http://localhost:7474", username="neo4j", password="mypassword")

#Categorias
TipoComida = db.labels.create("TipoComida")
Situacion = db.labels.create("Situacion")
Presupuesto = db.labels.create("Presupuesto")
Ambiente = db.labels.create("Ambiente")
Sentimientos= db.labels.create("Sentimientos")
Restaurantes = db.labels.create("Restaurantes")
Usuario = db.labels.create("Usuario")

#USUARIOS EN BASE DE DATOS
Rodrigo = db.nodes.create(name="Rodrigo Morales")
Oscar = db.nodes.create(name="Oscar Juarez")
Usuario.add(Rodrigo,Oscar)

#TODOS LOS TIPOS DE COMIDA
Pizza=db.nodes.create(name="Pizza")
Pollo =db.nodes.create(name="Pollo")
Hamburguesas =db.nodes.create(name="Hamburguesas")
Tacos=db.nodes.create(name="Tacos")
Pasta=db.nodes.create(name="Pasta")
Asados=db.nodes.create(name="Asados")
Suchi=db.nodes.create(name="Suchi")
ComidaChina=db.nodes.create(name="ComidaChina")
Vegetariano=db.nodes.create(name="Vegetariano")
Sandwich=db.nodes.create(name="Sandwich")
Crepes=db.nodes.create(name="Crepes")

TipoComida.add(Pizza,Pollo,Hamburguesas,Tacos,Pasta,Asados,Suchi,ComidaChina,Vegetariano,Sandwich,Crepes)

#TODAS LAS SITUACIONES

Pareja=db.nodes.create(name="Pareja")
ParejaJoven=db.nodes.create(name="ParejaJoven")
Amigos=db.nodes.create(name="Amigos")
Familia=db.nodes.create(name="Familia")
Adultos=db.nodes.create(name="Adultos")

Situacion.add(Pareja,ParejaJoven,Amigos,Familia,Adultos)

#TODOS LOS PRESUPUESTOS 

Alto=db.nodes.create(name="Alto")
Medio=db.nodes.create(name="Medio")
Bajo=db.nodes.create(name="Bajo")
Promociones=db.nodes.create(name="Promociones")

Presupuesto.add(Alto,Medio,Bajo,Promociones)

#AMBIENTE

AireLibre=db.nodes.create(name="AireLibre")
Karaoke=db.nodes.create(name="Karaoke")
Tematico=db.nodes.create(name="Tematico")
ComidaRapida=db.nodes.create(name="ComidaRapida")
Bar=db.nodes.create(name="Bar")
Romantico=db.nodes.create(name="Romantico")
Serio=db.nodes.create(name="Serio")

Ambiente.add(AireLibre,Karaoke,Tematico,ComidaRapida,Bar,Romantico,Serio)

#Restaurantes

BurgerKing=db.nodes.create(name="BurgerKing")
Trefratelli=db.nodes.create(name="Trefratelli")
Elpinche=db.nodes.create(name="Elpinche")
Mcdonalds=db.nodes.create(name="Mcdonalds")
Subway=db.nodes.create(name="Subway")
Saul=db.nodes.create(name="Saul")
TacoBell=db.nodes.create(name="Taco Bell")
Italiannis=db.nodes.create(name="Italiannis")
PandaExpresss=db.nodes.create(name="Panda Express")
Dominos=db.nodes.create(name="Dominos")
Restaurantes.add(BurgerKing,Trefratelli,Elpinche,Mcdonalds,Subway,Saul,TacoBell,Italiannis,PandaExpresss,Dominos)

#Dominos
ComidaRapida.relationships.create("a",Dominos)
Familia.relationships.create("a",Dominos)
Amigos.relationships.create("a",Dominos)
Pizza.relationships.create("a",Dominos)
Bajo.relationships.create("a",Dominos)
Promociones.relationships.create("a",Dominos)
Rodrigo.relationships.create("a",Dominos)

#Panda Express
ComidaChina.relationships.create("a",PandaExpresss)
ComidaRapida.relationships.create("a",PandaExpresss)
Familia.relationships.create("a",PandaExpresss)
Bajo.relationships.create("a",PandaExpresss)
Promociones.relationships.create("a",PandaExpresss)
Amigos.relationships.create("a",PandaExpresss)
Adultos.relationships.create("a",PandaExpresss)

#Trefratelli
Pasta.relationships.create("a",Trefratelli)
Pareja.relationships.create("a",Trefratelli)
Familia.relationships.create("a",Trefratelli)
Adultos.relationships.create("a",Trefratelli)
Medio.relationships.create("a",Trefratelli)
Promociones.relationships.create("a",Trefratelli)
Romantico.relationships.create("a",Trefratelli)
Bar.relationships.create("a",Trefratelli)
Serio.relationships.create("a",Trefratelli)
Oscar.relationships.create("a",Trefratelli)

#El pinche
Tacos.relationships.create("a",Elpinche)
Amigos.relationships.create("a",Elpinche)
Familia.relationships.create("a",Elpinche)
ParejaJoven.relationships.create("a",Elpinche)
Medio.relationships.create("a",Elpinche)
Tematico.relationships.create("a",Elpinche)


#Mcdonalds
Hamburguesas.relationships.create("a",Mcdonalds)
Amigos.relationships.create("a",Mcdonalds)
Familia.relationships.create("a",Mcdonalds)
Bajo.relationships.create("a",Mcdonalds)
ComidaRapida.relationships.create("a",Mcdonalds)

#Subway
Sandwich.relationships.create("a",Subway)
Amigos.relationships.create("a",Subway)
Promociones.relationships.create("a",Subway)
Familia.relationships.create("a",Subway)
Bajo.relationships.create("a",Subway)
ComidaRapida.relationships.create("a",Subway)

#BurgerKing
Hamburguesas.relationships.create("a",BurgerKing)
Amigos.relationships.create("a",BurgerKing)
Familia.relationships.create("a",BurgerKing)
Bajo.relationships.create("a",BurgerKing)
ComidaRapida.relationships.create("a",BurgerKing)

#Italiannis
Pasta.relationships.create("a",Italiannis)
Familia.relationships.create("a",Italiannis)
Pareja.relationships.create("a",Italiannis)
Adultos.relationships.create("a",Italiannis)
Medio.relationships.create("a",Italiannis)
Romantico.relationships.create("a",Italiannis)
Bar.relationships.create("a",Italiannis)
Serio.relationships.create("a",Italiannis)

#Saul
Crepes.relationships.create("a",Saul)
Pareja.relationships.create("a",Saul)
Adultos.relationships.create("a",Saul)
ParejaJoven.relationships.create("a",Saul)
Medio.relationships.create("a",Saul)
Serio.relationships.create("a",Saul)
Romantico.relationships.create("a",Saul)
AireLibre.relationships.create("a",Saul)

#Taco Bell
Tacos.relationships.create("a",TacoBell)
Amigos.relationships.create("a",TacoBell)
Bajo.relationships.create("a",TacoBell)
ComidaRapida.relationships.create("a",TacoBell)
Familia.relationships.create("a",TacoBell)

def recomedacion(nombre,ambiente,situacion,presupuesto,tipoComida):
    restaurantes={} #Se crea un diccionacio de restaurantes
    #Obtener todos los restaurantes
    q = 'MATCH (u: Restaurantes) RETURN u'
    results = db.query(q, returns=(client.Node))
    #Se agregan todos los restaurantes
    for i in results:
        restaurantes[i[0]["name"]]=0
    #--------------------------------- En base a tus amigos restaurantes-------------------------------------------------------#
    q = 'MATCH (u:Usuario)-[r:a]->(m:Usuario) WHERE u.name="'+nombre+'"RETURN u, type(r), m'
    amigos = db.query(q, returns=(client.Node,str,client.Node))
    for i in amigos:
        q = 'MATCH (u:Usuario)-[r:a]->(m:Restaurantes) WHERE u.name="'+i[0]["name"]+'"RETURN u, type(r), m'
        referenciados = db.query(q, returns=(client.Node,str,client.Node))
        for j in referenciados:
                #Obtener  todos las situaciones de restaurante
                q = 'MATCH (u:Situacion)-[r:a]->(m:Restaurantes) WHERE m.name="'+j[2]["name"]+'" RETURN u, type(r), m'
                results1 = db.query(q, returns=(client.Node, str, client.Node))
                for k in results1:
                    q = 'MATCH (u:Situacion)-[r:a]->(m:Restaurantes) WHERE u.name="'+k[0]["name"]+'"RETURN u, type(r), m'
                    results2 = db.query(q, returns=(client.Node, str, client.Node))
                    ## Aumentar en el diccionario, todos los restaurantes con ese ambiente            
                    for l in results2:
                        restaurantes[l[2]["name"]] = restaurantes[l[2]["name"]] + 1
                ##Obtener  todos los ambientes de restaurante
                q = 'MATCH (u:Ambiente)-[r:a]->(m:Restaurantes) WHERE m.name="'+j[2]["name"]+'" RETURN u, type(r), m'
                results1 = db.query(q, returns=(client.Node, str, client.Node))
                for k in results1:
                    q = 'MATCH (u:Ambiente)-[r:a]->(m:Restaurantes) WHERE u.name="'+k[0]["name"]+'"RETURN u, type(r), m'
                    results2 = db.query(q, returns=(client.Node, str, client.Node))
                    ## Aumentar en el diccionario, todos los restaurantes con ese ambiente            
                    for l in results2:
                        restaurantes[l[2]["name"]] = restaurantes[l[2]["name"]] + 1
                ##Obtener  todos los presupuestos de restaurante
                q = 'MATCH (u:Presupuesto)-[r:a]->(m:Restaurantes) WHERE m.name="'+j[2]["name"]+'" RETURN u, type(r), m'
                results1 = db.query(q, returns=(client.Node, str, client.Node))
                for k in results1:
                    q = 'MATCH (u:Presupuesto)-[r:a]->(m:Restaurantes) WHERE u.name="'+k[0]["name"]+'"RETURN u, type(r), m'
                    results2 = db.query(q, returns=(client.Node, str, client.Node))
                    ## Aumentar en el diccionario, todos los restaurantes con ese ambiente            
                    for l in results2:
                        restaurantes[l[2]["name"]] = restaurantes[l[2]["name"]] + 1
                ##Obtener  todos los presupuestos de restaurante
                q = 'MATCH (u:TipoComida)-[r:a]->(m:Restaurantes) WHERE m.name="'+j[2]["name"]+'" RETURN u, type(r), m'
                results1 = db.query(q, returns=(client.Node, str, client.Node))
                for k in results1:
                    q = 'MATCH (u:TipoComida)-[r:a]->(m:Restaurantes) WHERE u.name="'+k[0]["name"]+'"RETURN u, type(r), m'
                    results2 = db.query(q, returns=(client.Node, str, client.Node))
                    ## Aumentar en el diccionario, todos los restaurantes con ese ambiente            
                    for l in results2:
                        restaurantes[l[2]["name"]] = restaurantes[l[2]["name"]] + 1
    #--------------------------------- En base a tus restaurantes-------------------------------------------------------#
    q = 'MATCH (u:Usuario)-[r:a]->(m:Restaurantes) WHERE u.name="'+nombre+'"RETURN u, type(r), m'
    referenciados = db.query(q, returns=(client.Node,str,client.Node))
    for j in referenciados:
            #Obtener  todos las situaciones de restaurante
            q = 'MATCH (u:Situacion)-[r:a]->(m:Restaurantes) WHERE m.name="'+j[2]["name"]+'" RETURN u, type(r), m'
            results1 = db.query(q, returns=(client.Node, str, client.Node))
            for k in results1:
                q = 'MATCH (u:Situacion)-[r:a]->(m:Restaurantes) WHERE u.name="'+k[0]["name"]+'"RETURN u, type(r), m'
                results2 = db.query(q, returns=(client.Node, str, client.Node))
                ## Aumentar en el diccionario, todos los restaurantes con ese ambiente            
                for l in results2:
                    restaurantes[l[2]["name"]] = restaurantes[l[2]["name"]] + 1
            ##Obtener  todos los ambientes de restaurante
            q = 'MATCH (u:Ambiente)-[r:a]->(m:Restaurantes) WHERE m.name="'+j[2]["name"]+'" RETURN u, type(r), m'
            results1 = db.query(q, returns=(client.Node, str, client.Node))
            for k in results1:
                q = 'MATCH (u:Ambiente)-[r:a]->(m:Restaurantes) WHERE u.name="'+k[0]["name"]+'"RETURN u, type(r), m'
                results2 = db.query(q, returns=(client.Node, str, client.Node))
                ## Aumentar en el diccionario, todos los restaurantes con ese ambiente            
                for l in results2:
                    restaurantes[l[2]["name"]] = restaurantes[l[2]["name"]] + 1
            ##Obtener  todos los presupuestos de restaurante
            q = 'MATCH (u:Presupuesto)-[r:a]->(m:Restaurantes) WHERE m.name="'+j[2]["name"]+'" RETURN u, type(r), m'
            results1 = db.query(q, returns=(client.Node, str, client.Node))
            for k in results1:
                q = 'MATCH (u:Presupuesto)-[r:a]->(m:Restaurantes) WHERE u.name="'+k[0]["name"]+'"RETURN u, type(r), m'
                results2 = db.query(q, returns=(client.Node, str, client.Node))
                ## Aumentar en el diccionario, todos los restaurantes con ese ambiente            
                for l in results2:
                    restaurantes[l[2]["name"]] = restaurantes[l[2]["name"]] + 1
            ##Obtener  todos los presupuestos de restaurante
            q = 'MATCH (u:TipoComida)-[r:a]->(m:Restaurantes) WHERE m.name="'+j[2]["name"]+'" RETURN u, type(r), m'
            results1 = db.query(q, returns=(client.Node, str, client.Node))
            for k in results1:
                q = 'MATCH (u:TipoComida)-[r:a]->(m:Restaurantes) WHERE u.name="'+k[0]["name"]+'"RETURN u, type(r), m'
                results2 = db.query(q, returns=(client.Node, str, client.Node))
                ## Aumentar en el diccionario, todos los restaurantes con ese ambiente            
                for l in results2:
                    restaurantes[l[2]["name"]] = restaurantes[l[2]["name"]] + 1
    #------------------------------------En base a lo que decidiste-----------------------------------------------------------#
    # Sumar el valor de los valores elegidos
    q = 'MATCH (u:Ambiente)-[r:a]->(m:Restaurantes) WHERE u.name="'+ambiente+'"RETURN u, type(r), m'
    results2 = db.query(q, returns=(client.Node, str, client.Node))
    ## Aumentar en el diccionario, todos los restaurantes con el ambiente elegido          
    for l in results2:
        restaurantes[l[2]["name"]] = restaurantes[l[2]["name"]] + 5
    # Sumar el valor de los valores elegidos
    q = 'MATCH (u:Situacion)-[r:a]->(m:Restaurantes) WHERE u.name="'+situacion+'"RETURN u, type(r), m'
    results2 = db.query(q, returns=(client.Node, str, client.Node))
    ## Aumentar en el diccionario, todos los restaurantes con el ambiente elegido          
    for l in results2:
        restaurantes[l[2]["name"]] = restaurantes[l[2]["name"]] + 5
    # Sumar el valor de los valores elegidos
    q = 'MATCH (u:Presupuesto)-[r:a]->(m:Restaurantes) WHERE u.name="'+presupuesto+'"RETURN u, type(r), m'
    results2 = db.query(q, returns=(client.Node, str, client.Node))
    ## Aumentar en el diccionario, todos los restaurantes con el ambiente elegido          
    for l in results2:
        restaurantes[l[2]["name"]] = restaurantes[l[2]["name"]] + 5
    # Sumar el valor de los valores elegidos
    q = 'MATCH (u:TipoComida)-[r:a]->(m:Restaurantes) WHERE u.name="'+tipoComida+'"RETURN u, type(r), m'
    results2 = db.query(q, returns=(client.Node, str, client.Node))
    ## Aumentar en el diccionario, todos los restaurantes con el ambiente elegido          
    for l in results2:
        restaurantes[l[2]["name"]] = restaurantes[l[2]["name"]] + 5

        
    for key, value in sorted(restaurantes.iteritems(), key=lambda (k,v): (v,k), reverse=True):
         print "%s" % (key)

    

#Metodo para ingresar usuario a la base de datos
def ingresoUsuario(usuario):
    user = db.nodes.create(name=usuario)
    Usuario.add(user)
    print("\nSe ha ingresado correctamente\n")
#Metodo para realizar la union de un usuario con un determinado restaurante
def Usuariorestaurante(usuario):
    q = 'MATCH (u: Usuario) WHERE u.name="'+usuario+'" RETURN u'
    resultsU = db.query(q,returns=(client.Node))
    largo = len(resultsU)
    if(largo>0): #Validacion para ver que el usuario existe en la base de datos
        print("\nEstos son los restaurantes disponibles a elegir: ")
        q = 'MATCH (u: Restaurantes) RETURN u'
        results1 = db.query(q,returns=(client.Node,str,client.Node))
        for r in results1: #Imprime la lista de restaurantes en la base de datos
            print("-"+"%s"%(r[0]["name"]))
        rest = raw_input("Ingrese el nombre del restaurante que desea elegir: ")
        q = 'MATCH (u: Restaurantes) WHERE u.name="'+rest+'" RETURN u'
        results2 = db.query(q,returns=(client.Node))
        largo1 = len(results2)
        if(largo1>0):#Validacion para ver que el restaurante existe
            for r in results2:
                for i in resultsU:
                    i[0].relationships.create("a",r[0]) #Crea la union del usuario con el restaurante
            print("\nSe ha ingresado relacionado el restaurante:"+rest+", con el usuario: "+usuario+" exitosamente\n")
        else:
            print("\nEl restaurante ingresado no esta almacenado\n")
    else:
        print ("\nEl usuario ingresado no se encuentra dentro de la lista de datos\n")

def recomendacionPersonalizada():
    x = True #=============================================Ambiente
    while x:  #Para que el usuario pueda elegir un ambiente y si se equivoca vuelve a preguntar
        print("\nAmbientes a elegir: \n")
        q = 'MATCH (u: Ambiente) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        #Se agregan todos los ambientes
        for i in results:
            print("-"+"%s"%(i[0]["name"]))
        a = raw_input("Ingrese el ambiente que desea elegir: ") #pregunta el ambiente
        q = 'MATCH (u: Ambiente) WHERE u.name="'+a+'" RETURN u'
        results1 = db.query(q,returns=(client.Node))
        largo1 = len(results1)
        if(largo1>0): #Validacion que ingreso bien el ambiente
            for r in results1:
                ambiente = r[0]["name"] #Se guarda en la variable de ambiente la opcion que eligio el usuario
            print("\nUsted ha elegido "+ambiente+"\n")
            x = False
        else:
            print("\nNo ha ingresado bien el ambiente a elegir\n")
    x = True
    while x: #============================================Situaciones
        print("\nSituacion a elegir: \n")
        q = 'MATCH (u: Situacion) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        #Se agregan todos las situaciones
        for i in results:
            print("-"+"%s"%(i[0]["name"]))
        a = raw_input("Ingrese la situacion que desea elegir: ")
        q = 'MATCH (u: Situacion) WHERE u.name="'+a+'" RETURN u'
        results1 = db.query(q,returns=(client.Node))
        largo1 = len(results1)
        if(largo1>0): #Validacion que ingreso bien el ambiente
            for r in results1:
                situacion = r[0]["name"] #Se guarda en la variable de situacion la opcion que eligio el usuario
            print("\nUsted ha elegido "+situacion+"\n")
            x = False
        else:
            print("\nNo ha ingresado bien la situacion a elegir\n")
    x = True
    while x: #===============================================Presupuesto
        print("\nPresupuesto a elegir: \n")
        q = 'MATCH (u: Presupuesto) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        for i in results:
            print("-"+"%s"%(i[0]["name"]))
        a = raw_input("Ingrese el presupuesto que desea elegir: ")
        q = 'MATCH (u: Presupuesto) WHERE u.name="'+a+'" RETURN u'
        results1 = db.query(q,returns=(client.Node))
        largo1 = len(results1)
        if(largo1>0): #Validacion que ingreso bien el ambiente
            for r in results1:
                presupuesto = r[0]["name"]  #Se guarda en la variable de presupuesto la opcion que eligio el usuario
            print("\nUsted ha elegido "+presupuesto+"\n")
            x = False
        else:
            print("\nNo ha ingresado bien el presupuesto a elegir\n")
    x = True
    while x: #=============================================Tipo de comida
        print("\nTipo de coimida a elegir: \n")
        q = 'MATCH (u: TipoComida) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        #Se agregan todos los restaurantes
        for i in results:
            print("-"+"%s"%(i[0]["name"]))
        a = raw_input("Ingrese el tipo de comida que desea elegir: ")
        q = 'MATCH (u: TipoComida) WHERE u.name="'+a+'" RETURN u'
        results1 = db.query(q,returns=(client.Node))
        largo1 = len(results1)
        if(largo1>0): #Validacion que ingreso bien el ambiente
            for r in results1:
                tipocomida = r[0]["name"]   #Se guarda en la variable de tipo de comida la opcion que eligio el usuario
            print("\nUsted ha elegido "+tipocomida+"\n")
        else:
           print("\nNo ha ingresado bien lel tipo de comida a elegir\n")

#Metodo para imprimir
def Ambientes():
    x = True #=============================================Ambiente
    while x:  #Para que el usuario pueda elegir un ambiente y si se equivoca vuelve a preguntar
        print("\nAmbientes a elegir: \n")
        q = 'MATCH (u: Ambiente) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        #Se agregan todos los ambientes
        for i in results:
            print("-"+"%s"%(i[0]["name"]))
        a = raw_input("Ingrese el ambiente que desea elegir: ") #pregunta el ambiente
        q = 'MATCH (u: Ambiente) WHERE u.name="'+a+'" RETURN u'
        results1 = db.query(q,returns=(client.Node))
        largo1 = len(results1)
        if(largo1>0): #Validacion que ingreso bien el ambiente
            for r in results1:
                ambiente = r[0]["name"] #Se guarda en la variable de ambiente la opcion que eligio el usuario
            print("\nUsted ha elegido "+ambiente+"\n")
            x = False
        else:
            print("\nNo ha ingresado bien el ambiente a elegir\n")
    return ambiente
#Metodo para imprimir
def Situacion():
    x = True
    while x: #============================================Situaciones
        print("\nSituacion a elegir: \n")
        q = 'MATCH (u: Situacion) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        #Se agregan todos las situaciones
        for i in results:
            print("-"+"%s"%(i[0]["name"]))
        a = raw_input("Ingrese la situacion que desea elegir: ")
        q = 'MATCH (u: Situacion) WHERE u.name="'+a+'" RETURN u'
        results1 = db.query(q,returns=(client.Node))
        largo1 = len(results1)
        if(largo1>0): #Validacion que ingreso bien el ambiente
            for r in results1:
                situacion = r[0]["name"] #Se guarda en la variable de situacion la opcion que eligio el usuario
            print("\nUsted ha elegido "+situacion+"\n")
            x = False
        else:
            print("\nNo ha ingresado bien la situacion a elegir\n")
    return situacion
#Metodo para imprimir
def Presupuesto():
    x = True
    while x: #===============================================Presupuesto
        print("\nPresupuesto a elegir: \n")
        q = 'MATCH (u: Presupuesto) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        for i in results:
            print("-"+"%s"%(i[0]["name"]))
        a = raw_input("Ingrese el presupuesto que desea elegir: ")
        q = 'MATCH (u: Presupuesto) WHERE u.name="'+a+'" RETURN u'
        results1 = db.query(q,returns=(client.Node))
        largo1 = len(results1)
        if(largo1>0): #Validacion que ingreso bien el ambiente
            for r in results1:
                presupuesto = r[0]["name"]  #Se guarda en la variable de presupuesto la opcion que eligio el usuario
            print("\nUsted ha elegido "+presupuesto+"\n")
            x = False
        else:
            print("\nNo ha ingresado bien el presupuesto a elegir\n")
    return presupuesto
def TipoComida():
    x = True
    while x: #=============================================Tipo de comida
        print("\nTipo de comida a elegir: \n")
        q = 'MATCH (u: TipoComida) RETURN u'
        results = db.query(q,returns=(client.Node,str,client.Node))
        #Se agregan todos los restaurantes
        for i in results:
            print("-"+"%s"%(i[0]["name"]))
        a = raw_input("Ingrese el tipo de comida que desea elegir: ")
        q = 'MATCH (u: TipoComida) WHERE u.name="'+a+'" RETURN u'
        results1 = db.query(q,returns=(client.Node))
        largo1 = len(results1)
        if(largo1>0): #Validacion que ingreso bien el ambiente
            for r in results1:
                tipocomida = r[0]["name"]   #Se guarda en la variable de tipo de comida la opcion que eligio el usuario
            print("\nUsted ha elegido "+tipocomida+"\n")
            x = False
        else:
           print("\nNo ha ingresado bien lel tipo de comida a elegir\n")
    return tipocomida

def relacionUsuarios(usuario1,usuario2):
    q = 'MATCH (u: Usuario) WHERE u.name="'+usuario1+'" RETURN u'
    resultsU = db.query(q,returns=(client.Node))
    largo1 = len(resultsU)
    q = 'MATCH (u: Usuario) WHERE u.name="'+usuario2+'" RETURN u'
    resultsU2 = db.query(q,returns=(client.Node))
    largo2 = len(resultsU2)
    if(largo1>0 and largo2>0):
        for r in resultsU:
            for i in resultsU2:
                i[0].relationships.create("a",r[0])
                r[0].relationships.create("a",i[0])
        print ("Usuarios relacionados")
    else:
        print("Alguno de los usuarios no esta en la base de datos")
