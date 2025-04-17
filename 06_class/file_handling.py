file = open("new_file.txt", "w")

file.write("Hello, world!\n")  # \n creates a new line
file.write("This is another line.\n")
file.close()


lines = ["Line 1: Karachi\n", "Line 2: Lahore\n", "Line 3: Peshawar\n"]
file = open("my_file.txt", "a")  # run with mode w, and see the result
file.writelines(lines)
file.close()


file = open("my_file.txt", "r")
content = file.read()
# print(content)

file.seek(0)  # First move the pointer to the start

lines = file.readlines()
for line in lines:
    print(line)
    
    
try:
    with open('unique.txt', 'x') as file:
        # file.write('Created exclusively!')
        print("File created successfully!")
except FileExistsError:
    print("File already exists.")


print("--------------------------------------------------")

with open("new_file.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed here


def copy_file(source_path, destination_path):
    try:
        with open(source_path, "r") as source_file, open(destination_path, "w") as dest_file:
            for line in source_file:
                dest_file.write(line)
        print(f"File '{source_path}' copied to '{destination_path}' successfully.")
    except FileNotFoundError:
        print(f"Error: Source file '{source_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

copy_file("unique.txt", "unique_copy.txt")


# Create and write to a file
with open('demo.txt', 'w') as file:
    file.write('Python File Handling\n')
    file.write('Line 1\nLine 2\n')

# Read and print content
with open('demo.txt', 'r') as file:
    print("Content:")
    print(file.read())

# Append a new line
with open('demo.txt', 'a') as file:
    file.write('Appended line\n')

# Read lines using seek
with open('demo.txt', 'r+') as file:
    file.seek(0)
    print("First line:", file.readline())