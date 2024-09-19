class Rectangle():
    def __init__(self, width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width * self.height)
    
rect = Rectangle(4,5)
print(f"Area: {rect.area()}")     #output: Area:20
print(f"Perimeter: {rect.perimeter()}")     #output: Perimeter:18