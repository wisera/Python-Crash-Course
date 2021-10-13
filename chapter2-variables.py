#Use a variabel to represent a person's name, and priont a message to that person. Your message should be simple, such as, "Hello Eric, would like to learn some python today?"
name = "Eric"

print(f"Hello {name}, would you like to learn some Python?")

# Use a variable to represent a psern's name, and thern print that person's name in lowecase, uppsercase, and title case
name = "luan"

print(name.upper())
print(name.lower())
print(name.title())

# Find a quote from a famous person you admire. POrint the quote and the name of its author.

print('\tAlbert Einstein once said, "A person who never made a\n\tmistake never tried anything new"')

#Repeat last exercise but this time represent the famous person's name using a variable called famous_person. Then compose your message and represent it witha new variabel called message. Print your message

famous_person = "Albert Einstein"
message = print(f'\t{famous_person} once said, "A person who never made a\n\tmistake never tried anything new"')

#Use a variable ro represent a person's name, and iclude some whitespace characters at the beggining and end of the name. Make sure you use each character combination, "\t" and "\n" at least once. Print the anem once, so the whitespace around the name is displayed. Then porint the name using each of the thress stripping functions, lstrip(), rstrip(), and strip()

name = "\t\nluan\n"
print(name)
print(name.rstrip())
print(name.lstrip())
print(name.strip())

