from global_vars import *
from prettytable import PrettyTable

#dwarf info
dwarf_info_table = PrettyTable([""])
dwarf_info_table.add_row([""])
print(dwarf_info_table)

#dwarf info
def dwarf_info():
    dwarf_feature_table = PrettyTable(["Feature", "Description"])
    dwarf_feature_table.add_row(["Ability Score Increase", "Your Constitution score increases by 2."])
    dwarf_feature_table.add_row(["Darkvision", "You can see in dim light within 60 feet of you in shades of grey."])
    dwarf_feature_table.add_row(["Dwarven Resilience", "You have advantage on saving throws against poison and you have resistance to poison damage."])
    dwarf_feature_table.add_row(["Dwarven Combat Training", "You have proficiency with the battleaxe, handaxe, light hammer, and warhammer."])
    dwarf_feature_table.add_row(["Stonecunning", "Whenever you make a History check regarding stonework, add double your proficiency bonus to the check."])
    dwarf_feature_table.add_row(["Languages", "You can speak, read and write Common and Dwarvish."])
    print(dwarf_feature_table)
    #subrace info
    dwarf_subrace_feature_table = PrettyTable(["Subrace", "Feature", "Description"])
    dwarf_subrace_feature_table.add_row(["Hill", "Ability Score Increase", "Your Wisdom score increases by 1."])
    dwarf_subrace_feature_table.add_row(["Hill", "Dwarven Toughness", "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."])
    dwarf_subrace_feature_table.add_row(["Mountain", "Ability Score Increase", "Your Strength score increases by 2."])
    dwarf_subrace_feature_table.add_row(["Mountain", "Dwarven Armor Training", "You have proficiency with light and medium armor."])
    print(dwarf_subrace_feature_table)

#elf info
def elf_info():
    elf_feature_table = PrettyTable(["Feature", "Description"])
    elf_feature_table.add_row(["Ability Score Increase", "Your Dexterity score increases by 2."])
    elf_feature_table.add_row(["Darkvision", "You can see in dim light within 60 feet of you in shades of grey."])
    elf_feature_table.add_row(["Keen Senses", "You have proficiency in the Perception skill."])
    elf_feature_table.add_row(["Fey Ancestry", "You have advantage on saving throws against being charmed and magic can't put you to sleep."])
    elf_feature_table.add_row(["Stonecunning", "Whenever you make a History check regarding stonework, add double your proficiency bonus to the check."])
    elf_feature_table.add_row(["Languages", "You can speak, read and write Common and Elvish."])
    print(elf_feature_table)
    #subrace info
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

#halfling info
def halfling_info():
    halfling_feature_table = PrettyTable(["Feature", "Description"])
    halfling_feature_table.add_row(["Ability Score Increase", "Your Dexterity score increases by 2."])
    halfling_feature_table.add_row(["Lucky", "When you roll a 1 on an attack roll, ability check, or saving throw you may reroll and must use the new roll."])
    halfling_feature_table.add_row(["Brave", "You have advantages on saving throws against being frightened."])
    halfling_feature_table.add_row(["Languages", "You can speak, read and write Common and Halfling."])
    print(halfling_feature_table)
    #subrace info
    halfling_subrace_feature_table = PrettyTable(["Subrace", "Feature", "Description"])
    halfling_subrace_feature_table.add_row(["Lightfoot", "Ability Score Increase", "Your Charisma score increases by 1."])
    halfling_subrace_feature_table.add_row(["Lightfoot", "Naturally Stealthy", "You can attempt to hide when there is another ally near you."])
    halfling_subrace_feature_table.add_row(["Stout", "Ability Score Increase", "Your Constitution score increases by 1."])
    halfling_subrace_feature_table.add_row(["Stout", "Stout Resilience", "You have advantage on saving throws against poison, and you have resistance to poison damage."])
    print(halfling_subrace_feature_table)

#human info
def human_info():
    human_feature_table = PrettyTable(["Feature", "Description"])
    human_feature_table.add_row(["Ability Score Increase", "Your ability scores each increase by 1."])
    human_feature_table.add_row(["Languages", "You speak, read, and write Common and one extra language of your choice."])
    print(human_feature_table)

#display info
def race_info():
    race_info_view = input("Would you like to view race info? ").lower()
    if race_info_view in yes_l:
        print(all_races)
        race_view_choice = input("What race would you like to view? ")
        while race_view_choice not in all_races:
            print("Please choose a race listed below.")
            print(all_races)
            race_view_choice = input("What race would you like to view? ")
        if race_view_choice == all_races[0]:
            dwarf_info()
        elif race_view_choice == all_races[1]:
            elf_info()
        elif race_view_choice == all_races[2]:
            halfling_info()
        else:
            human_info()