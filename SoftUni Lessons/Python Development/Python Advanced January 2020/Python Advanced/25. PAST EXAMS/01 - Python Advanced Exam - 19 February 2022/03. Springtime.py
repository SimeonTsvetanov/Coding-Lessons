def start_spring(**data):
    result = ''
    dictionary = {}
    for value, key in data.items():
        if key not in dictionary:
            dictionary[key] = []
        dictionary[key].append(value)
    for key, values in sorted(dictionary.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f"{key}:\n"
        for value in sorted(values):
            result += f"-{value}\n"
    return result.strip()


# example_objects = {
#     "Water Lilly": "flower",
#     "Swifts": "bird",
#     "Callery Pear": "tree",
#     "Swallows": "bird",
#     "Dahlia": "flower",
#     "Tulip": "flower"
#     }
# print(start_spring(**example_objects))

# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

