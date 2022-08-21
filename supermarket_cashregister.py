
def printHyphen(number):
    print("-" * number)

def applyDiscount(totalAmount):
    printHyphen(45)
    print("\tHow do you want to pay?")
    printHyphen(45)
    print("1 - Cash")
    print("2 - Card Credit/Debit")
    printHyphen(45)
    option = int(input("Option:" + "\t"))
    
    discount = 0.0
    if option == 1:
        print("You have paid with cash")
        printHyphen(45)
        print("\n")
        if(totalAmount >= 100.00):
            discount = (totalAmount * 0.30)
        elif(totalAmount >= 50.00 and totalAmount < 100.00):
            discount = (totalAmount * 0.10)
    elif option == 2:
        print("You have paid with card")
        printHyphen(45)
        print("\n")
        if(totalAmount >= 100.00):
            discount = (totalAmount * 0.40)
        elif(totalAmount >= 50.00 and totalAmount < 100.00):
            discount = (totalAmount * 0.20)
    else:
        print("Invalid option")
    return discount

def saveProduct(codProduct, nameProduct, quantityProduct, priceProduct):
    return {"Codigo": codProduct, "Nombre": nameProduct, "Cantidad": quantityProduct, "Precio": priceProduct, "Total": (quantityProduct * priceProduct)}

def totalAmount(listBuyOut):
    total = 0.0
    for i in listBuyOut:
        total += i["Total"]
    return total

def printBuyOut(listBuyOut):
    numberProduct = 1
    
    printHyphen(35)
    print("\tThe BuyOut is:")
    printHyphen(35)
    
    for i in listBuyOut:
        
        printHyphen(35)
        print("\tProduct: ",numberProduct)
        printHyphen(35)
        print("Codigo: ", i["Codigo"])
        print("Nombre: ", i["Nombre"])
        print("Cantidad: ", i["Cantidad"])
        print("Precio: $ ", i["Precio"])
        print("Total: $ ", i["Total"])
        printHyphen(35)
        print("\n")
        numberProduct+=1

def printTotalBuyOut(buyOut, discount):
    printHyphen(28)
    print("\tTotal Buyout")
    printHyphen(28)

    printHyphen(28)
    print("Subtotal: $ ", totalAmount(buyOut))
    print("Discount: $ ", discount)
    print("Total: $ ", (totalAmount(buyOut) - discount))
    printHyphen(28)

def cashRegister():
    buyOut = []
    
    print("\n")
    printHyphen(45)
    print("\tWelcome to the Supermarket UGB")
    printHyphen(45)
    print("\n")
    
    while(True):
        printHyphen(45)
        codProduct = input("Please enter the id of the item: \n" + "ID:" + "\t")
        printHyphen(45)
        
        printHyphen(45)
        nameProduct = input("Please enter the name of the item: \n" + "Name:" + "\t")
        printHyphen(45)
        
        printHyphen(45)
        quantityProduct = int(input("Please enter the quantity of the item:\n" + "Quantity:" + "\t"))
        printHyphen(45)
        
        printHyphen(45)
        priceProduct = float(input("Please enter the price of the item:\n" + "Price: $" + "\t"))
        printHyphen(45)
        
        buyOut.append(saveProduct(codProduct, nameProduct, quantityProduct, priceProduct))
        
        printHyphen(75)
        addMoreProduct = int(input(
            "Do you want to add another product?, select the corresponding number!: \n 1 = Yes\n 2 = No\n" + "Option:" + "\t"))
        printHyphen(75)
        
        if addMoreProduct == 1:
            continue
        elif addMoreProduct == 2:
            discount = applyDiscount(totalAmount(buyOut))
            printBuyOut(buyOut)
            printTotalBuyOut(buyOut, discount)
            break
        else:
            print("Invalid option, your BuyOut is:\n")
            discount = applyDiscount(totalAmount(buyOut))
            printBuyOut(buyOut)
            printTotalBuyOut(buyOut, discount)
            break


cashRegister()