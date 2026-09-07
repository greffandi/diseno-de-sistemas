class Persona:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def detectar_rol(self):
        if "admin" in self.correo:
            return "administrador"
        elif "capitan" in self.correo:
            return "capitan"
        else:
            return "estudiante"


class ReglaPrioridad:
    def puede_reservar(self, horario):
        raise NotImplementedError


class ConPrioridad(ReglaPrioridad):
    def puede_reservar(self, horario):
        return True


class SinPrioridad(ReglaPrioridad):
    def puede_reservar(self, horario):
        return horario >= 18


class Estudiante(Persona):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo)
        self.reservas = []
        self.regla_prioridad = SinPrioridad()

    def reservar(self, cancha, horario):
        print(f"{self.nombre}: solicita reservar {cancha.id} a las {horario}:00")
        print(f"sistema: verifica disponibilidad de {cancha.id}")
        if not cancha.esta_disponible():
            print(f"sistema: sin disponibilidad en {cancha.id}")
            return None
        print(f"sistema: verifica regla de prioridad para {self.nombre}")
        if not self.regla_prioridad.puede_reservar(horario):
            print(f"sistema: reserva rechazada, antes de las 18:00 solo capitanes")
            return None
        reserva = Reserva(self, cancha, horario)
        self.reservas.append(reserva)
        print(f"sistema: reserva creada en {cancha.id} a las {horario}:00")
        return reserva

    def ver_reservas(self):
        print(f"{self.nombre}: solicita ver sus reservas")
        print(f"sistema: verifica si hay reserva realizada")
        if not self.reservas:
            print(f"sistema: no hay reservas")
            return
        for reserva in self.reservas:
            print(f"{self.nombre}: reserva en {reserva.cancha.id} a las {reserva.hora_inicio}:00, estado {reserva.estado}")


class Capitan(Estudiante):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo)
        self.regla_prioridad = ConPrioridad()


class Administrador(Persona):
    def gestionar_cancha(self, cancha):
        print(f"{self.nombre}: consulta la cancha {cancha.id}")
        print(f"sistema: verifica si {cancha.id} necesita mantenimiento")
        if cancha.necesita_mantenimiento:
            cancha.bloquear()
            print(f"sistema: {cancha.id} bloqueada por mantenimiento")
        else:
            print(f"sistema: {cancha.id} sigue disponible")

    def resolver_colision(self, colision):
        print(f"{self.nombre}: consulta conflicto en reserva")
        print(f"sistema: verifica si el conflicto es entre capitanes")
        tipo = colision.identificar_tipo()
        if tipo == "capitanes":
            print(f"sistema: conflicto entre capitanes detectado")
        else:
            print(f"sistema: verifica si el conflicto es entre estudiantes")
            print(f"sistema: conflicto entre estudiantes detectado")
        ganador = colision.reservas_en_conflicto[0]
        colision.resolver(ganador)
        print(f"{self.nombre}: decide asignar la reserva a {ganador.solicitante.nombre}")


class Cancha:
    def __init__(self, id, necesita_mantenimiento=False):
        self.id = id
        self.estado = "disponible"
        self.necesita_mantenimiento = necesita_mantenimiento

    def bloquear(self):
        self.estado = "mantenimiento"

    def esta_disponible(self):
        return self.estado == "disponible"


class Reserva:
    def __init__(self, solicitante, cancha, hora_inicio):
        self.solicitante = solicitante
        self.cancha = cancha
        self.hora_inicio = hora_inicio
        self.estado = "activa"

    def cancelar(self, horas_restantes):
        print(f"{self.solicitante.nombre}: solicita cancelar reserva en {self.cancha.id}")
        print(f"sistema: calcula tiempo restante hasta el inicio de la reserva")
        if horas_restantes < 2:
            self.estado = "no-show"
            print(f"sistema: registra la accion como no-show")
        else:
            self.estado = "cancelada"
            print(f"sistema: registra la cancelacion como cancelacion regular")


class Colision:
    def __init__(self, reservas_en_conflicto):
        self.reservas_en_conflicto = reservas_en_conflicto

    def identificar_tipo(self):
        tipos = set(type(r.solicitante).__name__ for r in self.reservas_en_conflicto)
        if tipos == {"Capitan"}:
            return "capitanes"
        return "estudiantes"

    def resolver(self, ganador):
        for reserva in self.reservas_en_conflicto:
            if reserva is not ganador:
                reserva.estado = "cancelada"
