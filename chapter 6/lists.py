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

words = ["apple", "kiwi", "banana"]
words.sort(key=len)
print(words)  # Output: ['kiwi', 'apple', 'banana']


words = ["apple", "kiwi", "banana"]
words.sort(key=lambda word: word[-1])
print(words)  # Output: ['banana', 'apple', 'kiwi']  # Sorted by last letter

numbers = [1, 2, 5, 7, 10]
numbers.reverse()
print(numbers)  # Output: [10, 7, 5, 2, 1]


for name in dir(str):
    if name.startswith("__"):
        continue
    print(name)

# List comprehension
# Without if condition
squared: list = [x**2 for x in [1, 2, 3, 4, 5] ] #  if x > 3 place this if condition and see
print(squared, " : ", type(squared))  # Output: [1, 4, 9, 16, 25]

squared: list = [x**2 for x in [1, 2, 3, 4, 5] if x > 3] #  if x > 3 place this if condition and see
print(squared, " : ", type(squared))  # Output: [1, 4, 9, 16, 25]