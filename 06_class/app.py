import math
import mymodule
import requests
import random
from typing import Tuple, List, Dict

print(math.sqrt(25))  # Output: 5.0

print("added two numbers")
print(mymodule.add(5, 3))  # Output: 8

# like we have third party library reqests, numpy, pandas etc.
response = requests.get("https://www.asharib.xyz/api/profile")
print(response.status_code)  # Output: {'name': 'Asharib', 'age': 25, ...}

# Functions defined in built-in modules
print(random.random())


print("This is a simple function")


def greetings():
    "This is docstring of greetings function"
    greet = "Hello World!"
    return greet


message = greetings()
print(message)


def greetingsName(name):
    "This is docstring of greetings function"
    print("Hello {}".format(name))
    return


greetingsName("Ali")
greetingsName("Omar")
greetingsName("Usman")

print("---------------------------------------")


def add(x: int, y: int = 0) -> float:
    return float(x + y)


print(float(add(10, 20)))
print(add(y=50.0, x=2.0))  # type hints are not enforced in Python

print(add(x=5))


def my_sum(*nums):
    print(type(nums), ",", nums)

    return sum(nums)


print("Sum   =", my_sum(1, 2, 3, 4, 5, 8, 5), "\n")
print("Sum   *[] =", my_sum(*[1, 2, 3, 4, 5, 8, 5]), "\n")
print("Sum   *() =", my_sum(*(1, 2, 3, 4, 5, 8, 5)), "\n")


def add(x, y):
    z = x + y
    return z


a = 10
b = 20
result = add(a, b)

print("a = {} b = {} a+b = {}".format(a, b, result))


# Function to calculate the factorial of a number using recursion
def factorial(n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120


def example_function(a: int, b: int = 0, *args: float, **kwargs: str) -> Tuple[int, List[float], Dict[str, str]]:
    """Example function demonstrating various parameter types.
    Args:
        a: An integer.
        b: An integer with a default value of 0.
        *args: Variable-length positional arguments of type float.
        **kwargs: Variable-length keyword arguments of type string.
    Returns:
        A tuple containing:
        - The sum of 'a' and 'b'.
        - A list of the variable-length positional arguments ('args').
        - A dictionary of the variable-length keyword arguments ('kwargs').
    """
    sum_ab = a + b
    args_list = list(args)  # Convert tuple to a list
    return sum_ab, args_list, kwargs

# Example usage
result = example_function(1, 2, 3.14, 2.71, name="Alice", city="New York")
print(result)

result = example_function(10, *[1.0, 2.0, 3.0], **{"country": "USA", "language": "English"})
result