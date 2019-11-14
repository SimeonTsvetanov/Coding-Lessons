width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())

total_free_space = width_free_space * length_free_space * height_free_space
used_space = 0

while True:
    count_boxes = input()
    if count_boxes == "Done":
        break
    count_boxes = int(count_boxes)
    used_space += count_boxes
    if used_space >= total_free_space:
        break

if used_space < total_free_space:
    print(f"{total_free_space - used_space} Cubic meters left.")
else:
    print(f"No more free space! You need {used_space - total_free_space} Cubic meters more.")


