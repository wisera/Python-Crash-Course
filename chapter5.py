# use a dictionary to store info about a person you know. Store their first name, last name, age, and the city they live in
# You should have keys such as first_name, last_name, age, and city. Print each piece of info stored in the dictionary

person = {
    'first_name':'Luan',
    'last_name':'Moreira',
    'age':'23',
    'city':'San Diego'
}

for value in person:
    print(person[value])

# use a dictionary to store peoples favorite numbers. Think of five names, and use them as keys in your dictionary.
# Think og a favorite number for each person, and store each as a value in your dicitonary.
# Print each persons name and their favorite number.

favorites = {
    'luan':22,
    'carlos':24,
    'daniel':10,
    'leo':13,
    'carol':29
}

for key in favorites:
    print(key)
for value in favorites:
    print(favorites[value])

 # make a dictionary containing three mahor rivers and the country each river runs through. One key-value paru might be 'nile : 'egypt'
 # use a loop to rpint ther name of each river included in the dictionary
 # use a loop to print the name of each country included in the dictionary

rivers = {
     'nile':'egypt',
     'amazon':'brazil',
     'canyon':'usa'
     }

for river in rivers:
    country = rivers[river]
    print(f'The {river} river runs through the country of {country}')

for river in rivers:
    print(river)
for country in rivers.values():
    print(country)

# make a list of people who should take the favorite languages poll. 
# Include some names that are already in the favorite_languages dictionary nad some that are not
# loop through the list of people who should take the poll. 
# If they have already taken the poll, print a message thanking them for responding
# If they have not take the poll, print a message inviting them to take the poll

favorite_languages = {
    'jen': 'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

people_for_poll = [
    'luan',
    'carlos',
    'phil',
    'edmundo',
    'edward'
]

for person in people_for_poll:
    if person in favorite_languages:
        print(f'hey {person}!\nThanks for taking the poll!')
    else:
        print(f'Hey {person}!\n You should take the damn poll!')