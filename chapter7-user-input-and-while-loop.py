# wirte a program that asks the user what kind od rental car they would like. 
# Print a message about that cat, such as "Let me see if I can find you a Subaru"

car_type = input('what kind of car do you want?')

print(f'Let me check if we have a {car_type}')

# ask the user how many people are in their dinner group
# if the answer is more than 8, porint a message saying that they will gave to wait for a table
# otherwise report that the table is ready

number_of_people = int(input('How many people are in your dinner group?'))

if number_of_people > 8 :
    print('Sorry you will have to wait')
else:
    print('Right this way sir')

# ask the user for a number, and then report if the number is a ultiple of 10 or not

number = int(input('Gimme a number and Ill let you know if its a multiple of 10 '))

if number % 10 == 0:
    print(f'{number} is a multiple of 10')
else:
    print(f'{number} is not a multiple of 10')

# write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
# as they enter each topping, print a message saying you will add that topping to their pizza

while True:
    topping = input("enter your favorite pizza toppings \n (enter 'quit' to stop)")
    if topping == 'quit':
        break

# or

active = True

while active:
    topping = input("enter your favorite pizza toppings \n (enter 'quit' to stop)")
    if topping == 'quit':
        active = False


# a movie theater charges different ticket prices depending on a person's age. 
# If a person is under the age 0f 3, the ticket is free
#  if they are between 3 and 12, the ticket is $10
# if they are over age 12, the ticket is $15
# write a loop in which you ask users their age, and then tell them the cost of their movie ticket

age = int(input('How old are you? '))

if age < 3:
    print('Your ticket is free')
elif age <= 3 or age < 12:
    print('Your ticket is $10')
else:
    print('Your ticket is $15')

# make a lit called sandwich_orders and fill it with the names of various sandwiches
# Then make an empty list called finished_sandwiches.
# Loop through the list of sandwich oreders and print a message for each order, such as I mde your tuna sandwich
# as each sandwich is amde, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made

sandwich_orders = ['tuna', 'blt', 'parma', 'cheese', 'salami']

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich} sandwich')
    finished_sandwiches.append(sandwich)

print(f'The following sandwiches have been made: ')

for sandwich in finished_sandwiches:
    print(f'{sandwich}')

# using the list sandwich_orders from last exercise, make sure the sandwich 'parma' appears in the list at leat 3 times
# add code near the beggining of your program to print a message saying the deli has run out of parma,
# and then use a while loop to remove all occurences of 'parma' from sandwich_orders
# make sure no parma sandwiches end up in finished_sandwiches

sandwich_orders = ['tuna', 'parma', 'blt', 'parma', 'cheese', 'parma', 'salami']

finished_sandwiches = []

print('sorry we ran out of parma')

while 'parma' in sandwich_orders:
    sandwich_orders.remove('parma')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich} sandwich')
    finished_sandwiches.append(sandwich)

print(f'The following sandwiches have been made: ')

for sandwich in finished_sandwiches:
    print(f'{sandwich}')

# write a program that polls users about their dream vacation.
# write a prompt similar to if you could visit one place in the world, where would you go?
# include a vlock of code that prints the results to the poll

dream_vacation = {}

poll_active = True

while poll_active:
    name = input('Hello, whats your name?')
    response = input('If you could visit one place in the world, where you you go?')
    dream_vacation[name] = response

    repeat = input(' would another person like to share? ( write quit to stop )')
    if repeat == 'quit':
        poll_active = False

print('The poll results are: ')

for name, response in dream_vacation.items():
    print(f'{name.title()} would like to go to {response.title()}')
