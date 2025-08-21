from breakCycle import breakCycle
from Clase01.calculateAverageHeight import calculateAverageHeight
from Clase01.determineParacetamolDoseForKids import determineParacetamolDoseForKids
from optionNotAvailable import optionNotAvailable


mathFunctionMapping = {
    1: calculateAverageHeight,
    2: determineParacetamolDoseForKids,
    # Agrega más opciones aquí
}

repeatCicle = True
print("Bienvenido!")
print("Este programa te ayudará a realizar difentes calculos matemáticos.")
while repeatCicle == True:
    print("Elije la opción que deseas experimentar: ")
    print("1. Calcular la altura promedio de un niño entre 0 y 12 meses de vida.")
    print("2. Calcular la dosis de paracetamol para niños de 1 a 12 años.")

    print("0. Salir del programa.")
    selectOption = int(input("Elija su opción. "))

    if selectOption == 0:
        print("Gracias por usar el programa. ¡Hasta luego!")
        exit()

    selectedOptionFunction = mathFunctionMapping.get(selectOption, optionNotAvailable)
    selectedOptionFunction()
    



    isLeave = breakCycle()
    if isLeave == True:
        exit()