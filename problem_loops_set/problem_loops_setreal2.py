#password checker
password = input('Create a password with at least 8 characters and one uppercase letter')
while len(password) <= 8 or password.lower() == password:
    print('Password is not valid. Try again')
    password = input()
print('Password is valid.')