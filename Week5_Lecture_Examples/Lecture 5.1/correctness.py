class Square(object):
    def __init__(self, length):
        self.length = length

r = Square(5)
print(r.length)  # 5
r.length = 6
area = r.length ** 2   # 36

print(area)