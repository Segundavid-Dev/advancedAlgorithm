# dynamically creates an open the filepath in write mode
file = open("file.txt", 'w')


# filePath directory (Relative)
filePath = 'file.txt'

# writing to file
with open(filePath, 'w') as file_object:
    file_object.write("Writing to files\n") 
    file_object.write("Advanced python\n")
    file_object.write("Working with files")

# reading file content line by line
with open(filePath, 'r') as fileObject:
    for word in fileObject:
        print(word)