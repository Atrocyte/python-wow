class Races:
    pass


class Character:
    name = ""
    race = ""
    role = ""

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name + ", the " + self.race + " " + self.role


Rahab = Character("Rahab")
Rahab.race = "undead"
Rahab.role = "rogue"

print(Rahab)

Tirsha = Character("Tirsha")
Tirsha.race = "human"
Tirsha.role = "mage"

print(Tirsha)