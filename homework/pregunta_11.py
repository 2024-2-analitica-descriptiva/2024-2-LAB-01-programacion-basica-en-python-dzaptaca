"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

x=list(z.strip().split('\t') for z in open("files/input/data.csv", "r").readlines())
def pregunta_11():
    l=[]
    y=list(list(z[3].split(',')) for z in x)
    for i in y:
        l=l+i
    l=sorted(list(set(l)))
    d={z:sum(int(t[1]) for t in x if z in t[3].split(',')) for z in l}
    return d

if __name__ == "__main__":
    print(pregunta_11()) 

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
