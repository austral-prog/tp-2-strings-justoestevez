def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    print("Ingresar gasto:")
    gasto = float(input())
    print(gasto)

    print("Dinero recibido")
    dinero = int(input())
    print(dinero)

    print("\nVuelto")

    vuelto = dinero - gasto

    print("\nPesos:")
    print(int(vuelto))

    centavos = round((vuelto - int(vuelto)) * 100)
    print("Centavos:")
    print(centavos)
   

