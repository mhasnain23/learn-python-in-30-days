# Creating lists with different data types
fruits: list  = ["apple", "banana", "cherry"]
numbers: list = [10, 20, 30, 40]
mixed: list   = ["hello", 42, 3.14, True]

print("fruits  = ", fruits)
print("numbers = ", numbers)
print("mixed   = ", mixed)

fruits: list = ["apple", "banana", "cherry"]
print(fruits[0])   # Output: apple
print(fruits[-3])  # Output: apple

fruits: list = ["apple", "banana", "cherry"]
fruits[-3] = "watermelon" # replacing "apple" with "watermelon"
print(fruits)  # Output: ['watermelon', 'banana', 'cherry']

fruits.append("mango")  # Adds a single element 'mango' to the end
print(fruits)  # Output: ['watermelon', 'banana', 'cherry', 'mango']


fruits.extend(["Graphs", "Kiwi"])
print(fruits)


fruits.remove("banana")
print(fruits)

deleted = fruits.pop(1)
print(deleted) # output cherry
print(fruits)


numbers: list[int] = [3, 1, 4, 1, 5, 9] # unsorted list
numbers.sort()
print(numbers)  # Output: [1, 1, 3, 4, 5, 9]


numbers = [4, 2, 9, 1]
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 4, 2, 1]