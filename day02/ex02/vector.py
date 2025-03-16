class Vector:
    def __init__(self, values):
        if isinstance(values, list):
            self.values = values
            self.shape = self._calculate_shape()
        elif isinstance(values, int):
            self.values = [[float(i) for i in range(values)]]
            self.shape = (1, values)
        elif isinstance(values, tuple) and len(values) == 2:
            a, b = values
            if a > b:
                raise ValueError("Invalid range: start value must be less than or equal to end value")
            self.values = [[float(i) for i in range(a, b)]]
            self.shape = (1, b - a)
        else:
            raise ValueError("Invalid input for Vector initialization")

    def _calculate_shape(self):
        if len(self.values) == 1:
            return (1, len(self.values[0]))
        elif len(self.values[0]) == 1:
            return (len(self.values), 1)
        else:
            raise ValueError("Invalid vector shape")

    def dot(self, other):
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape for dot product")
        result = sum(x * y for x, y in zip(self.values[0], other.values[0]))
        return result

    def T(self):
        transposed_values = [[val] for val in self.values[0]]
        return Vector(transposed_values)

    def __repr__(self):
        return f"Vector({self.values})"

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape for addition")
        result_values = [[x + y for x, y in zip(self_row, other_row)] for self_row, other_row in zip(self.values, other.values)]
        return Vector(result_values)

    def __sub__(self, other):
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape for subtraction")
        result_values = [[x - y for x, y in zip(self_row, other_row)] for self_row, other_row in zip(self.values, other.values)]
        return Vector(result_values)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result_values = [[x * other for x in row] for row in self.values]
            return Vector(result_values)
        elif isinstance(other, Vector):
            raise NotImplementedError("Vector multiplication is not implemented")
        else:
            raise NotImplementedError("Unsupported operation")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Division by zero is undefined")
            result_values = [[x / other for x in row] for row in self.values]
            return Vector(result_values)
        elif isinstance(other, Vector):
            raise NotImplementedError("Vector division is not implemented")
        else:
            raise NotImplementedError("Unsupported operation")

    def __rtruediv__(self, other):
        raise NotImplementedError("Reverse division is not implemented")


        