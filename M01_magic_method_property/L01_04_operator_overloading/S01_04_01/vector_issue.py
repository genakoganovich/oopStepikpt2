class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Что должна сделать эта строка? Python не знает.
# result = v1 + v2  # TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'