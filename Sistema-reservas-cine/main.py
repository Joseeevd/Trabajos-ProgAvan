from models import *
from datetime import datetime

listaUsuarios = [
    Usuario(1, "Javier", "javi@gmail.com", "2364748127", "9090", 10),
    Usuario(2, "Andrea", "andy@gmail.com", "2461728228","8444" ,50),
    Usuario(3, "Toño", "toñito@gmail.com", "2361231237","3123" ,150),
    Usuario(4, "Ximena", "xime@gmail.com", "2375675690","8678" ,200),
    Usuario(5, "Chloe", "chloe@gmail.com", "12625327865","0909" ,90)
]

listaEmpleados = [
    Empleado(1, "Juan Pérez", "juan.perez@email.com", "555-0101", "password123", "TAQUILLERO", "9:00-18:00"),
    Empleado(2, "María García", "m.garcia@email.com", "555-0202", "segura789", "ADMIN", "8:00-17:00"),
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

#print("LISTA DE USUARIOS")
#for u in listaUsuarios:
#    print(u)

#print("\nLISTA DE EMPLEADOS")   
#for e in listaEmpleados:
#    print(e)

#listaEmpleados[1].logout() #No tiene que funcionar
#listaEmpleados[1].login(2, "segura789")
#listaEmpleados[1].logout() #Claramente, ya funciona

#listaEmpleados[1].gestionarFunciones() #chi
#listaEmpleados[2].gestionarFunciones() #ño

#listaEmpleados[1].marcarEntrada()
#listaEmpleados[2].marcarEntrada()
#listaEmpleados[3].marcarEntrada()

#for p in listaPeliculas:
#    print(p.obtenerSinopsis())

#sala1 = Sala(1, "A1", "Adentro", "IMAX", 50, True)
#texto_hora = "26/02/2026 18:30:00"

# Convertir string a objeto datetime
#objeto_hora = datetime.strptime(texto_hora, "%d/%m/%Y %H:%M:%S")
#funcion1 = Funcion(1, listaPeliculas[1], sala1, objeto_hora, 150)

#funcion1.obtenerDetallesFuncion()
#print(type(Pelicula.cartelera[0]))
hora1 = datetime(2026, 3, 20, 15, 30)
sala1 = Sala(1, "Sala 1", "Interior", "IMAX", 20, True)
funcion1 = Funcion(1, listaPeliculas[9], sala1, hora1, 120.0)
listaUsuarios[0].crearReserva()
listaUsuarios[0].historialReservas[0].confirmarPago()
listaUsuarios[0].historialReservas[0].generarTicket()

listaUsuarios[1].crearReserva()
listaUsuarios[1].historialReservas[0].confirmarPago()
listaUsuarios[1].historialReservas[0].generarTicket()