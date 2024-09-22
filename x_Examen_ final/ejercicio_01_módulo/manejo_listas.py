
"""Primer ejercicio: Manejo de listas"""


import random


def lista_aleatoria():
    lista = [random.randint(1, 100) for _ in range(10)]
    print("La lista aleatoria ha sido generada:", lista)
    return lista


def repetidos(lista):
    lista_sin_repetidos = list(set(lista))
    print("La lista sin números repetidos es:", lista_sin_repetidos)
    return lista_sin_repetidos


def ordenar(lista):
    lista_mayor_a_menor = sorted(lista, reverse=True)
    lista_menor_a_mayor = sorted(lista)
    print("La lista ordenada de mayor a menor es:", lista_mayor_a_menor)
    print("La lista ordenada de menor a mayor es:", lista_menor_a_mayor)
    return lista_mayor_a_menor, lista_menor_a_mayor


def mayor_numero_par(lista):
    lista_pares = [num for num in lista if num % 2 == 0]
    if lista_pares:
        mayor_par = max(lista_pares)
        print("El mayor número par de la lista es:", mayor_par)
        return mayor_par
    else:
        print("No se encuentran números pares en la lista.")
        return None
