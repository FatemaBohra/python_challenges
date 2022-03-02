# 1 Write a program that will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

import math


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

# 6 Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to program in a comma-separated.
# For example the following comma separated input is given: 100,150,180 The output: 18,22,24. If the output received is in decimal form, it should be rounded off.

C = 50
H = 30


def calculate():
    numbers = map(int, input().split(','))
    lst = []
    for e in numbers:
        Q = math.floor(math.sqrt((2*C*e)/H))
        int_to_str = str(Q)
        lst.append(int_to_str)
    return (','.join(lst))  # 18, 22, 24


print(calculate())

# 7 Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i * j.
# Note: i=0,1.., X-1; j=0,1..,­Y-1. Suppose the following inputs are given to the program: 3,5
# Then, the output should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]


def two_dimensional_array():
    x, y = map(int, input().split(','))
    lst = []

    for i in range(x):
        tmp = []
        for j in range(y):
            tmp.append(i * j)
        lst.append(tmp)
    return lst


print(two_dimensional_array())

# 8 Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world

words = input().split(',')
words.sort()
print(', '.join(words))  # simple output
print(words)  # gives list as output

# 9 Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

lst = []

while True:
    x = input()
    if len(x) == 0:
        break
    lst.append(x.upper())

for line in lst:
    print(line)

# 10 Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again
# Then, the output should be: again and hello makes perfect practice world


def rm_duplicates_sorting():
    word = input().split()

    for e in word:
        if word.count(e) > 1:
            word.remove(e)

    word.sort()
    return(' '.join(word))


print(rm_duplicates_sorting())
# or
word = sorted(set(input().split()))
print(' '.join(word))
print(word)
