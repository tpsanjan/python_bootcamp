'''
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

'''
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
