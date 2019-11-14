import math

length_hall = float(input())
width_hall = float(input())
side_bar = float(input())

total_size_hall = length_hall * width_hall

bar_size = side_bar * side_bar
dance_space = total_size_hall * 0.19

total_free_space = total_size_hall - bar_size - dance_space

people_space = total_free_space / 3.2

print(math.ceil(people_space))

