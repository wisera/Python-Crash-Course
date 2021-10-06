# Think of at leat 3 kinds of pizza. Store them in a list, then use a for loop to print the name of each pizza
# modify your for loop to print a sentence using the name og the pizza instead of printinf just the name. For eac pizza you hsould say I like pizza flavor
# add a new line outside the for loop, that states how much you love pizza
best_pizzas = ['siciliana', 'burrata', 'pepperoni']
for pizza in best_pizzas:
    print(pizza)

for pizza in best_pizzas:
    print(f'I love {pizza} pizza')

print('These are my favourite pizza flavors')

#LIST COMPREHENSIONS

# Use a for loop to orint the numbers from 1 to 20

for number in range(1,21):
    print(number)

# now print a list of numbers from 1 to 200

my_list = list(range(1,201))
print(my_list)

# now use min() and max() to make sure your list actually starts at one and ends at 200
#also use sum()

print(min(my_list))
print(max(my_list))
print(sum(my_list))

# use the thrid argument of the range() function to make a list of odd numbers from 1 to 20. Use a for loop to print each number

odd_numbers = range(1,21,2)

for number in odd_numbers:
    print(number)

# make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list

multiples_of_3 = list(range(3,31,3))
for number in multiples_of_3:
    print(number)

# make a list of the first 10 cubes, ex.:(2**3), from 1 to 10, and use a for loop to print out each value
cubes = []
for number in range(1,11):
    cubes.append(number**3)
print(cubes)

# use a list comrpehension to generate a list of the first 10 cubes

cubes_comp = [number**3 for number in range(1,11)]
print(cubes_comp)

# using the created list best_pizzas, do the following:
# print the message The first theree intems in the list are:. Then use a slice to print the first three items from that list
best_pizzas = ['siciliana', 'burrata', 'pepperoni']
print(f'The first three items in the list are: \n{best_pizzas[:3]}')

#print the message Three items from the middle of the list are: Use slice
best_pizzas.append('bacon')
best_pizzas.append('mushroom')

print(f'The three items from the middle are: \n{best_pizzas[1:4]}')

#print the message Three last items...

print(f'The last three are: \n{best_pizzas[-3:]}')

# Make a copy of the best_pizzas, and call it friend_pizzas

friend_pizzas = best_pizzas[:]
print(friend_pizzas)

# add a new pizza to the original list
# add a different pizza to the friend_pizzas

best_pizzas.append('parma')
friend_pizzas.append('shizzle')

# prove that you have 2 separate lists. Print a message My favorite pizzas are:, and then use a for loop to print the first list.
# Print the message My frind's favorite pizzas are:. amd the use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list
print('My favorite pizzas are:')
for pizza in best_pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'
# write an if statement to test whether the alien's color is green. If it is, print a message the player just earned 5 points
# write one versiion of this p[rogram that passes the if test and another that fails
 
alien_color = 'green'

if alien_color == 'green':
    print('You just earned 5 points')

if alien_color == 'red':
    print('Hes red')

# choose a color for an alien as you did and write an if-else chain
# if the alien's color is green, print a statement that the player just earned 5 points for shooting the alien
# if the alien's color isnt green, print a staetement that the player just earned 10 points
# write one version of this program that runs the if block and another that runs the else block

alien_color = 'green'

if alien_color == 'green':
    print('You just earned 5 points')
else:
    print('you earned 10 points')

alien_color = 'red'

if alien_color == 'green':
    print('You just earned 5 points')
else:
    print('you earned 10 points')

# turn your if-else chain into an if-elif-else chain
# if the alien is green print a message that the player earned 5 points
# if the alein is yellow, print a message that the player earned 10 points
# if the alien is red, print a message that the player earned 15 points
# write 3 versions, making sure each message is printed for the appropriate color
alien_color = 'green'

if alien_color == 'green':
   print('You just earned 5 points')
elif alien_color == 'yellow':
    print('you earned 10 points')
elif alien_color == 'red':
    print('you earned 15 points')

alien_color = 'red'

if alien_color == 'green':
   print('You just earned 5 points')
elif alien_color == 'yellow':
    print('you earned 10 points')
elif alien_color == 'red':
    print('you earned 15 points')

alien_color = 'yellow'

if alien_color == 'green':
   print('You just earned 5 points')
elif alien_color == 'yellow':
    print('you earned 10 points')
elif alien_color == 'red':
    print('you earned 15 points')

# write an if-elif-else chain that determines a persons stage of life. Set a value for the variable age, and then:
# if the person is less than 2 years old, print a message that the person is a baby
# if the person is a least 2 years old but less than 4, print a message that person is a toddler
# if the persons is at leat 4 years old but less than 13, print a message that the person is a kid
# if the person is at least 13 but less than 20, print a message that the p[erson is a teen
# # if the person is at least 20 but less than 65, print that the person is an adult
# if the person is age 65 or older, print elder

age = 23

if age < 2:
    print('baby')
elif age >=2 and age < 4:
    print('toddler')
elif age >=4 and age < 13:
    print('kid')
elif age >=13 and age < 20:
    print('teen')
elif age >=20 and age < 65:
    print('adult')
elif age >=65:
    print('elder')

# make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list
# make a list of your 3 favorite fruits and call it favorite_fruits
# write 5 if statements. Each should check whether a certain kind of frui is in your list.
# if the fruit is in your list, the if block should print a statement, such as You really like banana!

favorite_fruits = ['apple', 'banana', 'orange']

if 'banana' in favorite_fruits:
    print('You like bananas!')
if 'strawberry' in favorite_fruits:
    print('you like strawberry!')
if 'orange' in favorite_fruits:
    print('you like orange!')
if 'blackberry' in favorite_fruits:
    print('you like blackberry!')
if 'apple' in favorite_fruits:
    print('you like apple!')

