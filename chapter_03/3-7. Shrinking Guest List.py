#You just found out that your new dinner table won’t
#arrive in time for the dinner, and you have space for only two guests.

#• Start with your program from Exercise 3-6. Add a new line that prints a
#message saying that you can invite only two people for dinner.

#• Use pop() to remove guests from your list one at a time until only two
#names remain in your list. Each time you pop a name from your list, print
#a message to that person letting them know you’re sorry you can’t invite
#them to dinner.

#• Print a message to each of the two people still on your list, letting them
#know they’re still invited.

#• Use del to remove the last two names from your list, so you have an empty
#list. Print your list to make sure you actually have an empty list at the end
#of your program.

guests = ["Papa", "Mama", "Illich", "Johanna"]
guests.insert(0, "Maria I")
guests.insert((len(guests)//2), "Maria V")
guests.append("Ivanna")
print(guests)
print("Lo siento solo puedo invitar a dos personas")
print("Lo lamento " + guests.pop() )
print("Lo lamento " + guests.pop() )
print("Lo lamento " + guests.pop() )
print("Lo lamento " + guests.pop(2) )
print("Lo lamento " + guests.pop(0) )
print(guests[0] + " " + guests[1] + " " + "aun siguen invitados")
del guests[0]
del guests[0]
print(guests)