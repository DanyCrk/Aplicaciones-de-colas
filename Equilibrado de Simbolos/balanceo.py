def balanceado(cadena, mostrar_pasos=True):
    pila = []
    
    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    aperturas = pares.values()
    cierres = pares.keys()

    if mostrar_pasos:
        print(f"\n Procesando: '{cadena}' ")

    for caracter in cadena:
        if caracter in aperturas:
            pila.append(caracter)
            if mostrar_pasos:
                print(f"'{caracter}' es apertura -> se apila. Pila actual: {pila}")

        elif caracter in cierres:
            if len(pila) == 0:
                if mostrar_pasos:
                    print(f"'{caracter}' es cierre, pero la pila está vacía, ERROR")
                return False, f"Error: se encontró '{caracter}' pero la pila está vacía."
            else:
                cima = pila[-1]
                if cima == pares[caracter]:
                    pila.pop()
                    if mostrar_pasos:
                        print(f"'{caracter}' coincide con la cima '{cima}' se extrae. Pila actual: {pila}")
                else:
                    if mostrar_pasos:
                        print(f"'{caracter}' no coincide con la cima '{cima}' ERROR")
                    return False, f"Error: se esperaba el cierre de '{cima}' pero se encontró '{caracter}'."

    if mostrar_pasos:
        print(f"\nFin de la cadena. Estado de la pila: {pila}")

    if len(pila) != 0:
        if mostrar_pasos:
            print("La pila no quedó vacía, ERROR")
        return False, f"Error: quedaron elementos sin cerrar en la pila: {pila}"

    if mostrar_pasos:
        print("La pila quedó vacía")
    return True, "La cadena está balanceada correctamente."

casos_prueba = [
    "[()]",       
    "([)]",       
    "[(])",       
    "([[]])",     
    "(()",        
    ")(",         
]

for caso in casos_prueba:
    resultado, mensaje = balanceado(caso)
    print(f"RESULTADO: Balanceada: {resultado} | {mensaje}")