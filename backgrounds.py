from global_vars import *

def acolyte_bkgrnd():
    global proficient_skills, known_languages, player_gold, special_traits
    proficient_skills += insight, religion
    iteration = 0
    while iteration < 2:
        extra_language = input("What language do you choose? ").title()
        while extra_language not in all_languages:
            print(all_languages)
            extra_language = input("What language do you choose? ").title()
        while extra_language in known_languages:
            print("Please choose a language that you do not know.")
            print(all_languages)
        known_languages.append(extra_language)
    player_gold += 15
    special_traits.append("Shelter of the Faithful")

def charlatan_bkgrnd():
    global proficient_skills, player_gold, player_inventory, special_traits
    proficient_skills += deception, sleight_of_hand
    player_inventory.append("Disguise Kit")
    player_gold += 15
    special_traits.append("False Identity")

def criminal_bkgrnd():
    global proficient_skills, player_gold, player_inventory, special_traits
    proficient_skills += deception, stealth
    player_inventory.append("Thieves' Tools")
    player_gold += 15
    special_traits.append("Criminal Contact")

def entertainer_bkgrnd():
    global proficient_skills, player_gold, player_inventory, special_traits
    proficient_skills += acrobatics, performance
    player_inventory.append("Disguise kit")
    player_gold += 15
    special_traits.append("By Popular Demand")

def folk_hero_bkgrnd():
    global proficient_skills, player_gold, player_inventory
    proficient_skills += animal_handling, survival
    player_gold += 10
    special_traits.append("Rustic Hospitality")

def hermit_bkgrnd():
    global proficient_skills, player_gold, player_inventory, known_languages, special_traits
    proficient_skills += medicine, religion
    player_inventory.append("Herbalism Kit")
    player_gold += 5
    extra_language = input("What language do you choose? ").title()
    while extra_language not in all_languages:
        print(all_languages)
        extra_language = input("What language do you choose? ").title()
    while extra_language in known_languages:
        print("Please choose a language that you do not know.")
        print(all_languages)
    known_languages.append(extra_language)

def noble_bkgrnd():
    global proficient_skills, player_gold, player_inventory, known_languages, special_traits
    proficient_skills += history, persuasion
    player_gold += 25
    extra_language = input("What language do you choose? ").title()
    while extra_language not in all_languages:
        print(all_languages)
        extra_language = input("What language do you choose? ").title()
    while extra_language in known_languages:
        print("Please choose a language that you do not know.")
        print(all_languages)
    known_languages.append(extra_language)
    special_traits.append("Position of Privilege")

def outlander_bkgrnd():
    global proficient_skills, player_gold, player_inventory, known_languages, special_traits
    proficient_skills += athletics, survival
    player_gold += 10
    extra_language = input("What language do you choose? ").title()
    while extra_language not in all_languages:
        print(all_languages)
        extra_language = input("What language do you choose? ").title()
    while extra_language in known_languages:
        print("Please choose a language that you do not know.")
        print(all_languages)
    known_languages.append(extra_language)
    special_traits.append("Wanderer")   

def sage_bkgrnd():
    global proficient_skills, player_gold, player_inventory, known_languages, special_traits
    proficient_skills += arcana, history
    iteration = 0
    while iteration < 2:
        extra_language = input("What language do you choose? ").title()
        while extra_language not in all_languages:
            print(all_languages)
            extra_language = input("What language do you choose? ").title()
        while extra_language in known_languages:
            print("Please choose a language that you do not know.")
            print(all_languages)
        known_languages.append(extra_language)
    special_traits.append("Researcher")

def soldier_bkgrnd():
    global proficient_skills, player_gold, special_traits
    proficient_skills += athletics, intimidation
    player_gold += 10
    special_traits.append("Military Rank")