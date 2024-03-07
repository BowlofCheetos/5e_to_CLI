from global_vars import *
from gear import *

#class traits
def barbarian_start():
    global player_hit_dice, proficient_saving_throws, proficient_weapons, proficient_armor, player_class, special_traits, rage_count, rage_damage
    player_class = player_classes[0]
    player_hit_dice = 12
    proficient_saving_throws += "STR", "CON"
    proficient_weapons += shield, martial_melee_weapons, martial_ranged_weapons
    proficient_armor += light_armor, medium_armor
    special_traits += "Rage", "Unarmored Defense"
    rage_count = 2
    rage_damage = 2