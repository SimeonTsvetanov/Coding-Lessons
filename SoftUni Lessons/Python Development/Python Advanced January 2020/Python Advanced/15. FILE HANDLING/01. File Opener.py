def work_at_home_file_opener():
    try:
        file = open('text.txt')
        print('File found')
    except FileNotFoundError:
        print('File not found')


def work_in_class_file_opener():
    file_path = 'files\\text.txt'
    try:
        open(file_path)
        print('File found')
    except FileNotFoundError as ex:
        print(ex)


if __name__ == '__main__':
    # work_at_home_file_opener()
    work_in_class_file_opener()

