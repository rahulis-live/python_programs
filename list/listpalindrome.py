# Check If List is Palindrome

l = [4,2,2,4]
li = []
for i in range(len(l) - 1 , -1 , -1):
    li.append(l[i])
print(li)

if li == l:
    print("palindrome")
else:
    print("not palindrome")        