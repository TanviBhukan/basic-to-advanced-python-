# python list program

# create a list
fruits = ["apple", "banana", "mango", "orange"]

# display the list
print("fruits list:", fruits)

# access elements by index
print("first fruit:", fruits[0])
print("last fruit:", fruits[-1])

# add new element to list
fruits.append("grapes")
print("after adding grapes:", fruits)

# insert element at specific position
fruits.insert(2, "cherry")
print("after inserting cherry at index 2:", fruits)

# remove element
fruits.remove("banana")
print("after removing banana:", fruits)

# change element
fruits[1] = "kiwi"
print("after changing index 1 to kiwi:", fruits)

# length of list
print("total fruits:", len(fruits))

# loop through list
print("looping through fruits:")
for fruit in fruits:
    print("-", fruit)
