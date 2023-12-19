class Shape:
  def area(self):
    pass
  def perimeter(self):
    pass

class Rectangle(Shape):
  def __init__(self, length, breadth):
    self.length = length
    self.breadth = breadth
  def area(self):
    return self.length*self.breadth
  def perimeter(self):
    return 2*(self.length*self.breadth)

class Square(Shape):
  def __init__(self, side):
    self.side = side
  def area(self):
    return self.side**2
  def perimeter(self):
    return 4*self.side

rectangle = Rectangle(4,2)
print(rectangle.area())
print(rectangle.perimeter())

square = Square(5)
print(square.area())
print(square.perimeter())


# In[ ]:




