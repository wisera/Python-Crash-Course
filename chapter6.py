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
