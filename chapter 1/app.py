
def giaic ():
    print("Hello world from giaic!")

# string (str)
first_name:str = "Muhammad"
last_name:str = "Hasnain!"
print(f"My name is {first_name + ' ' + last_name}")

# integer (int)
num1 = 45
num2 = 20
sum = num1 + num2
print("The sum of the num", sum) 

# float (float)

a = 2.7
b= 22.1

print(a + b)

# boolean (bool)
is_true = True
is_false = False

# list (list)
fruit:list[str] = ["Apple", "Banana", "Cherry"]
print(fruit[0:2])

# set (set)
set_data:set = {"apple", "banana", "cherry"}

# dictionary (dict)
dict_data:dict = {
    "name": "hasnain",
    "father_name": "aqeel",
    
}

print(dict_data) # output {'name': 'hasnain', 'father_name': 'aqeel'}
# None (NoneType)
is_none = None # tyoe of None is NoneType
print(is_none) # None

# frozen set (frozenset)
frezon_set = frozenset({"apple", "banana", "cherry"})
print(frezon_set) # frozenset({'banana', 'apple', 'cherry'})


# special keywords in ptthon
"""
pass # ``pass`` is a null statement in python. Nothing happens when it is executed. It is used as a placeholder.
if # ``if`` is a conditional statement that executes some specified code after checking if its expression is True.
elif # ``elif`` is short for else if. It allows us to check for multiple expressions.
else # ``else`` is a conditional statement that executes some specified code if the expression is False.
while # ``while`` is a loop that executes some specified code as long as the expression is True.
for # ``for`` is a loop that executes some specified code for each item in an iterable.
break # ``break`` is a statement that breaks out of the current loop.
continue # ``continue`` is a statement that skips the current iteration of the loop and continues to the next iteration.
"""