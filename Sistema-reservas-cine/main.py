from models import *

listaUsuarios = [
    Usuario(1, "Javier", "javi@gmail.com", "2364748127", "9090", 10),
    Usuario(2, "Andrea", "andy@gmail.com", "2461728228","8444" ,50),
    Usuario(3, "Toño", "toñito@gmail.com", "2361231237","3123" ,150),
    Usuario(4, "Ximena", "xime@gmail.com", "2375675690","8678" ,200),
    Usuario(5, "Chloe", "chloe@gmail.com", "12625327865","0909" ,90)
]

listaEmpleados = [
    Empleado(1, "Juan Pérez", "juan.perez@email.com", "555-0101", "password123", "Admin", "9:00-18:00"),
    Empleado(2, "María García", "m.garcia@email.com", "555-0202", "segura789", "Ventas", "8:00-17:00"),
    Empleado(3, "Carlos Ruiz", "cruiz@email.com", "555-0303", "carlos_dev", "Soporte", "14:00-22:00"),
    Empleado(4, "Ana Martínez", "ana.mtz@email.com", "555-0404", "anaMTZ2024", "Gerente", "9:00-18:00"),
    Empleado(5, "Luis Torres", "ltorres@email.com", "555-0505", "luisito_pass", "Almacén", "07:00-16:00")
]

#print("LISTA DE USUARIOS")
#for u in listaUsuarios:
#    print(u)

#print("\nLISTA DE EMPLEADOS")   
#for e in listaEmpleados:
#    print(e)

listaEmpleados[1].logout()
listaEmpleados[1].login(2, "segura789")
listaEmpleados[1].logout()