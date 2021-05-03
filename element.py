import random


class Element:

    def __init__(self):
        self.set_X(self.random_number(0, 1000))
        self.set_Y(self.random_number(0, 1500))
        self.set_Height(self.random_number(0, 1000))
        self.set_Width(self.random_number(0, 1000))
     

    def set_X(self, x):
        self._x = x

    def set_Y(self, y):
        self._y = y

    def set_Height(self, height):
        self._height = height

    def set_Width(self, width):
        self._width = width

    def get_X(self):
        return self._x

    def get_Y(self):
        return self._y

    def get_Width(self):
        return self._width

    def get_Height(self):
        return self._height    

    def random_number(self, min, max):
        return random.randint(min, max)

    """
    Get x and y coordinates of the element
    """
    def position(self):
        return self.get_X(), self.get_Y()


    """
    Get height and width of the element
    """
    def size(self):
        return self.get_Height(), self.get_Width()
