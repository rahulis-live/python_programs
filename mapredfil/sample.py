from functools import reduce

l = [1,2,3,4]

square = list(map(lambda x: x ** 2 , l))
print(square)

odd= list(filter(lambda x: x % 2 == 0 , l))
print(odd)

sum = reduce(lambda x, y: x + y , l)
print(sum)
