
def enterNumbers():
    numbers = []
    while True:
        number = int(input("Enter a number: "))
        if(number == 0):
            break
        else:
            numbers.append(number)
    totalAmount = sum(numbers)
    print("The total amount is: ", totalAmount)

enterNumbers()