#Make a list of the multiples of 3 from 3 to 30. Use a for loop to
#print the numbers in your list.

multiples = []
for number in range(3, 31):
    multiples.append(number*3)
    print(multiples)

print(multiples)