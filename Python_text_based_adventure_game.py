import time

# Initialize the player's location
location = "room1"

# Initialize the timer
start_time = time.time()

# Welcome the player
print("Welcome to the Haunted Mansion! Try to escape before time runs out.")

while True:
    # Check the player's location
    if location == "room1":
        print("You are in a dark room. There is a door to the north.")
        command = input("> ").lower()
        if command == "go north":
            location = "room2"
        else:
            print("I don't understand.")
    elif location == "room2":
        print("You are in a grand hallway. There is a door to the west and a door to the east.")
        command = input("> ").lower()
        if command == "go west":
            location = "room3"
        elif command == "go east":
            location = "room4"
        else:
            print("I don't understand.")
    elif location == "room3":
        print("You are in a dusty library. There is a door to the east.")
        command = input("> ").lower()
        if command == "go east":
            location = "room2"
        else:
            print("I don't understand.")
    elif location == "room4":
        print("You are in a dimly lit kitchen. There is a door to the north and a door to the west.")
        command = input("> ").lower()
        if command == "go north":
            location = "room5"
        elif command == "go west":
            location = "room2"
        else:
            print("I don't understand.")
    elif location == "room5":
        print("You are in a spooky attic. There is a door to the south.")
        command = input("> ").lower()
        if command == "go south":
            location = "room4"
        else:
            print("I don't understand.")
    # Check if the player has won or lost
    elapsed_time = time.time() - start_time
    if location == "room3":
        print("Congratulations! You have escaped the haunted mansion.")
        break
    elif elapsed_time > 60:
        print("Sorry, you have run out of time. The ghosts have caught you.")
        break

