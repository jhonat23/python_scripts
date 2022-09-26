class Vector():

    def __init__(self, x: int, y: int):
        self.x = x 
        self.y = y 

    def __str__(self):
        return f'Vector=({self.x},{self.y})'

    def __add__(self, other):
        self.resultx = self.x + other.x
        self.resulty = self.y + other.y
        return Vector(self.resultx, self.resulty)

if __name__ == '__main__':
    vector_1 = Vector(5,10)
    print(vector_1)
    vector_2 = Vector(20,-7)
    print(vector_2)
    vector_3 = vector_1 + vector_2
    print(vector_3)
