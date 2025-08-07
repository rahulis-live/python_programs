import numpy as np

#to creates an array
# arr = np.array([1,2,3,4])
# print(f"array is : {arr}")

# #array operations
# print("Multiplied by 2:", arr * 2)
# print("sum is:", np.sum(arr))


matrix = np.array([[1,2], [3,4]])
arr2=matrix[:2,::2]
print(arr2)
print("2D array is\n: ",matrix)
