from models import * 
from datetime import datetime, timedelta

meses = {"Enero": 1, 
         "Febrero": 2, 
         "Marzo": 3, 
         "Abril": 4, 
         "Mayo": 5, 
         "Junio": 6,
         "Julio": 7,
         "Agosto": 8,
         "Septiembre": 9,
         "Octubre": 10,
         "Noviembre": 11,
         "Diciembre": 12}

listaMeses = list(meses.keys())

listaUsuarios = [
    Usuario("Carmen", "2424272", 5),
    Usuario("David", "182319791", 3),
    Usuario("Phillip", "555555555", 2),
    Usuario("Josebas el auténtico", "75677567", 3),
    Usuario("Paola", "56235235", 5),
    Usuario("Ximena", "626289780", 3),
    Usuario("Ángela", "01800030300", 2),
    Usuario("Tomás", "182319791", 3),
    Usuario("Víctor", "134134867", 4),
    Usuario("Germán", "62456865", 1)
]

listaBibliotecarios = [
    Bibliotecario("Esteban", "12939813"),
    Bibliotecario("Marely", "6346457"),
    Bibliotecario("Antoine", "34534512"),
    Bibliotecario("Ulises", "86782345"),
    Bibliotecario("Karla", "41244234"),
    Bibliotecario("Rita", "234167243"),
    Bibliotecario("Lia", "7327227"),
    Bibliotecario("Marcelo", "153316"),
    Bibliotecario("Carlos", "6123612"),
    Bibliotecario("Charlie", "723479")
]

listaLibros = [
    # Gabriel García Márquez
    Libro("Cien años de soledad", 1967, "Gabriel García Márquez", "978-0307474728", "Realismo Mágico"),
    Libro("El amor en los tiempos del cólera", 1985, "Gabriel García Márquez", "978-0307387264", "Romance"),
    
    # Isabel Allende
    Libro("La casa de los espíritus", 1982, "Isabel Allende", "978-1501117015", "Realismo Mágico"),
    Libro("Paula", 1994, "Isabel Allende", "978-0060951580", "Memorias"),
    
    # Jorge Luis Borges
    Libro("Ficciones", 1944, "Jorge Luis Borges", "978-0307950925", "Fantasía"),
    Libro("El Aleph", 1949, "Jorge Luis Borges", "978-8420633114", "Fantasía"),
    
    # Agatha Christie
    Libro("Asesinato en el Orient Express", 1934, "Agatha Christie", "978-0062693655", "Misterio"),
    Libro("Diez negritos", 1939, "Agatha Christie", "978-8467045390", "Misterio"),
    
    # Stephen King
    Libro("El resplandor", 1977, "Stephen King", "978-0307743657", "Terror"),
    Libro("It", 1986, "Stephen King", "978-1501142970", "Terror")
]

listaRevistas = [
    Revista("National Geographic", 2024, 460, "Mensual"),
    Revista("Nature", 2024, 815, "Semanal"),
    Revista("Vogue", 2023, 132, "Mensual"),
    Revista("Forbes", 2024, 102, "Mensual"),
    Revista("Muy Interesante", 2024, 522, "Mensual"),
    Revista("Time", 2023, 3500, "Semanal"),
    Revista("The Economist", 2024, 9380, "Semanal"),
    Revista("Scientific American", 2023, 150, "Mensual"),
    Revista("Wired", 2024, 320, "Mensual"),
    Revista("Cosmopolitan", 2023, 210, "Mensual")
]

listaMatDigital = [
    MaterialDigital("Manual de Python PDF", 2023, "PDF", "https://ejemplo.com/python.pdf", 15.5),
    MaterialDigital("Curso SQL Video", 2022, "MP4", "https://ejemplo.com/sql_course.mp4", 450.0),
    MaterialDigital("Dataset Clientes CSV", 2024, "CSV", "https://ejemplo.com/data.csv", 2.3),
    MaterialDigital("Libro IA Avanzada", 2023, "EPUB", "https://ejemplo.com/ia.epub", 8.7),
    MaterialDigital("Tutorial React", 2024, "MKV", "https://ejemplo.com/react_tuto.mkv", 120.4),
    MaterialDigital("Guía Estilo CSS", 2021, "PDF", "https://ejemplo.com/css_guide.pdf", 4.2),
    MaterialDigital("Backup Base de Datos", 2024, "SQL", "https://ejemplo.com/db_backup.sql", 85.1),
    MaterialDigital("Infografía Redes", 2022, "PNG", "https://ejemplo.com/networks.png", 1.5),
    MaterialDigital("Podcast Tecnología", 2024, "MP3", "https://ejemplo.com/podcast_01.mp3", 64.0),
    MaterialDigital("Ebook Java", 2023, "PDF", "https://ejemplo.com/java_ebook.pdf", 12.9)
]

listaPrestamos = [
    
]

def pedirInt(mensaje: str, valorMinimo: int=0, valorMaximo: int = 9999) -> int:
    while True:
        try:
            valorIngresado = int(input(f"{mensaje}: ")) #Pedimos un valor NUMERICO N U M E RI CO 
            if valorMinimo <= valorIngresado <= valorMaximo:
                return valorIngresado
            print(f"Ingrese un valor entero entre {valorMinimo} y {valorMaximo}") #Mensaje por si te equivocaste
        except ValueError:
            print("Por favor, ingrese un número válido.")

def pedirOpcion(opciones: list[str]) -> int:
    
    for i, op in enumerate(opciones, 1):
        print(f"{i}. {op}")
        
    return pedirInt("Elija una opción", 1, len(opciones)) # DAmos a eleGIR entre 1 y el numero de ocpiones que existan

# Funciones del bibliotecario
def gestionDePrestamos():
    print("\n\n Ingrese los siguientes datos para prestar material \n\n")
    
    fechaActual = datetime.now()
    print(f"\nFecha de préstamo: {fechaActual}")
    
    
    while True:
        print("\nFecha de entrega")
        idMesEntrega = pedirOpcion(listaMeses)
        
        match idMesEntrega:
            case 1|3|5|7|8|10|12 : diasMax = 31
            case 4|6|9|11: diasMax = 30
            case 2: diasMax = 28
            
        diaEntrega = pedirInt("Ingrese el día de entrega", 1, diasMax)
        
        fechaEntrega = datetime(2026, idMesEntrega, diaEntrega, 23, 59, 59)
        print(f"Fecha ingresada: {fechaEntrega}")
        
        if fechaActual > fechaEntrega:
            print(f"La fecha de entrega ingresada no puede ser anterior al dia de hoy.")
        else: 
            break
    
    while True:   
        print("\nSelección de usuario")
        idUsSeleccionado = pedirOpcion(listaUsuarios)
        
        if listaUsuarios[idUsSeleccionado - 1].bloqueado:
            print(f"El usuario está bloqueado.")
        else: 
            break
    while True:
        print("\nSelección de material")
        tipoMat = pedirOpcion(["Libro", "Revista" ,"Material digital"])
        match tipoMat:
            case 1: 
                idMat = pedirOpcion(listaLibros)
                materialSolicitado = listaLibros[idMat-1]
            case 2: 
                idMat = pedirOpcion(listaRevistas)
                materialSolicitado = listaRevistas[idMat-1]
            case 3: 
                idMat = pedirOpcion(listaMatDigital)
                materialSolicitado = listaMatDigital[idMat-1]
        
        if materialSolicitado.disponible:
            break
        else:
            print(f"el material {materialSolicitado.titulo} no está disponible. Seleccione de nuevo.")
    
    prestamo = Prestamo(fechaActual, fechaEntrega, listaUsuarios[idUsSeleccionado - 1], materialSolicitado)
    listaPrestamos.append(prestamo)
    print(prestamo)
    print(f"\nEl préstamo ha sido realizado correctamente!")

# Funciones del usuario
def devolverMaterial(user: Usuario):
    print("\nDevolución de material")
    if user.listaActiva:
        while True:
            idMatAregresar = pedirOpcion(user.listaActiva)
            flag = user.devolverMaterial(user.listaActiva[idMatAregresar-1])
            if flag:
                print("Gracias por usar nuestros servicios.\n")
                break
    else:
        print("No tienes préstamos activos")

def verHistorial(user: Usuario):
    print("\nPrestamos acvitos")
    if user.listaActiva:
        for mat in user.listaActiva:
            print(mat)
    else:
        print("No tienes prestamos activos.")

def login():
    print(f"\n\n---- Inicio de sesión ----")
    tipo = pedirOpcion(["Usuario","Bibliotecario"])
    
    if tipo == 1:
        print("\n\nLista de usuarios activos: ")
        idSelec = pedirOpcion(listaUsuarios)
        mostrarMenuUsuario(listaUsuarios[idSelec-1])
    if tipo == 2:
        print("\n\nLista de bibliotecarios activos: ")
        idSelec = pedirOpcion(listaBibliotecarios)
        mostrarMenuBibliotecario(listaBibliotecarios[idSelec-1])

def mostrarMenuBibliotecario(user: Bibliotecario):
    while True:
        print(f"==== Menú de bibliotecario ====")
        print(f"Bienvenido, {user.nombre}")
        operacion = pedirOpcion([
                                "Realizar un préstamo",
                                "Cerrar sesión"
                                ])
        
        match operacion:
            case 1: gestionDePrestamos()
            case 2: break
    
def mostrarMenuUsuario(user: Usuario):
    while True:
        print(f"==== Menú de Usuario ====")
        print(f"Bienvenido, {user.nombre}")
        
        operacion = pedirOpcion([
                                "Ver prestamos activos",
                                "Devolver material",
                                "Pagar una multa",
                                "Cerrar sesión"
                                ])
        match operacion:
            case 1: verHistorial(user)
            case 2: devolverMaterial(user)
            case 3:print("")
            case 4: break


# Código Principal

while True:
    print("\n\n************************************")
    print("Sistema de gestión de bibliotecas1")
    print("************************************\n\n")
    op = pedirOpcion(["Iniciar sesión","Salir del programa"])
    if op == 1:
        login()
    elif op == 2:
        break
    else:
        print(f"Opcion no reconocida")