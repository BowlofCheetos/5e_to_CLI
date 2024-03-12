from global_vars import *

def acolyte_bkgrnd():
    global proficient_skills, known_languages, player_gold, special_traits
    proficient_skills += insight, religion
    iteration = 0
    while iteration < 2:
        print(all_languages)
        if iteration == 0:
            extra_language = input("What is the first language do you choose? ").strip().title()
        else:
            extra_language = input("What is the second language you choose? ").strip().title()
        while extra_language not in all_languages:
            print(all_languages)
            extra_language = input("What language do you choose? ").title()
        while extra_language in known_languages:
            print("Please choose a language that you do not know.")
            print(all_languages)
            extra_language = input("What language do you choose? ").title()
        known_languages.append(extra_language)
        iteration += 1
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
    print(all_languages)
    extra_language = input("What language do you choose? ").title()
    while extra_language not in all_languages:
        print(all_languages)
        extra_language = input("What language do you choose? ").title()
    while extra_language in known_languages:
        print("Please choose a language that you do not know.")
        print(all_languages)
        extra_language = input("What language do you choose? ").title()
    known_languages.append(extra_language)

def noble_bkgrnd():
    global proficient_skills, player_gold, player_inventory, known_languages, special_traits
    proficient_skills += history, persuasion
    player_gold += 25
    print(all_languages)
    extra_language = input("What language do you choose? ").title()
    while extra_language not in all_languages:
        print(all_languages)
        extra_language = input("What language do you choose? ").title()
    while extra_language in known_languages:
        print("Please choose a language that you do not know.")
        print(all_languages)
        extra_language = input("What language do you choose? ").title()
    known_languages.append(extra_language)
    special_traits.append("Position of Privilege")

def outlander_bkgrnd():
    global proficient_skills, player_gold, player_inventory, known_languages, special_traits
    proficient_skills += athletics, survival
    player_gold += 10
    print(all_languages)
    extra_language = input("What language do you choose? ").title()
    while extra_language not in all_languages:
        print(all_languages)
        extra_language = input("What language do you choose? ").title()
    while extra_language in known_languages:
        print("Please choose a language that you do not know.")
        print(all_languages)
        extra_language = input("What language do you choose? ").title()
    known_languages.append(extra_language)
    special_traits.append("Wanderer")   

def sage_bkgrnd():
    global proficient_skills, player_gold, player_inventory, known_languages, special_traits
    proficient_skills += arcana, history
    iteration = 0
    while iteration < 2:
        print(all_languages)
        if iteration == 0:
            extra_language = input("What is the first language do you choose? ").strip().title()
        else:
            extra_language = input("What is the second language you choose? ").strip().title()
        while extra_language not in all_languages:
            print(all_languages)
            extra_language = input("What language do you choose? ").title()
        while extra_language in known_languages:
            print("Please choose a language that you do not know.")
            print(all_languages)
            extra_language = input("What language do you choose? ").title()
        known_languages.append(extra_language)
        iteration += 1
    special_traits.append("Researcher")

def soldier_bkgrnd():
    global proficient_skills, player_gold, special_traits
    proficient_skills += athletics, intimidation
    player_gold += 10
    special_traits.append("Military Rank")

def bkgrnd_choice():
    global player_background
    print(all_backgrounds)
    choice = input("What background would you like? ").strip().title()
    while choice not in all_backgrounds:
        print("Please choose a background listed.")
        print(all_backgrounds)
        choice = input("What background would you like? ").strip().title()
    if choice == all_backgrounds[0]:
        acolyte_bkgrnd()
        player_background = all_backgrounds[0]
    elif choice ==all_backgrounds[1]:
        player_background = all_backgrounds[1]
    elif choice ==all_backgrounds[2]:
        player_background = all_backgrounds[2]
    elif choice ==all_backgrounds[3]:
        player_background = all_backgrounds[3]
    elif choice ==all_backgrounds[4]:
        player_background = all_backgrounds[4]
    elif choice ==all_backgrounds[5]:
        player_background = all_backgrounds[5]
    elif choice ==all_backgrounds[6]:
        player_background = all_backgrounds[6]
    elif choice ==all_backgrounds[7]:
        player_background = all_backgrounds[7]
    elif choice ==all_backgrounds[8]:
        player_background = all_backgrounds[8]
    else:
        player_background = all_backgrounds[9]
    