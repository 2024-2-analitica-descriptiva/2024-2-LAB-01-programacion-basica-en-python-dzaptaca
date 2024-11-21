"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from collections import Counter
x=list(z.strip().split('\t') for z in open("files/input/data.csv", "r").readlines())
def pregunta_09():
    y=','.join([','.join(z[4].split(",")) for z in x]).split(',')
    p=[z[0] for z in [k.split(':') for k in y]]
    ##q=list(set(z[0] for z in p))
    ##w=sorted([(z,min([int(t[1]) for t in p  if t[0] == z]),max([int(t[1]) for t in p  if t[0] == z])) for z in q])

    return dict(sorted(Counter(p).items()))

if __name__ == "__main__":
    print(pregunta_09()) 
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
