def fill_the_box(height, length, width, *args):
    box = height * length * width
    for cube in args:
        if cube == 'Finish':
            break
        box -= cube
    if box > 0:
        return f"There is free space in the box. You could put {box} more cubes."
    else:
        return f"No more free space! You have {abs(box)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(20 * '*')
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(20 * '*')
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
