# Let’s write a program to determine how many cans of paint we need to paint a room.

COVERAGE = 400

length = float(input('Enter Length: '))
width = float(input('Enter Width: '))
height = float(input('Enter height: '))
coat = float(input('Enter coats number: '))

surface_area = 2 * length * height + 2 * width * height + length * width
print("The total surface area to be painted is", surface_area, "square feet.")

coverage_needed = surface_area * coat

cans_of_paint_required = coverage_needed / COVERAGE

import math

cans_of_paint_required = math.ceil(cans_of_paint_required) # round up the result
print("You need to buy", cans_of_paint_required, "cans of 4L paint.")

