class Square:
  def __init__(self, side):
    self.side = side

  def get_area(self):
    return self.side * self.side

  def get_perimeter(self):
    return 4 * self.side

side = Square(5)

print("넓이: ", side.get_area())
print("둘레: ", side.get_perimeter())

