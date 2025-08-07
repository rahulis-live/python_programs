n = int(input("List the prime numbers up to: "))

for i in range(2, n):  # Start from 2, since 1 is not prime
    isPrime = True
    for j in range(2, int(i ** 0.5) + 1):  # Check divisibility up to square root of i
        if i % j == 0:
            isPrime = False
            break
    if isPrime:     #when the above inner for loop gets false, the below if condition runs and goes to next outer for loop iteration   
        print(i)
