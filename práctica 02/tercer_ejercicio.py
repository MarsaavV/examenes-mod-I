"""Tercer ejercicio"""

class Billetera:
    def __init__(self, nombre, apellido, soles, dolares, tipo_cambio):
        self.nombre = nombre
        self.apellido = apellido
        self.soles = soles
        self.dolares = dolares
        self.tipo_cambio = tipo_cambio

    def mostrar_saldos(self):
        print("{}, {} saldo en soles: {}, saldo en dólares: {}".format(self.nombre, self.apellido, self.soles, self.dolares))

    def transferir(self, monto, origen):
        if origen == "soles" and self.soles >= monto:
            self.soles -= monto
            self.dolares += monto / self.tipo_cambio
        elif origen == "dolares" and self.dolares >= monto:
            self.dolares -= monto
            self.soles += monto * self.tipo_cambio
        else:
            print("Fondos insuficientes")

    def retirar(self, monto, moneda):
        if moneda == "soles" and self.soles >= monto:
            self.soles -= monto
        elif moneda == "dolares" and self.dolares >= monto:
            self.dolares -= monto
        else:
            print("Fondos insuficientes")

        self.mostrar_saldos()

billetera = Billetera("Juan", "Pérez", 1000, 300, 3.7)

billetera.mostrar_saldos()
billetera.transferir(370, "soles")
billetera.transferir(80, "dolares")
billetera.retirar(300, "soles")
billetera.retirar(7000, "dolares")