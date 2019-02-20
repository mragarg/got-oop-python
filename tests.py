# Not 'real' tests

from character import Character

# Characters can be instantiated with name and avatar
arya = Character("Arya Stark", "arya.png", "sword")
jon = Character("Jon Snow", "jon.png", "sword")

print(arya.name, arya.avatar, arya.inventory)
print(jon.name, jon.avatar, jon.inventory)