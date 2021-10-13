# write a function called display_message() that prints one sentece telling everyone what you are learning about in this chapter
# call the function and make sure the message displays correctly

def display_message():
    """print what im learning"""
    print('Im learning about functions in Python')

display_message()

# write a funciton called favorite_book() that accepts one parameter, title.
# the funciton should print a message, such as One of my favorite books is Alice in Wonderland.
# call the funciton, making sure to include a book title as an argument in the funciton call

def favorite_book(title):
    """Print a message saying my favorite book"""
    print(f'My favorite book is called {title.title()}')

favorite_book('Interior Engineering')

# write a fucntion called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# the funciton should print a sentence summarizing the size of the shirt and the message printed on it
# call the funciton once using positional arguments to make a shirt.
# call the function a second time using keyword arguments

def make_shirt(size, message):
    """print size and message"""
    print(f'The size of the shirt is {size} and the text on it is {message}')

make_shirt(10,'my name is luan')
make_shirt(message='my name is luan', size='medium')

# modify the make_shirt() funciton so taht shirts are large by default w/ a message that reads I love Python
# make a large shirt and a medium shirt w/ the default message, and a shirt of any size w/ a different message

def make_shirt(size='large', message='I luv Python'):
    """print size and message"""
    print(f'The size of the shirt is {size} and the text on it is {message}')

make_shirt()
make_shirt(size='medium')
make_shirt(10, 'my name is luanzin')

# write a function called describe_city() that acepts the name of a city and its country
# the function should print a simple sentence, such as Reyk is in Iceland.
# give the parameter for the country a default value
# call your function for 3 different cities, at leat one of which is not the default

def describe_city(city, country='Brazil'):
    """print city name and country"""
    print(f'the city of {city.title()} is located in {country.title()}')

describe_city('niteroi')
describe_city('san diego','america')
describe_city(country='italy', city='milano')

# write a function called city_country() that takes in the name of a city and its country
# the fucntion should return a string like "Santiago, Chile"

def city_country(city,country):
    message = f"{city.title()}, {country.title()}"
    return message

my_city = city_country('san diego', 'america')
print(my_city)

# write a function called make_album() that builds a dictionary describing a music album
# the function should take in an artist name and an album title, and it should return a dictionary containing these 2 pieces of info
# use the fucntion to make 3 dictionaries representing different albums
# print each return value to show that the diciutonaries are storing the album info correctly
# use None to add an optinal parameter to make_album() that allows you to store the number of songs on an album
# if the calling line includes a value for the number of songs, add that vlaue to the albmumns dicitonary
# make at leat one new fucntuion call taht includes the number of songs on an album

def make_album(artist, name, songs=None):
    album = {
        'artist name' : artist.title(),
        'album name' : name.title()
    }
    if songs:
        album['number of songs'] = songs
    return album

album_0 = make_album('milena amaral', 'impossivel')
album_1 = make_album('iron maiden','fear of the dark')
album_2 = make_album('caio guerra', 'espelho', 1)

print(album_0)
print(album_1)
print(album_2)

# start w/ your program from last exercice. Write a while loop that allows users to enter an album's artist and title
# Once you have that info, call make_album() w/ the user's inpput and print the dicitonary thats created
# be sure to include a quit value in the while loop

def make_album(artist, name, songs=None):
    album = {
        'artist name' : artist.title(),
        'album name' : name.title()
    }
    if songs:
        album['number of songs'] = songs
    return album

while True:
    print("Hello, please enter the following information about your favorite music album")
    print("enter 'q' at any given time to stop")

    artist_name = input("Please enter your artist's name: ")
    if artist_name == 'q':
        break
    album_name = input("Please enter the name of the album: ")
    if album_name == 'q':
        break
    number_of_songs = input("Please enter the number of songs (optional): ")
    if number_of_songs == 'q':
        break

    album = make_album(artist_name, album_name, number_of_songs)
    print(album)