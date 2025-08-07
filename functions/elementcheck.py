# Check if a specific element is present in a list. If it is, print the element and its index position(s).
def elementswap(l,a,e):

    for i in range(l):
        if a[i] == e:
            print(f"element is {e},position is {i}")
    

l = int(input("Enter the total number of elements in the list: "))
print("Enter the Element: ")
a = []
for i in range(l):
    a.append(int(input()))
    
e = int(input("Enter the element to check: "))    
# print(a,e)  
        
        
elementswap(l,a,e)        