# default argument put in last
# variable number of argument define  using * that argument is form of tuple value
# if use **args then you  pass keword argument in function and this store as dictionary key and value style
# Scope : Region of code where variable is defined
# Debug:
# initate  debug mode :F5
# step by step : F10
# Go to definition of function F11
# Immediate out of function :Shift + F11
# chose the breakpoint according to need if you the error in the function set break point in the function definition if no error step out using shift F11.
# File Start : Ctr + Home
# File End Cursore : Ctr + End
# Line end: End buttone
# Line start :Home
# Move a current line or select multiline :Alt + arrow Key up and down
# Duplicate Line :select +shift +alt +down Key
# Select Current Line: Ctl +L


def multiplication(*numbers):
    print(numbers)  # (1,2,3,4,5)
    total = 1
    for num in numbers:
        total *= num
    return total


def identity_user(**user):
    print(user)  # {'id': 25, 'name': 'Jhon', 'bill': 2500}
    return print(user['name'])


print("start")
print(multiplication(1, 2, 3))
# print(identity_user(id=25, name='Jhon', bill=2500))
