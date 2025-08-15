def breakCycle():
    isRunning = True
    while isRunning == True:
        selectOption = int(input("Presione 1 para volver al inicio del programa, si no, presione 0 para salir. "))
        if selectOption == 1:
            return False
        elif selectOption == 0:
            isRunning = False
            print("Saliendo... Muchas gracias por usar el programa!")
            return True
        else:
            print("Opción no válida. Por favor, elige nuevamente.")