#program to find the factorial of a a number


# def fact(n):
#     if n == 0 or n ==1:
#         return 1
#     return n * fact(n - 1)
# n = int(input("enter the number"))
# print("factorial of a number is",fact(n))



n = int(input("enter the number"))
i =1
res = 1
while i <= n:
    res*= i
    i+=1
    
print("factorial of a number is",res)    