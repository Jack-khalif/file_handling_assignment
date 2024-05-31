# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is the first line.\n")
        file.write("The value of pi is approximately \[3.14159\].\n")
        file.write("The year is 2024.\n")
except PermissionError:
    print("Error: You do not have permission to create the file.")
except Exception as e:
    print(f"An error occurred: {e}")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file 'my_file.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This is the first appended line.\n")
        file.write("The second appended line contains the number \[42\].\n")
        file.write("The third appended line is the last one.\n")
except PermissionError:
    print("Error: You do not have permission to modify the file.")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("File operations completed.")
