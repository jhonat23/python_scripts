class Point(object):
    "Creation of point on a cartesian space (R2)"
    x = int
    y = int

    def __init__(self, x=0, y=0):
        "Constructor, must be numeric (int or float)"
        def is_number(value):
            "Check the attribute type, only int of float"
            return isinstance(value, (int, float))
        if is_number(x) and is_number(y):
            self.x = x
            self.y = y
        else:
            raise TypeError('attributes must be int or float')
        
    def __str__(self):
        "String representation"
        return '(' + str(self.x) + ' , ' + str(self.y) + ')'
    
    def __add__(self, other):
        "Returns a new Point object from the sum of two points"
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        "Returns a new Point object from the subtracction of two points"
        return Point(self.x - other.x, self.y - other.y)

    def norm(self):
        "Returns distance from the origin to point (vector)"
        return ((self.x)**2 + (self.y)**2)**(1/2)

    def distance(self, other):
        "Returns the module (distance) between two Point objects"
        np = self - other
        return np.norm()

p = Point(5, 7)
q = Point(2, 3)

print(p)
t = p + q
print(t)

r = p.distance(q)
print(r)