class Calculator(object):

    def validate_input(self, x, y):
        number_types = (int, long, float, complex)
        return isinstance(x, number_types) and isinstance(y, number_types)

    def add(self, x, y):
        if self.validate_input(x, y): return x + y
        else: raise ValueError

    def subtract(self, x, y):
        if self.validate_input(x, y): return x - y
        else: raise ValueError

    def divide(self, x, y):
        if self.validate_input(x, y): return x // y
        else: raise ValueError

    def multiply(self, x, y):
        if self.validate_input(x, y): return x * y
        else: raise ValueError
