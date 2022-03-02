# 1 Write a program that will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def div_by_7_not_5():
    li = []
    for i in range(2000, 3200 + 1):
        if i % 7 == 0 and i % 5 != 0:
            li.append(i)
    return li


print(div_by_7_not_5())

# 2 Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320


def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)


print(factorial(5))

# 3 With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included).
# then the program should print the dictionary. Suppose the following input is supplied to the program: 8
# Then, the output should be:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


def dictionary(number):
    dictionary = {}
    for i in range(1, number + 1):
        dictionary[i] = i * i
    return dictionary


print(dictionary(10))

# 4 Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98
# Then, the output should be: ['34', '67', '55', '33', '12', '98'], ('34', '67', '55', '33', '12', '98')


def every_number():
    # split - takes input as string and output as list.
    li = input("Enter series of number separated by comma: ").split(',')
    tup = tuple(li)
    return li, tup


print(every_number())

# 5 Define a class which has at least two methods:
# getString: to get a string from console input, printString: to print the string in upper case.
# Also please include simple test function to test the class methods.


class InputOutString():
    def getString(self):
        self.string = input("Enter the string: ")

    def printString(self):
        print(self.string.upper())


self_obj = InputOutString()
self_obj.getString()
self_obj.printString()
