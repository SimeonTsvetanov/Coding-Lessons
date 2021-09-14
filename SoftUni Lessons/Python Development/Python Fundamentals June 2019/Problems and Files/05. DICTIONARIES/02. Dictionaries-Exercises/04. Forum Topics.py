"""
Dictionaries - Exercises
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1088#3

SUPyF Dictionaries Exercises - 04. Forum Topics

Problem:
You have been tasked to store a few forum topics, and filter them by several given tags.
You will be given several input lines, containing data about topics in the following format:
{topic} -> {tag1, tag2, tag3...}
The topic and tags will be strings. They will NOT contain spaces or ‘-’, ‘>’ symbols.
If you receive an existing topic, you must add the new tags to it. There should be NO duplicate tags.
When you receive the command “filter”, you must end the input sequence. On the next line (after “filter”),
you will receive a sequence of tags, separated by a comma and a space. You must print ONLY those topics,
which contain all tags in the given sequence.
The topics must be printed in the following format:
{topic} | {#tag1, #tag2, …, #tagN}
NOTE: The tags have a number sign (‘#’) as a prefix.
EXAMPLES:
    INPUT <<<
HelloWorld -> hello, forum, topic
HelpWithHomework -> homework, forum, topic
filter
forum, topic
    OUTPUT >>>
HelloWorld | #hello, #forum, #topic
HelpWithHomework | #homework, #forum, #topic
    INPUT <<<
First -> this
First -> that
First -> who
Second -> this, what, why
First -> this
Third -> this, third
Third -> that
filter
that, this
    OUTPUT >>>
First | #this, #that, #who
Third | #this, #third, #that
"""

topics = {}

while True:
    command = input()
    if command == "filter":
        break
    a = [word for word in command.split(" -> ")]
    name = a[0]
    items = [word for word in a[1].split(", ")]
    if name not in topics.keys():
        topics[name] = []
        for item in items:
            if item not in topics[name]:
                topics[name] += [item]
    else:
        for item in items:
            if item not in topics[name]:
                topics[name].append(item)

tags = [tag for tag in input().split(", ")]

for topic, items in topics.items():
    if_all = len(tags)
    for item in tags:
        if item in items:
            if_all -= 1
    if if_all == 0:
        print(topic, end=" | ")
        print("#", end="")
        print(", #".join(items))


def another_solution():
    topics = {}

    while True:
        command = input().split(" -> ")
        if command[0] == "filter":
            break

        new_topic = command[0]
        new_tags = [word for word in command[1].split(", ")]

        if new_topic not in topics.keys():
            topics[new_topic] = new_tags
        else:
            for new_tag in new_tags:
                if new_tag not in topics[new_topic]:
                    topics[new_topic].append(new_tag)

    hot_tags = input().split(", ")

    for topic, tags in topics.items():
        if all(elem in tags for elem in hot_tags):
            print(f"{topic} | {', '.join([f'#{tag}' for tag in tags])}")


# another_solution()
