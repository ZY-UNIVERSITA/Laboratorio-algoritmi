import numpy as np
import math

arrayVuoto = (([], 0), -1)
arrayOrdinatosingoloElementoTrue = (([ x for x in range(1)], 0), 0)
arrayOrdinatosingoloElementoFalse = (([ x for x in range(1)], 1), -1)
arrayOrdinatoElementiMultipliTrue = (([ x for x in range(10)], 2), 2)
arrayOrdinatoElementiMultipliFalse = (([ x for x in range(10)], 15), -1)

# Random array for avg test case
def randomTest(ordinato):
    dimensioneArray = 100
    # genera un valore da ricercare
    randomChoice = np.random.randint(0, 150)

    # Se si richiede un array ordinato
    randomOrLinear = True
    
    # scelta tra un array già ordinato o un array casuale se la funzione non accetta il parametro "ordinato"
    if not(ordinato):
        randomOrLinear = np.random.choice(a=[True, False])

    if randomOrLinear:
        # crea un array ordinato
        array = np.arange(0, dimensioneArray, 1)
    else:
        # crea un array non ordinato
        array = np.random.randint(0, 100, dimensioneArray)

    valueInArray = np.where(array == randomChoice)
    
    return ((array, randomChoice), -1 if len(valueInArray[0]) == 0 else (valueInArray)[0][0] )

# create an array for worst case testing
def worstCase(lenArray):
    array = np.arange(0, 10000*lenArray)
    randomChoice = 10000*lenArray
    valueInArray = np.where(array == randomChoice)
    return ((array, randomChoice), -1 if len(valueInArray[0]) == 0 else (valueInArray)[0][0] )

# return array for testing
def returnTestCase(ordinato=False, numeroDiTest=10, plot=False):
    if (plot):
        array = [ worstCase(lenArray) for lenArray in range(0, numeroDiTest) ]
        print(array)
    else:
        array = [ randomTest(ordinato) for x in range(numeroDiTest) ]
        array.extend([arrayVuoto, arrayOrdinatosingoloElementoTrue, arrayOrdinatosingoloElementoFalse, arrayOrdinatoElementiMultipliTrue, arrayOrdinatoElementiMultipliFalse])
    
    return array
