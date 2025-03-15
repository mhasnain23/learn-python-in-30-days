
# Comparison operators
# ==, !=, >, <, >=, <=
x: int = 10
y: int = 20

print("x == y = ", x == y)  # False
print("x != y = ", x != y)  # True
print("x > y  = ", x > y)   # False
print("x < y  = ", x < y)   # True
print("x >= y = ", x >= y)  # False
print("x <= y = ", x <= y)  # True

# Logical operators
# and, or, not

# Already done in lesson 2
age: int = 25
is_student: bool = True

# Check if age is greater than 18 AND is_student is True
if age > 18 and is_student:
    print("You are eligible for a student discount.")

# Check if age is less than 12 OR greater than 60
if age < 12 or age > 60:
    print("You qualify for a special discount.")

# Check if the person is NOT a student
if not is_student:
    print("You are not a student.")
    
    
# The if statement
num: int = 10

if num > 0:
    print("The number is positive.")
    

# The else statement
num: int = -5

if num > 0:
    print("The number is positive.")
else:
    print("The number is not positive.")