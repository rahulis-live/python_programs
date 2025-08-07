ll = int(input("Enter the lower limit : "))
ul = int(input("Enter the upper limit : "))
print("List the prime numbers from lower limit to upper limit : ")


for i in range(ll, ul):  # Start from 2, since 1 is not prime
    isPrime = True
    for j in range(2, int(i ** 0.5) + 1):  # Check divisibility up to square root of i
        if i % j == 0:
            isPrime = False
            break
    if isPrime:     #when the above inner for loop gets false, the below if condition runs and goes to next outer for loop iteration   
        print(i)
