# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name 
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return f"{self.items}"

 # trying to print out items:
    def print_items(self):
        if len(self.items) == 0:
            print(f"There are no items in this room")
        else:
            print(f"\nItems in {self.name}: ")
            for i in self.items:
                print(i)

    def drop_item_in_room(self, item):
        if item in self.items: 
            self.items.remove(item)
        else:
            print(f"You are not carrying a {item} ")


# Example from guided project 
# Implement a class to hold room information. This should have name and
# description attributes.
# class Room:
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description

#     def __str__(self):
#         return f"{self.name}, {self.description}"