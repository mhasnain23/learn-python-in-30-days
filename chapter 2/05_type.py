a = "31.2"
b = float(a) # a but the type should be float
c = int(b) # convert the float to int
d = str(c) # convert the int to str
t = type(a) # class <int>

# print(t)
print("String value", a, "and their type", type(a))
print("Converted to float", b, "and their type", type(b))
print("Converted to integer means number", c, "and their type", type(c))
print("Converted to Str means text form", d, "and their type", type(d))