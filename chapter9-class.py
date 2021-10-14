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

# start w/ your program from last exercice.
# add an attribute called number_served w/ a default value of 0.
# Create an instance called restaurant from this class.
# print the number of customers the restaurant has served, and then change this value and print it again
# add a method called set_number_served() that lets you set the number of customers that have been served.
# call this method w/ a new number and print the value again
# add a method called increment_number_served() that lets you increment the number of customers who've been served
# call this method w/ any number you like that could represent how many customers were served in, say, a day of business

class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name.title()} serves {self.cuisine_type.title()} food")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open for business")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number_served):
        self.number_served += increment_number_served
restaurant = Restaurant('Mcdonalds','junk')

print(restaurant.number_served)
restaurant.number_served = 5
print(restaurant.number_served)

restaurant.set_number_served(10)
print(restaurant.number_served)

restaurant.increment_number_served(20)
print(restaurant.number_served)

# add an attribute called login_attempts to your User class from last exercise.
# write a method called increment_login_attempts() that increments the value of login_attempts by 1
# write another method called reset_login_attempts() that resets the value of login_attempts to 0
# make an instance of the User class and call increment_login_attempts() several times.
# print the value of login_attempts to make sure it was incremetned properly, and then call reset_login_attempts()
# print login_attempts again to make sure it was reset to 0

class User:

    def __init__(self, first_name, last_name, age, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()}, "
            f"he is {self.age} years old and he likes to {self.hobby}")
    
    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}, welcome back!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
    
my_user = User('ronaldo','gaucho','50','soccer')

my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
print(my_user.login_attempts)

my_user.reset_login_attempts()
print(my_user.login_attempts)

# an ice cream stand is a specific kind of restaurant. 
# Write a class called IceCreamStand that inherits from the Restaurant class you wrote from last exercise.
# add an attribute called flavors that stores a list of ice cream falvors.
# write a method that displats these flavors.
# create an instance of IceCreamStand, and call this method

class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name.title()} serves {self.cuisine_type.title()} food")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open for business")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number_served):
        self.number_served += increment_number_served
    
class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla','cholate','caramel']
    
    def display_flavors(self):
        print('We have the following flavors: ')
        for flavor in self.flavors:
            print(flavor)

quasar = IceCreamStand('quasar','ice cream')

quasar.display_flavors()

# an administrator is a special kind of user.
# write a class called Admin that inherits from the User class you wrote in the last exercise
# add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user"
# write a method called show_privileges() that lists the administrator's set of privileges
# create an instance of Admin, and call your method

class User:

    def __init__(self, first_name, last_name, age, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()}, "
            f"he is {self.age} years old and he likes to {self.hobby}")
    
    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}, welcome back!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    
    def __init__(self, first_name, last_name, age, hobby ):
        super().__init__(first_name,last_name,age,hobby)
        self.privileges = ['can add post','can delete post','can ban user']
    
    def show_privileges(self):
        print('These are the set of privileges the admin account has: ')
        for privilege in self.privileges:
            print(privilege)
    
admin_0 = Admin('admin','admin','100','administrate')

admin_0.show_privileges()

# write a separate Privileges class.
# the class should hae one attribute, privileges, that stores a list of sstrings as described in last exercise
# move the show_privileges() method to this class.
# make a Privileges instance as an attribute in the Admin class.
# create a new instance of Admin and use your method to show its privileges

class User:

    def __init__(self, first_name, last_name, age, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()}, "
            f"he is {self.age} years old and he likes to {self.hobby}")
    
    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}, welcome back!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    
    def __init__(self, first_name, last_name, age, hobby ):
        super().__init__(first_name,last_name,age,hobby)
        self.privileges = Privileges()

class Privileges:
    
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']
    
    def show_privileges(self):
        print('These are the set of privileges the admin account has: ')
        for privilege in self.privileges:
            print(privilege)

admin_1 = Admin('admin_1','admin_1',0,'administrate')

admin_1.privileges.show_privileges()
