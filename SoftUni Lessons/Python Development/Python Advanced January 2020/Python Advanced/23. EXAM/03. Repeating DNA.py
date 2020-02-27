def get_repeating_DNA(string):
    full_string = [sym for sym in string]
    sub_strings = []
    all_tens = []
    res = [string[i: j] for i in range(len(string))
           for j in range(i + 1, len(string) + 1)]
    for r in res:
        if len(r) == 10:
            all_tens.append(r)
    reps = []

    for str in all_tens:
        if all_tens.count(str) > 1:
            if str not in reps:
                reps.append(str)
    return reps


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)

