while True:
    command = input()
    if command == "stop playing":
        break

    nums = [int(i) for i in command.split(" ")if i != ""]

    unique = len(set(nums)) == len(nums)
    if unique:
        edited_unique_nums = []
        for num in nums:
            if num.__index__() % 2 == 0:
                edited_unique_nums += [num + 2]
            else:
                edited_unique_nums += [num]
        edited_unique_nums.sort()
        print("Unique list: ", end="")
        print(",".join(str(item) for item in edited_unique_nums))
        print(f"Output: {(sum(edited_unique_nums) / len(edited_unique_nums)):.2f}")

    else:
        edited_non_unique_nums = []
        for num in nums:
            if not num % 2 == 0:
                edited_non_unique_nums += [num + 3]
            else:
                edited_non_unique_nums += [num]
        edited_non_unique_nums.sort()
        print("Non-unique list: ", end="")
        print(":".join(str(item) for item in edited_non_unique_nums))
        print(f"Output: {(sum(edited_non_unique_nums) / len(edited_non_unique_nums)):.2f}")
