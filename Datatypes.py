
# Declaring Variables and Datatypes and printing
import time

x = 544
y = 55555.898989889
z = "Welcome To Python"
a = -78.8j
my_list =["My","name","is","ram"]
my_tuple =("i","am ",30,"year","old")
my_set ={"i","like","playing","basketball"}
my_dic ={"score" : 70,"time":100}
print("integer value of x is :",x)
print("float value of y is :",y)
print("string value of z is :",z)
print("complex value of a is :",a)
print("print the list value :",my_list)
print("print the tuple values :",my_tuple)
print("print the set values :",my_set)
print("print the dictionary values :",my_dic)

# printing the Data type of the Variables

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(my_list))
print(type(my_tuple))
print(type(my_set))
print(type(my_dic))


# Type cast the datatype
print(int(y))
print(float(x))
print(str(a))
print(complex(x))
print(complex(y))
print(list(my_tuple))
print(list(my_dic))


# Finding the length of the string and checking if words are present in the string

note ="To impact on something means to have a strong influence"
print(len(note))
print("impact" in note)
print("the" in note)
if "something" in note:
    print("yes,'something' is present")

if "the" not in note:
    print("true")

# Slicing and Indexing the strings
text ="i am very happy"
print(text[3])  #to print 3rd char
print(text[0:6]) #to print char from 0 to 5
print(text[0::2]) # to print char from 0 with step 2
print(text[-7:-2]) #to print char from 7th char to 2nd char from last

# Modifying the strings
print(text.replace("h","j"))
print(text.split("a"))
print((text.upper()))
print(text.lower())
print(text.endswith("y"))
print(text.capitalize())
print(text.count("a"))
print(text.index("a"))
texter ="to be on the moon"
print(text + texter)
print( f'Hello {text} {texter}')
texting =" Hello {0} {1} "
print(texting.format(text,texter))


#Operators
a=100
b=200
print(a+b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

if 5!=10:
    print("false")
if a>b:
    print("false")

if a==30 or b==200:
    print("true")

if a==40 and b==200:
    print("false")


# Input from the user
Name = input("enter the name: ")
print("your name is : " + Name)

Age = input("enter your age: ")
int(Age)
print(f' your name is {Name} and  {Age}')

#To print the time

Time=time.localtime()
current_time=time.strftime("%H:%M:%S",Time)
print(current_time)

# To print year,month and date
from datetime import datetime
now= datetime.now()
print (now.year)
print (now.month)
print (now.day)
