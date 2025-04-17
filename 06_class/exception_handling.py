# the try block


try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except:
    print("An error occurred!")


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


print("------------------------------------------------------")


def divide_numbers(a, b):
    try:
        result = a / b  # Test this block for errors
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Invalid input type. Numbers required.")
    else:
        print(f"Division successful. Result: {result}")
    finally:
        print("Operation complete.\n")


# Test cases
divide_numbers(10, 2)  # Successful division
divide_numbers(10, 0)  # ZeroDivisionError
divide_numbers(10, "2")  # TypeError


try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("Error: Invalid input. Please enter numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"The result is: {result}")
finally:
    print("Thank you for using the program!")


print("--------------------------------------------------")
class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""

    pass


def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    return f"{n} is positive"


try:
    print(check_positive(-5))  # Raises NegativeNumberError
except NegativeNumberError as e:
    print(
        f"Custom Exception Caught: {e}", " - Exception Class Type: ", type(e)
    )  # Output: Custom Exception Caught: Negative numbers are not allowed!



try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("Error: Invalid input. Please enter numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"The result is: {result}")
finally:
    print("Thank you for using the program!")