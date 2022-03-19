# triangle 
# sides of triangle(a, b)
# hight of triangle(h)
# angle between sides a and c

from math import*
class Triangle:
    def __init__(self, side_a = 8 , side_b = 6, height = 0.48, n=(0,0)):
        self.side_a = side_a
        self.side_b = side_b
        self.height = height
        self.n = n
        post = list(n)
        self.x = post[0]
        self.y = post[1]

    def perimeter(self):
        side_c = sqrt(self.side_a + self.side_b)
        perimeter = self.side_a + self.side_b + side_c
        print(perimeter)
    
    def area(self):
        area = 0.5 * self.side_a * self.height
        print(area)

    def distance(self):
        return (self.x **2 + self.y **2) **0.5

    def position(self):
        print("x: ", self.x,"y: ", self.y)

    def movement(self,direction,move):
        x_d = self.x
        y_d = self.y
        print("direction_list = [UP, DOWN, LEFT, RIGHT]")
        if direction == "UP":
            y_d = self.y + move
        elif direction == "DOWN":
            y_d = self.y - move
        elif direction == "RIGHT":
            x_d = self.x + move
        elif direction == "LEFT":
            x_d = self.x - move
        self.x = x_d
        self.y = y_d
        return 0

direction_list = ["UP","DOWN","LEFT","RIGHT"]    
triangle = Triangle()

while True:
    question = input('Do you want to enter a move? (YES/NO)\n')
    while question == 'YES' or question == "Yes" or question == "yes":
        a = input('Input DIRECTION AND DISTANCE\n').split()
        if a[0] in direction_list:
            #direction = a[0]
            #distance = a[1]
            triangle.movement(a[0], float(a[1]))
            print("Position: ")
            triangle.position()
            print ("distance ",triangle.distance())
        else: 
            print('Invalid Input')  
    break

print("Perimeter: ")
triangle.perimeter()
print("Area: ")
triangle.area()
print("Movement: ")
triangle.move()