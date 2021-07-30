import re

print('Welcome to Email Format Checker:')
print('Lets see if you entered an Email in the correct format')

print('\n')

print('1: The email must start with one or more letters, numbers, ., _')
print('2: The email must have a @ symbol after your email username')
print('3: The email website name must have one or more letters, numbers or dashes')
print('4: The email must have a dot after the website name')
print('5: The email must end in a one or more letters or numbers')

print('\n')

user_email = input('What Email would you like to choose?  ')

regex = '^[a-zA-Z0-9._]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]+$'

if (re.search(regex, user_email)):
    print(f'Great Job, "{user_email}" is a valid email')
else:
    print(f'Error: "{user_email}" not a valid email')
