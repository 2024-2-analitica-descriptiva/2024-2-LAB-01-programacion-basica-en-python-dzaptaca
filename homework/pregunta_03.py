"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

x=list(z.strip().split('\t') for z in open("files/input/data.csv", "r").readlines())
def pregunta_03():
    y=list(set(z[0] for z in x))
    y=sorted([(z,sum([int(t[1]) for t in x  if t[0] == z])) for z in y])
    return y
if __name__ == "__main__":
    print(pregunta_03()) 

    """filter = [z for z in x  if z[0] == "Date" or z[1] == "2013"]
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
