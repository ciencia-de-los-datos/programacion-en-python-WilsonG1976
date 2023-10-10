"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv

def pregunta_01():
    """Retorne la suma de la segunda columna. Rta/ 214
    """
    suma = 0
    with open('data.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter='\t')
        for fila in lector_csv:
            valor = float(fila[1])
            suma += valor
        #print(suma)
    return suma


def pregunta_02():
    """Retorne la cantidad de registros por cada letra de la primera columna como la lista de tuplas (letra, cantidad), ordendas alfabéticamente. Rta/
    [("A", 8),
    ("B", 7),
    ("C", 5),
    ("D", 6),
    ("E", 14),]    """
    contador = {}
    with open('data.csv', 'r') as archivo_csv:
      lector_csv = csv.reader(archivo_csv, delimiter='\t')
      for fila in lector_csv:
          letra = fila[0]
          contador[letra] = contador.get(letra, 0) + 1
    resultado = sorted(contador.items())
    #print(resultado)
    #for letra, cantidad in resultado:
    #    print(f"('{letra}', {cantidad})") 
        
    return resultado

def pregunta_03():
    """Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente. Rta/
    [("A", 53),
    ("B", 36),
    ("C", 27),
    ("D", 31),
    ("E", 67),]    """
    sumalet = {}
    with open('data.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter='\t')  
        for fila in lector_csv:
            letra = fila[0]
            valor = int(fila[1])
            sumalet[letra] = sumalet.get(letra, 0) + valor
        resultado = sorted(sumalet.items())
        #print(resultado)
    #for letra, suma in resultado:
    #    print(f"('{letra}', {suma})")
    return resultado


def pregunta_04():
    """ La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de registros por cada mes, tal como se muestra a continuación. Rta/
    [("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3), ]    """
    from collections import defaultdict
    conteomes = defaultdict(int)
    with open('data.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter='\t')
        
        for fila in lector_csv:
            fecha = fila[2]
            mes = fecha[5:7] #extrae los primeros 7 caracteres de la fecha
            conteomes[mes] += 1  
        resultado = sorted(conteomes.items())
            #print(resultado)
        #for mes, cantidad in resultado:
            #print(f"('{mes}', {cantidad}),")
    return resultado


def pregunta_05():
    """ Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada letra de la columa 1. Rta/
    [  ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),  
    ]  
    """
    maxmin_letra = {}
    with open('data.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter='\t')

        for fila in lector_csv:
            letra = fila[0]
            valor = int(fila[1])
            if letra in maxmin_letra:
                valormax, valormin = maxmin_letra[letra]
                valormax = max(valormax, valor)
                valormin = min(valormin, valor)
                maxmin_letra[letra] = (valormax, valormin)
            else:
                maxmin_letra[letra] = (valor, valor)
    resultado = sorted(maxmin_letra.items())
         
    #for letra, (maximo, minimo) in resultado:
    #    print(f"('{letra}', {maximo}, {minimo}),")
    return resultado


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    maxmin_letra = {}
    with open('data.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter='\t')
        for fila in lector_csv:
            diccionario = fila[4]
            pares = diccionario.split(',')
            for par in pares:
                clave, valor_str = par.split(':')
                valor = int(valor_str)
                if clave in maxmin_letra:
                    minimo, maximo = maxmin_letra[clave]
                    minimo = min(minimo, valor)
                    maximo = max(maximo, valor)
                    maxmin_letra[clave] = (minimo, maximo)
                else:
                    maxmin_letra[clave] = (valor, valor)
    resultado = sorted([(clave, minimo, maximo) for clave, (minimo, maximo) in maxmin_letra.items()])

    #for clave, minimo, maximo in resultado:
    #    print(f"('{clave}', {minimo}, {maximo}),")


    return resultado


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    asociacionletra = {}


    with open('data.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter='\t')

        for fila in lector_csv:
            # Asumiendo que la primera columna es la columna 2 (índice 1) y la segunda columna es la columna 1 (índice 0)
            valor_colum2 = int(fila[1])
            letra_colum1 = fila[0]

            # Agrega la letra a la lista correspondiente en el diccionario
            if valor_colum2 in asociacionletra:
                asociacionletra[valor_colum2].append(letra_colum1)
            else:
                asociacionletra[valor_colum2] = [letra_colum1]

# Convierte el diccionario en una lista de tuplas y ordena alfabéticamente por valor de columna 2
    resultado = sorted([(valor, letras) for valor, letras in asociacionletra.items()])


    return resultado


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    asociaciovalor = {}

    with open('data.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter='\t')

        for fila in lector_csv:
            # Asumiendo que la segunda columna es la columna 2 (índice 1) y la primera columna es la columna 1 (índice 0)
            valor_colum2 = int(fila[1])
            letra_colum1 = fila[0]

            # Agrega la letra a la lista correspondiente en el diccionario
            if valor_colum2 in asociaciovalor:
                asociaciovalor[valor_colum2].append(letra_colum1)
            else:
                asociaciovalor[valor_colum2] = [letra_colum1]

    # Convierte el diccionario en una lista de tuplas y ordena alfabéticamente por valor de columna 2
    resultado = sorted([(valor, sorted(list(set(letras)))) for valor, letras in asociaciovalor.items()])
    return resultado



def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    import json
    conteo_clave = {}

    with open('data.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter='\t')

        for fila in lector_csv:
            clave_colum5 = fila[4]
            if clave_colum5 in conteo_clave:
                conteo_clave[clave_colum5] += 1
            else:
                conteo_clave[clave_colum5] = 1

    resultado_json = json.dumps(conteo_clave, indent=4)
    return resultado_json


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    resultado = []


    with open('data.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter='\t')

        for fila in lector_csv:
            # Asumiendo que la primera columna contiene la letra (índice 0)
            letra_colum1 = fila[0]
            # Asumiendo que las columnas 4 y 5 contienen elementos
            cantidad_colum4 = len(fila[3].split(','))
            cantidad_colum5 = len(fila[4].split(','))

            # Agregar una tupla con la letra y las cantidades a la lista de resultados
            resultado.append((letra_colum1, cantidad_colum4, cantidad_colum5))
    
    return resultado


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    suma = {}


    with open('data.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter='\t')

        for fila in lector_csv:
            letra_colum4 = fila[3].lower()
            valor_colum2 = float(fila[1])
            if letra_colum4 in suma:
                suma[letra_colum4] += valor_colum2
            else:
                suma[letra_colum4] = valor_colum2
    resultados = {k: v for k, v in sorted(suma.items())}


    return resultados


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    suma_por_letra = {}


    with open('data.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter='\t')

        for fila in lector_csv:
            letra_columna1 = fila[0]
            valor_columna5 = fila[4].split(',')
            for par in valor_columna5:
                clave, valor = par.split(':')
                valor = int(valor)
                if letra_columna1 in suma_por_letra:
                    if clave in suma_por_letra[letra_columna1]:
                        suma_por_letra[letra_columna1][clave] += valor
                    else:
                        suma_por_letra[letra_columna1][clave] = valor
                else:
                    suma_por_letra[letra_columna1] = {clave: valor}

    # Calcular la suma total por letra
    suma_total_por_letra = {}
    for letra, valores in suma_por_letra.items():
        suma_total_por_letra[letra] = sum(valores.values())

    # Ordenar el diccionario alfabéticamente por clave (letra)
    suma_total_por_letra_ordenada = {k: v for k, v in sorted(suma_total_por_letra.items())}

    # Llamar a la función y almacenar el resultado en una variable
    resultado = suma_total_por_letra_ordenada


    return resultado
