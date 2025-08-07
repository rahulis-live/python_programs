# Modify the tuple

t = (10, 20, 30)
temp = list(t)

temp[1] = 99  # Modify second element
t = tuple(temp)
print("Modified tuple:", t)
