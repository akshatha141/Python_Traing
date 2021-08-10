# Functions
from random import shuffle


def my_fuction():
    print("hello")
my_fuction()

#Check if num is even or odd using function
def check_no(num):
    if num%2==0:
        print(f'{num} is a even number')
    else:
        print(f'{num} is odd number')

check_no(5)

#Check if num is even or odd using Input function
def check_no(num):
    if num%2==0:
        print(f'{num} is a even number')
    else:
        print(f'{num} is odd number')

number=input("enter the number: ")
check_no(int(number))

#To find min of two numbers

def minimum(a, b):
    if a <= b:
        return a
    else:
        return b

print(minimum(7, 15))


# * args [used to pass n number of arguments
def my_marks(*score):
    print("marks of john is" + f'{score[2]}')

my_marks(10,20,30,40)


# **keyword [will receive dictionary of arguments]
def my_scores(**scores):
    print("marks  is" + f'{scores["raj"]}')

my_scores(john="50",raj="80",riya="70")

#default parameter
def brand_name(brand="puma"):
    print("My brand name is:  " + brand)

brand_name()

#Map
my_list=[2,3,4,5,6,7,8]

def square(num):
    return num**2

for item in map(square,my_list):
    print(item)

# Filter
my_page=[2,3,4,5,6,7,8,9]

def even_odd(num):
    return num%2==0

print(list(filter(even_odd,my_page)))

#Lambda function
square=lambda num:num**2

print(square(5))

# to remove words using lambda
def remove_words(list1, remove_words):
    result = list(filter(lambda word: word not in remove_words, list1))
    return result


colors = ['orange', 'red', 'green', 'black']
remove_colors = ['orange', 'black']
print("Original list:", colors)
print("\nAfter removing the words from the said list:")
print(remove_words(colors, remove_colors))

# To remove all occurance of 30

list1 = [5, 30, 15, 30, 25, 50, 30]

def removeValue(sampleList, val):
    for value in sampleList:
        if value!=val:
            print(value)


removeValue(list1, 30)

# Tuple unpacking

name_price=[("rice",400),("wheat",300),("flour",100)]
for price_name, price in name_price:
    print(price)

working_hours =[('sam',300),('tom',200),('pam',600)]

def employee_max(working_hours):
    current_max_hours=0
    employee_name=" "

    for employee, hours in working_hours:
        if hours > current_max_hours:
            current_max_hours = hours
            employee_name = employee

    return employee_name, current_max_hours

print(employee_max(working_hours))


#To find sum of dictionary values

my_dict={"raj":50,"max":80,"sita":90,"tom":40}

def sum_dict(num):
    sum=0
    for i in my_dict:
        sum=sum + my_dict[i]
    return sum

print("sum of all values is : ",sum_dict(my_dict))

#to count number of chars,digits and symbols in string

inputString = "P@#yn26at^&i5ve"
print("total counts of chars, digits,and symbols \n")

def findDigitsCharsSymbols(inputString):
    charCount = 0
    digitCount = 0
    symbolCount = 0
    for char in inputString:
        if char.islower() or char.isupper():
            charCount += 1
        elif char.isnumeric():
            digitCount += 1
        else:
            symbolCount += 1

    print("Chars = ", charCount, "Digits = ", digitCount, "Symbol = ", symbolCount)

findDigitsCharsSymbols(inputString)

# to count how many times "sun" is used

def sun_count(x):
    count = 0
    for item in x:
        if item == "sun":
            count = count + 1

    print(count)

next_list=["earth", "buzz","moon","sun","mars","sun","sun","water"]
sun_count(next_list)

#function to print area of a circle
def area_circle(radius):
    pi = 3.14
    area = pi * radius**2
    return area
area_circle(4)


