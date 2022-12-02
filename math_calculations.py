def cirlce():
    print("\nThis program calculates the area or radius of a circle\n")
    message = input("Type 'area' to calculate area or 'rad' to calculate radius: ")
    pi = 22 / 7
    if message.lower() ==  'area':
        radius = int(input("\nWhat is the value of the radius: "))
        #pi = 22 / 7
        area_of_circle = pi * (radius ** 2)
        return "\nArea of the cirle is: " + str(area_of_circle)
    elif message.lower() == 'rad':
        area = int(input("\nWhat is the value of the area: "))
        #pi == 22 / 7
        radius_of_circle = (area / pi) ** 0.5
        return "\nRadius of the circle is: " + str(radius_of_circle)
    else:
        print("Invalid input detected")

def rectangle():
    print("This program calculates the perimeter and area of a rectangle\n")
    length = int(input("\nType the length of the rectangle: "))
    breadth = int(input("\nType the breadth of the rectangle: "))
    message = input("\nType 'peri' to calculate perimeter or 'area' to calculate area: ")
    if message.lower() == "peri":
        perimeter_of_rectangle = 2 * (length + breadth)
        return "\nPerimeter of the rectangle is: " + str(perimeter_of_rectangle)
    elif message.lower() == "area":
        area_of_rectangle = length * breadth
        return "\nArea of the rectangle is: " + str(area_of_rectangle)
    else:
        print("Invalid input detected!")

def square():
    print("This program calculates the perimeter and area of a square\n")
    length = int(input("\nType the length of the square: "))
    message = input("\nType 'peri' to calculate perimeter or 'area' to calculate area: ")
    if message.lower() == "peri":
        perimeter_of_square = 4 * length
        return "\nPerimeter of the square is: " + str(perimeter_of_square)
    elif message.lower() == "area":
        area_of_square = length ** 2
        return "\nArea of the square is: " + str(area_of_square)
    else:
        print("Invalid input detected!")


message = input("""
    Type 'circle' to solve cicle related math, 
    Type 'rectangle' to solve rectangle related math,
    Type 'square' to solve rectangle related math 
>> """)

if message.lower() == "circle":
    print(cirlce())
elif message.lower() == "rectangle":
    print(rectangle())
elif message.lower() == "square":
    print(square())
else:
    print("Invalid input detected!")