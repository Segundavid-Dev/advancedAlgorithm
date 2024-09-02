#A set is a collection data type that is mutable and dosen't allow duplicates elements
# Created using curly brackets but dosen't use the key value pairs like the dictionary does, instead just single elements seprated by a comma

myset = {1,2,3,4,5,6}
print(type(myset))

#create an empty set using the set method
myset1 = set()
print(myset1)

#Removes an element from a set
myset.remove(1)
print(myset)

# Iterate over a set and print each elements
for i in myset:
    print(i)

# List comprehension for set
square = {i*i for i in myset}
print(square)

#Operations on set --union & intersection
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

#union opeartion
u = odds.union(evens) #combines elements from both set without duplication
print(u)

#intersection operation
x = odds.intersection(primes) #Returns the intersection of two sets as set
print(x)

#difference operation
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,13,16,17}

diff = setA.difference(setB) #Return the elements that are in A but not in B as a new set
print(diff)

#symmetric difference
symmetric_diff = setA.symmetric_difference(setB)
print(symmetric_diff)


#!Important :: we also have the difference_update, symmetric_difference_update, intersection_update method

print(setA.issubset(setB)) #subset operation (returns boolean values)
print(setA.issubset(setB)) #superset operation (returns boolean values)
print(setA.isdisjoint(setB)) #disjoint operation (returns boolean values)

