import numpy as np


arr = np.arange(10)
print("Array ban đầu:", arr)
print("Kiểu dữ liệu của arr:", arr.dtype)
print("Kích thước của arr:", arr.shape)


arr_odd = arr[arr % 2 != 0]
arr_even = arr[arr % 2 == 0]
print("Array các phần tử lẻ:", arr_odd)
print("Array các phần tử chẵn:", arr_even)


arr_update_1 = np.where(arr % 2 == 0, arr, 100.23)
print("Array sau khi cập nhật:", arr_update_1)
