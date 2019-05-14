# Using one of the programs you wrote in this chapter, 
# add several lines to the end of the program that do the following: 
# • Print the message, The first three items in the list are: . 
#   Then use a slice to print the first three items from that program’s list . 
# • Print the message, Three items from the middle of the list are: . 
#   Use a slice to print three items from the middle of the list . 
# • Print the message, The last three items in the list are: . 
#   Use a slice to print the last three items in the list . 

cubes = []

[cubes.append(number**3) for number in range(1,10)]

print(cubes)
print("The first three items in the list are: ")
print(cubes[0:3])

print(cubes)
middle = len(cubes)//2
print("Three items from the middle of the list are: ")
print(cubes[middle:])

print(cubes)
print("The last three items in the list are: ")
print(cubes[-3:])