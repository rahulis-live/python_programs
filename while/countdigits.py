# Count the number of digits in a number

# Get number input
num = int(input("Enter a number: "))
num = abs(num)
count = len(str(num))

print(f"Number of digits: {count}")
