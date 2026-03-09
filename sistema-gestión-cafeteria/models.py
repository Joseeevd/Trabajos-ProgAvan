from enum import Enum


# Enums para las cosas que existen (Esta vez si lo implementé)
class Rol(Enum):
    BARISTA = "Barista"
    MESERO = "Mesero"
    GERENTE = "Gerente"

class Temperatura(Enum):
    FRIA= "Fría"
    CALIENTE = "Caliente"

class EstadoPedido(Enum):
    PENDIENTE = "Pendiente"
    PREPARANDO = "Preparando"
    ENTREGADO = "Entregado"

# Módulo de personas
class Persona:
    # Nota -> Los ID tanto de clientes como de personas ahora seran variables 'autoincrementables' y privadas para evitar repeticion en el sistema
    _contadorId = 1
    
    def __init__(self, nombre: str, email: str, contrasena: str):
        self.idPersona = Persona._contadorId
        Persona._contadorId += 1 # Aumentamos en 1 
        
        self.nombre = nombre
        self.email = email
        self.contrasena = contrasena
        
    def login(self, contrasena: str) -> bool:
        return self.contrasena == contrasena
        
    def actualizarPerfil(self, valor):
        self.nombre = valor


class Cliente(Persona):
    def __init__(self, nombre: str, email: str, contrasena: str, puntosFidelidad: int):
        super().__init__(nombre, email, contrasena)
        self.puntosFidelidad = puntosFidelidad
        self.historialPedidos = []
    
    def __str__(self):
        return super().__str__()
    
    # Se agrega el pedido al historial
    def realizarPedido(self, pedido: Pedido):
        self.historialPedidos.append(pedido)
        print(f"Pedido registrado con éxito")
        
    def consultarHistorial(self):
        if self.historialPedidos:
            for pedido in self.historialPedidos:
                print(pedido)
        else:
            print("No hay pedidos registrados para este cliente.")

    # Cada 10 pts son 10 ($1 = 1pt, pero se gastan de a 10) pesos de descuento, por lo que la funcion retorna el descuento si es aplicable
    def canjearPuntos(self, cantidadPuntos: int):
        if cantidadPuntos > self.puntosFidelidad:
            print("No tiene puntos suficientes para realizar esta acción.")
            return 0.0
        else:
            self.puntosFidelidad -= cantidadPuntos
            descuento = (cantidadPuntos // 10) * 1.0
            print(f"Puntos canjeados: {cantidadPuntos}, descuento al total: ${descuento:.2f}")
            return descuento
            
        
class Empleado(Persona):
    def __init__(self, nombre: str, email: str, contrasena: str, rol: Rol):
        super().__init__(nombre, email, contrasena)
        self.rol = rol # BARISTA, MESERO, GERENTE
        
    def actualizarInventario(self, inventario: Inventario, ingrediente: str, cantidad: int):
        inventario.ingredientes[ingrediente] = inventario.ingredientes.get(ingrediente, 0) + cantidad
        print(f"Se ha actualizado el stock de {ingrediente}, cantidad actual: {inventario.ingredientes[ingrediente]} unidades")

        
    def cambiarEstadoPedido(self, pedido: Pedido, estadoNuevo: EstadoPedido):
        pedido.estado = estadoNuevo
        print(f"Se ha actualizado el estado del pedido {pedido.idPedido} a {estadoNuevo.value}")


# MODULO DE PRODUCTOS
class ProductoBase:
    _contador_prod = 1
    
    def __init__(self, nombre: str, precioBase: float, ingredientes: list[str]):
        self.idProducto  = ProductoBase._contador_prod
        ProductoBase._contador_prod += 1
        
        self.nombre = nombre
        self.precioBase = precioBase
        self.ingredientes = ingredientes
        

class Bebida(ProductoBase):
    
    # Un diccionario que contiene el nombre del extra y su valor
    precioExtras = {
        "Shot extra de espresso": 12,
        "Leche deslactosada": 6.50,
        "Leche de almendras": 14,
        "Cold foam de vainilla": 18,
        "Cold foam de coco": 20,
    }
    
    def __init__(self, nombre: str, precioBase: float, tamano: str, temperatura: Temperatura, ingredientes: list[str]):
        super().__init__(nombre, precioBase, ingredientes)
        self.tamano = tamano
        self.temperatura = temperatura
        self.modificadores = [] #Lista de los modificadores, se agregan en otro apartado        
    
    def agregarExtra(self, nombreExtra: str):
        if nombreExtra in self.precioExtras:
            self.modificadores.append(nombreExtra)
            print(f"Se ha añadido el extra de {nombreExtra} (${self.precioExtras[nombreExtra]:.2f})")
        else:
            print(f"El extra no se reconoce o no esta disponible.")
            

    def calcularPrecioFinal(self):
        totalExtras = sum(self.precioExtras.get(modificador, 0) for modificador in self.modificadores)
        return self.precioBase + totalExtras
    
class Postre(ProductoBase):
    
    def __init__(self, nombre: str, precioBase: float, esVegano: bool, sinGluten: bool):
        super().__init__(nombre, precioBase)
        self.esVegano = esVegano
        self.sinGluten - sinGluten
        
    def __str__(self):
        return f"ID: {self.idProducto}, Nombre: {self.nombre}, Precio base: ${self.precioBase}, Es vegano: {self.esVegano}, Sin gluten: {self.sinGluten}"


# Log[i]stica y ventas

class Pedido:
    _contador_pedido = 1
    
    def __init__(self, cliente: Cliente):
        self.idPedido   = Pedido._contador_pedido
        Pedido._contador_pedido += 1
        
        self.cliente = cliente
        self.productos = []
        self.estado = EstadoPedido.PENDIENTE
        self.total = 0
    
    def imprimirPedido(self):
        print(f"\n  ── Pedido #{self.idPedido}")
        print(f"  Cliente : {self.cliente.nombre}")
        print(f"  Estado  : {self.estado.value}")
        print("  Productos:")
        for p in self.productos:
            print(f"    • {p.descripcion()}")
        print(f"  Total   : ${self.total:.2f}")
      
    def agregarProducto(self, producto: ProductoBase):
        self.productos.append(producto)
    
    def calcularTotal(self, descuento: float):
        subtotal = sum(p.calcularPrecioFinal() for p in self.productos) #Sumamos toooodos los productos con sus respectivos extras (si aplica) dentro de la lista del pedido
        self.total = max(0.0, subtotal - descuento) #Establecemos el total de la cuenta (en el objeto pues)
        return self.total
    
    #Esta función itera sobre todos los productos dentro de la lista, viendo que ingredientes requieren y validando que existan suficientes para hacer la bebida o postre
    def validarStock(self, inventario: Inventario) -> bool:
        for producto in self.productos:
            for ingre in producto.ingredientes:
                if inventario.ingredientes.get(ingre, 0) < 1:
                    print(f"Sin stock para ingrediente '{ingre}' requerido por '{producto.nombre}'.")
                    return False
        return True
    
class Inventario:
    
    inventarioIngredientes = []
    
    def __init__(self, ingredientes: dict[str, int]):
        self.ingredientes = ingredientes
        
    def reducirStock(self, cantidad):
        print(f"Se ha reducido {cantidad} al stock de ///")
        
    def notificarFaltante(self, ingrediente):
        print(f"Se ha establecido el estado de {ingrediente} como faltante")
    
    
    def mostrarInventario(self):
        print("\nINVENTARIO:")
        if self.ingredientes:
            for ing, cantidad in self.ingredientes.items():
                print(f"Ingrediente: {ing}, cantidad: {cantidad}")
        else:
            print("No hay ingredientes registrados")