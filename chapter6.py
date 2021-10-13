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

# use the dictionary person created before. 
# Make 2 new dictionaries representing different people, adns tore all 3 dicitonaries in a list called people
# Loop through your list of people. As you loop through the list, print everything you know about each person.

person_0 = {
    'first_name':'Luan',
    'last_name':'Moreira',
    'age':'24',
    'city':'San Diego'
}

person_1 = {
    'first_name':'Carlos',
    'last_name':'Menezes',
    'age':'23',
    'city':'Nikity City'
}

person_2 = {
    'first_name':'Daniel',
    'last_name':'Bressan',
    'age':'22',
    'city':'Vargem Grande Paulista'
}

people = [person_0, person_1, person_2]

for person in people:
    print(f"My name is {person['first_name']} {person['last_name']}"
            f"\nI'm {person['age']} years old"
            f"\nand I'm from {person['city']}"
    )

# make several dictionaries, where each dictionary represents a different pet.
# in each dicitonary, include the kind of animal and the owner's name.
# store these dictionaries in a list called pets.
# next loop through your list and as you do, print everything you know about each pet

pet_0 = {
    'kind':'dog',
    'name':'doco',
    'owner_name':'carol'
}

pet_1 = {
    'kind':'cat',
    'name':'toguro',
    'owner_name':'luan'

}

pets = [pet_0, pet_1]

for pet in pets:
    print(f"This little guy's name is {pet['name'].title()}, obviously he is a {pet['kind'].lower()}"
            f"\nhis owner is called {pet['owner_name'].title()}")

# make a dictionary called favorite_places. 
# Think of 3 names to use as keys in the dicitironary , and store one to three favorite pklaces for eadh person.
# Loop through the dicitonary and print each person's name and their favorite places

favorite_places = {
    'luan':'san diego',
    'marcos':'el salvador',
    'carol':'italy'
}

for key in favorite_places:
    value = favorite_places[key]
    print(f"{key.title()}'s place is {value.title()}")

# modify the second exedrice so each person can have more than one favorite number. 
# Then print each person's name along with their favoreite numbers

favorites = {
    'luan':[22,2],
    'carlos':[24,8],
    'daniel':[10,30],
    'leo':[13,10],
    'carol':[29,88]
}

for name,number in favorites.items():
    print(f"{name.title()}'s favorite numbers are {number[0]} and {number[1]}")

# make a dictionary called cities. Use the names of three cities as keys in your dicitionary. 
# Create a dicitonary of information about each city and include the county that the city is in, population, and fact
# print the name of each city and all of rhe info you have about it

cities = {
    'san diego': {
        'country': 'usa',
        'population': 10,
        'fact':'luan was born here'
    },

    'nikity': {
        'country': 'brazil',
        'population':11,
        'fact':'luan lived here'
        },
    
    'sampa': {
        'country': 'brazil',
        'population': 12,
        'fact':'luan visited here'
    }
}

for city, city_items in cities.items():
    print(f"The city of {city.title()} is located in the country of {city_items['country'].title()}, "
        f"\nits population is of {city_items['population']} people, "
        f"\na fact about it is that {city_items['fact']}"
    )