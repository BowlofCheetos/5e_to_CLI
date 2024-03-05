from global_vars import *
from player_intro import *
from gear import *
from prettytable import PrettyTable

#dwarf traits
def dwarf_traits():
    global con_score, special_traits, proficient_saving_throws, damage_resistance, known_languages, wis_score, dwarven_toughness, player_race, player_subrace, str_score, proficient_armor
    #base traits
    player_race = "Dwarf"
    con_score += 2
    special_traits += "Darkvision", "Stonecunning"
    proficient_saving_throws += "Poison"
    damage_resistance += "Poison"
    known_languages.append('Dwarvish')
    #subrace selection and traits
    print(dwarf_subraces)
    subrace_info = input("Would you like to view subrace info? ").lower()
    while subrace_info not in yes_l and subrace_info not in no_l:
        print(dwarf_subraces)
        subrace_info = input("Would you like to view subrace info? ").lower()
    if subrace_info in yes_l:
        dwarf_subrace_feature_table = PrettyTable(["Subrace", "Feature", "Description"])
        dwarf_subrace_feature_table.add_row(["Hill", "Ability Score Increase", "Your Wisdom score increases by 1."])
        dwarf_subrace_feature_table.add_row(["Hill", "Dwarven Toughness", "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."])
        dwarf_subrace_feature_table.add_row(["Mountain", "Ability Score Increase", "Your Strength score increases by 2."])
        dwarf_subrace_feature_table.add_row(["Mountain", "Dwarven Armor Training", "You have proficiency with light and medium armor."])
        print(dwarf_subrace_feature_table)
    print(dwarf_subraces)
    subrace_choice = input("What subrace would you like to be? ").title()
    while subrace_choice not in dwarf_subraces:
        print(dwarf_subraces)
        subrace_choice = input("What subrace would you like to be? ").title()
    if subrace_choice == dwarf_subraces[0]:
        wis_score += 1
        dwarven_toughness = 1
        player_subrace = "Hill Dwarf"
    else:
        str_score += 2
        proficient_armor += light_armor, medium_armor
        player_subrace = "Mountain Dwarf"