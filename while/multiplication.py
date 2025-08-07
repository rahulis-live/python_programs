# program to write the multiplication of a anumber

n = int(input("Enter the number: "))

for i in range(1,n + 1):
    print(f"Multiplication Table of {i} is :")
    for j in range(1,11):
        print(f"{j} * {i} = {i*j}")
    