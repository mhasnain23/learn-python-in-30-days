# special keywords in ptthon
"""
# ``pass`` is a null statement in python. Nothing happens when it is executed. It is used as a placeholder.
" ``if`` is a conditional statement that executes some specified code after checking if its expression is True.
# ``elif`` is short for else if. It allows us to check for multiple expressions.
# ``else`` is a conditional statement that executes some specified code if the expression is False.
# ``while`` is a loop that executes some specified code as long as the expression is True.
# ``for`` is a loop that executes some specified code for each item in an iterable.
# ``break`` is a statement that breaks out of the current loop. we already learn this in while loop
# ``continue`` is a statement that skips the current iteration of the loop and continues to the next iteration.
"""


# ``pass`` is a null statement in python. Nothing happens when it is executed. It is used as a placeholder.
def main ():
    pass


# ``if`` is a conditional statement that executes some specified code after checking if its expression is True.
i = 2
user_guess = int(input("Please guss the number between 1-5: "))

if i == user_guess :
    print("you win")
    
    
    
# ``elif`` is short for else if. It allows us to check for multiple expressions."
if 3 >= 4:
    print(False)
elif 3>=3:
    print(True)
    

# ``else`` is a conditional statement that executes some specified code if the expression is False.
name = "Hasnain"
cast = "Siddique"
full_name = name + cast
if full_name == name.startswith("Has") or cast.startswith("Arain"):
    print("Person Authorized✅")
else :
    print("Unknown Person❌")
    
    
# ``while`` is a loop that executes some specified code as long as the expression is True.
is_student = True
student_class = 9 

while is_student:
    print("You are already admitted")
    if is_student or student_class >= 9:
        print("You are High School")
        break # I use break coz this stop the execution. if you accidently miss this so your while loop run infinitly when condition is true
    
    

# ``for`` is a loop that executes some specified code for each item in an iterable.
list_items = [23, 45, 67, 10, 50]
for i in list_items: 
    print(i)


# ``continue`` is a statement that skips the current iteration of the loop and continues to the next iteration.
for i in list_items:
    if i == 5:
        print(2)
    continue




# def giaic ():
#     print("Hello world from giaic!")

# # string (str)
# first_name:str = "Muhammad"
# last_name:str = "Hasnain!"
# print(f"My name is {first_name + ' ' + last_name}")

# # integer (int)
# num1 = 45
# num2 = 20
# sum = num1 + num2
# print("The sum of the num", sum) 

# # float (float)

# a = 2.7
# b= 22.1

# print(a + b)

# # boolean (bool)
# is_true = True
# is_false = False

# # list (list)
# fruit:list[str] = ["Apple", "Banana", "Cherry"]
# print(fruit[0:2])

# # set (set)
# set_data:set = {"apple", "banana", "cherry"}

# # dictionary (dict)
# dict_data:dict = {
#     "name": "hasnain",
#     "father_name": "aqeel",
    
# }

# print(dict_data) # output {'name': 'hasnain', 'father_name': 'aqeel'}
# # None (NoneType)
# is_none = None # tyoe of None is NoneType
# print(is_none) # None

# # frozen set (frozenset)
# frezon_set = frozenset({"apple", "banana", "cherry"})
# print(frezon_set) # frozenset({'banana', 'apple', 'cherry'})