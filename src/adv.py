from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


item = {
    'sword': Item('-Sword', 'A cool sword'),
    'grail': Item('-Grail', 'The Holy Grail!')
}

room['foyer'].add_item(item['sword'])
room['treasure'].add_item(item['grail'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# player = Player("Drake", room['outside'])

name = input("Enter player name: ")
room = room["outside"]
player = Player(name, room)

# Write a loop that:

valid_directions = ("n", "s", "e", "w")
# * Prints the current room name
print(f"\nWelcome {player.name}.\n\nYou are currently in the {player.room.name}. {player.room.description}!")

while True:
    # * Waits for user input and decides what to do.
    command = input(f"\nWhere would you like to go next?\n\n(N, S, E, W or Q to quit the game): ").lower()
    answer = command.split(" ")

    # If the user enters a cardinal direction, attempt to move to the room there.
    if command in valid_directions:
        player.move(command)
    # grabing item
    elif command == "i":
        # trying to print out items:
        # print(f"\n{[(item.name,item.description) for item in player.room.items]}")
        player.room.print_items()
        print()
        player.print_items()

    elif command == "d":
        if player.items == None:
            print("You have nothing in your inventory")
        else:
            print(f"\nYou have:")
            for count, item in enumerate(player.items, 1):
                print(count, item)
            dropSomething = input("\nWould you like to drop something (y/n)?: ")
            if dropSomething == "y" or dropSomething == "yes" and len(player.items) >= int(item) -1:
                item = input("\nInput the number of the items to drop: ")
                if len(player.items) >= int(item) -1:
                    try:
                        player.room.items = player.items[int(item) - 1]
                        item.on_drop()
                        print(f"\nyou dropped it!\n")   
                    except:
                        print("You don't have that item to drop!")


    # If the user enters "q", quit the game.
    elif command == "q":
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n      See you next time\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        break
    else:
        print("Please input N, S, E, W or Q to quit the game")




# Example from the guided project 
# Make a new player object that is currently in the 'outside' room.
# player = Player(room['outside'])
# possible_directions = ['n', 's', 'e', 'w']
# ​
#  Write a loop that:
# while True:
#     #
#     # * Prints the current room name
#     # * Prints the current description (the textwrap module might be useful here).
#     # * Waits for user input and decides what to do.
#     print(f"{player.location}\n")
# ​
#     # when input comes in, strip off whitespace, lowercase the input, and split it 
#     command = input("What would you like to do? ").strip().lower().split()[0]
#     command = command[0]
# ​
#     if command == 'q':
#         break
# ​
#     if command in possible_directions:
#         # check to see if we can go in that direction 
#         # if we can, go there 
#         player.try_direction(command)



