s= input("Enter the string: ")
o= ""
n = len(s)

for i in range(0,n):
    if i % 2 == 0:
        o+=s[i].upper()
    else:
         o+=s[i].lower()
print(o)        

