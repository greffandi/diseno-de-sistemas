#Vehiculo que se mueva -> la funcion se va a llamar mover 

#Auto -> mueve por carretera -> Conduciendo por carretera
#Bote -> mueve por agua -> Navegando por agua
#avion -> mueve por aire -> Volando por aire


class ComportamientoVehiculo():
    def mover(self):
        raise NotImplementedError

class ComportamientoAuto(ComportamientoVehiculo):
    def mover(self):
        print("Conduciendo por carretera")

class ComportamientoBote(ComportamientoVehiculo):
    def mover(self):
        print("Navegando por agua")

class ComportamientoAvion(ComportamientoVehiculo):
    def mover(self):
        print("Volando por aire")


class Vehiculo:
    def __init__(self, comportamiento_vehiculo):
        self.comportamiento_vehiculo = comportamiento_vehiculo

    def mover(self):
        self.comportamiento_vehiculo.mover()


class Auto(Vehiculo):
    def __init__(self):
        super().__init__(ComportamientoAuto())

class Bote(Vehiculo):
    def __init__(self):
        super().__init__(ComportamientoBote())

class Avion(Vehiculo):
    def __init__(self):
        super().__init__(ComportamientoAvion())


if __name__ == "__main__":
    auto = Auto()
    auto.mover()      

    bote = Bote()
    bote.mover()       

    avion = Avion()
    avion.mover()      
