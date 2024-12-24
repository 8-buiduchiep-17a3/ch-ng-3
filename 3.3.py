import numpy as np


arr_a = [1, 2, 3, 2, 3, 4, 3, 4, 5, 6]
arr_b = [7, 2, 10, 2, 7, 4, 9, 4, 9, 8]


arr_c = list(set(arr_a) & set(arr_b))


arr_d = list(set(arr_a) - set(arr_b))

arr_e = np.array([2, 6, 1, 9, 10, 3, 27, 8, 6, 25, 16])
arr_f = arr_e[(arr_e >= 5) & (arr_e <= 10)]

arr_c, arr_d, arr_f
