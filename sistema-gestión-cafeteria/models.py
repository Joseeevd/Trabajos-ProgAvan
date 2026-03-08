from enum import Enum


# Enums para las cosas que existen (Esta vez si lo implementé)
class Rol(Enum):
    BARISTA  = "Barista"
    MESERO   = "Mesero"
    GERENTE  = "Gerente"

class Temperatura(Enum):
    FRIA     = "Fría"
    CALIENTE = "Caliente"

class EstadoPedido(Enum):
    PENDIENTE   = "Pendiente"
    PREPARANDO  = "Preparando"
    ENTREGADO   = "Entregado"

# Módulo de personas
class Persona:
    # Nota -> Los ID tanto de clientes como de personas ahora seran variables 'autoincrementables' y privadas para evitar repeticion en el sistema
    _contadorId = 1
    
    def __init__(self, nombre: str, email: str):
        self.idPersona = Persona._contadorId
        Persona._contadorId += 1 # Aumentamos en 1 
        
        self.nombre = nombre
        self.email = email
        
    def login(self):
        print("Logeado!")
        
    def actualizarPerfil(self, valor):
        self.nombre = valor


class Cliente(Persona):
    def __init__(self,nombre: str, email: str, puntosFidelidad: int):
        super().__init__(nombre, email)
        self.puntosFidelidad = puntosFidelidad
        self.historialPedidos = []
    
    def __str__(self):
        return super().__str__()
    
    def realizarPedido(self):
        print("Pidiendo...")
        
    def consultarHistorial(self):
        if self.historialPedidos:
            for pedido in self.historialPedidos:
                print(pedido)
        else:
            print("No hay pedidos registrados para este cliente.")

    def canjearPuntos(self):
        print(f"Usted tiene {self.puntosFidelidad} puntos acumulados")
        
class Empleado(Persona):
    def __init__(self,  nombre: str, email: str, rol: Rol):
        super().__init__(nombre, email)
        self.rol = rol # BARISTA, MESERO, GERENTE
        
    def actualizarInventario(self):
        print("Actualizando inventario...")
        
    def cambiarEstadoPedido(self):
        print("Cambiando estado del pedido...")


# MODULO DE PRODUCTOS
class ProductoBase:
    
    def __init__(self, idProducto: int, nombre: str, precioBase: float):
        self.idProducto = idProducto
        self.nombre = nombre
        self.precioBase = precioBase
        

class Bebida(ProductoBase):
    
    def __init__(self, idProducto: int, nombre: str, precioBase: float, tamano: str, temperatura: Temperatura, modificadores: list):
        super().__init__(idProducto, nombre, precioBase)
        self.tamano = tamano
        self.temperatura = temperatura
        self.modificadores = modificadores
        
    def agregarExtra(self):
        print("Extra agregado!")

    def calcularPrecioFinal(self):
        precioFinal = (len(self.modificadores) * 10) + self.precioBase
        return precioFinal
    
class Postre(ProductoBase):
    
    def __init__(self, idProducto: int, nombre: str, precioBase: float, esVegano: bool, sinGluten: bool):
        super().__init__(idProducto, nombre, precioBase)
        self.esVegano = esVegano
        self.sinGluten - sinGluten
        
    def __str__(self):
        return f"ID: {self.idProducto}, Nombre: {self.nombre}, Precio base: ${self.precioBase}, Es vegano: {self.esVegano}, Sin gluten: {self.sinGluten}"


# Log[i]stica y ventas

class Pedido:
    
    def __init__(self, idPedido: int, productos: list[ProductoBase], estado: str, total: float):
        self.idPedido = idPedido
        self.productos = productos
        self.estado = estado #PENDIENTE, PREPARANDO, ENTREGADO
        self.total = total
    
    def calcularTotal(self):
        return 100
    
    def validarStock(self, producto):
        if producto > 0:
            return True
        
        return False
    
class Inventario:
    
    inventarioIngredientes = []
    
    def __init__(self, ingredientes: map):
        self.ingredientes = ingredientes
        
    def reducirStock(self, cantidad):
        print(f"Se ha reducido {cantidad} al stock de ///")
        
    def notificarFaltante(self, ingrediente):
        print(f"Se ha establecido el estado de {ingrediente} como faltante")