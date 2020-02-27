from pyfiglet import figlet_format
from termcolor import colored


def print_art(message):
    # text = figlet_format("Python", font="isometric1")
    ascii_art = figlet_format(message)
    print(ascii_art)


if __name__ == '__main__':
    print_art(input())
