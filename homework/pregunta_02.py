"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from collections import Counter

x = open("files/input/data.csv", "r").readlines()
def pregunta_02():
    y=(z.strip().split('\t')[0] for z in x)
    return list(sorted(Counter(y).items()))

if __name__ == "__main__":
    print(pregunta_02()) 
        




    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
