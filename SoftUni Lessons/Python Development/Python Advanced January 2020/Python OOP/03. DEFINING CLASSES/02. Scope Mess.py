"""
# This is from work at home:
x = "global"
def outer():
    global x
    x = "local"
    def inner():
        global x
        x = "nonlocal"
        print("inner:", x)
    def change_global():
        global x
        x = "global: changed!"
    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()
print(x)
outer()
print(x)
"""


# And this is the solution from work in class:
"""
We have learned quite a lot about the nonlocal and global functions.
Yet I didn't get the nonlocal quite a lot.
It's worth it to watch the video again in the future.
"""

x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)

"""
global
outer: local
inner: nonlocal
outer: nonlocal
global: changed!
"""
