hello = "hello"
space = " "
world = "world"

# variable string
hello_world = hello + space + world

# list of string values
list_string = [hello_world, hello_world, hello_world]

# regular form of print
print("regular: " + hello_world)

# print string value with .capitalize() method which change first letter of value to capital
print("capitalize: " + hello_world.capitalize())

# print string value with .title() method which change first letter of value to capital even after spaces
print("title: " + hello_world.title())

# print string value with .upper() method which change value to uppercase
print("upper: " + hello_world.upper())

# print string value with .upper() method which change value to lowercase
print("lower : " + hello_world.lower())

# print string value with .join() method which join specific value between every list value
print("join (-) : " + " - ".join(list_string))

# print string value with .removeprefix() method which remove fist char of string value by given param
print("removePrefix (h) : " + hello_world.removeprefix("h"))

# print string value with .removeprefix() method which remove fist char of string value by given param
print("removeSuffix (d) : " + hello_world.removesuffix("d"))

# print string value with .replace() method which replace specific char of string value
print("replace (h -> y) : " + hello_world.replace("h", "y"))
