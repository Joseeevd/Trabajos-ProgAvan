from models import * 


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

def mostrarMenuCliente(cliente: Cliente):
    while True:
        print(f"\n\n---- Menu Cliente - {cliente.nombre} (Puntos de fidelidad: {cliente.puntosFidelidad}) ----")

        op = pedirOpcion([
            "Realizar un pedido",
            "Ver pedidos realizados",
            "Canjear puntos",
            "Actualizar perfil",
            "cerrar sesión"
        ])
        
        match op:
            case _:
                break

def mostrarMenuEmpleados(empleado: Empleado):
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
            
            case _:
                break

# Esta ocasion usaremos diccionarios para hacer un listado donde NO SE PUEDAN REPETIR LOS EMAILS que se ingresen.
dictEmpleados = {}
dictClientes = {}