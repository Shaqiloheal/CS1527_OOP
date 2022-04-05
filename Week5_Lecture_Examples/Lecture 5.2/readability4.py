from collections import namedtuple

def get_name():
    name = namedtuple("name", ["first", "middle", "last"])
    return name("Warren", "Francis", "Spalding")

name = get_name()

# much easier to read
print(name.first, name.middle, name.last)  # Warren Francis Spalding
