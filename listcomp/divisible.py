# Numbers divisible by 3 and 5 between 1 to 100 using list comprehension


b = [i for i in range(1,101) if i % 3 == 0 and i & 5 == 0]
print(b)