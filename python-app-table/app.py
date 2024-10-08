# Function to print the multiplication table of 2
def print_table_of_2():
    number = 2
    print(f"Multiplication Table of {number}:")
    for i in range(1, 11):  # Loop through numbers 1 to 10
        print(f"{number} x {i} = {number * i}")

# Call the function to print the table
print_table_of_2()

