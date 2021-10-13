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