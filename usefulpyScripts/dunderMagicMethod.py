#Declare your own string class 
class String:
    #Magic Method to initiate object
    def __init__(self, string):
        self.string = string 

    #Print our string object 
    def __repr__(self):
        return 'Object: {}'.format(self.string)
#Driver Code 
if __name__ == '__main__':
    #Object Creation
    string1 = String("Hello")
    #Print object location
    print(string1)