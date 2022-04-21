def reverse_text(text):
    for letter in text[::-1]:
        yield letter


for char in reverse_text("step"):
    print(char, end='')
