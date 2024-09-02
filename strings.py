# A string is ordered and immutable collection data types, used for text representation
# A string is created with wither single quotes or double quotes

my_string = 'hello world'
print(type(my_string))

# Triples quotes, this is mostly used for documentation inside our code, used to print multi-line strings

#Substring values
char = my_string[0:5]
print(char)

#concatenation of strings
f_name = "david"
l_name = "segun"

full_name = f_name +" "+ l_name
print(full_name)


my_string ='      Hello world    '
my_string = my_string.strip() #strip() method removes white space
print(my_string)

print(f_name.upper()) #Returns uppercase value
print(f_name.lower()) #Return lowercase value
print(full_name.capitalize()) #Capitalize the first word

#Replace strings
print(my_string.replace("world", "universe"))

sentence = 'how are you doing'
my_list = sentence.split()
print(my_list)

#Formatting strings 
# --using the f string method 
name = "David"
print(f"my name is {name}")

# --using the .format() method
age = 12
print("Wale is {} years old".format(age))

# --using the placeholder % method
var = 3.1234567
print("The var is %.2f" %var)