# A list is a collection data type that is : ordered, muatable, allow duplicate elements
# A list allows for different data types
mylist = ['banana', 'cherry', 'apple']
print(mylist)

# A list can also created by an list function available in python
mylist2 = list()
print(mylist2)   #Then append valued to the end of the list

#Different methods in lists
print(len(mylist)) #Check the no of elements available

mylist.append("lemon") #Append element to the end of the list
print(mylist)

mylist.insert(2, 'coconut')  #insert element in a specific index location
print(mylist)

mylist.remove("banana")  #Remove first occurence of the value
print(mylist)

mylist.pop()  #Remove the last element of the list
print(mylist)

mylist.clear() #Remove all the values in the list and return an empty list
print(mylist)

mylist3 = ['pizza', 'burger', 'ketchup', 'chips']
mylist3.reverse() #Reverse the index position of the list from last to first
print(mylist3)

mylist3.sort() #Sort the list alphabetically (This method affects the originality of the list)
print(mylist3)

new_list = sorted(mylist3) #same functionality as the sort() method but stores values in a seprate list
print(new_list)

multiple_value_list = ['Fruits'] * 3
print(multiple_value_list)

#Concatenate two string with the + operator
all_list = new_list + multiple_value_list
print(all_list)

number_list = [1,2,3,4,5,6,7,8,9] #accessing list values with start and stop indexes
print(number_list[0:4])

list_orginal = ['Football', 'Tennis', 'Ballet', 'Skating']
list_copy = list_orginal.copy() #AMke a copy of the original list without affecting the real list
list_copy.append('swimming')
print(list_copy)
print(list_orginal)

#List Comprehension :: An elegant and a fast method to create a new list from an exisiting list

a =  [1,2,3,4,5,6]
b = [i*i for i in a] #Print the squared of each elements
print(b)