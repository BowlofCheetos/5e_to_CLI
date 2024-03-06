from global_vars import *
from player_intro import *
from gear import *
from spells import *
from prettytable import PrettyTable

#dwarf traits
def dwarf_traits():
    global con_score, special_traits, proficient_saving_throws, damage_resistance, known_languages, wis_score, dwarven_toughness, player_race, player_subrace, str_score, proficient_armor, proficient_weapons
    #base traits
    player_race = "Dwarf"
    con_score += 2
    proficient_weapons += battleaxe, handaxe, light_hammer, warhammer
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

#elf traits
def elf_traits():
    global dex_score, int_score, proficient_weapons, player_subrace, known_languages, known_cantrips, wis_score, cha_score
    dex_score += 2
    special_traits.append("Darkvision")
    proficient_skills.append("Perception")
    saving_throw_adv.append("Charmed")
    known_languages.append("Elvish")
    #subrace selection and traits
    print(elf_subraces)
    subrace_info = input("Would you like to view subrace info? ").lower()
    while subrace_info not in yes_l and subrace_info not in no_l:
        print(elf_subraces)
        subrace_info = input("Would you like to view subrace info? ").lower()
    if subrace_info in yes_l:
        elf_subrace_feature_table = PrettyTable(["Subrace", "Feature", "Description"])
        elf_subrace_feature_table.add_row(["High", "Ability Score Increase", "Your Intelligence score increases by 1."])
        elf_subrace_feature_table.add_row(["High", "Elf Weapon Training", "You have proficiency with the longsword, shortsword, shortbow, and longbow."])
        elf_subrace_feature_table.add_row(["High", "Cantrip", "You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting modifier for it."])
        elf_subrace_feature_table.add_row(["High", "Extra Language", "You can speak, read, and write one extra language of your choice."])
        elf_subrace_feature_table.add_row(["Wood", "Ability Score Increase", "Your Wisdom score increases by 1."])
        elf_subrace_feature_table.add_row(["Wood", "Elf Weapon Training", "You have proficiency with the longsword, shortsword, shortbow, and longbow."])
        elf_subrace_feature_table.add_row(["Wood", "Mask of the Wild", "You can attempt to hide when lightly obscured."])
        elf_subrace_feature_table.add_row(["Drow", "Ability Score Increase", "Your Charisma score increases by 1."])
        elf_subrace_feature_table.add_row(["Drow", "Superior Darkvision", "Your darkvision has a range of 120 feet."])
        elf_subrace_feature_table.add_row(["Drow", "Drow Magic", "You know the dancing lights cantrip\nAt 3rd level you know Faerie Fire\nAt 5th level you know Darkness\nAll can be cast once per day. Charisma is your spellcasting ability for them."])
        elf_subrace_feature_table.add_row(["Drow", "Drow Weapon Training", "You have proficiency with rapiers, shortswords, and hand crossbows."])
        print(elf_subrace_feature_table)
    print(elf_subraces)
    subrace_choice = input("What subrace would you like to be? ").title()
    while subrace_choice not in elf_subraces:
        print(elf_subraces)
        subrace_choice = input("What subrace would you like to be? ").title()
    if subrace_choice == elf_subraces[0]:
        int_score += 1
        proficient_weapons += longsword, longbow, shortsword, shortbow
        player_subrace = "High Elf"
        for x in wizard_cantrips:
            print(x.name)
        cantrip_choice = input("What cantrip do you choose? ").title()
        while cantrip_choice not in wizard_cantrips:
            for x in wizard_cantrips:
                print(x.name)
            cantrip_choice = input("What cantrip do you choose? ").title()
        for x in wizard_cantrips:
            if cantrip_choice == x.name:
                known_cantrips.append(x)
        print(all_languages)
        extra_language = input("What language do you choose? ")
        while extra_language not in all_languages:
            print(all_languages)
            extra_language = input("What language do you choose? ")
        while extra_language == all_languages[1]:
            print("You already known Elvish, choose another.")
            print(all_languages)
            extra_language = input("What language do you choose? ")
        known_languages.append(extra_language)
        player_subrace = "High Elf"
    elif subrace_choice == elf_subraces[1]:
        wis_score += 1
        proficient_weapons += longsword, longbow, shortsword, shortbow
        special_traits.append("Mask of the Wild")
        player_subrace = "Wood Elf"
    else:
        cha_score += 2
        special_traits.append("Superior Darkvision")
        known_cantrips.append(dancing_lights)
        proficient_weapons += rapier, shortsword, hand_crossbow
        player_subrace = "Drow"