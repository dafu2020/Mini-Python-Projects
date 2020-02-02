PI = 3.14159

radius = 0
radius = float(input('Enter radius: '))

circumference = 2 * PI * radius
print("Circumference:", circumference)

area = PI * radius * radius
print("Area:", area)

double_radius = 2*radius
print("Double radius:", double_radius)

new_circumference = 2 * PI * double_radius
print("New circumference:", new_circumference)

new_area = PI * double_radius * double_radius
print("New area:", new_area)

circumference_increased = new_circumference / circumference
area_increased = new_area / area

print("As the radius doubled, the circumference will increased by",
      circumference_increased,  "times, and the area will increased by", area_increased, "times.")