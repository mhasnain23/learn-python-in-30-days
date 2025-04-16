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
