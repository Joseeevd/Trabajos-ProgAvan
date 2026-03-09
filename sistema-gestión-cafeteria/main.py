from models import * 

listaClientes = [
    Cliente("Juan Pérez", "juan.perez@email.com", "pass1234", 150),
    Cliente("María García", "m.garcia88@email.com", "segura_99", 420),
    Cliente("Carlos López", "clopez_dev@email.com", "carlos*2024", 10),
    Cliente("Ana Martínez", "ana.mtz@email.com", "flower88", 850),
    Cliente("Luis Rodríguez", "l.rodriguez@email.com", "admin_pass", 125),
    Cliente("Elena Sánchez", "elena.s@email.com", "p@ssword!", 310),
    Cliente("Roberto Gómez", "robert.g@email.com", "beto_1990", 55),
    Cliente("Lucía Torres", "lutorres@email.com", "lucia.star", 940),
    Cliente("Diego Fernández", "d.fer@email.com", "df_2026_x", 0),
    Cliente("Sofía Castro", "sofia.castro@email.com", "sofi_vip", 2100)
]



listaEmpleados = [
    Empleado("Pedro Martínez", "pedro.martinez@cafe.com", "GerenT3#24", Rol.GERENTE),
    Empleado("Ana García", "ana.garcia@cafe.com", "AnaB@rista", Rol.BARISTA),
    Empleado("Juan López", "juan.lopez@cafe.com", "JuanB23_", Rol.BARISTA),
    Empleado("María Rodríguez", "maria.rodriguez@cafe.com", "M@riaB_99", Rol.BARISTA),
    Empleado("Carlos Pérez", "carlos.perez@cafe.com", "CP25_b@", Rol.BARISTA),
    Empleado("Laura Sánchez", "laura.sanchez@cafe.com", "LauS2024", Rol.BARISTA),
    Empleado("Diego Fernández", "diego.fernandez@cafe.com", "DiegM1", Rol.MESERO),
    Empleado("Sofía Gómez", "sofia.gomez@cafe.com", "SofiM2_", Rol.MESERO),
    Empleado("Javier Torres", "javier.torres@cafe.com", "JaviM3#", Rol.MESERO),
    Empleado("Elena Castro", "elena.castro@cafe.com", "ElenM4*", Rol.MESERO)
]

listaPedidos = [
    Pedido(listaClientes[0]),
    Pedido(listaClientes[1]),
    Pedido(listaClientes[2]),
    Pedido(listaClientes[3]),
    Pedido(listaClientes[4]),
    Pedido(listaClientes[5]),
    Pedido(listaClientes[6]),
    Pedido(listaClientes[7]),
    Pedido(listaClientes[8]),
    Pedido(listaClientes[9]),
]

# Esta ocasion usaremos diccionarios para hacer un listado donde NO SE PUEDAN REPETIR LOS EMAILS que se ingresen.
dictEmpleados = {}
dictClientes = {}
for c in listaClientes:
    dictClientes[c.email] = c
    
for e in listaEmpleados:
    dictEmpleados[e.email] = c

# Funcion para solicitar (con sus debidas validaciones) valores ENTEROSS entre ciertos rangos, se repite hasta que el usuario meta un dato v[a]lido
def pedirInt(mensaje: str, valorMinimo: int=0, valorMaximo: int = 9999) -> int:
    while True:
        try:
            valorIngresado = int(input(f"{mensaje}: ")) #Pedimos un valor NUMERICO N U M E RI CO 
            if valorMinimo <= valorIngresado <= valorMaximo:
                return valorIngresado
            print(f"Ingrese un valor entero entre {valorMinimo} y {valorMaximo}") #Mensaje por si te equivocaste
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Una funcion a la que le metes una lista y muy convenientemente te hace el menu de opciones que genial
def pedirOpcion(opciones: list[str]):
    
    for i, op in enumerate(opciones, 1):
        print(f"{i}. {op}")
        
    return pedirInt("Elija una opción: ", 1, len(opciones)) # DAmos a eleGIR entre 1 y el numero de ocpiones que existan

def verPedidos():
    print("---- Pedidos registrados ----")
    if listaPedidos:
        for p in listaPedidos:
            p.imprimirPedido()
    else:
        print("No hay pedidos registrados")

def login():
    print("---- INICIO DE SESIÓN ----")
    email = input("Ingrese su email: ")
    contra = input("Ingrese su contraseña: ")

    usuario = dictClientes.get(email) or dictEmpleados.get(email) # Vemos si existe el email ingresado en cualquiera de los 2 diccionarios
    if not usuario:
        print("El usuario no se encontró.")
        return
    if not usuario.login(contra):
        print("La contraseña no es correcta")
        return
    
    #SI todo sale bien
    print(f"Bienvenid@, {usuario.nombre}.")
    usuarioActual = usuario
    
    
    #PARTE IMPORTANTISIMA DEL CODIGO 
    # verificar el usuario es instancia de la clase cliente o empleado, para abrir un menu segun lo que sea
    if isinstance(usuario, Cliente):
        mostrarMenuCliente(usuario)
        
    elif isinstance(usuario, Empleado):
        mostrarMenuEmpleado(usuario)

def mostrarMenuCliente(cliente: Cliente):
    while True:
        print(f"\n\n---- Menu Cliente - {cliente.nombre} (Puntos de fidelidad: {cliente.puntosFidelidad}) ----")

        op = pedirOpcion([
            "Realizar un pedido",
            "Ver pedidos realizados",
            "Cerrar sesión"
        ])
        
        match op:
            case _:
                break

def mostrarMenuEmpleado(empleado: Empleado):
    while True:
        print(f"\n\n---- Menu Empleado - {empleado.nombre} ({empleado.rol.value}) ----")
        
        op = pedirOpcion([
            "Ver pedidos",
            "Cambiar estado de pedido",
            "Ver inventario",
            "Actualizar inventario",
            "Ver clientes registrados",
            "Cerrar sesión"
        ])
        
        match op:
            case 1: verPedidos()
            case 3: Inventario.mostrarInventario()
            case _:
                break


# Código principal

print("SISTEMA DE GESTION DE CAFETERIAS")
while True:
    op = pedirOpcion([
        "Iniciar sesion",
        "Registrarse como cliente",
        "Salir del programa"
    ])
    match op:
        case 1:
            login()
        case _:
            print("Saliendo del programa...")
            break