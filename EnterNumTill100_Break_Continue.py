def number1():
    """Loop will continue till the number greater than 100 is entered"""  #Docstring Gives summary of the function
    while(True):
        a = int(input("Enter a number"))
        if a < 100:
            print("Try again")
            continue #Loop will continue till the if statement is true
        else:
            print("Congratulation you enter number greater than 100")
            break #Loop will break

number1()
print(number1.__doc__) #Printing whatever written in the DocString for the function