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





