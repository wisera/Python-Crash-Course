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
