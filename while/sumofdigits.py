#program to find the sum of disits of a number

n =input("Enter a number: ")
s = 0
length = len(n)

for i in range(0,length):
    s += int(n[i])
    
print(f"sum of digits is :{s}")