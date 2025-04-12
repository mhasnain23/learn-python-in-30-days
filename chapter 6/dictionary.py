
tuple1: tuple = tuple(["apple", "banana", "cherry"]) # cast a list into tuple
tuple2: tuple = (10, 20, 30) # tuple


# Using tuples as keys in dictionaries (because they are immutable)
my_dict = {tuple1: "This is a tuple key", tuple2: "Another tuple key"}
print("Dictionary with tuple keys:", my_dict)

# 
a: int = input ("Enter your name: ")
print(a, type(a) )

american_cities: dict = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
print(american_cities[0])



# Create a dictionary to store a person's details
person: dict = {
    "name": "Alice",
    "age": 25,
    "visited_cities": american_cities
}
print(person)


thisdict: dict = dict(name = "John", age = 36, country = "Norway") # It is also possible to use the dict() constructor to make a dictionary.
print(type(thisdict)," - ", thisdict, )

a: set = set()



