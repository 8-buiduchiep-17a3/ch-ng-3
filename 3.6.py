import numpy as np


arr = np.full((3, 3), 'True')
print("Array 3x3 với giá trị 'True':")
print(arr)


arr_ID = np.array([0, 12345678])
arr_2D = arr_ID.reshape(1, -1)  
arr_2D = arr_2D[:, [0, 2, 1]]  
print("\nArray 2D sau khi hoán đổi cột 1 và cột 3:")
print(arr_2D)


arr_2D[[0, 1]] = arr_2D[[1, 0]] 
print("\nArray 2D sau khi hoán đổi dòng 1 và dòng 2:")
print(arr_2D)


arr_2D = arr_2D[::-1] 
print("\nArray 2D sau khi đảo ngược các dòng:")
print(arr_2D)


arr_2D = arr_2D[:, ::-1]  
print("\nArray 2D sau khi đảo ngược các cột:")
print(arr_2D)


arr_2D_null = np.array([[1, 2, 3], [np.NaN, 5, 6], [7, np.NaN, 9], [4, 5, 6]])
contains_null = np.isnan(arr_2D_null).any()  
print("\nArray 2D có chứa giá trị rỗng (NaN)?", contains_null)


arr_2D_null = np.nan_to_num(arr_2D_null, nan=0) 
print("\nArray 2D sau khi thay thế NaN bằng 0:")
print(arr_2D_null)
