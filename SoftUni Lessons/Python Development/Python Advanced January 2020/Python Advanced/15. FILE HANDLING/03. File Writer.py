def work_at_home_file_writer():
    file = open('my_first_file.txt', 'w')
    file.write("'I just created my first file!'\n")
    file.close()


def work_in_class_file_writer():
    file_path = "my_first_file.txt"
    text = "I just created my first file!"
    # TODO TO add the rest of the code later.


if __name__ == '__main__':
    # work_at_home_file_writer()
    work_in_class_file_writer()

