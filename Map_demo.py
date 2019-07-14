"""
Demo of Map function and Lambda (one liner function )
"""
numbers = ["3", "34", "64"]
print(type(numbers))
numbers = list(map(int,numbers))
print(type(numbers))

def square(a):
    return a*a
def cube(a):
    return a*a*a
func = [square, cube]
num = [2, 3, 5, 6, 7, 8, 9]
for i in range(5):
    val = list(map(lambda x: x(i), func))
    print(val)


if __name__ == "__main__":
    pass