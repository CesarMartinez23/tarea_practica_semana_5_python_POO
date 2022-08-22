
class Library:

    # Creacion del metodo contructor de la clase
    def __init__(self):
        # Creamos una lista donde almacenaremos los libros.
        self.books = []

    # Creacion de la funcion del menu principal de la gestion de la libreria
    def mainMenu(self):
        # Menu Principal de la gestion de la libreria
        print("\n")
        print("*" * 45)
        print("\tWelcome to the Library UGB")
        print("*" * 45 + "\n")
        print("-" * 45)
        print("1. Add Book" + "\n" + "2. List Books" + "\n" +
              "3. Search Book" + "\n" + "4. Edit Book" + "\n" + "5. Exit")
        print("-" * 45)
        
        # Dependiendo de la opcion seleccionada se ejecutara una accion.
        optionSelected = int(input("Select an option: "))
        print("-" * 45 + "\n")
        if optionSelected == 1:
            self.addBook()
        elif optionSelected == 2:
            self.listBooks()
        elif optionSelected == 3:
            self.searchBook()
        elif optionSelected == 4:
            self.editBook()
        elif optionSelected == 5:
            print("Exiting program...")
            exit()
            
        self.mainMenu()

    # Creacion de la funcion para agregar un libro a la libreria.
    def addBook(self):
        print("*" * 46)
        print("\t \tAdd a New Book")
        print("*" * 46)
        
        # Recibimos los datos del libro a agregar.
        idBook = input("Enter the id of the book: ")
        nameBook = input("Enter the name of the book: ")
        authorBook = input("Enter the author of the book: ")
        publisherBook = input("Enter the publisher of the book: ")
        stockBook = int(input("Enter the stock of the book: "))
        priceBook = float(input("Enter the price of the book: $ "))
        
        # Enviamos los datos del libro a la lista de libros.
        self.books.append({'id': idBook, 'name': nameBook, 'author': authorBook,
                          'publisher': publisherBook, 'stock': stockBook, 'price': priceBook})
        print("-" * 46)

    # Creacion de la funcion para listar los libros existentes de la libreria.
    def listBooks(self):
        print("*" * 46)
        print("\t \tList of Books")
        print("*" * 46)
        print("\n")
        
        numberBook = 1
        
        # Si la lista de libros esta vacia, se mostrara un mensaje.
        if len(self.books) == 0:
            print("\tNo books in the library")
        else:
            # Si la lista de libros no esta vacia, se mostraran el dato del nombre del libro.
            for i in range(len(self.books)):
                print("-" * 46)
                print("Book: ", numberBook)
                print("-" * 46)
                print("Name:\t" + self.books[i]['name'])
                # print(self.books[i]['id'], self.books[i]['name'], self.books[i]
                #       ['publisher'], self.books[i]['stock'], self.books[i]['price'])
                print("-" * 46)
                numberBook += 1

    # Creacion de la funcion para buscar un libro en la libreria.
    def searchBook(self):
        print("*" * 46)
        print("\t \tSearch Book")
        print("*" * 46)
        
        # Se recibe el nombre del libro a buscar.
        search = input("Enter the name of the book: ")
        
        # Recorremos la lista de libros para buscar el libro.
        for i in range(len(self.books)):
            
            # Si el nombre del libro es igual al nombre buscado, se mostrara el libro.
            if self.books[i]['name'] == search:
                print("\n")
                print("*" * 46)
                print("\tDetails of the book")
                print("*" * 46)
                print("Id Book: ", self.books[i]['id'])
                print("Name Book: ", self.books[i]['name'])
                print("Author Book: ", self.books[i]['author'])
                print("Publisher Book: ", self.books[i]['publisher'])
                print("Stock Book: ", self.books[i]['stock'])
                print("Price Book: $ ", self.books[i]['price'])
                print("-" * 46)
                break
        else:
            # Si el nombre del libro no es igual al nombre buscado, se mostrara un mensaje. 
            print("\tBook not found")
            print("\n")
            self.searchBook()
        return i

    # Creacion de la funcion para editar los datos de un libro existente.
    def editBook(self):
        print("*" * 46)
        print("\t \tEdit Book")
        print("*" * 46)
        
        # Reutilizamos la funcion searchBook para buscar el libro a editar.
        search = self.searchBook()
        
        # Se solicita que datos se desean editar. Y mientras el usuario ingrese una opcion valida, se editara el libro. Y cuando desee salir, salira del bucle de este menu para editar.
        while(True):
            print("-" * 45)
            print("Select witch field you want to edit: ")
            print("1. Id Book" + "\n" + "2. Name Book" + "\n" + "3. Author Book" + "\n" +
                  "4. Publisher Book" + "\n" + "5. Stock Book" + "\n" + "6. Price Book" + "\n" + "7. Exit")
            print("-" * 45)
            
            # Se solicita la opcion deseada.
            inputSelected = int(input("Select an option: "))
            
            # Dependiendo de la opcion seleccionada, se editara el campo de el libro seleccionado.
            if inputSelected == 1:
                newId = input("Enter the new id of the book: ")
                self.books[search]['id'] = newId
            elif inputSelected == 2:
                newName = input("Enter the new name of the book: ")
                self.books[search]['name'] = newName
            elif inputSelected == 3:
                newAuthor = input("Enter the new author of the book: ")
                self.books[search]['author'] = newAuthor
            elif inputSelected == 4:
                newPublisher = input("Enter the new publisher of the book: ")
                self.books[search]['publisher'] = newPublisher
            elif inputSelected == 5:
                newStock = int(input("Enter the new stock of the book: "))
                self.books[search]['stock'] = newStock
            elif inputSelected == 6:
                newPrice = float(input("Enter the new price of the book: $ "))
                self.books[search]['price'] = newPrice
            elif inputSelected == 7:
                break


library = Library()
library.mainMenu()