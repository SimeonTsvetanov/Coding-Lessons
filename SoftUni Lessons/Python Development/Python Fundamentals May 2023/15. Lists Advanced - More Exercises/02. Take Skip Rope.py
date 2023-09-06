string = input()

nums = [int(num) for num in string if num.isdigit()]
not_nums = [element for element in string if not element.isdigit()]

take_list = [nums[i] for i in range(0, len(nums)) if i % 2 == 0]
skip_list = [nums[i] for i in range(0, len(nums)) if i % 2 != 0]

result = []

for i in range(len(take_list)):
    result += not_nums[0:take_list[i]]
    not_nums = not_nums[take_list[i] + skip_list[i]:]

print(''.join(result))
