from models import * 

listaClientes = [
    Cliente("Jose el cliente", "jose@email.com", "1234", 150),
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
print(f"\n\n Listado de clientes")
for c in listaClientes:
    print(c)

listaEmpleados = [
    Empleado("Jose el gerente", "jose@cafe.com", "1234", Rol.GERENTE),
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
print(f"\n\n Listado de empleados")
for e in listaEmpleados:
    print(e)

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
print(f"\n\n Listado de pedidos")
for ped in listaPedidos:
    ped.imprimirPedido()

listaBebidas = [
    Bebida("Americano", 35.0, "Mediano", Temperatura.CALIENTE, ["Café"]),
    Bebida("Latte", 50.0, "Mediano", Temperatura.CALIENTE, ["Café", "Leche"]),
    Bebida("Latte Vainilla", 60.0, "Mediano", Temperatura.CALIENTE, ["Café", "Leche", "Vainilla"]),
    Bebida("Flat White", 55.0, "Mediano", Temperatura.CALIENTE, ["Café", "Leche"]),
    Bebida("Caramel Macchiato", 75.0, "Grande", Temperatura.CALIENTE, ["Café", "Leche", "Caramelo"]),
    Bebida("Frappé Moka", 85, "Grande", Temperatura.FRIA, ["Café", "Leche", "Chocolate líquido", "Hielo"]),
    Bebida("Frappé Capuchino", 80, "Grande", Temperatura.FRIA, ["Café", "Leche", "Hielo"]),
    Bebida("Frappé Caramelo", 85, "Grande", Temperatura.FRIA, ["Café", "Leche", "Hielo", "Caramelo"]),
    Bebida("Malteada de Fresa", 75, "Mediano", Temperatura.FRIA, ["Leche", "Helado Fresa"]),
    Bebida("Malteada de Chocolate", 75, "Mediano", Temperatura.FRIA, ["Leche", "Helado Chocolate"])
]
print(f"\n\n Listado de bebidas")
for bebida in listaBebidas:
    print(bebida.descripcion())

listaPostres = [
    Postre("Pastel de Chocolate Clásico", 150.0, False, False, ["Harina", "Huevo", "Azúcar", "Chocolate líquido"]),
    Postre("Galletas de Mantequilla", 45.0, False, False, ["Galletas", "Mantequilla"]),
    Postre("Flan de Vainilla", 35.0, False, True, ["Leche", "Huevo", "Azúcar", "Vainilla"]),
    Postre("Pay de Queso Individual", 60.0, False, False, ["Galletas", "Mantequilla", "Azúcar"]), 
    Postre("Copa Helado Chocolate & Caramelo", 55.0, False, True, ["Helado Chocolate", "Caramelo"]),
    Postre("Affogato", 65.0, False, True, ["Helado vainilla", "Café"]),
    Postre("Bizcocho Vainilla-Fresa", 40.0, False, False, ["Harina", "Huevo", "Vainilla"]),  
    Postre("Plato de galletas (10 unidades)", 45.0, False, False, ["Galletas"]), 
    Postre("Crepas con Chocolate Líquido", 50.0, False, False, ["Harina", "Leche", "Chocolate líquido"]),
    Postre("Dulce de Leche Artesanal (Frasco)", 120.0, False, True, ["Leche", "Azúcar", "Vainilla"])
]
print(f"\n\n Listado de postres")
for postre in listaPostres:
    print(postre.descripcion())

# En lugar de hacer 10 inventarios, metemos 10 elementos a un solo inventario (Para mantener la coherencia)
inventarioCafeteria = Inventario({
    "Leche" : 100,
    "Hielo" : 100,
    "Caramelo" : 70,
    "Harina" : 20,
    "Huevo" : 20,
    "Azúcar" : 20,
    "Café" : 100,
    "Vainilla" : 18,
    "Helado Chocolate": 4,
    "Helado Fresa": 10,
    "Helado Vainilla": 10,
    "Chocolate líquido": 20,
    "Galletas": 100,
    "Mantequilla": 20
})
print(f"\n\n Listado de elementos en el inventario")
for elemento in inventarioCafeteria.ingredientes:
    print(f"{elemento} -> cantidad: {inventarioCafeteria.ingredientes.get(elemento, 0)}")

# Esta ocasion usaremos diccionarios para hacer un listado donde NO SE PUEDAN REPETIR LOS EMAILS que se ingresen.
dictEmpleados = {}
dictClientes = {}

#metemos a los clientes y los empleados en sus diccionarios haciendo pares de "email" : Persona (objeto correspondiente)
for c in listaClientes:
    dictClientes[c.email] = c
    
for e in listaEmpleados:
    dictEmpleados[e.email] = e

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
def pedirOpcion(opciones: list[str]) -> int:
    
    for i, op in enumerate(opciones, 1):
        print(f"{i}. {op}")
        
    return pedirInt("Elija una opción", 1, len(opciones)) # DAmos a eleGIR entre 1 y el numero de ocpiones que existan

# Funciones de clientes
def registrarseComoCliente():
    print("\n\nBienvenido a nuestra cafetería! \n A continuación, proporcione los siguientes datos para crearle una cuenta: ")
    
    nombre = input("Nombre:")
    
    while(True):
        mail = input("Email: ")
        if mail in dictClientes or mail in dictEmpleados:
            print("Este email ya se encuentra registrado, proporcione uno válido.")
        else:
            break
    
    contra = input("Contraseña: ")
    
    nuevoCliente = Cliente(nombre, mail, contra, 0)
    listaClientes.append(nuevoCliente) # Lo metemos al listado global
    dictClientes[mail] = nuevoCliente #Para poder iniciar sesión
    print("\nUsted se ha registrado correctamente! Inicie sesión para realizar un pedido.")

def pedirExtras(bebida: Bebida):
    print("\nExtras de la bebida: \n")
    listaExtras = []
    listaExtras.append("Ningún extra + $0")
    extras = list(Bebida.precioExtras.keys())
    for ex in Bebida.precioExtras:
        text = f"{ex} + ${Bebida.precioExtras.get(ex, 0):.2f}"
        listaExtras.append(text)
        
    numExtra = pedirOpcion(listaExtras)
    if numExtra > 1: 
        bebida.agregarExtra(extras[numExtra-2])
    
    return bebida

def realizarPedido(client: Cliente):
    print("\n\n---- REALIZANDO PEDIDO ----")
    
    # Una lista para operar sobre todo
    menuDeLaCafe = listaBebidas + listaPostres
    listaNombrePrecio = []
    
    # Metemos dentro de una lista unos strings para mostrar el menú
    for elemento in menuDeLaCafe:
        texto = f"{elemento.nombre} - ${elemento.precioBase:.2f}"
        listaNombrePrecio.append(texto)
        
    #Primero lo primero, crear un pedido a nombre de la persona
    pedido = Pedido(client)
    
    while True:
        idProductoSeleccionado = pedirOpcion(listaNombrePrecio)
        
        if isinstance(menuDeLaCafe[idProductoSeleccionado - 1], Bebida):
            menuDeLaCafe[idProductoSeleccionado - 1].modificadores = [] #Vaciamos los posibles modificadores anteriories 
            bebidaCopia = menuDeLaCafe[idProductoSeleccionado - 1]
            producto = pedirExtras(bebidaCopia)
        else:
            producto = menuDeLaCafe[idProductoSeleccionado - 1]

        if not pedido.validarStock(inventarioCafeteria):
            print("No hay suficiente stock para completar su pedido.")
            return
        else:
            pedido.agregarProducto(producto)
        
        continuar = int(input("\nDesea añadir algo más a la cuenta? (1. Si, 2 No): "))
        if(continuar != 1): break
    
    if client.puntosFidelidad >= 10:
        usarPuntos = int(input(f"Usted tiene {client.puntosFidelidad} puntos, ¿Desea canjearlos? (1. Si, 2. No): "))
        if usarPuntos == 1:
            cantidadPuntos = pedirInt("Ingrese la cantidad de puntos (10pts -> $10 de descuento)", 10, client.puntosFidelidad)
            descuento = client.canjearPuntos(cantidadPuntos)
        else:
            descuento = 0.0
    
    pedido.calcularTotal(descuento)
    
    print("\n---- Resumen de la cuenta ----")
    pedido.imprimirPedido()
    
    client.historialPedidos.append(pedido)
    listaPedidos.append(pedido)
    print("\nGracias por su compra! \n")  
    
def verPedidosRealizados(cliente: Cliente):
    print(f"---- Pedidos realizados de {cliente.nombre} ----")
    if cliente.historialPedidos:
        for pedido in cliente.historialPedidos:
            print(pedido.imprimirPedido())
    else:
        print("No tienes pedidos registrados.")

# Funciones de empleados

def verPedidos():
    print("---- Pedidos registrados ----")
    if listaPedidos:
        for p in listaPedidos:
            p.imprimirPedido()
    else:
        print("No hay pedidos registrados")

def cambiarEstadoPedidos():
    verPedidos()
    numPedido = pedirInt("Seleccione un pedido para cambiar el estado", 1, len(listaPedidos))
    
    numEstadoSeleccionado = pedirOpcion([EstadoPedido.PENDIENTE.value, EstadoPedido.PREPARANDO.value, EstadoPedido.ENTREGADO.value])
    
    if numEstadoSeleccionado == 1: estadoSeleccionado = EstadoPedido.PENDIENTE
    if numEstadoSeleccionado == 2: estadoSeleccionado = EstadoPedido.PREPARANDO
    if numEstadoSeleccionado == 3: estadoSeleccionado = EstadoPedido.ENTREGADO
    
    listaPedidos[numPedido-1].estado = estadoSeleccionado

def actualizarInventario():
    
    # Metemos a una lista los ingredientes actuales (Principalmente para usar la función de pedirOpcion, que ocupa una lista de strings como argumento)
    listaIngredientes = []
    for ing in inventarioCafeteria.ingredientes:
        listaIngredientes.append(ing)
    
    #Se pide el número del ingrediente 
    numIng = pedirOpcion(listaIngredientes)

    #Pedimos una cantidad entera positiva    
    cantidad = pedirInt("Ingrese la cantidad a ingresar", 1, 500)
    
    #Buscamos el elemento dentro del listado de ingredientes y le agregamos la cantidad deseada
    inventarioCafeteria.ingredientes[listaIngredientes[numIng-1]] += cantidad
    print(f"\nSe ha agregado la cantidad de {cantidad} al stock de {listaIngredientes[numIng-1]} correctamente! \n")

def verClientesRegistrados():
    print("----- Clientes Registrados ----")
    for cliente in listaClientes:
        print(cliente)

#Funciones generales de menús e inicio de sesión
def login():
    usuario = None
    print("---- INICIO DE SESIÓN ----")
    email = input("Ingrese su email: ")
    contra = input("Ingrese su contraseña: ")

     # Vemos si existe el email ingresado en cualquiera de los 2 diccionarios
    usuario = dictClientes.get(email) or dictEmpleados.get(email)
    
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
            case 1: realizarPedido(cliente)
            case 2: verPedidosRealizados(cliente)
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
            case 2: cambiarEstadoPedidos()
            case 3: inventarioCafeteria.mostrarInventario()
            case 4: actualizarInventario()
            case 5: verClientesRegistrados()
            case _:
                break


# Código principal
print("\n\n\n - - - - SISTEMA DE GESTION DE CAFETERIAS - - - - ")
while True:
    print("\n----------------------------------------------")
    op = pedirOpcion([
        "Iniciar sesion",
        "Registrarse como cliente",
        "Salir del programa"
    ])
    print("\n----------------------------------------------")
    match op:
        case 1:
            login()
        case 2:
            registrarseComoCliente()
        case _:
            print("Saliendo del programa...")
            break