# Collection modules in python implements special container data type and provides alterantives with some additional functionality instead of the general data type like dictionaries, list, sets, tuples
from collections import Counter
from collections import namedtuple

strings = 'aaaaabbbbccc'

my_counter = Counter(strings)
print(my_counter)
print(type(my_counter))
print(my_counter.most_common(1)) #Returns the most common elements in the counter object
print(list(my_counter.elements())) #Returns elements a a list


#namedtuples
points = namedtuple('points', 'x,y')
pt = points(x=2, y=10)
print(pt)

#orderdDictionaries
#Same as the dictionary data type only that they remember the order in which items were inserted


