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
    barbarian_skills = [animal_handling, athletics, intimidation, nature, perception, survival]
    #skill choice
    iteration = 0
    while iteration < 2:
        print(barbarian_skills)
        skill_choice = input("What skill would you like to be proficient in? ").strip().title()
        while skill_choice not in barbarian_skills:
            print("Please choose a skill listed.")
            print(barbarian_skills)
            skill_choice = input("What skill would you like to be proficient in? ").strip().title()
        barbarian_skills.remove(skill_choice)
        proficient_skills.append(skill_choice)
        iteration += 1
    #equipment choice
    equip_choice_1 = input("Would you like (a) Greataxe or (b) Any martial weapon? ").strip().lower()
    while equip_choice_1 != 'a' and equip_choice_1 != 'b':
        equip_choice_1 = input("Would you like (a) Greataxe or (b) Any martial melee weapon? ").strip().lower()
    if equip_choice_1 == 'a':
        player_weapons.append(greataxe)
    else:
        print(martial_melee_weapons)
        weapon_choice = input("What weapon would you like to choose? ").strip().title()
        