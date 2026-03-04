from datetime import datetime

# MÓDULO DE PERSONAS
class Persona:
    
    def __init__(self, idPersona: int, nombre: str, email: str, telefono: str, contrasena: str):
        self.idPersona = idPersona
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.contrasena = contrasena
        self.logeado = False 

    def __str__(self):
        return f"ID persona: {self.idPersona} - Nombre: {self.nombre} - Email: {self.email} - Teléfono: {self.telefono} - Contraseña: {self.contrasena} - Logeado: {self.logeado}"

    def login(self, id: int, c: str):
        if self.idPersona == id and self.contrasena == c:
            print(f"Bienvenido, {self.nombre}")
            self.logeado = True
        else:
            print(f"El ID de usuario o la contraseña son incorrectos, intente de nuevo")
    
    def logout(self):
        if self.logeado == True:
            print("Logout correcto")
            self.logeado = False
        else:
            print("No se ha iniciado sesion")
            
    def actualizarDatos(self):
        print(f"ID de usuario: {self.idPersona}")
        print("---- ACTUALIZACIÓN DE DATOS ----")
        print("1. ID de usuario")
        print("2. Nombre")
        print("3. Email")
        print("4. Teléfono")
        print("5. Contraseña")
        print("6. Cancelar acción")
        print("-----------------------------")
        op = int(input("Seleccione un valor para actualizar:"))
        
        #Verificación de opción y que esté dentro del rango definido (1-6)
        if op >= 1 and op <= 5:
            if op != 1:
                valorNuevo = input("Ingrese el nuevo valor: ")
            else:
                valorNuevo = int(input("Ingrese el nuevo valor (SOLO NUMEROS ENTEROS): "))
            
        
        
        #Para asignar los valores
        match op:
            case 1: 
                self.idPersona = valorNuevo
                print("El ID fue actualizado correctamente!")
            case 2: 
                self.nombre = valorNuevo
                print("El nombre fue actualizado correctamente!")
            case 3: 
                self.email = valorNuevo
                print("El email fue actualizado correctamente!")
            case 4: 
                self.telefono = valorNuevo
                print("El teléfono fue actualizado correctamente!")
            case 5: 
                self.contrasena = valorNuevo
                print("La contraseña fue actualizada correctamente!")
                
            case 6: print("Acción cancelada.")
            case _: print("Opción no reconocida, regresando al menú principal...")
        

class Usuario(Persona):
    #
    def __init__(self, idPersona: int, nombre: str, email: str, telefono: str, contrasena: str, puntosFidelidad: int):
        super().__init__(idPersona, nombre, email, telefono, contrasena)
        self.puntosFidelidad = puntosFidelidad
        self.historialReservas = []

    def imprimirHistorialReservas(self):
        if len(self.historialReservas) == 0:
            print("\nNo hay reservas registradas en su cuenta.")
        else:
            for r in self.historialReservas:
                print(r)
        
    def crearReserva(self):
        print("-----------------------------------------------------------")
        print(f"\nUsuario: {self.nombre} (Puntos: {self.puntosFidelidad})")
        #Peliculas
        while(True):
            flag = False
            Pelicula.imprimirCartelera()
            nombrePeli = input("Ingrese el título de la película: ")
            for peli in Pelicula.cartelera:
                if(peli.titulo == nombrePeli):
                    flag = True
                    #peliculaSeleccionada = peli
                    break
            if(flag == False):
                print("[ERROR]: La película no se encontró (Cuidado con las mayúsculas, espacios y tildes.)")
            else:
                break
        
        #Asignación de la función
        while(True):
            flag = False
            Funcion.imprimirFunciones(nombrePeli)
            if len(Funcion.funciones) > 0 :
                idFuncionSelec = int(input("Ingrese el ID de la función que desea ver: "))
            else:
                print("No hay funciones para esta película")
                return
            
            
            # iteramos en nuestra 'cartelera' de funciones y vemos cuales existen para la película seleccioanda
            for f in Funcion.funciones:
                if(f.idFuncion == idFuncionSelec):
                    flag = True
                    funcionSeleccionada = f
            
            if(flag == True):
                break
            else:
                print("[ERROR]: El ID ingresado no existe.")  
        
                 
                        
        #Seleccion de asientos
        while(True):
            asientos = input("\nIngrese los asientos que quiere reservar, separados por comas: ")
            asientosSolicitados = [asiento.strip() for asiento in asientos.split(',')] #un 'parseo' para que los asientos se vuelvan parte de una lista individual
            print("[SISTEMA]: Verificando disponibilidad...")
            
            resultadoAsignacion = funcionSeleccionada.calcularAsientosLibres(asientosSolicitados)

            if resultadoAsignacion:  
                montoBase =  funcionSeleccionada.precioBase * len(asientosSolicitados)
                print(f"Monto base por {len(asientosSolicitados)} asientos: ${montoBase}")
                
                # opacandastar! Si llega acá es pq todo está chido, momento de hacer la Reserva
                reserva = Reserva(Reserva.contadorReservas, self, funcionSeleccionada, asientosSolicitados)
                Reserva.contadorReservas += 1 # Aumentamos el 'id' global de reservas
                self.historialReservas.append(reserva)
                print("Su reserva ha sido guardada correctamente!")
                
                break #chau while
        
    def consultarPromociones(self):
        print("nohay")

    def cancelarReserva(self, reserva):
        reserva.estado = "CANCELADA"
        print(f"La reserva con ID {reserva.idReserva} fue cancelada exitosamente")
        
class Empleado(Persona):
    def __init__(self, idPersona: int, nombre: str, email: str, telefono: str, contrasena: str, rol: str, horario: str):
        super().__init__(idPersona, nombre, email, telefono, contrasena)
        self.rol = rol #TAQUILLERO, ADMIN, LIMPIEZA
        
        # La hora se da en un string de forma "10:00-19-00" (formato de 24hrs, horaEntrada-horaSalida)
        self.horaEntrada, self.horaSalida = horario.split("-")
        
        
    def marcarEntrada(self):
        print(f"¡A trabajar, {self.nombre}! son las {self.horaEntrada} y podrás salir a las {self.horaSalida}")

    def gestionarFunciones(self):
        if self.rol == "ADMIN":
            print("Usted puede gestionar las funciones")
        else:
            print("Usted no puede gestionar las funciones")

# GESTIÓN COMERCIAL      
class Promocion:
    
    def __init__(self, codigo: str, descripcion: str, porcentajeDescuento: float, fechaExpiracion: datetime):
            self.codigo = codigo
            self.descripcion = descripcion
            self.porcentajeDescuento = porcentajeDescuento
            self.fechaExpiracion = fechaExpiracion
    
    def __str__(self):
        return f"Código: {self.codigo}, Descripción: {self.descripcion}, Porcentaje de descuento: {(self.porcentajeDescuento)}%, Fecha de expiración: {self.fechaExpiracion}"
    
    def esValida(self):
        print("Puede ser")
        return True
    
    def aplicarDescuento(self, monto: float):
        return monto * 0.01 + 100
    
    
    
class Reserva:
    contadorReservas = 1    
    
    def __init__(self, idReserva: int, usuario: Usuario, funcion, asientos: list):
        self.idReserva = idReserva
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos
        self.montoTotal = 0
        self.estado = "PENDIENTE"
        
    def __str__(self):
        return f"ID reserva: {self.idReserva}, Función: {self.funcion.pelicula.titulo}, Estado: {self.estado}"
    
    def confirmarPago(self):
        self.montoTotal = len(self.asientos) * self.funcion.precioBase  #numero de asientos * precio por boleto
        self.estado = "PAGADA"
        print(f"Total a pagar por {len(self.asientos)} asientos: ${self.montoTotal}")
        
    def generarTicket(self):
        if self.estado == "PAGADA":
            print(f"\n\n---- TICKET DE LA FUNCIÓN {self.idReserva} ----")
            print(f"Usuario: {self.usuario.nombre}")
            print(f"Función: {self.funcion.idFuncion}")
            print(f"Hora: {self.funcion.horarioInicio}")
            print(f"Asientos seleccionados: {self.asientos}")
            print(f"Monto total: ${self.montoTotal:2f}")
        else:
            print("La reserva debe estar pagada para imprimir su ticket.")  


# MODULO DE INFRAESTRUCTURA
class Espacio:
    def __init__(self, idEspacio: int, nombre: str, ubicacion: str):
        self.idEspacio = idEspacio
        self.nombre = nombre
        self.ubicacion = ubicacion
        
    def verificarDisponibilidad(self):
        print("disponible?")

    def limpiarEspacio():
        print("Limpiando...")

class Sala(Espacio):
    def __init__(self, idEspacio, nombre, ubicacion, tipo: str, capacidadTotal: int, esVip: bool):
        super().__init__(idEspacio, nombre, ubicacion)
        self.tipo = tipo #2D, 3D, IMAX
        self.capacidadTotal = capacidadTotal
        self.esVip = esVip
    
    def ajustarAforo(self):
        print("Aforo ajustado")

    def obtenerTipoSala(self):
        return self.tipo
    
class ZonaComida(Espacio):
    def __init__(self, idEspacio, nombre, ubicacion, listaProductos: list, stockActual: map):
        super().__init__(idEspacio, nombre, ubicacion)
        self.listaProductos = listaProductos
        self.stockActual = stockActual
        
    def venderProducto(self, producto):
        print(f"Se ha vendido el producto {producto}")
        
    def actualizarInventario(self, producto, cantidad):
        print(f"Se ha restado la cantidad de {cantidad} al stock de {producto}")
        print(f"Stock actual: {self.stockActual}")
        
# LÓGICA DE FUNCIONES Y PELÍCULAS
class Pelicula:
    cartelera = []
    
    def __init__(self, titulo: str, duracion: int, clasificacion: str, genero: str, sinopsis: str):
        self.titulo = titulo
        self.duracion = duracion #Duración en minutos
        self.clasificacion = clasificacion
        self.genero = genero # Terror, Romance, Acción, Familiar, Animada
        self.sinopsis = sinopsis
        
        self.cartelera.append(self)
        
    def __str__(self):
        return f"{self.titulo} ({self.duracion} min) | [{self.clasificacion}] | Género: {self.genero} | Sinopsis: {self.sinopsis}"
        
    def obtenerSinopsis(self):
        return self.sinopsis
    
    def esAptaParaTodoPublico(self):
        if self.clasificacion == "R" or self.clasificacion == "PG-13":
            return False
        
        return True
    
    @classmethod
    def imprimirCartelera(self):
        print("\n---- CARTELERA ACTUAL ----")
        for p in self.cartelera:
            print(f"{p.titulo} ({p.duracion} min) | [{p.clasificacion}]")

class Funcion:
    funciones = []
    
    def __init__(self, idFuncion: int, pelicula: Pelicula, sala: Sala, horarioInicio: datetime, precioBase: float):
        self.idFuncion = idFuncion
        self.pelicula = pelicula
        self.sala = sala
        self.horarioInicio = horarioInicio
        self.precioBase = precioBase
        self.listaAsientosOcupados = []
        
        self.funciones.append(self)
        
    def __str__(self):
        return f"ID: {self.idFuncion}, Película: {self.pelicula.titulo}, Sala: {self.sala.nombre} ({self.sala.tipo}, Hora:{self.horarioInicio}, Precio: ${self.precioBase})"
        
    def calcularAsientosLibres(self, asientosSolicitados: list) -> bool:
        flag = True
        for a in asientosSolicitados:
            if a in self.listaAsientosOcupados:
                print(f"[ERROR]: El asiento {a} ya se encuentra ocupado, seleccione asientos disponibles.")
                flag = False
                return False
        if flag:
            for asien in asientosSolicitados: self.listaAsientosOcupados.append(asien) #Metemos los asientos a la lista de la función seleccionada si todo está correcto
            print(self.listaAsientosOcupados)
            print(f"'\nTodo correcto! los asientos {asientosSolicitados} han sido bloqueados")
            return True
            
    def obtenerDetallesFuncion(self):
        print(f"---- FUNCIÓN (ID: {self.idFuncion})")
        print(f"{self.pelicula.titulo} - {self.pelicula.duracion} minutos")
        print(f"Sala: {self.sala.nombre} ({self.sala.tipo})")
        print(f"Hora de inicio: {self.horarioInicio}")
        print(f"Precio base por boleto: ${self.precioBase}")
    
    @classmethod   
    def imprimirFunciones(self, tituloAFiltrar: str):
        print("\n---- FUNCIONES ----")
        if(self.funciones):
            for funcion in self.funciones:
                if funcion.pelicula.titulo == tituloAFiltrar:
                    print(funcion)
        else:
            print(f"No hay funciones existentes para la película de {tituloAFiltrar}")
