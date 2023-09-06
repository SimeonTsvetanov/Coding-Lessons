def palindrome_integers(nums):
    nums = [int(num) for num in nums.split(', ')]
    [print(str(num) == str(num)[::-1]) for num in nums]


palindrome_integers(input())
