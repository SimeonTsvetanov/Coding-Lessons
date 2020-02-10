from os import remove


def file_manipulator():
    """
    Create a program that will receive commands until the command "End". The commands can be:
    - Create, - Add, - Replace, - Delete:
    :return: Modified text file.
    """
    while True:
        command = input().split("-")
        if command[0] == "End":
            print("Solved by Simeon Tsvetanov")
            break
        elif command[0] == "Create":
            create(file_name=command[1])
        elif command[0] == "Add":
            add(file_name=command[1], content=command[2])
        elif command[0] == "Replace":
            replace(file_name=command[1], old_string=command[2], new_string=command[3])
        elif command[0] == "Delete":
            delete(file_name=command[1])


def create(file_name: str):
    """
    Create-{file_name}" - Creates the given file with an empty content.
    If the file already exists, remove the existing text in it (as if the file is created again)
    :param file_name: The name of the file we want to create.
    :return: New Empty file with the name given.
    """
    # Using "with open" so that it will close it self automatically:
    with open(file_name, "w") as file:
        pass
    # Second Option is to use "OPEN" only:
    # new_file = open(file_name, 'w')
    # new_file.close()


def add(file_name: str, content: str):
    """
    Add-{file_name}-{content}" - Append the content and a new line after it.
    If the file does not exist, create it and add the content
    :param file_name: The file we want to append text to
    :param content: The text we want to append
    :return: Appending text to the file
    """
    # Using "with open" so that it will close it self automatically:
    with open(file_name, "a") as file:
        file.write(f"{content}\n")

    # Second Option is to use "OPEN" only:
    # file = open(file_name, 'a')
    # file.write(f"{content}\n")
    # file.close()


def replace(file_name: str, old_string: str, new_string: str):
    """
    Replace-{file_name}-{old_string}-{new_string}"
    Open the file and replace all the occurrences of the old string with the new string.
    If the file does not exist, print: "An error occurred"
    :param file_name: The file to be opened
    :param old_string: The text we want to Replace
    :param new_string: The new text
    :return: New File on top of the old but with changes.
    """
    try:  # Replacing only if the file exists. Otherwise: look at the except rule!
        with open(file_name, "r") as file:  # Using mode: "r" so we can check if the file exist
            file_data = file.read()
            new_file_data = file_data.replace(old_string, new_string)
            with open(file_name, "w") as new_file:  # Creating the new file and adding the new data in it.
                new_file.write(new_file_data)
    except FileNotFoundError:
        print(f"An error occurred")


def delete(file_name: str):
    """
    Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred
    :param file_name: The name of the file we want to delete
    :return: Just Delete the file.
    """
    try:
        remove(file_name)
    except FileNotFoundError:
        print(f"An error occurred")


if __name__ == '__main__':
    file_manipulator()
