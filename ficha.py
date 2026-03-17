def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)


  
    nombre_sucio = input("Nombre completo: ")
    email_sucio = input("Email: ")
    n1 = input("Nota 1: ")
    n2 = input("Nota 2: ")
    n3 = input("Nota 3: ")

   
    nombre_completo = nombre_sucio.strip().title()
    email = email_sucio.strip().lower()
    
  
    espacio = nombre_completo.find(" ")
    nombre = nombre_completo[:espacio]
    apellido = nombre_completo[espacio + 1:]
    
   
    iniciales = (nombre_completo[0] + nombre_completo[espacio + 1]).upper()
    
    
    dominio = email[email.find('@') + 1:]

  
    nota_1, nota_2, nota_3 = int(n1), int(n2), int(n3)
    suma = nota_1 + nota_2 + nota_3
    promedio = suma / 3
    promedio_entero = suma // 3

  
    print("=" * 24)
    print("    FICHA DEL ALUMNO") 
    print("=" * 24)
    print(f"Nombre: {nombre_completo}")
    print(f"Email: {email}")
    print(f"Caracteres en nombre: {len(nombre_completo)}")
    print(f"Iniciales: {iniciales}")
    print(f"Usuario: {apellido.lower()}.{nombre.lower()}")
    print(f"Email valido: {'@' in email}")
    print(f"Dominio: {dominio}")
    print(f"Nombre para archivo: {nombre_completo.replace(' ', '_')}")
    print(f"Cantidad de a: {nombre_completo.lower().count('a')}")
    print(f"Codigo secreto: {nombre_completo.upper()[::-1]}")
    print(f"Nota 1: {nota_1}")
    print(f"Nota 2: {nota_2}")
    print(f"Nota 3: {nota_3}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {promedio_entero}")
    print("=" * 24)
