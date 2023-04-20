rectangle = []
sides = 4
for i in range(0, int(sides/2)):
    rectangle_side = int(input())
    rectangle.append(rectangle_side)
print(rectangle)
square_rectangle = rectangle[0] * rectangle[1]
print(square_rectangle)