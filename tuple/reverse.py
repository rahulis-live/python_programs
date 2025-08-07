# reverse elements in tuple

l = (4,2,2)
l = list(l)
li= []
for i in range(len(l) - 1 , -1 , -1):
    li.append(l[i])
print(tuple(li))
