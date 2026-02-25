

class Persona:
    
    def __init__(self, idPersona: int, nombre: str, email: str, telefono: str, contrasena: str):
        self.idPersona = idPersona
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.contrasena = contrasena
        self.logeado = False 

    def login(self, id: str, c: str):
        if self.idPersona == id and self.contrasena == c:
            print(f"Bienvenido, {self.nombre}")
            self.logeado = True
        else:
            print(f"El Id de usuario o la contraseña son incorrectos, intente de nuevo")
    
    def logout(self):
        if self.login() == True:
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
    
    def __init__(self, idPersona: int, nombre: str, email: str, telefono: str, puntosFidelidad: int):
        super().__init__(idPersona, nombre, email, telefono)
        self.puntosFidelidad = puntosFidelidad
        
    def crearReserva(self):
        print("Reserva creada")
        
    def consultarPromociones(self):
        print("nohay")

    def cancelarReserva(self):
        print("Reserva cancelada")
        
        
class Promocion:
    
    def __init__(self, codigo: str, descripcion: str, porcentajeDescuento: float, fechaExpiracion: str):
            self.codigo = codigo
            self.descripcion = descripcion
            self.porcentajeDescuento = porcentajeDescuento
            self.fechaExpiracion = fechaExpiracion
    
    def esValida(self):
        print("Puede ser")
        return True
    
    def aplicarDescuento(self, monto: float):
        return monto * 0.01 + 100