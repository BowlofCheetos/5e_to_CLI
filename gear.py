from global_vars import *

#armor skeleton
class armor:
    def __init__(self, type, cost, armor_class, strength, stealth, weight):
        global med_dex_mod
        self.type = type
        self.cost = cost
        self.armor_class = armor_class
        self.strength = strength
        self.stealth = stealth
        self.weight = weight
        if dex_mod > 2:
            med_dex_mod = 2
        else:
            med_dex_mod = dex_mod

#armor database
#light
padded_armor = armor("Light", 5, (11 + dex_mod), 0, True, 8)
leather_armor = armor("Light", 10, (11 + dex_mod), 0, False, 10)
studded_leather_armor = armor("Light", 45, (12 + dex_mod), 0, False, 13)
light_armor = [padded_armor, leather_armor, studded_leather_armor]

#medium
hide_armor = armor("Medium", 10, (12 + med_dex_mod), 0, False, 12)
chain_shirt = armor("Medium", 50, (13 + med_dex_mod), 0, False, 20)
scale_mail = armor("Medium", 50, (14 + med_dex_mod), 0, True, 45)
breastplate = armor("Medium", 400, (14 + med_dex_mod), 0, False, 20)
half_plate = armor("Medium", 750, (15 + med_dex_mod), 0, True, 40)
medium_armor = [hide_armor, chain_shirt, scale_mail, breastplate, half_plate]

#heavy
ring_mail = armor("Heavy", 30, 14, 0, True, 40)
chain_mail = armor("Heavy", 75, 16, 13, True, 55)
splint = armor("Heavy", 200, 17, 15, True, 60)
plate = armor("Heavy", 1500, 18, 15, True, 65)

#shield
shield = armor("Heavy", 10, 2, 0, False, 6)

#weapon skeleton
class weapon:
    def __init__(self, name, cost, damage, weight, finesse, light, versatile, two_handed, heavy):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.weight = weight
        self.finesse = finesse
        self.light = light
        self.versatile = versatile
        self.two_handed = two_handed
        self.heavy = heavy

#weapon database
#simple melee
club = weapon("Club", 1, 4, 2, False, True, False, False, False)
dagger = weapon("Dagger", 2, 4, 1, True, True, False, False, False)
greatclub = weapon("Greatclub", 1, 8, 10, False, False, False, True, False)
handaxe = weapon("Handaxe", 5, 6, 2, False, True, False, False, False)
javelin = weapon("Javelin", 1, 6, 2, False, False, False, False, False)
light_hammer = weapon("Light Hammer", 2, 4, 2, False, True, False, False, False)
mace = weapon("Mace", 5, 6, 4, False, False, False, False, False)
quarterstaff = weapon("Quarterstaff", 1, 6, 4, False, False, True, False, False)
sickle = weapon("Sickle", 1, 4, 2, False, True)
spear = weapon("Spear", 1, 6, 3, False, False, False, False, False)
unarmed_strike = weapon("Unarmed Strike", 0, str_mod, 0, False, False, False, False, False)
simple_weapons = [club, dagger, greatclub, handaxe, javelin, light_hammer, mace, quarterstaff, sickle, spear, unarmed_strike]