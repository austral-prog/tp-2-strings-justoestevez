def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"
    print(f"Palabra: {palabra}")
    
    longitud = len(palabra)
    print(f"Longitud: {longitud}")
    
    primera_letra = (palabra[0])
    print(f"Primera letra: {primera_letra}")
    
    ultima_letra = (palabra[-1])
    print(f"Ultima letra: {ultima_letra}")
    
    repetida = palabra * 3
    print(f"Repetida: {repetida}")
    
    decorada = f"{palabra}"
    print(f"Decorada: ***{decorada}***")
