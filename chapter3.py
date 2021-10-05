# store the names of a few friends in a list called names. Print each eprsons name by accessing each element in tue list, one at a time.
names = ['dudu', 'daniel', 'iron', 'leo']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# Start w/ the list used before, but now print a message to them. The text of each message should be the sa,e, but each message should be personalized w/ the persons name
print(f'Hello {names[0]} have a great day!')
print(f'Hello {names[1]} have a great day!')
print(f'Hello {names[2]} have a great day!')
print(f'Hello {names[3]} have a great day!')

# Make a list that includes at leat three people youd like to invite do dinner. Then use your list to print a message to each person, inviting them to dinner
guests = ['ronaldo', 'robin', 'ronaldin']
print(f'Welcome to my dinner {guests[0]}')
print(f'Welcome to my dinner {guests[1]}')
print(f'Welcome to my dinner {guests[2]}')

# Someone wont be able to go to dinner. Modify your list replacing the name of the guest who cant make it w/ the name of a new person you are inviting

guests.remove('ronaldin')
print(guests)
guests.append('claudin')
print(guests)

#You just found a bigger table, now invite more people! Use insert() to add one new guest to the beggining of your list, use insert() to add one new guest to the middle of your list, use append() to add one new guest top the end of your list

print(guests)
guests.insert(0, 'robson')
print(guests)
guests.insert(2, 'milton')
print(guests)
guests.append('joao')
print(guests)

# time to delete people off dinner! Use pop() ti remove guests from your list one at a time until only two names remain inyour list. Each time you pop a name form your list, print a message to that eprson letting them knwo youre very sorry oyu cant invite them
pop1 = guests.pop()
print(f'Sorry {pop1}')
pop2 = guests.pop()
print(f'Sorry {pop2}')
pop3 = guests.pop()
print(f'Sorry {pop3}')
pop4 = guests.pop()
print(f'Sorry {pop4}')
print(guests)

# message whos still invited

print(f'hey {guests[0]} you are still invited')
print(f'hey {guests[1]} you are still invited')

# use del to remove the last 2 names, print your list to make sure you ahve an empty list

del guests[1]
del guests[0]
print(guests)