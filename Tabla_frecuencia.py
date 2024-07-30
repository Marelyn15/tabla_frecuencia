from collections import Counter
import math

group = [3,6,6,8,2,5,7,3,8,1,5,6,4,4,2,5,6,2,9,4,2,3,7,7,7]
percentil = 85

def tabla_frecuencia(grupo,percentil):
    #frecuencia absoluta

    # Convierte en diccionario los elementos sin repetición 
    # su valor es el número de veces que se repite
    FA = Counter(grupo)
    #Organizando
    FA = dict(sorted(FA.items()))
    print("Esto es la frecuencia absoluta (FA)", FA)

    CI = [] #Clave Individual
    #Valores de la clave individual
    for index, valor in enumerate(FA.keys()):
        CI.insert(index,valor)

    #Frecuencia absoluta acumulada
    nuevo_valor = 0
    FAA = []
    for index, valor in enumerate(FA.values()): 
        nuevo_valor = valor + nuevo_valor
        FAA.insert(index,nuevo_valor)

    FAA = dict(zip(CI,FAA))
    print(f"Frecuencia Absoluta acumulada (FAA) {FAA}")


    #frecuencia relativa
    # Desde el diccionario de frecuencia absoluta se toma el numero y su frecuencia 
    # Esto a su vez se divide entre el largo del grupo del inicio
    # Cuando se tiene el resultado se entra en una entrada de diccionario (osea el num)
    FR = {num: round(freq / len(grupo),2) for num, freq in FA.items()} # Numero : frecuencia relativa
    print(f"Esto es la frecuencia relativa (FR) {FR}")

    #Frecuencia relativa acumulada:
    nuevo_valor = 0
    FRA = []
    for index, valor in enumerate(FR.values()):
        nuevo_valor = valor + nuevo_valor
        FRA.insert(index,round(nuevo_valor,2))
    FRA = dict(zip(CI, FRA))
    print(f"Esto es frecuencia relativa acumulada (FRA) {FRA}")

    VI = [] #Clave Individual
    #Valores de la clave individual
    for index, valor in enumerate(FA.values()):
        VI.insert(index,valor)
    VI = sum(VI)
    print(VI)

    pxn = (VI * percentil) / 100
    print(f"El percentil a {percentil} % es {pxn} que sería más cercano al {math.ceil(pxn)} de la frecuencia absoluta")


tabla_frecuencia(group,percentil)


def tabla_frecuencia_intervalo(grupo):
    pass


def caja_bigotes(grupo):
    pass

