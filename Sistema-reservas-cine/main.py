from models import *
from datetime import datetime

#Valores varios para las operaciones
idFuncionActual = 7 #Para aumentar los ID constantemente
year = 2026

listaUsuarios = [
    Usuario(1, "Javier", "javi@gmail.com", "2364748127", "9090", 10),
    Usuario(2, "Andrea", "andy@gmail.com", "2461728228","8444" ,50),
    Usuario(3, "Toño", "toñito@gmail.com", "2361231237","3123" ,150),
    Usuario(4, "Ximena", "xime@gmail.com", "2375675690","8678" ,200),
    Usuario(5, "Chloe", "chloe@gmail.com", "12625327865","0909" ,90)
]

listaEmpleados = [
    Empleado(1, "Juan Pérez", "juan.perez@email.com", "555-0101", "1111", "TAQUILLERO", "9:00-18:00"),
    Empleado(2, "María García", "m.garcia@email.com", "555-0202", "007", "ADMIN", "8:00-17:00"),
    Empleado(3, "Carlos Ruiz", "cruiz@email.com", "555-0303", "carlos_dev", "TAQUILLERO", "14:00-22:00"),
    Empleado(4, "Ana Martínez", "ana.mtz@email.com", "555-0404", "anaMTZ2024", "LIMPIEZA", "9:00-18:00"),
    Empleado(5, "Luis Torres", "ltorres@email.com", "555-0505", "luisito_pass", "LIMPIEZA", "07:00-16:00")
]

listaPeliculas = [
    Pelicula("El Conjuro", 112, "R", "Terror", "Investigadores paranormales ayudan a una familia acosada por una presencia oscura."),
    Pelicula("Titanic", 194, "PG-13", "Romance", "Dos jóvenes de distintas clases sociales se enamoran a bordo del transatlántico."),
    Pelicula("Mad Max: Fury Road", 120, "R", "Acción", "Una mujer se rebela contra un tirano en un futuro postapocalíptico."),
    Pelicula("Toy Story", 81, "G", "Animada", "Los juguetes de un niño cobran vida cuando él no está presente."),
    Pelicula("Paddington", 95, "G", "Familiar", "Un oso peruano viaja a Londres en busca de un nuevo hogar."),
    Pelicula("Hereditary", 127, "R", "Terror", "Una familia sufre sucesos perturbadores tras la muerte de la abuela."),
    Pelicula("The Notebook", 123, "PG-13", "Romance", "Un hombre lee a una mujer una historia de amor escrita en un viejo cuaderno."),
    Pelicula("John Wick", 101, "R", "Acción", "Un exasesino busca venganza contra quienes le quitaron lo que más amaba."),
    Pelicula("Spider-Man: Into the Spider-Verse", 117, "PG", "Animada", "Varios héroes arácnidos de distintas dimensiones deben unir fuerzas."),
    Pelicula("Matilda", 98, "PG", "Familiar", "Una niña inteligente con poderes mágicos enfrenta a su malvada directora.")
]

listaSalas = [
    Sala(1, "Sala 1", "Interior", "2D", 50, False),
    Sala(2, "Sala 2", "Interior", "3D", 60, False),
    Sala(3, "Sala 3", "Interior", "4D", 30, False),
    Sala(4, "Sala 4", "Interior", "IMAX", 70, False),
    Sala(5, "Sala 5", "Interior", "2D", 50, False),
    Sala(6, "Sala 6", "Interior", "IMAX", 100, False),
]

listaFunciones = [
    Funcion(1, listaPeliculas[0], listaSalas[0], datetime(2026, 3, 10, 20, 30), 80),
    Funcion(2, listaPeliculas[0], listaSalas[1], datetime(2026, 3, 11, 20, 30), 90),
    Funcion(3, listaPeliculas[3], listaSalas[2], datetime(2026, 4, 18, 17, 30), 85),
    Funcion(4, listaPeliculas[3], listaSalas[3], datetime(2026, 4, 19, 12, 00), 120),
    Funcion(5, listaPeliculas[9], listaSalas[4], datetime(2026, 3, 25, 14, 15), 60),
    Funcion(6, listaPeliculas[9], listaSalas[5], datetime(2026, 3, 10, 20, 30), 100),
]

listaPromos = [
    Promocion("SABADAZOOO", "20% de descuento en sábados", 20, datetime(2026, 6, 10)),
    Promocion("BUAPOS", "50% de descuento a estudiantes de la BUAP", 50, datetime(2026, 12, 31)),
    Promocion("FAMILYSUNDAYS", "10% de descuento en domingos", 10, datetime(2026, 5, 29))
]


while(True):
    flag = False #Validación de credenciales
    print("\n\n---------------------------------------------------")
    print("INICIO DE SESIÓN")
    print("---------------------------------------------------")
    rol = input("¿Es usted usuario (u) o empleado (e)? Ingrese la letra correspondiente: ")
    idUser = int(input("Ingrese su ID de usuario (SOLO NÚMEROS ENTEROS): "))
    password = input("Ingrese su contraseña: ")
    
    if rol == "u":
        for user in listaUsuarios:
            if user.idPersona == idUser and user.contrasena == password:
                flag = True
                personaLogeada = user
    elif rol == "e":
        for user in listaEmpleados:
            if user.idPersona == idUser and user.contrasena == password:
                flag = True
                personaLogeada = user
    else:
        print("Seleccione un rol válido (Usuario o empleado) para continuar")
        break
    
    if flag:
        personaLogeada.login(idUser, password)
        
        if rol == "u":
            while(True):
                print("Menú de usuario")
                print("1. Realizar una reservación")
                print("2. Revisar historial de funciones")
                print("3. Cancelar una función")
                opcion = int(input("Ingrese el número correspondiente: "))
                
                if opcion < 1 or opcion > 3:
                    print("[ERROR]: Opción no reconocida")
                else:
                    match opcion:
                        case 1: personaLogeada.crearReserva()
                        case 2: personaLogeada.imprimirHistorialReservas()
                        case 3:
                            personaLogeada.imprimirHistorialReservas()
                            idcancelar = int(input("\nIngrese el ID de la reserva a cancelar"))
                            
                restart2 = int(input(f"¿Desea consultar algo más, {personaLogeada.nombre}? (1. SI, 2. NO): "))
                if(restart2 != 1): break 
                
        elif rol == "e":        
            while(True):
                print("\nMenú de empleado")
                print("1. Agregar nueva función")
                print("2. Agregar nueva película")
                print("3. Agregar nueva promoción")
                opcion = int(input("Ingrese el número correspondiente: "))
                
                if opcion < 1 or opcion > 3:
                    print("[ERROR]: Opción no reconocida")
                else:
                    match opcion:
                        case 1: 
                            print("\nIngrese los datos correspondientes para agregar una nueva función")
                            print("\nTITULO")
                            while(True):
                                flag2 = False
                                Pelicula.imprimirCartelera()
                                nombrePeli = input("Ingrese el título de la película: ")
                                for peli in Pelicula.cartelera:
                                    if(peli.titulo == nombrePeli):
                                        flag2 = True
                                        peliculaSeleccionada = peli
                                        break
                                if(flag2 == False):
                                    print("[ERROR]: La película no se encontró (Cuidado con las mayúsculas, espacios y tildes.)")
                                else:
                                    break
                            print("\nSALA")
                            while(True):
                                flag2 = False
                                for sala in listaSalas:
                                    print(f"ID: {sala.idEspacio}, nombre: {sala.nombre}, tipo: {sala.tipo}")
                                idSala = int(input("Ingrese el ID de la sala a asignar: "))
                                for sala in listaSalas:
                                    if idSala == sala.idEspacio:
                                        flag2 = True
                                        salaSeleccionada = sala
                                        break
                                if(flag2 == False):
                                    print("[ERROR]: La sala no se encontró, ingrese un ID válido")
                                else:
                                    break
                            
                            
                            print("\nDatos del horario y fecha")
                            mes = int(input("Ingrese el mes: "))
                            dia = int(input("Ingrese el dia: "))
                            hora = int(input("Ingrese la hora: "))
                            mins = int(input("Ingrese los minutos: "))
                            
                            fechaProporcionada = datetime(year, mes, dia, hora, mins)
                            
                            precioBase = float(input("Defina un precio base por boleto: "))
                            
                            funcionCreada = Funcion(idFuncionActual, peliculaSeleccionada, salaSeleccionada, fechaProporcionada, precioBase)
                            print(f"Detalles de la función: \n{funcionCreada}")
                            listaFunciones.append(funcionCreada)
                            
                            
                        case 2: 
                            print("\nIngrese los datos correspondientes para agregar una nueva película")
                            tituloo = input("Ingrese el título: ")
                            duracion = int(input("Ingrese la duración en minutos: "))
                            clasif = input("Ingrese la clasificación (R, PG-13, G, etc.): ")
                            genero = input("Ingrese el género: ")
                            sinopsis = input("Ingrese una sinopsis: ")
                            
                            peliNueva = Pelicula(tituloo, duracion, clasif, genero, sinopsis)
                            print(f"Datos de la película: \n{peliNueva}")
                            listaPeliculas.append(peliNueva)

                        case 3:
                            print("\nIngrese los datos correspondientes para agregar una nueva promoción")
                            code = input("Ingrese el código (mayúsculas): ")
                            descripcion = input("Ingrese una descripción breve: ")
                            porcentaje = float(input("Ingrese el porcentaje de descuento: "))
                            print("Datos de la fecha de expiración")
                            mes = int(input("Ingrese el mes: "))
                            dia = int(input("Ingrese el día: "))
                            
                            promoNueva = Promocion(code, descripcion, porcentaje, datetime(year, mes, dia))
                            listaPromos.append(promoNueva)
                            
                            print("\nPromociones actuales: ")
                            for promo in listaPromos:
                                print(promo)

                            
                restart2 = int(input(f"¿Desea consultar algo más, {personaLogeada.nombre}? (1. SI, 2. NO): "))
                if(restart2 != 1): break 
        else:
            print("El usuario o la contraseña no coinciden, intente de nuevo.")
            
    
    restart = int(input("\n\n¿Desea realizar otra operación? (1. SI, 2. NO): "))
    if(restart != 1): break 
