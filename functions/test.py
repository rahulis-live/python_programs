

#arbitrary arguments = to add n number of elements
def sum(*a):
    s = 0
    for i in a:
        s+=i
    return s    


print(sum(1,2,3,4))

#arbitrary ket arguements = to add and display key value element
def demo(**s):
    return s
print(demo(name="rahul",age ='23'))
    