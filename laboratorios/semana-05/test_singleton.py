from singleton import GestorDeConfiguracion, reserva_permitida

def reset_singleton():
    GestorDeConfiguracion._objeto = None
    yield
    GestorDeConfiguracion._objeto = None

def test_rechaza_reserva():
    config = GestorDeConfiguracion.obtener_objeto()
    config.modo_mantenimiento = True
    assert reserva_permitida(config) is False

def test_reserva_aceptada():
    config = GestorDeConfiguracion.obtener_objeto()
    config.modo_mantenimiento = False
    assert reserva_permitida(config) is True
    
    
# El test falla porque el singleton guarda su instancia en _objeto, así que
# ambos tests comparten el mismo objeto: test_rechaza_reserva corre primero y
# deja modo_mantenimiento = True, y cuando test_reserva_aceptada pide la
# instancia recibe ese mismo objeto ya modificado, por lo que reserva_permitida
# da False en vez de True. La solución es resetear
# GestorDeConfiguracion._objeto = None antes de cada test (por ejemplo con una
# fixture) y fijar explícitamente modo_mantenimiento en cada uno, en vez de
# depender del estado que dejó el test anterior.
    