# PointPublic class declares public attributes x and y

class PointPublic:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# PointPrivateGetterSetter class declares private attributes _x and _y, and getter and setter methods

class PointPrivateGetterSetter:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
    
    # gettter methods for private attributes _x and _y 
    
    def get_x(self):
        return self._x

    def get_y(self):
        return self._y
        
    # setter methods for private attributes _x and _y
    
    def set_x(self, x):
        self._x = x
        
    def set_y(self, y):
        self._y = y
        
# PointPrivatePythonicGetterSetter class declares private attributes _x and _y, and getter and setter methods

class PointPrivatePythonicGetterSetter:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
    
    # getter methods following Python coding conventions (pythonic code) are implemented using @property
    
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    # setter methods following Python coding conventions (pythonic code) are implemented using @attribute.setter

    @x.setter
    def x(self, x):
        self._x = x

    @y.setter
    def y(self, y):
        self._y = y
        
        
if __name__ == '__main__':

    # Point object p1 with public attributes

    p1 = PointPublic(1, 0)
    
    print ("Point p1 with public attributes \n")
    print ("p1=(" + str(p1.x) + "," + str(p1.y) + ")")

    p1.x = 2
    p1.y = 5

    print("p1=(" + str(p1.x) + "," + str(p1.y) + ") \n")
  
  
    # Point object p2 with private attributes and getter and setter methods
  
    p2 = PointPrivateGetterSetter(1, 0)
    
    print ("Point p2 with private attributes and getter and setter methods \n")
    print ("p2=(" + str(p2.get_x()) + "," + str(p2.get_y()) + ")")

    p2.set_x(2)
    p2.set_y(5)
    
    print ("p2=(" + str(p2.get_x()) + "," + str(p2.get_y()) + ") \n")
    
    # since x and y attributes are private, they can only be accessed using the getter and setter methods
    # the instruction below causes the exception AttributeError: 'PointPrivateGetterSetter' object has no attribute 'x'
    #
    # print ("p2=(" + str(p2.x) + "," + str(p2.y) + ") \n")


    # Point object p3 with private attributes and pythonic getter and setter methods

    p3 = PointPrivatePythonicGetterSetter(1, 0)

    print ("Point p3 with private attributes and pythonic getter and setter methods \n")
    print ("p3=(" + str(p3.x) + "," + str(p3.y) + ")")

    p3.x = 2
    p3.y = 5

    print ("p3=(" + str(p3.x) + "," + str(p3.y) + ") \n")

    # pythonic getter and setter functions let access private attributes using the same syntax as for public attributes