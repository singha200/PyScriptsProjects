
"""
Take input from user as n 
Take input from user as typeofpattern as str

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
typeofpattern = str(input("Enter True for increamental or False for Decremental pattern "))
#Print the half pyramid in incremental form
if typeofpattern == "True":
    for i in range(0, n+1):
        for j in range(1, i+1):
            print("*",end=" ")
        print("\r")    
#Print the pyramid in decremental form 
elif typeofpattern == "False":
    for i in range(n-1,0,-1):
        for j in range(0 ,i+1):
            print("*",end=" ")
        print("\r")
