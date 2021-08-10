# Declaring Sets
this_set ={"apple","mango","orange"}
print(this_set)
print(type(this_set))
print(len(this_set))

#Acessing and modifying sets
this_set.add("watermelon")
print(this_set)
my_set ={"banana","melon"}
this_set.update(my_set)
print(this_set)
this_set.pop()
print(this_set)
this_set.remove("banana")
print(this_set)

# Joining the sets
set4={"apple","mango","cucumber","lemon"}
set1= this_set.union(set4)
print(set1)
this_set.intersection_update(set4)
print(this_set)
set2 =this_set.intersection(set4)
print(set2)
this_set.symmetric_difference_update(set4)
print(this_set)
set5 =this_set.difference(set4)
print(set5)


# Dictionary
this_dict= {"age": 40,"year":1995,"brand":"puma","type":"wood"}
print(this_dict)
print(type(this_dict))
print(len(this_dict))

# Acessing and modifying the Dictionary
print(this_dict["age"])
print(this_dict.values())
print(this_dict.keys())
this_dict["age"] = 90
print(this_dict)
print(this_dict.items())
this_dict.update({"age":100})
print(this_dict)
this_dict["color"]="blue"
print(this_dict)
this_dict.pop("age")
print(this_dict)
this_dict.popitem()
print(this_dict)

#Dictionary unpacking

for x in this_dict.keys():
    print(x)

for y in this_dict.values():
    print(y)

for x,y in this_dict.items():
    print(x)
    print(y)







