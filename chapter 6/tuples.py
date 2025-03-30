tuple1: tuple = tuple(["apple", "banana", "cherry"]) # cast a list into tuple
tuple2: tuple = (10, 20, 30) # tuple
mixed_tuple: tuple = ("hello", 42, 3.14, True) # tuple
print("tuple1      =", tuple1)
print("tuple2      =", tuple2)
print("mixed_tuple =", mixed_tuple)


tuple_1: tuple = (10, 20, 30) # tuple
tuple_2: tuple = (10, 20, 30) # tuple

print("id(tuple_1) = ", id(tuple_1)) # unique memory address
print("id(tuple_2) = ", id(tuple_2)) # unique memory address

print("tuple_1 == tuple_2 = ", tuple_1 == tuple_2) # comparing by value


# tuples are immutable