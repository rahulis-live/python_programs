# Count occurrences of 50

t = (10, 50, 20, 50, 30, 50)
target = 50
count = 0

for i in t:
    if i == target:
        count += 1

print("Number of times 50 appears:", count)
