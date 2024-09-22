
"""Tercer ejercicio: Decorador para medir el tiempo de ejecución"""

import time
from functools import wraps


def medicion_de_tiempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        tiempo_total = end_time - start_time
        print("Tiempo de ejecución de {}: {} segundos"
              .format(func.__name__, tiempo_total))
        return result
    return wrapper


@medicion_de_tiempo
def suma_de_elementos(**kwargs):
    suma = sum(kwargs.values())
    print("La suma de los elementos es: {}".format(suma))
    return suma


@medicion_de_tiempo
def numero_mayor(**kwargs):
    mayor = max(kwargs.values())
    print("El número mayor es: {}".format(mayor))
    return mayor


@medicion_de_tiempo
def calculo_tiempo(**kwargs):
    print("Los números proporcionados son:", kwargs)
    return kwargs


print("Ejemplo 1: Sumar 6 números")
suma_de_elementos(a=10, b=20, c=30, d=40, e=50, f=60)
print("")

print("Ejemplo 2: Encontrar el mayor de 6 números")
numero_mayor(x=8, y=12, z=3, w=15, v=7, u=9)
print("")

print("Ejemplo 3: Prueba con varios parámetros")
calculo_tiempo(n1=5, n2=15, n3=25, n4=35, n5=45, n6=55)
print("")
