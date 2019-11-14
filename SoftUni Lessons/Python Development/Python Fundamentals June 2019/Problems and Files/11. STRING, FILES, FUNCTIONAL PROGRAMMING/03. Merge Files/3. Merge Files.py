with open('Input1.txt', 'r') as file_1:
    file_1_list = file_1.readlines()
with open('Input2.txt', 'r') as file_2:
    file_2_list = file_2.readlines()

merged = list(zip(file_1_list, file_2_list))
with open("nums_merged.txt", "a") as file:
    for el in merged:
        file.write(el[0])
        file.write(el[1])



