n = int(input())
rest = 0
for i in range(1111, 10000):
    k = i % 10
    rest = i / 10
    m = int(rest % 10)
    rest = rest / 10
    ll = int(rest % 10)
    rest = rest / 10
    o = int(rest % 10)
    if o != 0 and ll != 0 and m != 0 and k != 0:
        if n % o == 0 and n % ll == 0 and n % m == 0 and n % k == 0:
            print(f"{o}{ll}{m}{k}", end=" ")

