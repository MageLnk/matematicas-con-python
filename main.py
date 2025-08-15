from breakCycle import breakCycle

repeatCicle = True
while repeatCicle == True:
    print("Bienvenido!")
    # print("Elije la opción que deseas realizar: ")
    # print("¿Sabes si un número real es positivo, negativo o cero?")



    isLeave = breakCycle()
    if isLeave == True:
        exit()