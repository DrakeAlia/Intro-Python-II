class Item:
    def __init__(self, name, description):
        self.name = name 
        self.description = description
# player takes item
    def on_take(self):
        print(f"You have picked up {self.name}.")
# player drops item
    def on_drop(self):
        print(f"You have dropped {self.name}.")