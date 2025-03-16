# Iterate over a list
fruits: list = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
print("----------------------------------------------")    


# Iterate over a string to get each character
word: str = "Python"
for letter in word:
    print(letter) # P, y, t, h, o, n
    
    
print("----------------------------------------------")
    
# In Python, a for loop can have an else block. The else block runs only if the loop completes without a break statement.
# loop with else no break
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
else:
    print("Loop completed successfully!")
    


print("----------------------------------------------")


# loop with else with break
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
    if num == 3:
        print("Breaking the loop!")
        break
else:
    print("Loop completed successfully!")  # This will NOT run
    
    
print("----------------------------------------------")

# Searching with else

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 6:
        print("Number found!")
        break
else:
    print("Number not found!")  # Runs because 6 is not in the list
    
# range method
# Print numbers from 0 to 4
for i in range(5):
    print(i)
    
print("----------------------------------------------")
# Print even numbers from 2 to 10
for i in range(2, 11,2):
    print(i)
    
    
print("----------------------------------------------")
    
for _ in range(10): # Just to show that _ is a loop variable, but its throwaway variable
    # Code to be executed 100,000 times
    print(f"Hello, World! Iteration { _ }")
    
    
print("----------------------------------------------")

# Print numbers from 1 to 5
count: int = 1
while count <= 5:
    print(count)
    count += 1
    
print("----------------------------------------------")

# Break example
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0, 1, 2, 3, 4
    
print("----------------------------------------------")

# Continue example
for i in range(5):
    if i == 3:
        continue  # Skip the current iteration, hence 3 is not printed
    print(i)  # Prints 0, 1, 2, 4
    
print("----------------------------------------------")

# Multiplication table
for outer in range(1, 6): # outer loop
    print(f"Multiplication table for {outer}:")
    for inner in range(1, 6): # nested inner loop
        print(f"{outer} * {inner} = {outer * inner}")
    print()  # Add a blank line after each row
    
    
print("--------------------------------------")

# Sum numbers from 1 to 100
total: int = 0
for i in range(1, 101):
    total += i
print("Sum of numbers from 1 to 100:", total)


# Find factors of a number
num: int = 24
factors = []
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)
print(f"Factors of {num}: {factors}")
