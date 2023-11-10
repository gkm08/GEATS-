class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(self.brand, self.model, self.year)

mycar = Car("Hyondai", "Sonata", "2022")
mycar.display_info()