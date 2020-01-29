def to_string(text_list):
    return ''.join(text_list)


def permute(aa, ll, rr):
    if ll == rr:
        print(to_string(aa))
    else:
        for i in range(ll, rr + 1):
            aa[ll], aa[i] = aa[i], aa[ll]
            permute(aa, ll + 1, rr)
            a[ll], a[i] = a[i], a[ll]  # backtrack


string = input()
n = len(string)
a = list(string)
permute(a, 0, n - 1)


