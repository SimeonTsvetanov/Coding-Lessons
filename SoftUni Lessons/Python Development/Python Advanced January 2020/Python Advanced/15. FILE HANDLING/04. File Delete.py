import os


def work_at_home_file_delete():
    try:
        os.remove("my_first_file.txt")
    except FileNotFoundError:
        print('File already deleted!')


def work_in_class_file_delete():
    #  TODO - add the code when the teacher uploads it.
    pass


if __name__ == '__main__':
    # work_at_home_file_delete()
    work_in_class_file_delete()

