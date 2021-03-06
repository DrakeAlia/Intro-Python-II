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
    'sword': Item('Sword', 'A cool sword'),
    'grail': Item('Grail', 'THE GRAIL')
}

room['foyer'].items = item['sword']
room['treasure'].items = item['grail']

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
        print("\n{item for item in player.room.items}")
    # If the user enters "q", quit the game.
    elif command == "q":
        print("See you next time")
        break
    else:
        print("Please input N, S, E, W or Q to quit the game")