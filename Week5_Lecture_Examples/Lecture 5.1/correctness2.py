"""Good Practice: Use built-in property decorator for more protection"""
class Square(object):
    def __init__(self, length):
        self._length = length

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @length.deleter
    def length(self):
        del self._length

print(Square.mro())
