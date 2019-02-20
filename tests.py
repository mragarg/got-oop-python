# Not 'real' tests

from character import Character

# Characters can be instantiated with name and avatar
arya = Character("Arya Stark", "arya.png")
jon = Character("Jon Snow", "jon.png")

print(arya.name, arya.avatar)
print(jon.name, jon.avatar)

#Adding 2 items to inventory - inventory length should == 2
arya.inventory.append("sword")
arya.inventory.append("mask")

print("Arya has %d item(s)." % len(arya.inventory))