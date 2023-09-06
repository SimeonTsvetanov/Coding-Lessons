def chars_in_range(a, b):
    a, b = sorted([ord(a), ord(b)])
    result = ''
    for i in range(a + 1, b):
        result += chr(i) + ' '
    return result


print(chars_in_range(input(), input()))
