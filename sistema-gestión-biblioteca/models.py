from datetime import datetime


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
        self.bloqueado = False
        
    def devolverMaterial(self, mat: Material):
        if mat in self.listaActiva:
            
            self.listaActiva.remove(mat)
            mat.disponible = True
            print("El material ha sido devuelto correctamente!")
            return True
        else:
            print(f"El material '{mat.titulo}' no se encontró dentro de su lista de préstamos activos.")
            return False
        
class Bibliotecario(Persona):
    def __init__(self, nombre: str, telefono: str):
        super().__init__(nombre, telefono)
        
    def gestionarPrestamo(self, fechaInicio: datetime, fechaDevolucion: datetime, user: Usuario, material: Material):
        
        if not material.disponible:
            print("El material no se encuentra disponible")
            return False
        if len(user.listaActiva) == user.limitePrestamos:
            print("El usuario ya alcanzó su límite de prestamos")
            return False
        
        if fechaDevolucion < fechaInicio:
            print("La fecha de devolución es menor a la fecha de inicio. VUelva a ingresar los datos.")
            return False
        
        if  user.bloqueado:
            print(f"El usuario {user.nombre} tiene prohibido solicitar material de la biblioteca. \nLlame a la policía inmediatamente.")
            return False
        
        Prestamo(fechaInicio, fechaDevolucion, user, material)
        user.listaActiva.append(Prestamo)
        return True

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
    def __init__(self, titulo: str, añoPublicacion: int):
        self.idMaterial = Material._contadorMaterial
        Material._contadorMaterial += 1
        self.titulo = titulo
        self.añoPublicacion = añoPublicacion
        self.disponible = True
        
        Catalogo.listadoMaterial.append(self)
        
class Libro(Material):
    def __init__(self, titulo: str, añoPublicacion: int, autor: str, isbn: str, genero: str):
        super().__init__(titulo, añoPublicacion)
        self.autor = autor
        self.isbn = isbn
        self.genero = genero
    
    def __str__(self):
        return f"'{self.titulo}' | Autor: {self.autor} ({self.añoPublicacion})"
        
class Revista(Material):
    def __init__(self, titulo: str, añoPublicacion: int,edicion: int, periodicidad: str):
        super().__init__(titulo, añoPublicacion)
        self.edicion = edicion
        self.periodicidad = periodicidad

    def __str__(self):
        return f"{self.titulo} (Edición #{self.edicion}) | {self.periodicidad} - {self.añoPublicacion}"
        
class MaterialDigital(Material):
    def __init__(self, titulo: str, añoPublicacion: int,tipoArchivo: str, urlDescarga: str, tamañoMB: float):
        super().__init__(titulo, añoPublicacion)
        self.tipoArchivo = tipoArchivo
        self.urlDescarga = urlDescarga
        self.tamañoMB = tamañoMB

    def __str__(self):
        return f"{self.titulo} [{self.tipoArchivo}] | Tamaño: {self.tamañoMB} MB | Link: {self.urlDescarga}"
#otro mas
class Prestamo:
    _contadorPrestamos = 1
    def __init__(self, fechaInicio: datetime, fechaDevolucion: datetime, usuario: Usuario, material: Material): 
        self.idPrestamo = Prestamo._contadorPrestamos
        Prestamo._contadorPrestamos += 1
        self.fechaInicio = fechaInicio
        self.fechaDevolucion = fechaDevolucion
        self.usuario = usuario
        self.material = material
        
        self.material.disponible = False
        
    def __str__(self):
        return f"[{self.idPrestamo}] - F. Inicio: {self.fechaInicio}, F. Devolución: {self.fechaDevolucion}, Usuario: {self.usuario.nombre}, Material: {self.material.titulo}"
        
class Penalizacion:
    
    def __init__(self, motivo: str):
        self.monto = 0.0
        self.motivo = motivo
        self.pagada = False
        
    def calcularMulta(self, prestamo: Prestamo):
        cantidadDias = prestamo.fechaDevolucion - prestamo.fechaInicio
        
        if cantidadDias < 0:
            print("El préstamo sigue activo")
        if 1 <= cantidadDias <= 3:
            print(f"Se le ha multado con $30 por no entregar el libro en {cantidadDias} días.")
        elif 4 <= cantidadDias <= 7:
            print(f"Se le ha multado con $100 por no entregar el libro en {cantidadDias} días.")
        
    def pagarMulta(self):
        self.pagada = True
    
    def bloquearUsuario(self, user: Usuario):
        user.bloquedo = True
        print(f"El usuario {user.nombre} ha sido agregado a la lista negra.")
        
        
        