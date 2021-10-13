# make a class called Restaurant. 
# The __init__() method for Restaurant should store 2 attributes: a restaurant_name and a cuisine_type.
# make a method called describe_restaurant() that prints these 2 pieces of info,
# and a method called open_restaurant() that prints a message indicating that the restaurant is open
# make an instance called restaurant from your class. Print the 2 attributes individually, and then call both methods

class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name.title()} serves {self.cuisine_type.title()} food")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open for business")

restaurant = Restaurant('Seu Antonio', 'Brazilian')

print(restaurant.restaurant_name, restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# start w/ your class from last exercise
# create 3 different instances form the class, and call describe_restaurant() for each instance

class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name.title()} serves {self.cuisine_type.title()} food")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open for business")

restaurant_0 = Restaurant('Sal Gastronomia', 'Brazilian')
restaurant_1 = Restaurant('00 Pizzeria', 'Italian')
restaurant_2 = Restaurant('Gendai', 'Japanese')

restaurant_0.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()

# make a class called User.
# create 2 attributes called first_name and last_name, 
# and then create several other attributes that are typically sttored in a user profile
# make a method called describe_user() that prints a summary of the user's info
# make another method called greet_user() that prints a personalized greeting to the user
# create several instances representing deifferent users, and call both methods for each user

class User:

    def __init__(self, first_name, last_name, age, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby

    def describe_user(self):
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()}, "
            f"he is {self.age} years old and he likes to {self.hobby}")
    
    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}, welcome back!")

user_0 = User('luan','moreira','24','play the guitar')
user_1 = User('carlos','edwards','23','eat shizzle (just kiddin, s2 carlos)')

user_0.describe_user()
user_0.greet_user()

user_1.describe_user()
user_1.greet_user()