class Color():

    def __init__(self, color_name):
        self.color_name = color_name

    def __str__(self):
        return self.color_name

    def __eq__(self, other):
        return self.color_name == other.color_name


# default constants
Color.WHITE = Color("white")
Color.BLACK = Color("black")
