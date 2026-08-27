class ComportamientoVuelo():
    def volar(self):
        raise NotImplementedError  # excepcion
        
class VuelaConAlas(ComportamientoVuelo):
    def volar(self):
        print("Volando con alas")
        
class Novuela(ComportamientoVuelo):
    def volar(self):
        print("No vuela")
        
class ComportamientoGraznar():
    def graznar(self):
        raise NotImplementedError  # excepcion

class GraznidoNormal(ComportamientoGraznar):
    def graznar(self):
        print("Cuack!")
        
class GraznidoDeGoma(ComportamientoGraznar):
    def graznar(self):
        print("Chirrido de goma")


class Pato:
    # CORREGIDO: Se cambiaron a dobles guiones bajos __init__
    def __init__(self, comportamiento_vuelo, comportamiento_graznido):
        self.comportamiento_vuelo = comportamiento_vuelo
        self.comportamiento_graznido = comportamiento_graznido

    def nadar(self):
        print("Nadando")
        
    def graznar(self):
        self.comportamiento_graznido.graznar()
        
    def volar(self):
        self.comportamiento_vuelo.volar()
        
class PatoSalvaje(Pato):
    # CORREGIDO: __init__
    def __init__(self):
        vuela_alas = VuelaConAlas()
        graznido_normal = GraznidoNormal()
        super().__init__(vuela_alas, graznido_normal) # CORREGIDO: super().__init__

class PatodeGoma(Pato):
    # CORREGIDO: __init__
    def __init__(self):
        graznido_de_goma = GraznidoDeGoma()
        no_vuela = Novuela()
        super().__init__(no_vuela, graznido_de_goma) # CORREGIDO: super().__init__


if __name__ == "__main__":
    salvaje = PatoSalvaje()
    salvaje.nadar()
    salvaje.graznar()
    salvaje.volar()
    
    print()
    
    goma = PatodeGoma()
    goma.nadar()
    goma.graznar()
    goma.volar()