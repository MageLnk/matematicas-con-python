def determineParacetamolDoseForKids():
    # Esta función calcula la dosis recomendada de paracetamol para un niño 
    # de 1 a 12 años de edad basados en la regla de Young.
    print ("Recuerde que esta calculadora calcula entre la edad de 1 a 12 años.")
    age = float(input("¿Cuántos años tiene el niño? (1-12) "))
    if age < 1 or age > 12:
        print("Edad no válida. Debe estar entre 1 y 12 años.")
        return
    dosage = (500*age) / (age+12)  # NOTA: Dosis basada en tabletas de 500 mg
    print(f"La dosis recomendada de paracetamol para un niño de {age} años es {dosage:.1f} mg.")
    print("Considere que el cálculo se hizo en relación a una pastilla de 500 mg.")
    return