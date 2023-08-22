import imaplib


class Asiento:

    def _init_(self, color, precio, registroAsiento):
        color.self = color
        precio.self = precio
        registroAsiento.self = registroAsiento

    def cambiarColor(self, nuevoColor, color):
        if nuevoColor == ("rojo" == nuevoColor or"verde" == nuevoColor or "amarillo" == nuevoColor or"negro"== nuevoColor or"blanco" == nuevoColor):
            nuevoColor.self == color


class Motor:
    def _init_(self, numeroCilindros, tipo, registroMotor):
        numeroCilindros.self= numeroCilindros
        tipo.self = tipo
        registroMotor.self = registroMotor

    def cambiarRegistro(self, nuevoRegistro, registroMotor):
        self.nuevoRegistro = registroMotor

    def asignarTipo(self, nuevoTipo):
        if nuevoTipo == "electrico" or "gasolina":
            self.tipo = nuevoTipo
        else:
            tipo = tipo    

class Auto:
    def _init_(self, modelo, precio, asiento, marca, motor, registroAuto, cantidadCreados):
        modelo.self = modelo
        precio.self = precio
        asiento.self = []
        marca.self= marca
        motor.self = motor
        registroAuto.self = registroAuto
        cantidadCreados = cantidadCreados

    def cantidadAsientos(self, asientos ):
        asientos.self = asientos
    

    def verificarIntegridad ( self, class Auto, class Motor, class Asiento):
        
        
            print("Las piezas no son originales")