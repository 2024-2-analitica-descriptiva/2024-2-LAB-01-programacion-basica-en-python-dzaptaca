"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

x=list(z.strip().split('\t') for z in open("files/input/data.csv", "r").readlines())
for i in x:
    l=[]
    for j in i[4].replace(':',',').split(','):
        try:
            int(j)
            l.append(int(j))
        except ValueError:
            pass
        except TypeError:
            pass
        
    i.append(sum(l))
def pregunta_12():
    y=list(set(z[0] for z in x))
    return(dict(sorted((z,sum(t[5] for t in x if t[0]==z)) for z in y)))

if __name__ == "__main__":
    print(pregunta_12()) 
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
