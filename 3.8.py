import numpy as np
import pandas as pd


with open('heights.txt', 'r', encoding='utf-8-sig') as f:
    heights = [float(value.strip().replace(',', '.')) for line in f.readlines() for value in line.strip().split()]

with open('positions.txt', 'r') as f:
    positions = [line.strip() for line in f.readlines()]


print("Heights:", heights)
print("Positions:", positions)


np_positions = np.array(positions)
print("Kiểu dữ liệu của np_positions:", np_positions.dtype)


np_heights = np.array(heights)
print("Kiểu dữ liệu của np_heights:", np_heights.dtype)

gk_heights = np_heights[np_positions == 'GK']
average_gk_height = np.mean(gk_heights)
print("Chiều cao trung bình của các GK:", average_gk_height)


non_gk_heights = np_heights[np_positions != 'GK']
average_non_gk_height = np.mean(non_gk_heights)
print("Chiều cao trung bình của các vị trí khác:", average_non_gk_height)


data = {'position': positions, 'height': heights}
players_df = pd.DataFrame(data, dtype={'position': 'str', 'height': 'float'})
print("\nDữ liệu players:")
print(players_df)

sorted_players = players_df.sort_values(by='height', ascending=False)
highest_player = sorted_players.iloc[0]
lowest_player = sorted_players.iloc[-1]

print("\nVị trí có chiều cao cao nhất:", highest_player['position'], "với chiều cao:", highest_player['height'])
print("Vị trí có chiều cao thấp nhất:", lowest_player['position'], "với chiều cao:", lowest_player['height'])
