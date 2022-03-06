# 1 Write a program that will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

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
