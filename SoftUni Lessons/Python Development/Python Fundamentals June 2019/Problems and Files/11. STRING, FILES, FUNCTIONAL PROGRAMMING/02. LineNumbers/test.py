with open('input.txt', 'r') as file:
    counter = 1
    for line in file.readlines():
        with open("Output.txt", "a") as file_2:
            file_2.write(f"{counter}. ")
            file_2.write(line)
            counter += 1
