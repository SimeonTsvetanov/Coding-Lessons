full_line = ""
new_list = []
while True:
    data = input()
    if data == "DEBUG":
        break

    full_line += data
    full_line_list = [item for item in full_line.split("32656 19759 32763") if item != ""]
    for line in full_line_list:
        new_list = [int(item) for item in line.split(" ") if item != ""]
        print(new_list)
        count_letters = new_list[1]

print(new_list)

