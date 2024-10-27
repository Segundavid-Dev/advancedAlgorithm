"""
Author:sgedavid03@gmail.com
Computes and displays the Flesch Index and the Grade Level Equivalent for the readability of a text file.
"""

# Take the inputs
fileName = input("Enter the fileName: ")
inputFile = open(fileName, 'r')
text = inputFile.read()
# print(text)

# count the sentence
sentences = text.count('.') + text.count('?') + text.count(':') + text.count(';') + text.count('!')
# print(sentence)

# count the words
words = len(text.split())
# print(words)

# count the syallables
syllables = 0
for word in text.split():
    for vowel in ['a', 'e', 'i', 'o', 'u']:
        syllables += word.count(vowel)
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 1
    if word.endswith('le'):
        syllables += 1
    

# compute the Flesch index and grade level
index = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables * words)
level = round(0.39 * words / sentences) + 11.8 * (syllables / words - 15.59)

# output results
print(f"The flesh index is {index}")
print(f"The Grade level is equivalent to {level}")
print(f"sentences: {sentences}")
print(f"words: {words}")
print(f"syllables: {syllables}")