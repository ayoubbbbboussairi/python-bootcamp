import re

# Open the file
filename = 'C:/Users/user/Desktop/python_bootcamp/test/data.txt'

with open(filename, "r") as file:
    # Read the content of the file
    file_content = file.read()

    # Use re.findall() to find all integers in the text
    numbers = re.findall('[0-9]+', file_content)

    # Convert each string to an integer and sum them up
    sum_of_numbers = sum(map(int, numbers))

    # Print the result
    print("Sum:", sum_of_numbers)
