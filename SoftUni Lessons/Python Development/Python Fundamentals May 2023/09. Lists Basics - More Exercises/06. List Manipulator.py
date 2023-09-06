nums = [int(n) for n in input().split(' ')]

while True:
    command = input().split(' ')
    if command[0] == 'end':
        print(nums)
        break

    # EXCHANGE
    elif command[0] == 'exchange':
        index = int(command[1])
        if 0 <= index < len(nums):
            nums = nums[index + 1:] + nums[:index + 1]
        else:
            print(f"Invalid index")

    # MIN / MAX / EVEN / ODD
    elif command[0] == 'max':
        if command[1] == 'even':
            try:
                print(len(nums) - 1 - nums[::-1].index(max([el for el in nums if el % 2 == 0])))
            except ValueError:
                print(f"No matches")
        elif command[1] == 'odd':
            try:
                print(len(nums) - 1 - nums[::-1].index(max([el for el in nums if el % 2 != 0])))
            except ValueError:
                print(f"No matches")
    elif command[0] == 'min':
        if command[1] == 'even':
            try:
                print(len(nums) - 1 - nums[::-1].index(min([el for el in nums if el % 2 == 0])))
            except ValueError:
                print(f"No matches")
        elif command[1] == 'odd':
            try:
                print(len(nums) - 1 - nums[::-1].index(min([el for el in nums if el % 2 != 0])))
            except ValueError:
                print(f"No matches")

    # FIRST {count} even/odd
    elif command[0] == 'first':
        count = int(command[1])
        if count > len(nums):
            print(f"Invalid count")
            continue
        if command[2] == 'even':
            print([n for n in nums if n % 2 == 0][:count])
        elif command[2] == 'odd':
            print([n for n in nums if n % 2 != 0][:count])

    # LAST {count} even/odd
    elif command[0] == 'last':
        count = int(command[1])
        if count > len(nums):
            print(f"Invalid count")
            continue
        if command[2] == 'even':
            print([n for n in nums if n % 2 == 0][::-1][:count][::-1])
        elif command[2] == 'odd':
            print([n for n in nums if n % 2 != 0][::-1][:count][::-1])
