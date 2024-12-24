import numpy as np
with open('heights_1.txt', 'r', encoding='utf-8-sig') as file:
    height = list(map(int, file.read().strip().split(',')))
with open('weights_1.txt', 'r', encoding='utf-8-sig') as file:
    weight = list(map(int, file.read().strip().split(',')))

arr_height = np.array(height)
arr_weight = np.array(weight)
arr_height_m = arr_height * 0.0254
arr_weight_kg = arr_weight * 0.453592
arr_bmi = arr_weight_kg / (arr_height_m ** 2)
players_bmi_under_21 = arr_bmi[arr_bmi < 21]
print(f"Các cầu thủ có BMI < 21: {players_bmi_under_21}")
average_height = np.mean(arr_height_m)
average_weight = np.mean(arr_weight_kg)
print(f"Chiều cao trung bình: {average_height} m")
print(f"Cân nặng trung bình: {average_weight} kg")
max_height = np.max(arr_height_m)
max_weight = np.max(arr_weight_kg)
print(f"Chiều cao lớn nhất: {max_height} m")
print(f"Cân nặng lớn nhất: {max_weight} kg")
min_height = np.min(arr_height_m)
min_weight = np.min(arr_weight_kg)
print(f"Chiều cao nhỏ nhất: {min_height} m")
print(f"Cân nặng nhỏ nhất: {min_weight} kg")
