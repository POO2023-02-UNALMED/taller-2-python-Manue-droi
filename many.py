class Asiento:


    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, nuevoColor, color):
        if (nuevoColor == "rojo" or nuevoColor =="verde" or nuevoColor == "amarillo" or nuevoColor =="negro" or nuevoColor == "blanco"):
            self.nuevoColor = str(color)


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros= numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevoRegistro):
        self.registro = int(nuevoRegistro)

    def asignarTipo(self, nuevoTipo):
        if nuevoTipo == "electrico" or nuevoTipo =="gasolina":
            self.tipo = str(nuevoTipo)   

class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados):
        self.modelo = modelo
        self.preciof = precio
        self.Asiento = asientos
        self.marca= marca
        self.Motor = motor
        self.registro = registro
        self.cantidadCreados = cantidadCreados

    def cantidadAsientos(self, asientos ):
        asientos = asientos
    


 