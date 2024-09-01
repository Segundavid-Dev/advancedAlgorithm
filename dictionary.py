# Dictionary is a collection data type that is unordered and mutable, consists of a collection of  key value where each key maps the associated key it values

my_dict = {
    "name": "David",
    "age": 19,
    "city": "lagos"
}

print(my_dict)

#Using the dict method to create a dictionary
new_user = dict(name= 'Esther', age=17, city='Lagos')
print(new_user)

#Accesing dictionary values
my_dict["age"]
my_dict['name']
my_dict['city']

my_dict['email'] = "Segdavid03@gmail.com"
print(my_dict)

#Delete items
del my_dict["age"]
print(my_dict)


#loop through a dictionary
for key in my_dict.keys():
    print(key)
for values in my_dict.values():
    print(values)
for key, values in my_dict.items():
    print(key, values)


#Update method to update dictionary status
my_dict1 = {
    "name": "Daniel",
    "age": 21,
    "email": "segdaniel07@gmail.com"
}

my_dict2 = {
    "name": "Tofunmi",
    "age": 24,
    "email": "segtofunmi11@gmail.com",
    "city": "ile-ife"
}

my_dict1.update(my_dict2)
print(my_dict1)