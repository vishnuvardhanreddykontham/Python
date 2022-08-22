#Write a program to check whether the given password is valid or not .
#conisder the password to be valid if it contain at least one digit ands one capital.
#input:it will be a single line containng string
#output: valid password or invalid password
#ex:GJ22191gopi
#ouput:valid password
'''password = input("enter the password: ")
number_pass = False
upper_pass = False
for i in password:
    if i.isupper():
        upper_pass = True
    elif i.isnumeric():
        number_pass = True
    if number_pass and upper_pass:
        print("valid password")
        break
else:
    print("not valid password")
#output:enter the password: GJ22191gopi
valid password
enter the password: gopi
not valid password'''
