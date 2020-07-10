# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def __str__(self):
        return f"\nNow you are in the {self.room.name}. {self.room.description}."
    
    def player_location(self):
        return f"{self.room}"

# moving player to one of 4 directions n,s,e,w 
# otherwise if directions is unavavialbe for a room then try a diffrerent route 
    def move(self, direction):
        if getattr(self.room, f"{direction}_to") is not None:
            self.room = getattr(self.room, f"{direction}_to")
            print(self)
# Print an error message if the movement isn't allowed.
        else:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n  Try a different direction!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
# adding item
    def add_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        if item in self.items:
            item.on_drop()
            self.items.remove(item)

    # trying to print out items:
    def print_items(self):
        print("Items you are currenlty carrying in your inventory: ")
        for i in self.items:
            print(i)


# Example from guided project
# Write a class to hold player information, e.g. what room they are in
# currently.
# class Player:
#     def __init__(self, location):
#         self.location = location

#     def try_direction(self, command):
#         attribute = command  + '_to'

#         # see if the current room has the attribute 
#         # we can use a Python function called `hasattr`
#         if hasattr(self.location, attribute):
#             # use `getattr` to actually move to the room 
#             self.location = getattr(self.location, attribute)
#         else:
#             print("You can't go that way!\n")