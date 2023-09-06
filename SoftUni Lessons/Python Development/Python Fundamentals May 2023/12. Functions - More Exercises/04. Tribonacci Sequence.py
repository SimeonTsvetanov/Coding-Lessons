def tribonacci_sequence(count):
    sequence = []

    num = 1

    for i in range(count):
        if len(sequence) <= 1:
            sequence.append(num)
        elif len(sequence) == 2:
            sequence.append(num + num)
        else:
            sequence.append(sum(sequence[-3:]))
    print(' '.join([str(s) for s in sequence]))


tribonacci_sequence(int(input()))
