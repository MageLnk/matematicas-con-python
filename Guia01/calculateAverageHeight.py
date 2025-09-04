def calculateAverageHeight():
    #Calcula la altura promedio de un niño entre 0 y 12 meses de vida.
    age = int(input("¿Cuántos meses tiene de edad el niño? (0-12) "))
    if age < 0 or age > 12:
        print("Edad no válida. Debe estar entre 0 y 12 meses.")
        return
    result = 2/3 * age + 48
    print(f"La altura promedio del niño de {age} meses es {result:.1f} cm.")
    return