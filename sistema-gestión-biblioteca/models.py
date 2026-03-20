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
        self.multasActivas = []
    
    def __str__(self):
        return f"{self.nombre}"
    
    def mostrarInfo(self):
        return f"[{self.id}] -> {self.nombre}, teléfono: {self.telefono}, Límite de préstamos: {self.limitePrestamos}, Bloqueado: {self.bloqueado}"
        
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
        
    def __str__(self):
        return f"{self.nombre}"
        
    def mostrarInfo(self):
        return f"[{self.id}] -> {self.nombre}, teléfono: {self.telefono}"
        
    def gestionarPrestamo(self, fechaInicio: datetime, fechaDevolucion: datetime, user: Usuario, material: Material):
        
        if not material.disponible:
            print("El material no se encuentra disponible")
            return 
        if len(user.listaActiva) == user.limitePrestamos:
            print("El usuario ya alcanzó su límite de prestamos")
            return 
        
        if fechaDevolucion < fechaInicio:
            print("La fecha de devolución es menor a la fecha de inicio. VUelva a ingresar los datos.")
            return 
        
        if  user.bloqueado:
            print(f"El usuario {user.nombre} tiene prohibido solicitar material de la biblioteca. \nLlame a la policía inmediatamente.")
            return 
        
        pres = Prestamo(fechaInicio, fechaDevolucion, user, material)
        #user.listaActiva.append(material)
        #print(user.listaActiva)
        return pres

    def transferirMaterial(self, material: Material, sucursalActual: Sucursal, sucursalDestino: Sucursal):
        sucursalActual.retirarMaterialCatalogoLocal(material)
        sucursalDestino.agregarMaterialACatalogoLocal(material)
        print(f"El material '{material.titulo}' se a transferido de {sucursalActual.nombre} a {sucursalDestino.nombre}")

class Sucursal:
    _contadorSucursal = 1
    def __init__(self, nombre: str):
        self.idSucursal = Sucursal._contadorSucursal
        Sucursal._contadorSucursal += 1
        self.nombre = nombre
        self.catalogoLocal = []
        
        Catalogo.listadoMaterial[self] = []
        
    def __str__(self):
        return f"{self.nombre} -> Material en el catálogo: {len(self.catalogoLocal)} ejemplares"
        
    def agregarMaterialACatalogoLocal(self, material: Material):
        self.catalogoLocal.append(material)
        Catalogo.listadoMaterial[self] = self.catalogoLocal
        
    def retirarMaterialCatalogoLocal(self, material: Material):
        self.catalogoLocal.remove(material)
        Catalogo.listadoMaterial[self] = self.catalogoLocal
        
    
class Catalogo:
    
    # Sucursal : List[Material]
    listadoMaterial = {}
    
    @classmethod
    def imprimirListadoMaterial(cls):

        if cls.listadoMaterial:            
            for sucursal, listaMateriales in cls.listadoMaterial.items():
                titulosMat = ""
                print(f"\nSucursal: {sucursal}")
                
                if listaMateriales:
                    for mat in listaMateriales:
                       titulosMat += mat.titulo
                       if not mat == listaMateriales[-1]:
                            titulosMat += ", "
                else:
                    titulosMat = "Sin existencia"
                
                print(f"Material: {titulosMat}")
    
    @classmethod
    def buscarPorAutor(cls, autorBuscado: str, lista: list[Libro]):
        res = []
        
        print("Buscando....")
        for libro in lista:
            if libro.autor == autorBuscado:
                res.append(libro)        
        
        return res
        

    @classmethod
    def buscarEnTodasLasSucursales(cls, titulo: str):
        print("Buscando....")
            
        for sucursal, listaMateriales in cls.listadoMaterial.items():  
            #print(f"\n{sucursal}")
            for mat in listaMateriales:
                #print(mat.titulo)
                if titulo == mat.titulo: 
                    print(f"El material '{mat.titulo}' ha sido encontrado en la sucursal {sucursal.nombre}")
                    return
                
        print("El material no se ha encontrado.")



# Normalelelelele normalololololo
class Material:
    _contadorMaterial = 1
    def __init__(self, titulo: str, añoPublicacion: int):
        self.idMaterial = Material._contadorMaterial
        Material._contadorMaterial += 1
        self.titulo = titulo
        self.añoPublicacion = añoPublicacion
        self.disponible = True
        
        #Catalogo.listadoMaterial.append(self)
        
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
        self.usuario.listaActiva.append(self.material) #añadimos el material a la lista activa del usuario al crear un préstamo
        
    def __str__(self):
        return f"[{self.idPrestamo}] - F. Inicio: {self.fechaInicio}, F. Devolución: {self.fechaDevolucion}, Usuario: {self.usuario.nombre}, Material: {self.material.titulo}"
        
class Penalizacion:
    
    def __init__(self, motivo: str):
        self.monto = 0.0
        self.motivo = motivo
        self.pagada = False
        
    def __str__(self):
        return f"Penalización -> Motivo: {self.motivo}, Monto a pagar: ${self.monto:.2f}, Pagada: {self.pagada}"
        
    def calcularMulta(self, prestamo: Prestamo):
        diferencia = prestamo.fechaDevolucion - prestamo.fechaInicio
        cantidadDias = diferencia.days
        
        if cantidadDias < 0:
            print("Gracias por devolver el material a tiempo!")
        if 1 <= cantidadDias <= 3:
            print(f"Se le ha multado con $30 por no entregar el libro en {cantidadDias} días.")
            self.monto = 30.0
            prestamo.usuario.multasActivas.append(self)
        elif 4 <= cantidadDias <= 7:
            print(f"Se le ha multado con $100 por no entregar el libro en {cantidadDias} días.")
            self.monto = 100.0
            prestamo.usuario.multasActivas.append(self)
        
    def pagarMulta(self):
        self.pagada = True
        print(f"Por favor, pague el monto de ${self.monto:.2f} MXN")
    
    def bloquearUsuario(self, user: Usuario):
        user.bloquedo = True
        print(f"El usuario {user.nombre} ha sido agregado a la lista negra.")
        
        
        