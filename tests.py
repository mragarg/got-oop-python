# Not 'real' tests

from character import Character
from character import Hero
from character import Monster

# Characters can be instantiated with name and avatar
arya = Character("Arya Stark", "arya.png")
jon = Character("Jon Snow", "jon.png")

print(arya.name, arya.avatar)
print(jon.name, jon.avatar)

# Adding 2 items to inventory - inventory length should == 2
arya.inventory.append("sword")
arya.inventory.append("mask")

print("Arya has %d item(s)." % len(arya.inventory))

# Arya should have a `greet` method and return
# "Hello, I am Arya Stark. I am awesome" when called
print(arya.greet())

# Arya should have a `greet` method that accepts another Character
# Return "Hello, Jon Snow, I am Arya Stark. I am awesome."
print(arya.greet(jon))

# Testing adding, viewing, and removing items to inventory
arya.add_inventory("food")
print(arya.view_inventory())
arya.remove_inventory("sword")
print(arya.view_inventory())


# Hero class
bronn = Hero("Bronn of the Blackwater", "bron.png")
print(bronn.name)

# Hero should be able to greet Character
print(bronn.greet(arya))
print(jon.greet(bronn))

# Monster class
joffrey = Monster("Joffrey Baratheon", "joffrey.png")
print(joffrey.name)

# Hero greets Monster
jon = Hero("Jon Snow", "jon.png")
print(jon.greet(joffrey))
