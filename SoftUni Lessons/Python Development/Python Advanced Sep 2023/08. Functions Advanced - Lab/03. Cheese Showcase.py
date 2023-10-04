# White a function called sorting_cheeses that receives keywords arguments:
# •	The key represents the name of the cheese
# •	The value is a list of quantities (integers) of the pieces of the given cheese


def sorting_cheeses(**kwargs):
    result = ''
    for key, value in sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f"{key}\n"
        for pieces in sorted(value, reverse=True):
            result += f"{pieces}\n"
    return result.strip()


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
