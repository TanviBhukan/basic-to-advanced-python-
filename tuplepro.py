# python tuple program

# create a tuple
colors = ("red", "green", "blue", "yellow")

# display the tuple
print("colors tuple:", colors)

# access elements by index
print("first color:", colors[0])
print("last color:", colors[-1])

# length of tuple
print("total colors:", len(colors))

# loop through tuple
print("looping through colors:")
for color in colors:
    print("-", color)

# check if an item exists
if "green" in colors:
    print("yes, green is in the tuple")

# slicing a tuple
print("sliced colors (index 1 to 3):", colors[1:3])

# nested tuple
nested = (1, 2, (3, 4, 5))
print("nested tuple:", nested)
print("access 4 from nested tuple:", nested[2][1])
