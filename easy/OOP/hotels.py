class Hotel:
    ""
    name = str
    address = str 
    score = float
    price = float

    def __init__(self, name, address, score=0, price=float('inf')):

        def is_string(string):
            "Check if a attr have str format"
            return isinstance(string, str) and len(string) != 0 
            
        def is_number(value):
            "Check the attribute type, only int of float"
            return isinstance(value, (int, float))
        
        def non_zero(value):
            "Check if value is less or equal zero"
            if is_number(value):
                if value == 0 or value < 0:
                    value = float('inf')
                else:
                    return value
            else:
                raise TypeError('Data must be int or float')

        if is_string(name) and is_string(address):
            self.name = name
            self.address = address
        else:
            raise TypeError('Data must be strings')
        
        if is_number(score):
            self.score = score
        else:
            raise TypeError('Data must be int or float')
        
        self.price = non_zero(price)

    def __repr__(self):
            return self.name + ' de ' + self.address + ' -' + ' Score: '  + str(self.score) + ' -' + ' Price: '  + str(self.price) + ' Pesos'
    
    def ratio(self):
        return ((self.score**2)*10.) / self.price

## sorting comparators

    def __eq__(self, other):
        return (self.ratio() == other.ratio())
    
    def __ne__(self, other):
        return (self.ratio() != other.ratio())
    
    def __lt__(self, other):
        return (self.ratio() < other.ratio())
    
    def __le__(self, other):
        return (self.ratio() <= other.ratio())
    
    def __gt__(self, other):
        return (self.ratio() > other.ratio())
    
    def __ge__(self, other):
        return (self.ratio() >= other.ratio())

##TESTING AREA

h = Hotel("Hotel City", "Mercedes", 3.25, 78)
i = Hotel("Hotel Mascardi", "Bariloche", 6, 150)

print(h < i)

print(h, i)
