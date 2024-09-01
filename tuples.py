# A tuples is an ordeered data type that is similar to the list data type but cannot be changed or modified after been created

mytuple = ('Max', 28, 'boston')
print(mytuple)

mylist = ['apple', 'banana','cherry']
mytuple2 = tuple(mylist) #Using the built in tuple function to create a tuple from a list
print(mytuple2)

#Iterating over each elemets in a tuple
for i in mytuple2:
    print(i)

#Check if elements are in a tuple
if "apple" in mytuple2:
    print("yes")
else:
    print("no")


letters = ('a','a','b','c','d','e','f')
print(len(letters))  #Get no of elements in a tuple

print(letters.count('a')) #Count the occurence of elements in a tuple
print(letters.index('b')) #Print index postion of letters

#Slicing in tuples
letters_substrings = letters[1:4]
print(letters_substrings)

#Unpacking values in tuples
my_info = "David", '19', 'Lagos'
name, age, city = my_info
print(name)
print(age)
print(city)

#when working with tuples and list, it is worth to remember that working with tuples  might be better than list as python can making some internal optimization when dealing with the memory of tuples

import sys

my_list = [0,1,2, "hello", True]
my_tuple = (0,1,2, "hello", True)
#Get the size of the tuple and byte in memory
print(sys.getsizeof(my_tuple), bytes)
print(sys.getsizeof(my_list), bytes)


import timeit #To calculate the amount of time in seconds to print the same values 1million times, The amount of time for the tuple is considerably less than list
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))