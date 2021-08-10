# List for Loops
my_list =["welcome","to","india","from","japan","after",20,"years"]
for x in my_list:
    print(x)

for i in range(len(my_list)):
    print(my_list[i])

[print(y) for y in my_list]

# List while loop
i=0
while i<len(my_list):
     print(my_list[i])
     i += 1


# to reverse input word
word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char],end="")  # end="" suspends new line and prints space


# to print even and odd numbers
my_num=[5,6,7,8,9,10,11,12]
for num in my_num:
    if num%2 == 0:
        print(f'{num} is even ')
    else:
        print(f'{num} is odd')

#Display number from 10 to 1

for num in range(10, -1, -1):
    print(num)

#Reverse the list

num_1 = [10, 20, 30, 40, 50]
start = len(num_1) - 1
stop = -1
step = -1
for i in range(start, stop, step) :
    print(num_1[i])


#Nested for loop

for x in [2,4,5]:
    for y in [10,20,30]:
        print(x*y)

# looping with step
for item in my_list[0::2]:
    print(item)

# to append square of each number to new list

list1=[3, 7, 6, 8, 9, 11, 15, 20]
list2=[]
#Type your answer here.
for i in list1:
    list2.append(i**2)

print(list2)

# to append positive num to new list
list11=[111, 32, -9, -45, -17, 9, 85, -10]
list22=[]
#Type your answer here.
for i in list11:
    if i>0:
        list22.append(list11)


print(list22)

#Emumerate produces index and char values
text ="India tour"
for x,y in enumerate(text):
    print(x)
    print('\n')
    print(y)

#zip function
text = [1,2,3,4]
text_1 = ['a','b','c','d']
for item in zip(text,text_1):
    print(item)

# Concat two index
mylist=['m','list','include']
mylist1=['y','s','ed']

for x,y in zip(mylist,mylist1):
    print(x+y) # [ my,lists,included]


#Break statement
movies = [
	(
		"chak de india",
		"sharuk",
		2004
	),
	(
		"tashan",
		"akshay kumar",
		2000
	),
	(
		"talash",
		"rani",
		2000
	)
]
print(type(movies))
for movie in movies:
 if movie[0] == "chak de india":
     print("Got the movie chak de india")
     break

#to print student marks
student_name = 'Soraj'

marks = {"James": 95, 'Soraj': 55, 'raj': 77}

for student in marks:
    if student == student_name:
        print(f'soraj marks is {marks[student]}')
        break
else:
    print('No entry with that name found.')



#write a program to find numbers divisible by 7 and multiply of 5 between 1500 and 2700

nl=[]
for x in range(1500, 2000):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))

#write program to find number less than 150 and divisible by 5
list1 =[12,15,32,42,55,75,122,132,150,180,200]
for i in list1:
    if i>150:
        break
    elif i%5 ==0:
        print(i)



#Compare each pair of elements and print the larger of the two.

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for a, b in zip(list_a, list_b):

   if a>b:

       print(a)
   else:

     print(b)
















