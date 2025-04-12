# Learning python operators

# 1. Arithmetic Operators
add = 5 + 3
print(add) # => 8
subtract = 10 - 4
print(subtract) # => 6
mul = 6 * 2
print(mul) # => 12
divide = 10 / 2
print(divide) # => 5.0
floor_divide = 10 // 3
print(floor_divide) # => 3
modulus = 10 % 3
print(modulus) # => 1
exponential = 2 ** 3
print(exponential) # => 8

print("-------------------------------------------------")

# 2. Comparison Operator
equal_to = 5 == 5
print(equal_to) # => True 
not_equal_to = 5 != 3
print(not_equal_to) # => False
greater = 6 > 4
print(greater) # => True
less = 3 < 7
print(greater) # => True
greater_equal_to = 6 >= 6
print(greater_equal_to) # => True
greater_equal_to = 5 <= 8
print(greater_equal_to) # => True

print("-------------------------------------------------")

# 3. Logical Operators
and_condition = (5 > 2 and 4 > 1)
print(and_condition) # => True
or_condition = (5 > 2 or 4 < 1)
print(or_condition) # => True
or_condition = not(5 > 2)
print(or_condition) # => False


print("-------------------------------------------------")

# 4. Identity Operators
x = 4
y = 4
print(x is y) # => True
x = 4
y = 4
print(x is not y) # => False

print("-------------------------------------------------")

# 5. Membership Operators
list_of_num = [1,2,3]
print(3 in list_of_num)
list_of_num_not = [1,2,4]
print(3 not in list_of_num_not)


print("-------------------------------------------------")

# 6. Bitwise Operators
a = 5  # 0101 in binary
b = 3  # 0011 in binary

print(a & b)  # AND -> 0001 -> 1
print(a | b)  # OR  -> 0111 -> 7
print(a ^ b)  # XOR -> 0110 -> 6


# 7. Assignments Operators
x = 10
x += 5  # x = x + 5 -> 15
x &= 7  # x = x & 7 -> 15 & 7 -> 0111 -> 7
x |= 2  # x = x | 2 -> 0111 | 0010 -> 0111 -> 7
x ^= 4  # x = x ^ 4 -> 0111 ^ 0100 -> 0011 -> 3
x <<= 1 # x = x << 1 -> 0110 -> 6
x >>= 2 # x = x >> 2 -> 0001 -> 1
print(x)  # Output: 1
