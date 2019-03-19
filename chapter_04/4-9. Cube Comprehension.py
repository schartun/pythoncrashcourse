#Use a list comprehension to generate a list of the
#first 10 cubes.

cubes = []

[cubes.append(number**3) for number in range(1,10)]

print(cubes)
