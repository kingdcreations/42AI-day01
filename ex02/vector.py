class Vector():
    """docstring for Vector."""

    def __init__(self, arg):
        self.values = []
        if isinstance(arg, list):
            for x in arg:
                if not isinstance(x, float):
                    self.ft_exit("Vector values must only be floats")
            self.values = arg
        elif isinstance(arg, int):
            for x in range(0, arg, 1 if arg >= 0 else -1):
                self.values.append(float(x))
        elif isinstance(arg, range):
            for x in arg:
                self.values.append(float(x))
        elif isinstance(arg, tuple) and len(arg) == 2:
            for x in arg:
                if not isinstance(x, int):
                    self.ft_exit("Range musts only contain ints")
            for x in range(arg[0], arg[1], 1 if arg[0] < arg[1] else -1):
                self.values.append(float(x))
        else:
            self.ft_exit("Vector values must only be list, int or range")
        self.size = len(self.values)

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = (f"(Vector {self.values})")
        return txt

    def __repr__(self):
        txt = (f"{self.__class__.__name__}{self.values}")
        return txt

    def __add__(self, other):
        if isinstance(other, (int, float)):
            arr = Vector(self.size)
            for i in range(0, self.size):
                arr.values[i] = self.values[i] + other
            return arr
        elif isinstance(other, Vector) and self.size == other.size:
            arr = Vector(self.size)
            for i in range(0, self.size):
                arr.values[i] = self.values[i] + other.values[i]
            return arr
        else:
            self.ft_return("Must be two vector of the same size")

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            arr = Vector(self.size)
            for i in range(0, self.size):
                arr.values[i] = self.values[i] - other
            return arr
        elif isinstance(other, Vector) and self.size == other.size:
            arr = Vector(self.size)
            for i in range(0, self.size):
                arr.values[i] = self.values[i] - other.values[i]
            return arr
        else:
            self.ft_return("Must be two vector of the same size")

    def __rsub__(self, other):
        if isinstance(other, (Vector)):
            return other.__sub__(self)
        elif isinstance(other, (int, float)):
            arr = Vector(self.size)
            for i in range(0, self.size):
                arr.values[i] = other - self.values[i]
            return arr
        self.ft_return("Must be two vector of the same size")

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            arr = Vector(self.size)
            for i in range(0, self.size):
                arr.values[i] = self.values[i] * other
            return arr
        elif isinstance(other, Vector) and self.size == other.size:
            arr = Vector(self.size)
            end = 0
            for i in range(0, self.size):
                arr.values[i] = self.values[i] * other.values[i]
                end += arr.values[i]
            return end
        else:
            self.ft_return("Must be two vector of the same size")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if (other == 0):
            self.ft_return("Cannot divide by zero")
        elif isinstance(other, int) or isinstance(other, float):
            arr = Vector(self.size)
            for i in range(0, self.size):
                arr.values[i] = self.values[i] / other
            return arr
        else:
            self.ft_return("Must divide by int or float")

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)) and other != 0:
            return self.__mul__(1/other)
        self.ft_return("Must divide by a non zero scalar")

    def ft_exit(self, s):
        print(s)
        exit()

    def ft_return(self, s):
        print(s)
        return
