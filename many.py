class Asiento:

    def __init__(self, color, precio, registroAsiento):
        color.self = color
        precio.self = precio
        registroAsiento.self = registroAsiento

    def cambiarColor(self, nuevoColor, color):
        if nuevoColor == "rojo" or nuevoColor =="verde" or nuevoColor == "amarillo" or nuevoColor =="negro" or nuevoColor =="blanco" == nuevoColor:
            nuevoColor.self = str(color)


class Motor:
    def __init__(self, numeroCilindros, tipo, registroMotor):
        numeroCilindros.self= numeroCilindros
        tipo.self = tipo
        registroMotor.self = registroMotor

    def cambiarRegistro(self, nuevoRegistro):
        self.registroMotor = int(nuevoRegistro)

    def asignarTipo(self, nuevoTipo):
        if nuevoTipo == "electrico" or nuevoTipo =="gasolina":
            self.tipo = str(nuevoTipo)   

class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registroAuto, cantidadCreados):
        modelo.self = modelo
        precio.self = precio
        Asiento = asientos
        marca.self= marca
        Motor = motor
        registroAuto.self = registroAuto
        cantidadCreados = cantidadCreados

    def cantidadAsientos(self, asientos ):
        asientos.self = asientos
    


    def verificarIntegridad ( self, import class Auto(), import class Motor(), import class Asiento()):
        if registroAuto == registroMotor == registroAsiento:
            print("Auto original")
        else:
            print("Las piezas no son originales")