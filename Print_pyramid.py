
"""
Take input from user as n 
Take input from user as typeofpattern as boolean

If typeofpattern is True then print 
*
**
***
****
If typeofpattern is False print 
****
***
**
*
"""
n = int(input("Enter the rows to print the star pattern "))
typeofpattern = bool(int(input("Enter True for increamental or False for Decremental pattern ")))
if typeofpattern == True:
    for i in range(0, n+1):
        for j in range(1, i+1):
            print("*",end=" ")
        print("\r")    
elif typeofpattern == False:
    for i in range(n,0,-1):
        for j in range(0 ,i+1):
            print("*",end=" ")
        print("\r")
