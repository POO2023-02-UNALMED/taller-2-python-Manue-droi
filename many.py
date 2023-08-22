class Asiento:


    def __init__(self, color, precio, registroAsiento):
        self.color = color
        self.precio = precio
        self.registroAsiento = registroAsiento

    def cambiarColor(self, nuevoColor, color):
        if nuevoColor == "rojo" or nuevoColor =="verde" or nuevoColor == "amarillo" or nuevoColor =="negro" or nuevoColor =="blanco" == nuevoColor:
            self.nuevoColor = str(color)


class Motor:
    def __init__(self, numeroCilindros, tipo, registroMotor):
        self.numeroCilindros.self= numeroCilindros
        self.tipo = tipo
        self.registroMotor = registroMotor

    def cambiarRegistro(self, nuevoRegistro):
        self.registroMotor = int(nuevoRegistro)

    def asignarTipo(self, nuevoTipo):
        if nuevoTipo == "electrico" or nuevoTipo =="gasolina":
            self.tipo = str(nuevoTipo)   

class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registroAuto, cantidadCreados):
        self.modelo = modelo
        self.preciof = precio
        self.Asiento = asientos
        self.marca= marca
        self.Motor = motor
        self.registroAuto = registroAuto
        self.cantidadCreados = cantidadCreados

    def cantidadAsientos(self, asientos ):
        asientos = asientos
    


    def verificarIntegridad ( self, import class Auto(), import class Motor(), import class Asiento()):
        if registroAuto == registroMotor == registroAsiento:
            print("Auto original")
        else:
            print("Las piezas no son originales")