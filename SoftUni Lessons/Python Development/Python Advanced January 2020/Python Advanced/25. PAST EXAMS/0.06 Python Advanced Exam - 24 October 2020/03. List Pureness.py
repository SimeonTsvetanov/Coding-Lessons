# 40/100 in Judge I don't have time to bother with it now.

def best_list_pureness(nums: list, count: int):
    best = -11111111111111
    best_rotation = 0
    rotation = 0

    for _ in range(count):
        new_list = []
        for index in range(len(nums)):
            num = nums[index]
            new_list.append(num * index)
        if sum(new_list) > best:
            best = sum(new_list)
            best_rotation = rotation
        rotation += 1
        nums = nums[-1:] + nums[:-1]

    return f"Best pureness {best} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
