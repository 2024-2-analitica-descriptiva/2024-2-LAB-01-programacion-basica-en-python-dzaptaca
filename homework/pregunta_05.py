"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

x=list(z.strip().split('\t') for z in open("files/input/data.csv", "r").readlines())
def pregunta_05():
    y=list(set(z[0] for z in x))
    y=sorted([(z,max([int(t[1]) for t in x  if t[0] == z]),min([int(t[1]) for t in x  if t[0] == z])) for z in y])
    return y
if __name__ == "__main__":
    print(pregunta_05()) 
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
