import math
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return math.sqrt(sum(coordinates_squared))

    def normalize(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal('1.0')/magnitude)
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dot_product(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalize()
            u2 = v.normalize()
            angle_in_radians = acos(u1.dot(u2))

            if (in_degrees):
                degrees_per_radian = 180. / pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot comoute an angle with the zero vector')
            else:
                raise e


'''
v = Vector([-0.221, 7.437])
print "1 - %s" %v.magnitude()

v1 = Vector([8.813, -1.331, -6.247])
print "2 - %s" % v1.magnitude()

v2 = Vector([5.581, -2.136])
print "3 - %s" % v2.normalize()

v3 = Vector([1.996, 3.108, -4.554])
print "4 - %s" % v3.normalize()
'''
v = Vector([7.887, 4.138])
print "1 - %s" % v.dot_product(Vector([-8.802, 6.776]))

v2 = Vector([-5.955, -4.904, -1.874])
print "2 - %s" % v2.dot_product(Vector([-4.496, -8.755, 7.103]))

v3 = Vector([3.183, -7.627])
print "3 - %s" % v3.angle_with(Vector([-2.668, 5.319]))

