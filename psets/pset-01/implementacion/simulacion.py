from modelo import Estudiante, Capitan, Administrador, Cancha, Colision
 
estudiante = Estudiante("Ana", "ana@estudiante.uni.edu")
capitan = Capitan("Luis", "luis@capitan.uni.edu")
capitan2 = Capitan("Jorge", "jorge@capitan.uni.edu")
estudiante2 = Estudiante("Pedro", "pedro@estudiante.uni.edu")
admin = Administrador("Marta", "marta@admin.uni.edu")
 
for persona in [estudiante, capitan, admin]:
    print(f"{persona.nombre}: ingresa con correo {persona.correo}")
    print(f"sistema: verifica el dominio del correo")
    print(f"sistema: concede acceso como {persona.detectar_rol()}")
 
cancha1 = Cancha("Cancha 1")
cancha2 = Cancha("Cancha 2", necesita_mantenimiento=True)
 
estudiante.reservar(cancha1, 17)
capitan.reservar(cancha1, 17)
 
estudiante.reservar(cancha2, 20)
 
reserva_ana = estudiante.reservar(cancha1, 20)
estudiante.ver_reservas()
 
if reserva_ana:
    reserva_ana.cancelar(1)
 
estudiante2.ver_reservas()
 
admin.gestionar_cancha(cancha1)
admin.gestionar_cancha(cancha2)
 
reserva_luis = capitan.reservar(cancha1, 15)
reserva_jorge = capitan2.reservar(cancha1, 15)
colision_capitanes = Colision([reserva_luis, reserva_jorge])
admin.resolver_colision(colision_capitanes)
 
reserva_ana2 = estudiante.reservar(cancha1, 19)
reserva_pedro = estudiante2.reservar(cancha1, 19)
colision_estudiantes = Colision([reserva_ana2, reserva_pedro])
admin.resolver_colision(colision_estudiantes)