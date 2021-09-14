def strange_zoo():
    tail, body, head = input(), input(), input()
    meerkat = [tail, body, head]
    meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
    print(meerkat)


# strange_zoo()


def courses():
    my_list = []
    for each_time in range(int(input())):
        my_list.append(input())
    print(my_list)


# courses()


def list_statistics():
    positive_list = []
    negative_list = []

    for each_time in range(int(input())):
        num = int(input())
        if num >= 0:
            positive_list.append(num)
        else:
            negative_list.append(num)

    print(positive_list)
    print(negative_list)
    print(f"Count of positives: {len(positive_list)}")
    print(f"Sum of negatives: {sum(negative_list)}")


# list_statistics()


def search():
    num = int(input())
    word = input()
    list_words = []
    filtered_words = []

    for each_time in range(num):
        sentence = input()
        list_words.append(sentence)
        if word in sentence:
            filtered_words.append(sentence)

    print(list_words)
    print(filtered_words)


# search()


def number_filter():
    nums = []
    for each_time in range(int(input())):
        nums.append(int(input()))
    command = input()
    if command == "even":
        print([num for num in nums if num % 2 == 0])
    elif command == "odd":
        print([num for num in nums if num % 2 != 0])
    elif command == "negative":
        print([num for num in nums if num < 0])
    elif command == "positive":
        print([num for num in nums if num >= 0])


# number_filter()
