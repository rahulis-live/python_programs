#write a program to find the sum of digits in a single unit

n =int(input("Enter a number: "))
s= 0
while n!=0:
    r = n % 10
    s+=r
    n//=10
    if s > 9 and n == 0:
        n = s
        s = 0
       
print(f"sum of digits in a single unit is :{s}")
