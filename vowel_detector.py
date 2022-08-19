
def printHyphen():
    print("-------------------------------------------------------")


def enterVowel():

    vowels = ['a', 'e', 'i', 'o', 'u']

    while(True):
        vowel = input("Enter a vowel: ")
        if vowel.isdigit():
            printHyphen()
            print("Wrong data type, enter only a letter, please try again.")
            printHyphen()
        elif len(vowel) > 1:
            printHyphen()
            print("The data cannot be processed, please try again.")
            printHyphen()
        elif vowel.lower() not in vowels:
            printHyphen()
            print(f"Is a consonant: {vowel}")
            printHyphen()
            break
        elif vowel.lower() in vowels:
            printHyphen()
            print(f"Is a vowel: {vowel}")
            printHyphen()
            break


enterVowel()