# python set program - flowers

# create a set of flowers
flowers = {"rose", "lotus", "lily", "jasmine"}

# display the set
print("flowers set:", flowers)

# add a flower
flowers.add("sunflower")
print("after adding sunflower:", flowers)

# remove a flower
flowers.remove("lotus")
print("after removing lotus:", flowers)

# check if a flower exists
if "rose" in flowers:
    print("yes, rose is in the set")

# length of the set
print("total flowers:", len(flowers))

# loop through the set
print("looping through flowers:")
for flower in flowers:
    print("-", flower)

# sets automatically remove duplicates
more_flowers = {"rose", "marigold", "lily"}
flowers.update(more_flowers)
print("after adding more flowers:", flowers)

# set operations example
tropical = {"hibiscus", "jasmine", "lotus"}
print("union with tropical flowers:", flowers | tropical)
print("intersection with tropical flowers:", flowers & tropical)
