
"""Problema 01"""

nombre = "Livia"
salario = 2700
edad = ("20")
compañia = "Interbank"
print("nombre:", type(nombre))
print("salario:", type(salario))
print("edad:", type(edad))
print("compañia:",type(compañia))

edad2= int(edad)
print("edad2:",type(edad2))

if edad2 > 30:
    print("Usted tiene un bono de 10% en el mes de diciembre")
    bono_porcentaje = 0.10
else:
    print("Usted tiene un bono del 5% en el mes de diciembre")
    bono_porcentaje = 0.05

bono_1= (salario*bono_porcentaje)
print(bono_1)
bono_final= (salario ** 2) + bono_1
print(bono_final)

