def concatenate(*args, **kwargs):
    arguments = ''.join(args)
    for key, value in kwargs.items():
        if key in arguments:
            arguments = arguments.replace(key, value)
    return arguments


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
