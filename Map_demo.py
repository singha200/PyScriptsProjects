"""
Demo of Map function and Lambda (one liner function )
"""
numbers = ["3", "34", "64"]
print(type(numbers))
numbers = list(map(int,numbers))
print(type(numbers))


square = list(map(lambda x: x*x,numbers))
print(square)
if __name__ == "__main__":
    pass