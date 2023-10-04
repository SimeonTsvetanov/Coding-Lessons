def rectangle(length, width):
    if not (isinstance(length, int) and isinstance(width, int)):
        return f"Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return 2 * (width + length)

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


print(rectangle(2, 10))
print(rectangle('2', 10))
