#Count the Number of Vowels in a String


n = input("Enter the string : ")
s = "aeiouAEIOU"
count = 0

for i in n:
    if i in s:
        count+=1
        
print(count)
