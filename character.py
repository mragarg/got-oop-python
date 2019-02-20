
# Name
# Avatar (profile picture)

# def do_stuff():
#       pass

class Character():
    
    # Constructor Method
    def __init__(self, new_name, new_avatar):
        # 'self' is similar to 'this' in other languages
        self.name = new_name
        self.avatar = new_avatar
        self.inventory = []

    #someone=None is similar to `null` in other langauges
    def greet(self, someone=None):
        if someone:
            # Hero greets Monster
            if type(self) == Hero and type(someone) == Monster:
                return "Hello, %s. Nobody likes you. Love, %s" % (someone.name, self.name)
            # Monster greets Hero
            if type(self) == Monster and type(someone) == Hero:
                return "Hello, %s. My name is %s and I'm going to ruin your life." % (someone.name, self.name)
            # Character greets Character
            else:
                return "Hello, %s, I am %s. I am awesome." % (someone.name, self.name)
        # Character greets nobody
        else:
            return "Hello, I am %s. I am awesome." % self.name

    #Add item to inventory
    def add_inventory(self, item):
        self.inventory.append(item)

    #View item from inventory
    def view_inventory(self):
        return self.inventory

    #Remove item from inventory
    def remove_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print("Item not in inventory.")

# Hero is a kind of Character
# Hero is a subclass of Character
# Hero inherits from Character
# Character is the superclass of Hero
class Hero(Character):
    pass

class Monster(Character):
    pass