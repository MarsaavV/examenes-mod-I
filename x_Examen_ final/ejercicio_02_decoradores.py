
"""Segundo ejercicio: Decorador de conteos"""

from functools import wraps
import datetime


def conteo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        total_params = len(args) + len(kwargs)

        if total_params > 1:
            print("La función {} recibió {} parámetros."
                  .format(func.__name__, total_params))
            result = func(*args, **kwargs)
            print("Función {} fue ejecutada correctamente."
                  .format(func.__name__))
            return result
        else:
            print("Función '{}' requiere más de un parámetro para ejecutarse."
                  .format(func.__name__))

    return wrapper


@conteo
def registro_de_personas(nombre, edad):

    hora_registro = datetime.datetime.now().strftime("%H:%M")
    print("persona registrada: Nombre: {}, Edad: {}, Hora de registro: {}"
          .format(nombre, edad, hora_registro))


def calculo_de_media(nota1, nota2, nota3, nota4):

    media = (nota1 + nota2 + nota3 + nota4) / 4
    print("La media de las notas es: {}".format(media))
    return media


registro_de_personas("Livia", 18)
calculo_de_media(18, 15, 17, 14)
