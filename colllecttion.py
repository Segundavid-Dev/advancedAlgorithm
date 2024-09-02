# Collection modules in python implements special container data type and provides alterantives with some additional functionality instead of the general data type like dictionaries, list, sets, tuples
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

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

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

#Defaultdict -- Returns the default value of the specified data type
d = defaultdict(float)
d['a'] = 1
d['b'] = 2
d['c'] = 3

print(d['']) #Returns float default value


#deque -- open ended queue data type, elememnts can be accessed from the head and tail
dequeue = deque()
dequeue.append('a')
dequeue.append('b')
dequeue.append('c')
dequeue.appendleft('3') #append element from the left postion
print(dequeue)

dequeue.popleft() #remove elements from the left position
print(dequeue)

dequeue.extendleft([3,4,5])
print(dequeue)

dequeue.rotate(2)
print(dequeue)