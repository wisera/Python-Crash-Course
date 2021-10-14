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

# write a program that prompts the user for their name.
# when they respond, write their name to a file called guest.txt

name = input('tell me ur name: ')

with open('guest.txt', 'w') as file_object:
    file_object.write(name)

with open('guest.txt') as file_object:
    contents = file_object.read()
    print(contents)

# write a while loop that prompts users for their name.
# when they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt
# make sure each entry appears on a new line in the file

while True:
    print('Tell me your name ( press q to quit )')
    name = input('name: ')
    if name == 'q':
        break
    print(f'Welcome {name.title()}')
    
    with open('guest_book.txt', 'a') as file_object:
        file_object.write(f'{name}\n')

with open('guest_book.txt') as file_object:
    contents = file_object.read()
    print(contents)

# one common problem when prompting for numerical inpout occurs when people provide text instead of numbers
# when you try to convert the inoput to an int, you'll get a ValueError
# write a program that prompts for two numbers.
# add them together and print the result
# catch the ValueError if either input value is not a number, and print a firendly error message.
# test your program by entering two numbers and then entering some text instead of a number

while True:
    print('Enter 2 numbers and I will add them')
    print("press 'q' to quit")
    
    first_number = input('enter your first number: ')
    if first_number == 'q':
        break
    second_number = input('enter your second number: ')
    if second_number == 'q':
        break

    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print('please enter a number!')
    else:
        print(f'Your result is {result}')

