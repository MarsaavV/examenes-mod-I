
"""Segundo ejercicio"""

class Persona:
    def __init__(self):
        self.nombre=""
        self.edad=""
        self.saldo= 2700
        self.nacionalidad= "peruana"

    def metodo(self):
        self.nombre=input("Ingrese el nombre de la persona: ")
        self.edad=int(input("Ingrese la edad: "))

    def cumpleaños(self):
        self.edad+=1

    def AumentoSueldo(self):
        self.saldo*=1.3
        return self.saldo

    def edad_en_el_año(self, año):
        años_aumentados=año-2024
        edad_del_futuro=self.edad+años_aumentados
        return print("En el año {}, tendrá {} años".format(año, edad_del_futuro))

    def mostar_saldo(self):
        print("{} tiene un saldo actual de {}".format(self.nombre, self.saldo))

    def transferencia_1(self,persona,monto):
        if self.saldo >= monto:
            self.saldo -= monto
            persona.saldo += monto
            print("{} ha transferido {} a {}".format(Primera_persona,monto,Segunda_persona))
        else:
            print("Saldo insuficiente")

Primera_persona=Persona()
Primera_persona.metodo()
Nuevo_sueldo_1=Primera_persona.AumentoSueldo()
print("El sueldo incrementado es de: {}".format(Nuevo_sueldo_1))
print(Primera_persona.edad_en_el_año(2025))

Segunda_persona=Persona()
Segunda_persona.metodo()
Nuevo_sueldo_2=Primera_persona.AumentoSueldo()
print("El sueldo incrementado es de: {}".format(Nuevo_sueldo_2))
print(Segunda_persona.edad_en_el_año(2025))

monto_a_transferir = int(input("Ingrese el monto que {} desea transferir a {}: ".format(Primera_persona.nombre,Segunda_persona.nombre)))
print("{} ha transferido {} a {}".format(Primera_persona,monto_a_transferir,Segunda_persona))