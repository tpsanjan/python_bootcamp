''
## User defined function demo
def greet(name):
    print("Hello, " + name)

greet("Sanjan")     # Output: Hello, Sanjan
greet("Matt")       # Output: Hello, Matt
print('\n')

''
## Adding default value
def greet1(name = "there"):
    print("Hello, " + name)

greet1()             # Output: Hello, there
greet1("Sanjan")     # Output: Hello, Sanjan
print('\n')

''
## Function documentation using docstrings that can be retrieved using help()
def greet2(name = "there"):
    """Print a greeting message to the person with the given name."""
    print("Hello, " + name)

help(greet2)

greet2()
greet2("Sanjan")
greet2("Matt")
print('\n')
''

## Lets build a custom function to compute the exponent of a number
def power(base, exponent):
    pow = 1
    for i in range(exponent):
        pow *= base
    return pow

a = 2
exp = 3
print(power(a, exp))

# Do you think above implementation is perfect !?
print('Power fun O/P: ', power(a, -3), ' vs Expected O/P: ', (a ** (-3)) )

# Homework: Try modifying the above function to account for edge cases!
''