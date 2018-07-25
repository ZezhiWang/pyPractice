# description: This is my first program 

# author : WANG, ZEZHI

# date: August 31, 2015

def hypotenuse ():
    base = raw_input("Enter the base of the triangle: ")
    base = float(base)

    height = raw_input("Enter the height of the triangle: ")
    height = float(height)

    return (base ** 2 + height ** 2) ** (0.5)

print hypotenuse()

    
