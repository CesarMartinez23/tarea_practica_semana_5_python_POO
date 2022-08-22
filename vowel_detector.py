
# Creacion de una funcion la cual recibe un caracter de tipo string y si este es una vocal, se retornara que es una vocal, de lo contrario, se retornara que es una consonante, pero si este es un dijito muestra un error de tipo de dato ingresado.
def enterVowel():

    # Se crea una lista con las vocales.
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Se solicita al usuario que ingrese una letra, y dependiendo de lo ingresado se valida y se ejecuta una accion.
    while(True):
        vowel = input("Enter a vowel: ")
        if vowel.isdigit():
            print("-" * 55)
            print("Wrong data type, enter only a letter, please try again.")
            print("-" * 55)
        elif len(vowel) > 1:
            print("-" * 55)
            print("The data cannot be processed, please try again.")
            print("-" * 55)
        elif vowel.lower() not in vowels:
            print("-" * 55)
            print(f"Is a consonant: {vowel}")
            print("-" * 55)
            break
        elif vowel.lower() in vowels:
            print("-" * 55)
            print(f"Is a vowel: {vowel}")
            print("-" * 55)
            break

enterVowel()