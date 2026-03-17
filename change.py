def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
     gasto = float(input("Ingresar gasto: "))
    recibido = int(input("Dinero recibido: "))

   
    vuelto = recibido - gasto
    
   
    pesos = int(vuelto)
    
    
    centavos = round((vuelto - pesos) * 100)


    print("\nVuelto")
    print("\nPesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)

if __name__ == "__main__":
    change()
