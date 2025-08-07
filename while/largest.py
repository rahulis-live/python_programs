# largest among n numbers
n  = int(input("Enter the total number : "))
largest = 0

for i in range(n):
   i  = int(input())
   if i >  largest :
       largest = i
print(largest)       