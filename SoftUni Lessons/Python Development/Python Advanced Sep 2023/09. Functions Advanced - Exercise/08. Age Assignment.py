def age_assignment(*args, **kwargs):
    names = {arg: 0 for arg in args}

    for letter, age in kwargs.items():
        for name in names.keys():
            if name[0] == letter:
                names[name] = age

    for_print = ""

    for name, age in sorted(names.items(), key=lambda x: x[0]):
        for_print += f"{name} is {age} years old.\n"

    return for_print


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))