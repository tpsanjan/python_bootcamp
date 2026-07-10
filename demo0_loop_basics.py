## Loops in python (for and while)

# 'for' loop can be used to iterate over a list, tuple, dictionary or any other iterable
cars = ["bmw", "audi", "renault"]
for car in cars:
    print(car)

''	
# 'while' loop is executed as long as the condition is true and exits once it becomes false
count = 1
while count <= 10:
    print(count)
    count += 1
# Note: It is important that the condition eventually becomes false. Else it will become an infinite loop!
# In other words, when designing a loop -- both start and stop criteria should be clearly defined.
''

## Lets look at some other variants of 'for' loop

print("Using range() to generate index:")
for i in range(5):
    # Note: the stop value is not included
    print(i)

print("Modified step-size demo:")
for i in range(0, 10, 2):
    # range can take 3 inputs: START (optional, default val = 0), STOP, and STEP-SIZE (optional, default val = 1)
    print(i)

print("Reverse 'for' loop:")
for i in range(5, 0, -1):
    print(i)
''

# 'for' loop with an index
cars = ["bmw", "audi", "renault"]
for i in range(len(cars)):
    print(i, cars[i])
''

# Automatically generate indices using enumerate()
cars = ["bmw", "audi", "renault"]
for i, car in enumerate(cars):
    # enumerate() returns two outputs - an index and the element
    print(i, car)
''

# What if you don't like the 0-based indexing?
cars = ["bmw", "audi", "renault"]
print('\n')
print('Lets modify the 0-based indexing')
for i, car in enumerate(cars, 1): # by default, index starts at 0 -- here we are specifying 1 as the start
    # enumerate() returns two outputs - an index and the element
    print(i, car)
''

# Inline 'for' loop
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]	# note: ** stands for exponent while * is for multiplication
print(squares)
# Note: This is a compact way to implement 'for' loop via list comprehension!

# Can you make this one-liner !?
''

## Adding break and continue statement into a loop

# How to break a 'for' loop midway?
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        # end 'for' loop
        break
    print(num)

# Note: when the compiler encounters 'break' statement, it exits the loop without going through the subsequent statements in the 'for' module
''

# How to break a 'while' loop midway?
n = 1
while n <= 10:
    print(n)
    if n == 5:
        break
    n += 1
print("Loop Ended")
''

# Use 'continue' to skip a particular iteration of 'for' loop
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        continue
    print(num)
''

# Lets look at using 'continue' in a 'while' loop along with list.pop()
my_list = [1, 2, 3, 4, 5]
while my_list:
    val = my_list.pop()
    if val == 3:
        continue
    print(val)
''

# How to break out of an infinite while loop?
while True:
    # Note: We are inside an infinte loop!
    value = input("Enter a number OR type out 'stop': ")
    if value == "stop":
        break
    print(int(value) ** 2)
print("Loop Ended")
''

## Nested loops

# Nested 'for' loop
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]     # its a 3x3 matrix!

for row in numbers:
    for num in row:
        print(num)
''

# Nested 'while' loop
x = 1
y = 1

# can you guess the output !?
while x <= 5:
    while y <= x:
        print(y, end = " ")    # By default, print ends with '\n'
                               # instead we swap it with space char
        y += 1                 # short hand for y = y + 1 
    
    # Note: we are now in outer 'while' loop
    print()                    # same as print('\n')
    x += 1  # short hand for x = x + 1
    y = 1   # to reset the value of y to 1
    
''