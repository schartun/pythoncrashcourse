#You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.

#>Start with your program from Exercise 3-4. Add a print statement at the
#end of your program stating the name of the guest who can’t make it.

#>Modify your list, replacing the name of the guest who can’t make it with
#the name of the new person you are inviting.

#>Print a second set of invitation messages, one for each person who is still
#in your list.


guests = ["Papa", "Mama", "Illich", "Johanna"]
print("Disculpen pero " + guests[3] + " no podra venir")
guests[3] = "Karina"
message = "Wellcome to the place"
print(message + " " + guests[0])
print(message + " " + guests[1])
print(message + " " + guests[2])
print(message + " " + guests[3])

