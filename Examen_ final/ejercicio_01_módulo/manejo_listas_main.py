
import manejo_listas


def main():

    lista_aleatoria = manejo_listas.lista_aleatoria()

    lista_sin_repetidos = manejo_listas.repetidos(lista_aleatoria)

    ordenar = manejo_listas.ordenar(lista_sin_repetidos)

    mayor_numero_par = manejo_listas.mayor_numero_par(lista_sin_repetidos)


if __name__ == "__main__":
    main()
