import numpy as np
import ast


baseball = []

with open('baseball_2D.txt', 'r', encoding='utf-8-sig') as file:  
    for line in file:
     
        baseball.append(ast.literal_eval(line.strip()))


np_baseball = np.array(baseball)


np_baseball = np.squeeze(np_baseball)

print(f"Kiểu dữ liệu của np_baseball: {np_baseball.dtype}")
print(f"Kích thước của np_baseball: {np_baseball.shape}")


print("\nCác giá trị của dòng thứ 50 trong np_baseball:")
print(np_baseball[49])  


np_weight = np_baseball[:, 1]
print("\nDữ liệu từ cột 2 (cân nặng):")
print(np_weight)


height_of_124th = np_baseball[123, 0] 
print(f"\nChiều cao của vận động viên thứ 124 là: {height_of_124th} inches")


average_height = np.mean(np_baseball[:, 0])
average_weight = np.mean(np_baseball[:, 1])
print(f"\nChiều cao trung bình: {average_height} inches")
print(f"Cân nặng trung bình: {average_weight} pounds")


correlation = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])[0, 1]
print(f"\nHệ số tương quan giữa chiều cao và cân nặng: {correlation}")

if correlation > 0:
    print("Mối tương quan giữa chiều cao và cân nặng là tương quan thuận.")
elif correlation < 0:
    print("Mối tương quan giữa chiều cao và cân nặng là tương quan nghịch.")
else:
    print("Chiều cao và cân nặng không có mối tương quan.")
