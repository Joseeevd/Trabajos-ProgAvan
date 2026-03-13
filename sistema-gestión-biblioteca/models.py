from datetime import date


class Persona:
    _contadorID = 1
    def __init__(self, nombre: str, telefono: str):
        self.id = Persona._contadorID
        Persona._contadorID +=1
        self.nombre = nombre
        self.telefono = telefono
        
class Usuario(Persona):
    def __init__(self, nombre: str, telefono: str, limitePrestamos: int):
        super().__init__(nombre, telefono)
        self.limitePrestamos = limitePrestamos
        self.listaActiva = [] #Prestamos
        
class Bibliotecario(Persona):
    def __init__(self, nombre: str, telefono: str):
        super().__init__(nombre, telefono)
        
    def gestionarPrestamo(self, prestamo: Prestamo):
        print("Gestionando préstamo")

    def transferirMaterial(self, material, sucursalDestino):
        print(f"El material '{material}' se a transferido a la sucursal {sucursalDestino}")

class Sucursal:
    _contadorSucursal = 1
    def __init__(self, nombre: str):
        self.idSucursal = Sucursal._contadorSucursal
        Sucursal._contadorSucursal += 1
        self.nombre = nombre
        self.catalogoLocal = []
        
    
class Catalogo:
    listadoMaterial = []
    
    @classmethod
    def buscarPorAutor(self, autor: str):
        print("buscando....")

    def buscarEnTodasLasSucursales(self, titulo: str):
        print("Buscando....")



# Normalelelelele normalololololo
class Material:
    _contadorMaterial = 1
    def __init__(self, titulo: str, añoPublicacion: int, disponible: bool):
        self.idMaterial = Material._contadorMaterial
        Material._contadorMaterial += 1
        self.titulo = titulo
        self.añoPublicacion = añoPublicacion
        self.disponible = disponible
        
class Libro(Material):
    def __init__(self, titulo: str, añoPublicacion: int, disponible: bool, autor: str, isbn: str, genero: str):
        super().__init__(titulo, añoPublicacion, disponible)
        self.autor = autor
        self.isbn = isbn
        self.genero = genero
        
class Revista(Material):
    def __init__(self, titulo: str, añoPublicacion: int, disponible: bool, edicion: int, periodicidad: str):
        super().__init__(titulo, añoPublicacion, disponible)
        self.edicion = edicion
        self.periodicidad = periodicidad
        
class MaterialDigital(Material):
    def __init__(self, titulo: str, añoPublicacion: int, disponible: bool, tipoArchivo: str, urlDescarga: str, tamañoMB: float):
        super().__init__(titulo, añoPublicacion, disponible)
        self.tipoArchivo = tipoArchivo
        self.urlDescarga = urlDescarga
        self.tamañoMB = tamañoMB
        
#otro mas
class Prestamo:
    _contadorPrestamos = 1
    def __init__(self, fechaInicio: date, fechaDevolucion: date, usuario: Usuario, material: Material): 
        self.idPrestamo = Prestamo._contadorPrestamos
        Prestamo._contadorPrestamos += 1
        self.fechaInicio = fechaInicio
        self.fechaDevolucion = fechaDevolucion
        self.usuario = usuario
        self.material = material
        
class Penalizacion:
    
    def __init__(self, monto: float, motivo: str, pagada: bool):
        self.monto = monto
        self.motivo = motivo
        self.pagada = pagada
        