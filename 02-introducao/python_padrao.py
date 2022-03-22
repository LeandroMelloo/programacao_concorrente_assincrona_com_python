import datetime
import math


def main():
    inicio = datetime.datetime.now()

    computar(fim=50_000_000) # cronometro finalizou vai para proxima linha

    tempo = datetime.datetime.now() - inicio

    print(f'Terminou em {tempo.total_seconds():.2f} segundos')


def computar(fim, inicio=1):
    posicao = inicio
    fator = 1000 * 1000

    """
        posicao = 1 -> pois inicio que é passado por parametro equivale a 1
        fim = 50 milhões -> pois fim que é passado por parametro equivale a computar(fim=50_000_000)
    """

    while posicao < fim:
        posicao += 1
        math.sqrt((posicao - fator) * (posicao - fator)) # calculando a raiz quadrada


if __name__ == '__main__':
    main()

"""
Terminou em 13.73 segundos
"""
