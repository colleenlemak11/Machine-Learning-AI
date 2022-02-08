# class PointPublic:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
    
#     # PointPrivateGetterSetter class declares private attributes _x and _y and getter and setter methods
#     class PointPrivateGetterSetter:
#         def __init__(self, x=0, y=0):
#             self._x = x
#             self._y = y
        
#         # getter methods for private attributes _x and _y
#         def get_x(self):
#             return self._x
        
#         def get_y(self):
#             return self._y
        
#         # setter methods for private attributes _x and _y
#         def set_x(self, x):
#             self._x = x
            
#         def set_y(self, y):
#             self._y = y
    
    
# if __name__ == '__main__':
#     # Point object p1 with public attrbutes
    
#     p1 = PointPublic(1,0)
    
#     print("Point p1 with public attributes \n")
#     print("p1=(" + str(p1.x) + "," + str(p1.y) + ") \n")
    
#     # Point object p2 with private attributes and getter and setter methids
#     p2 = PointPrivateGetterSetter(1,0)
    
#     print("Point p2 with private attributes and getter and setter methods \n")
#     print("p2=(" + str(p2.get_x()) + "," + str(p2.get_y()) + ") \n")

#     p2.set_x(2)
#     p2.set_y(5)
    
#     print("p2=" + str(p2.get_x()) + "," + str(p2.get_y()) + ") \n")

#     p3 = PointPrivatePythonGetterSetter(1,0)
#     print("Point p3 with private attributes and pythonic getter and setter methods \n")
#     print("p3=(")
    
    
# class PointPrivatePythonGetterSetter:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
        
#         @property
#         def x(self):
#             return self._x
        
#         @property
#         def y(self):
#             return self._y
        
#         @x.setter
#         def x(self, x):
#             self._x = x
        
#         @y.setter
#         def y(self, y):
#             self._y = y
            
        
    
    