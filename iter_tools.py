# itertools product, permutations, combinations, accumulate, groupby and infinite iteratos

from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import accumulate
from itertools import count, cycle, repeat
import operator

a = [1,2,3,4]
b = [3,4]

#calculate the cartesian product
prod = product(a, b)
print("\n",list(prod))  #convert to a list to see the product

#Returns all the possible combination of the items
perm = permutations(a)
print("\n",list(perm))


comb = combinations(a,2)
print("\n",list(comb))


acc = accumulate(a, func=operator.mul)
print(list(acc))

acc = accumulate(a, func=max)
print(list(acc))

#count function 
for i in count(1):
    print(i)
    if i == 15:
        break

#cycle function infinitely
for i in cycle(a):
    print(i)

#repeat function
for i in repeat(1,4):
    print(i)