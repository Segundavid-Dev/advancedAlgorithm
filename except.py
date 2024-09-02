#Exception in python

#There are different kinds of exception errors in python
# typeError, NameError, fileNotFoundError, valueError, indexError, keyError

#Raising an error
x = -5
if x < 0:
    raise Exception("number should be greater than 0")

#Assertion method
y = 2
assert(y < 0),"Number less than 0"

# Handling exception with try and catch statements
try:
    a = 5 / 0
except ZeroDivisionError:
    print('an error happened')
finally:
    print("cleaning up...")