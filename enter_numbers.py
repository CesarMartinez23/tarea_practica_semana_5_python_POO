
# Creacion de una funcion para ingresar numeros y mientras este no sea un 0 (cero), se agregaran a una lista, cuando se ingrese el 0 (cero), se retornara la suma total de los numeros almacenados en la lista.
def enterNumbers():
    
    # Se crea una lista vacia.
    numbers = []
    
    # Mientras el usuario no ingrese un 0 (cero), se ingresaran numeros a la lista.
    while True:
        number = int(input("Enter a number: "))
        
        # Si el usuario ingresa un 0 (cero), se retornara la suma total de los numeros almacenados en la lista.
        if(number == 0):
            break
        else:
            numbers.append(number)
    totalAmount = sum(numbers)
    print("The total amount is: ", totalAmount)

enterNumbers()