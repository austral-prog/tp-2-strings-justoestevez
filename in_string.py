def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    nombre = input("Ingresar nombre:"). lower()
    contiene_a = "a" in nombre
    contiene_e = "e" in nombre
    contiene_i = "i" in nombre
    contiene_o = "o" in nombre
    contiene_u = "u" in nombre

    print(f"Contiene a: {contiene_a}")
    print(f"Contiene e: {contiene_e}")
    print(f"Contiene i: {contiene_i}")
    print(f"Contiene o: {contiene_o}")
    print(f"Contiene u: {contiene_u}")
