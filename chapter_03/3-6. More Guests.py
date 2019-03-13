#You just found a bigger dinner table, so now more space is
#available. Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
#statement to the end of your program informing people that you found a
#bigger dinner table.
#• Use insert() to add one new guest to the beginning of your list.

#• Use insert() to add one new guest to the middle of your list.

#• Use append() to add one new guest to the end of your list.

#• Print a new set of invitation messages, one for each person in your list.

guests = ["Papa", "Mama", "Illich", "Johanna"]
print("Recien consegui una mesa mas grande :-)")
guests.insert(0, "Maria I")
guests.insert((len(guests)//2), "Maria V")
guests.append("Ivanna")
message = "Wellcome to the place"
print(message + " " + guests[0])
print(message + " " + guests[1])
print(message + " " + guests[2])
print(message + " " + guests[3])
print(message + " " + guests[4])
print(message + " " + guests[5])
print(message + " " + guests[6])