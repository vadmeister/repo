#Task2. Write a script to print out a set containing all the colours from color_list_1 which are not present in color_list_2
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Color sets: ")
print(color_list_1)
print(color_list_2)
print("Difference of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))
print("Difference of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))

