# 1 Write a program that will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

import zlib
import random
import re
from pprint import pprint
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


# 11 Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example: 0100,0011,1010,1001
# Then the output should be: 1010

data = input().split(',')
data = [num for num in data if int(num, 2) % 5 == 0]
print(','.join(data))
#  or
data = input().split(',')
lst = []
for num in data:
    if int(num, base=2) % 5 == 0:
        lst.append(num)
print(','.join(lst))

# 12 Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

even_nums = []
for i in range(1000, 3001):  # i = 1000
    s = str(i)  # s = '1000'
    # s[0] = '1' -> int('1') -> 1 % 2, s[1] = '0' -> int('0') -> 0 % 2
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
        even_nums.append(s)
print(",".join(even_nums))

# 13 Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program: hello world! 123
# Then, the output should be: LETTERS 10 DIGITS 3

sentence = input("Enter sentence: ")
letters, digits = 0, 0
for l in sentence:
    if l.isalpha:
        letters = letters + 1
    elif l.isdigit:
        digits = digits + 1
    else:
        pass
print(f'LETTERS {letters}')
print(f'DIGITS {digits}')
# or
s = input()
d = {"DIGITS": 0, "LETTERS": 0}
for c in s:
    if c.isdigit():
        d["DIGITS"] += 1
    elif c.isalpha():
        d["LETTERS"] += 1
    else:
        pass
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])

# 14 Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program: Hello world!
# Then, the output should be: UPPER CASE 1 LOWER CASE 9

sentence = input("Enter the sentence: ")
upper, lower = 0, 0

for l in sentence:
    if l.isupper():
        upper += 1
    elif l.islower():
        lower += 1
    else:
        pass
print("UPPER: ", upper)
print("LOWER: ", lower)

# 15 Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program: 9
# Then, the output should be: 11106

a = input()  # a = '4'
# (int(2*'4')) -> int('44') -> 44
total = int(a) + int(2*a) + int(3*a) + int(4*a)
print(total)

# 16 Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9
# Then, the output should be: 1,9,25,49,81

lst = input().split(',')
my_lst = []
for num in lst:
    if int(num) % 2 != 0:
        square_each = str(int(num)**2)
        my_lst.append(square_each)
print(','.join(my_lst))

# 17 Write a program that computes the net amount of a bank account based a transaction log from console input.
# Suppose the following input is supplied to the program: D 300, D 300, W 200, D 100
# Then, the output should be: 500

amount = 0
while True:
    transaction = input().split(' ')
    if transaction[0] == 'D':
        amount = amount + int(transaction[1])
    elif transaction[0] == 'W':
        amount = amount - int(transaction[1])
    elif input() == '':
        break
    print(f'Your current balance is: {amount}')

# 18 A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be: ABd1234@1


def is_low(x):                  # Returns True  if the string has a lowercase

    for char in x:
        if 'a' <= char and char <= 'z':
            return True
    return False


def is_up(x):                   # Returns True  if the string has a uppercase
    for char in x:
        if 'A' <= char and char <= 'Z':
            return True
    return False


def is_num(x):                  # Returns True  if the string has a numeric digit
    for char in x:
        if '0' <= char and char <= '9':
            return True
    return False


def is_other(x):                # Returns True if the string has any "$#@"
    for char in x:
        if char == '$' or char == '#' or char == '@':
            return True
    return False


passwords = input().split(',')
lst = []

for word in passwords:
    length = len(word)
    # Checks if all the requirments are fulfilled
    if 6 <= length and length <= 12 and is_low(word) and is_up(word) and is_num(word) and is_other(word):
        lst.append(word)

print(",".join(lst))

# 19 You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name
# 2: Then sort based on age
# 3: Then sort by score
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be: [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

lst = []
while True:
    s = input().split(',')
    if not s[0]:                          # breaks for blank input
        break
    lst.append(tuple(s))

# here key is defined by lambda and the data is sorted by element priority 0>1>2 in accending order
lst.sort(key=lambda x: (x[0], int(x[1]), int(x[2])))
print(lst)

# 20 Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
# Suppose the following input is supplied to the program:7
# Then, the output should be:0 7


class MyGen():
    def div_by_seven(self, num):
        for number in range(0, num + 1):
            if number % 7 == 0:
                yield number


for i in MyGen().div_by_seven(int(input("Enter a number... "))):
    print(i)

# 21 A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# Please write a program to compute the euclidean distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example: If the following tuples are given as input to the program: UP 5 DOWN 3 LEFT 3 RIGHT 2
# Then, the output of the program should be: 2
# Here distance indicates to euclidean distance.Import math module to use sqrt function.

x, y = 0, 0  # cartesian plane
while True:
    movement = input().split()
    if not movement:
        break
    if movement[0] == 'UP':
        y = y + int(movement[1])
    elif movement[0] == 'DOWN':
        y = y - int(movement[1])
    elif movement[0] == 'LEFT':
        x = x - int(movement[1])
    elif movement[0] == 'RIGHT':
        x = x + int(movement[1])
    else:
        pass

# euclidean distance = square root of (x^2+y^2) and rounding it to nearest integer
distance = round(math.sqrt(x**2 + y**2))
print(distance)

# 22 Write a program to compute the frequency of the words from the input. The output should outlet after sorting the key alphanumerically.
# Suppose the following input is supplied to the program: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be: 2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1

words = input().split()
words.sort()
dictionary = {}

for char in words:
    dictionary[char] = words.count(char)
print(dictionary)
# or
p = input().split()
pprint({i: p.count(i) for i in p})

# 23 Write a method which can calculate square value of number
# Using the ** operator which can be written as n**p where means n^p


def cal_square_val(number):
    square = number**2
    return square


print(cal_square_val(2))
print(cal_square_val(7))

# 24 Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
# Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
# And add document for your own function, The built-in document method is __doc__

print(abs.__doc__)
print(int.__doc__)
print(str.__doc__)
print(sorted.__doc__)


def power(num, pow):
    return num**pow


print(power(3, 4))
print(pow.__doc__)

# 25 Define a class, which have a class parameter and have a same instance parameter.


class Animal():
    name = 'Animal'

    def __init__(self, name=None):
        self.name = name


cat = Animal('Cat')
print(Animal.name, cat.name)

goat = Animal('Goat')
print(Animal.name, goat.name)
# or
cow = Animal()
cow.name = 'Cow'
print(Animal.name, cow.name)

# 26 Define a function which can compute the sum of two numbers.
# Define a function with two numbers as arguments. You can compute the sum in the function and return the value.


def sum_of_two_num():
    number1 = int(input("Enter first numbers: "))
    number2 = int(input("Enter second numbers: "))
    return number1 + number2


print(sum_of_two_num())

# or


def sum_of_two_num(num1, num2):
    return num1 + num2


print(sum_of_two_num(7, 3))

# 27 Define a function that can convert an integer into a string and print it in console.


def convert_int_to_str(number):
    int_to_str = str(number)
    return (int_to_str)


print(convert_int_to_str(3))

# 28 Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.


def str_to_int_and_its_sum(str1, str2):
    sum = int(str1) + int(str2)
    return sum


print(str_to_int_and_its_sum('10', '7'))

# 29 Define a function that can accept two strings as input and concatenate them and then print it in console.


def concatenate_strings(str1, str2):
    concatenate = str1 + str2
    return concatenate


print(concatenate_strings('Love ', 'Yourself'))  # Love Yourself
print(concatenate_strings('12', '3'))  # 123

# 30 Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.


def maximum_len(str1, str2):
    if len(str1) == len(str2):
        return str1, str2
    elif len(str1) > len(str2):
        return str1
    else:
        return str2


print(maximum_len('Hello', 'There'))
print(maximum_len('Take', 'it'))
print(maximum_len('We', 'Win'))

# 31 Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys.


def print_dict():
    dictionary = {}

    for i in range(1, 21):
        dictionary[i] = i**2
    return dictionary


print(print_dict())

# 32 Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys. The function should just print the keys only.


def print_keys():
    dictionary = {}

    for i in range(1, 21):
        dictionary[i] = i**2
    return dictionary.keys()


print(print_keys())

# 33 Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).


def print_list():
    values = []
    for i in range(1, 21):
        square_of_numbers = i**2
        values.append(square_of_numbers)
    return values


print(print_list())

# 34 Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the first 5 elements in the list.


def first_5_elements():
    values = []
    for i in range(1, 21):
        square_of_num = i**2
        values.append(square_of_num)
    return values[:5]


print(first_5_elements())

# 35 Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the last 5 elements in the list.


def first_5_elements():
    values = []
    for i in range(1, 21):
        square_of_num = i**2
        values.append(square_of_num)
    return values[-5:]


print(first_5_elements())

# 36 Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print all values except the first 5 elements in the list.


def first_5_elements():
    values = []
    for i in range(1, 21):
        square_of_num = i**2
        values.append(square_of_num)
    return values[5:]


print(first_5_elements())

# 37 Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).


def print_tuple():
    values = []
    for i in range(1, 21):
        square_of_nums = i**2
        values.append(square_of_nums)
    return tuple(values)


print(print_tuple())

# 38 With a given tuple (1,2,3,4,5,6,7,8,9,10),
# write a program to print the first half values in one line and the last half values in one line.


def first_half_last_half():
    tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    first_half = tup[:5]
    last_half = tup[5:]
    return first_half, last_half


print(first_half_last_half())

# 39 Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).


def even_val_tuple():
    values = []
    tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    for i in tup:
        if i % 2 == 0:
            values.append(i)
    return tuple(values)


print(even_val_tuple())

# 40 Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".


def print_Yes():
    str = input("Enter string: ")  # string as input
    if str == 'Yes' or str == 'yes' or str == 'YES':
        return 'Yes'
    else:
        return 'No'


print(print_Yes())

# 41 Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squaredNumbers = map(lambda x: x**2, li)  # returns map type object data
print(list(squaredNumbers))           # converting the object into list

# 42 Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].


def sq_of_evenNum():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evenNumbers = map(lambda x: x**2, filter(lambda x: x % 2 == 0, lst))
    return list(evenNumbers)


print(sq_of_evenNum())
# or


def even(x):
    return x % 2 == 0


def squer(x):
    return x**2


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# first filters number by even number and the apply map() on the resultant elements
li = map(squer, filter(even, li))
print(list(li))

# 43 Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).


def evenNum(i):
    return i % 2 == 0


print(list(filter(evenNum, range(1, 21))))

# 44 Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).


def sq_num(i):
    return i**2


print(list(map(sq_num, range(1, 21))))

# 45 Define a class named American which has a static method called printNationality.


class American():
    @staticmethod
    def printNationality():
        print('I am American')


anAmerican = American()
# this will not run if @staticmethod does not decorates the function.
anAmerican.printNationality()
# Because the class has no instance.

American.printNationality()    # this will run even though the @staticmethod
# does not decorate printNationality()

# 46 Define a class named American and its subclass NewYorker.


class American():
    pass


class NewYorker(American):
    pass


american = American()
newYorker = NewYorker()

print(american)
print(newYorker)

# 47 Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.


class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area_of_cir(self):
        return ((self.radius**2) * (3.14))  # r^2(pi)


circle = Circle(3)
print(circle.area_of_cir())

# 48 Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.


class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area_of_rec(self):
        return self.length * self.width


rectangle = Rectangle(4, 2)
print(rectangle.area_of_rec())

# 49 Define a class named Shape and its subclass Square.
# The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.


class Shape():
    def __init__(self):
        pass

    def area(self, length=0):
        return length


class Square(Shape):
    def __init__(self, length=0):
        Shape.__init__(self)
        self.length = length

    def area(self, length=0):
        return self.length * self.length


square = Square(5)
print(square.area())
print(Square().area())

# 50 Please raise a RuntimeError exception.

'''raise RuntimeError('Something went wrong.')'''

# 51 Write a function to compute 5/0 and use try/except to catch the exceptions.


def division():
    return 5/0


try:
    division()
except ZeroDivisionError:
    print("Why on earth you are dividing a number by ZEROOO!")

# 52 Define a custom exception class which takes a string message as attribute.


class CustomException(Exception):
    def __init__(self, message):
        self.message = message


customException = CustomException('Something went wrong')
print(customException)

# 53 Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
# Example: If the following email address is given as input to the program:john@google.com
# Then, the output of the program should be: john

email = input("Enter your email: ")
username_of_email = email.split('@')
print(username_of_email[0])

# 54 Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.
# Example: john@google.com
# Then, the output of the program should be: google

email = "john@google.com elise@python.com"
pattern = "\w+@(\w+).com"
ans = re.findall(pattern, email)
print(ans)

# 55 Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
# Example: 2 cats and 3 dogs.
# Then, the output of the program should be:['2', '3']


def find_digits():
    words = input("Enter string").split()
    digits = []

    for char in words:
        if char.isdigit():
            digits.append(char)
    return digits


print(find_digits())

# 56 Print a unicode string "hello world".

unicodeString = u"hello world"
print(unicodeString)

# 57 Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

string_ASCII = input("enter string")
encoded = string_ASCII.encode('utf-8')
print(encoded)

# 58 Write a special comment to indicate a Python source code file is in unicode.

# -*- coding: 'utf-8' -*-

# 59 Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
# Example: 5
# Then, the output of the program should be: 3.55

n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i/(i+1)
print(round(sum, 2))  # rounded to 2 decimal point

# 60 Write a program to compute: f(n)=f(n-1)+100 when n>0 and f(0)=0 with a given n input by console (n>0).
# Example: 5
# Then, the output of the program should be:500
# Hint: We can define recursive function in Python.


def f(n):
    if n == 0:
        return 0
    else:
        return f(n-1) + 100


num = int(input("Enter a number: "))
print(f(num))

# 61 The Fibonacci Sequence is computed based on the following formula:f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n input by console.
# Example: 7
# Then, the output of the program should be: 13


def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)


num = int(input("Enter a num: "))
print(f(num))

# 62 The Fibonacci Sequence is computed based on the following formula: f(n)=0 if n=0, f(n)=1 if n=1, f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n input by console.
# Example: 7
# Then, the output of the program should be: 0,1,1,2,3,5,8,13


def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)


num = int(input("Enter a num: "))
values = (str(f(i)) for i in range(0, num + 1))
print(','.join(values))

# 63 Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
# Example: 10
# Then, the output of the program should be: 0,2,4,6,8,10


def even_value(n):
    for number in range(0, n + 1):
        if number % 2 == 0:
            yield number


num = int(input("Enter num: "))
values = []
for i in even_value(num):
    values.append(str(i))
print(','.join(values))

# 64 Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
# Example: 100
# Then, the output of the program should be: 0,35,70


def div_by_5_7(n):
    for number in range(0, n + 1):
        if number % 5 == 0 and number % 7 == 0:
            yield number


num = int(input("Enter num: "))
values = []
for i in div_by_5_7(num):
    values.append(str(i))
print(','.join(values))

# 65 Please write assert statements to verify that every number in the list [2,4,6,8] is even.
# Hints Use "assert expression" to make assertion.

li = [2, 4, 5, 6, 8]
for i in li:
    assert i % 2 == 0

# 66 Please write a program which accepts basic mathematic expression from console and print the evaluation result.
# Example: 35 + 3
# Then, the output of the program should be: 38
# Hint: Use eval() to evaluate an expression.


def mathematic_expression():
    expression = (input("Enter an expression: "))
    result = eval(expression)
    return result


print(mathematic_expression())

# 67 Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
# Hint: Use if/elif to deal with conditions.


def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = round((low + high) / 2)

        if lst[mid] == item:
            return mid
        elif lst[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


lst = [1, 3, 5, 7, 9, 13]
print(binary_search(lst, 9))

# 68 Please generate a random float where the value is between 10 and 100 using Python module.
# Hint: Use random.random() to generate a random float in [0,1].

random_num = random.uniform(10, 100)
print(random_num)

# 69 Please generate a random float where the value is between 5 and 95 using Python module.
# Hint: Use random.random() to generate a random float in [0,1]

random_num = random.uniform(5, 95)
print(random_num)

# 70 Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
# Hint : Use random.choice() to a random element from a list.


def random_even_val():
    random_val = [i for i in range(0, 11, 2)]
    return(random.choice(random_val))


print(random_even_val())

# 71 Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension.


def div_by_5_7():
    random_val = [i for i in range(10, 151) if i % 35 == 0]
    return random.choice(random_val)


print(div_by_5_7())

# 72 Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
# Hint: Use random.sample() to generate a list of random values.


def random_5_val():
    random_val = random.sample(range(100, 201), 5)
    return random_val


print(random_5_val())

# 73 Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.


def even_5_num():
    random_val = random.sample([i for i in range(100, 201) if i % 2 == 0], 5)
    return random_val


print(even_5_num())

# 74 Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.


def div_by_5_7():
    random_val = random.sample([i for i in range(1, 1001) if i % 35 == 0], 5)
    return random_val


print(div_by_5_7())

# 75 Please write a program to randomly print a integer number between 7 and 15 inclusive.
# Hint: Use random.randrange() to a random integer in a given range.


def randomly_print_integer():
    random_int = random.randrange(7, 16)
    return random_int


print(randomly_print_integer())

# 76 Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
# Hint: Use zlib.compress() and zlib.decompress() to compress and decompress a string.

# In Python 3 zlib.compress() accepts only DataType <bytes>
s = bytes('hello world!hello world!hello world!hello world!', 'utf-8')
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))
