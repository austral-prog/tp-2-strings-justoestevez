def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    
    gasto = float(input("Ingresar gasto:"))
    recibido = int(input("Dinero recibido:"))

    vuelto = recibido - gastos
    
    pesos = int(vuelto)
    
    centavos = (vuelto - pesos) * 100

    print("\nVuelto")
    print("\nPesos:")
    print(pesos)
    print("Centavos:")
    print(int(centavos))
    
   

