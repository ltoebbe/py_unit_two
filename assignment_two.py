import math

side_length = input("side length (ft) of the perimeter of the garden:")
plant_space = input("space (ft) between plants:")
bed_depth = input("depth (ft) of flower beds:")
gravel_depth = input("depth (ft) of gravel:")

total_area = float(side_length)**2
circle_area = math.pi*((float(side_length)/4)**2)
semicircle_area = float(circle_area)/2
gravel_area = float(total_area)-(float(circle_area)*3)

plants_in_1ss = float(semicircle_area)/float(plant_space)
plants_in_c = float(circle_area)/float(plant_space)
plants_total = (int(plants_in_1ss)*4)+int(plants_in_c)
soil_in_ss = float(semicircle_area)*float(bed_depth)
soil_in_c = float(circle_area)*float(bed_depth)
soil_total = float(soil_in_c)+(float(soil_in_ss)*4)
gravel_total = float(gravel_area)*float(gravel_depth)

print("plants total:", plants_total)
print("plants in center bed:", int(plants_in_c))
print("plants in each auxiliary bed:", int(plants_in_1ss))
print("soil total:", round(float(soil_total), ndigits=1), "sq. ft.")
print("soil in center bed:", round(float(soil_in_c), ndigits=1), "sq. ft.")
print("soil in each auxiliary bed:", round(float(soil_in_ss), ndigits=1), "sq. ft.")
print("gravel total:", round(float(gravel_total), ndigits=1), "sq. ft.")
