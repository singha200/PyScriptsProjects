#Loop will continue till the number greater than 100 is entered

while(True):
    a = int(input("Enter a number"))
    if a < 100:
        continue #Loop will continue till the if statement is true
    else:
        print("Congratulation you enter number greater than 100")
        break #Loop will break