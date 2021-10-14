# open a blank file in your text editor and write a few lines summarizing what you've learned so far about Python.
# start each line w/ the phrase 'In Python you can...'
# save the file as learning_pyhon.txt in the same dir as your exercises
# write a program that reads the file and prints what you wrote 3 times
# print the contents once by readin in the entire file, once by looping over the file object, 
# and once by storing the lines in a list and then working w/ them outside the with block

file_name = 'learning_python.txt'

with open(file_name) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# you can use the replace() method to replace any word in a string w/ a different word.
# read in each line from the filem and replace Python for C
# print the modified line to the screen

with open(file_name) as file_object:
    for line in file_object:
        print(line.replace('Python','C').rstrip())