from proyecto import *

menu = True
while menu:
    print "1.Ingresar un usuario a la base de datos"
    print "2.Relacionar un restaurante con un usuario"
    print "3.Ver recomendaciones"
    print "4.Relacionar usuario con otro usuario"
    print "5.Salir"
    op = int(raw_input("Ingrese una opcion"))
    if op==1:
        usuario = raw_input("Ingrese nombre de usuario para guardar")
        ingresoUsuario(usuario)
    elif op== 2:
        usuario = raw_input("Ingrese el nombre de usuario")
        Usuariorestaurante(usuario)
    elif op == 3:
        usuario = raw_input("Ingrese el nombre de usuario")
        ambiente = Ambientes()
        situacion = Situacion()
        presupuesto = Presupuesto()
        tipoComida = TipoComida()
        print("\nEstos son los restaurantes que se le recomiendan\n")
        recomedacion(usuario,ambiente,situacion,presupuesto,tipoComida)  
    elif op == 4:
        usuario1 = raw_input("Ingrese primer usuario")
        usuario2 = raw_input("Ingrese segundo usuario")
        relacionUsuarios(usuario1,usuario2)
    else:
        menu = False
