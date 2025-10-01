# python dictionary program

# create a dictionary
student = {
    "name": "tanvi",
    "age": 21,
    "course": "mca",
    "city": "pune"
}

# display the dictionary
print("student dictionary:", student)

# access elements by key
print("student name:", student["name"])
print("student age:", student["age"])

# add a new key-value pair
student["semester"] = 3
print("after adding semester:", student)

# change value of a key
student["city"] = "lohegaon"
print("after changing city:", student)

# remove a key-value pair
student.pop("course")
print("after removing course:", student)

# loop through dictionary
print("looping through student dictionary:")
for key, value in student.items():
    print("-", key, ":", value)

# check if key exists
if "age" in student:
    print("age key exists")

# get all keys and values
print("all keys:", student.keys())
print("all values:", student.values())
