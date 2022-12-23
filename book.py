booktype = input("What type of book is this?")
if booktype =="adv":
    print("I like adveture books!")
print("Finish reading book.")

activitytype = input("Please enter the activity you wish to perform.")
if activitytype == "play":
    print("Playing is fun!")
else:
    print("That seems like an interesting activity.")
print("Let's start the activity.")

direction = input("What direction do you wish to travel?")
if direction == "north":
    print("north is up!")
elif direction == "east":
    print("east is right!")
elif direction == "west":
    print("west is left!")
elif direction == "south":
    print("south is down!")
else:
    print("Give a correct direction!")


