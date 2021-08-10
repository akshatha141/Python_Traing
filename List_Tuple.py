# Declaring a list and printing
this_list = ["water","land","air","fire",11,22,33]
print(this_list)
print(type(this_list)) #type of list
print(len(this_list)) #length of list

# Modifying the list
print(this_list[2]) # print 3rd element
print(this_list[-4]) # print 4th element from the last
print(this_list[2:5]) # print elements from 3 to 5
print(this_list[0::3]) # print element from start with step of 3
print(this_list[-6:-2]) # print element from 6th last to 2th last

if "land" in this_list:
    print("yes")

if "earth" not in this_list:
    print("not present")

# Changing the list items
this_list[1]="earth"
print(this_list)
this_list[2:4]=["moisture","humidity"]
print(this_list)
this_list.insert(0,"oil")
print(this_list)
this_list.pop(3)
print(this_list)
this_list.remove("oil")
print(this_list)
this_list.append("oil")

my_list =[67,"year","old"]
this_list.extend(my_list) # to include elements from my_list + this_list
print(this_list)
my_list.remove(67)  #to remove element 67
print(my_list)

# Sorting the list

my_list.sort()
print(my_list)  # to sort ascending order
my_list.sort(reverse=True)
print(my_list)  #to sort in desending order
print(my_list.count("old")) #to print no of old used in the list

# reversing the list items
first_list=[300,700,566,897,999]
first_list[::-1]
print(first_list)



# Tuples

this_tuple=("eyes","nose","ear","mouth")
my_tuple =("skin",)
print(this_tuple)
print(my_tuple)
print(type(this_tuple)) #to print type
print(type(my_tuple))
print(len(this_tuple)) #length of tuple
print(len(my_tuple))

# Acessing tuples
print(this_tuple[1]) # to print 1st element
print(this_tuple[2:4]) #to print elements from 3 to 5
print(this_tuple[-2])  # last 2nd element
print(this_tuple.count("ear"))

# Modifying tuples
y =list(this_tuple)
y.append("hair")
this_tuple=tuple(y)
print(this_tuple)
y =list(this_tuple)
y[1]="hands"
this_tuple=tuple(y)
print(this_tuple)

# tuple unpacking
list_tuple=[(2,4),(6,9),(7,0)]
print(list_tuple)
for x,y in list_tuple:
    print(x)
    print(y)





