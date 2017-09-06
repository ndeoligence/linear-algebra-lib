from math import sqrt
from functools import reduce


def test():
    vectors = [
        Vector([-0.221, 7.437]),
        Vector([5.581, -2.136]),
        Vector([8.813, -1.331, -6.247]),
        Vector([1.996, 3.108, -4.554]),
    ]
    for v in vectors:
        print(f'v = {v}')
        # print(f'\tabs(v) = {v.abs()}')
        # print(f'\tnormal(v) = {v.normal()}')
        print(f'\tVs zero = {v.zero()}')
        print(f'\tv is zero? = {v.isZero()}')


class Vector(object):
    def __init__(self, coordinates):
        assert (isinstance(coordinates, list))
        self.coordinates = tuple(coordinates)
        self.dim = len(coordinates)

    def __str__(self):
        return f'Vector: {self.coordinates}'

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def __add__(self, other):
        assert (self.dim == other.dim)
        return Vector([x+y for x, y in zip(self.coordinates, other.coordinates)])

    def __sub__(self, other):
        assert (self.dim == other.dim)
        return Vector([x - y for x, y in zip(self.coordinates, other.coordinates)])

    def __rmul__(self, x):
        return [x*e for e in self.coordinates]

    def dot(self, other):
        assert (len(self.coordinates) == len(other.coordinates))
        prod = 0
        for i in range(0, len(self.coordinates)):
            prod += self.coordinates[i] * other.coordinates[i]
        return prod

    def abs(self):
        return sqrt(reduce(lambda x, y: x+y, [x**2 for x in self.coordinates]))

    def normal(self):
        if self.isZero():
            return None
        return 1/self.abs() * self

    def isZero(self):
        return self == self.zero()

    def zero(self):
        return Vector([0 for i in range(self.dim)])


if __name__=='__main__':
    test()
