# triangle 
# sides of triangle(a, b)
# hight of triangle(h)
# angle between sides a and c

from math import*
class Triangle:
    def __init__(self, side_a = 6 , side_b = 8, height = 5, n=(0,0)):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = sqrt((self.side_a ** 2) + (self.side_b ** 2))
        self.height = height
        self.n = n
        post = list(n)
        self.x = post[0]
        self.y = post[1]

    def perimeter(self):
        perimeter = self.side_a + self.side_b + self.side_c
        print(perimeter)
    
    def area(self):
        area = 0.5 * self.side_a * self.height
        print(area)

    def distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def position(self):
        print("x: ", self.x,"y: ", self.y)

    def movement(self, direction, move):
        x_d = self.x
        y_d = self.y
        if direction == "UP" or direction == "up":
            y_d = self.y + move
        elif direction == "DOWN" or direction == "down":
            y_d = self.y - move
        elif direction == "RIGHT" or direction == "right":
            x_d = self.x + move
        elif direction == "LEFT" or direction == "left":
            x_d = self.x - move
        self.x = x_d
        self.y = y_d
        return 0

direction_list = ["UP", "DOWN", "LEFT", "RIGHT", "up", "down", "right", "left"]    
triangle = Triangle()
print("Perimeter: ")
triangle.perimeter()
print("Area: ")
triangle.area()

while True:
    question = input('Do you want to enter a move? (YES/NO)\n')
    while question == 'YES' or question == "Yes" or question == "yes":
        a = input('INPUT DIRECTION AND DISTANCE\n').split()
        if a[0] in direction_list:
            triangle.movement(a[0], float(a[1]))
            print("Position: ")
            triangle.position()
            print ("distance:",triangle.distance())
        else: 
            print('Invalid Input')  
    break
