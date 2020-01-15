class Vector2f():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector2f(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vector2f(self.x - other.x, self.y - other.y)
        
    def __len__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
        
    def __eq__(self, other):
        if other is None:
            return False
        return self.x == other.x and self.y == other.y
        
    def __hash__(self):
        return hash(self.__str__())
        
    def __str__(self):
        return f'({self.x}; {self.y})'
        
    def __repr__(self):
        return f'Vector2f({self.x}, {self.y})'

    def normalize(self):
        newx = 0 if self.x == 0 else self.x / abs(self.x)
        newy = 0 if self.y == 0 else self.y / abs(self.y)
        return Vector2f(newx, newy)

    def scalar_mult(self, scalar):
        return Vector2f(self.x * scalar, self.y * scalar)


Vector2f.DESTROY = Vector2f(-1, -1)
