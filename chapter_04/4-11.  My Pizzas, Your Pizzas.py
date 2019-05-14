# Start with your program from Exercise 4-1 (page 60) . 
# Make a copy of the list of pizzas, and call it friend_pizzas . Then, do the following: 

# • Add a new pizza to the original list .
# • Add a different pizza to the list friend_pizzas .
# • Prove that you have two separate lists . 
#    Print the message, My favorite pizzas are:, 
#    and then use a for loop to print the first list . 
#    Print the message, My friend’s favorite pizzas are:, 
#    and then use a for loop to print the sec-ond list . 
#    Make sure each new pizza is stored in the appropriate list . 

pizzas = ["stravaganza", "margarita", "diabola"]

friend_pizzas = pizzas[:]

pizzas.append("4estaciones")
friend_pizzas.append("4quesos")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend’s favorite pizzas are:")
for friend in friend_pizzas:
    print(friend)