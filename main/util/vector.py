class Vector2f():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector2f(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vector2f(self.x - other.x, self.y - other.y)
        
    def to_list(self):
        return [self.x, self.y]
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    def __hash__(self):
        return hash(f'{self.x}, {self.y}')