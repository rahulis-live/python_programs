#write a program to find count the number of digits in a number

n = int(input("Enter the number: "))
count = 0

while n > 0:
    n//=10
    count+= 1
print("count of digits in number is: ",count)    
    