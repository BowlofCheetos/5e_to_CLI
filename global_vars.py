import random

#global variables
base = 0
score_base = 8
modifier_base = -1
prof_bonus = 2

#global lists
yes_l = ['yes', 'y']
no_l = ['no', 'n']
all_languages = ['Dwarvish', 'Elvish', 'Giant', 'Gnomish', 'Goblin', 'Goblin', 'Halfling', 'Orc']

#race lists
all_races = ['Dwarf', 'Elf', 'Halfling', 'Human',]
dwarf_subraces = ['Hill', 'Mountain']
elf_subraces = ['High', 'Wood', 'Drow']
halfling_subraces = ['Lightfoot', 'Stout']

#player starting scores
str_score = score_base
dex_score = score_base
con_score = score_base
int_score = score_base
wis_score = score_base
cha_score = score_base

#player starting modifiers
str_mod = modifier_base
dex_mod = modifier_base
con_mod = modifier_base
int_mod = modifier_base
wis_mod = modifier_base
cha_mod = modifier_base

#saving throws
proficient_saving_throws = []
saving_throw_adv = []

#damage adjustments
damage_resistance = []

#known languages
known_languages = ['Common']

#special traits
special_traits = []
dwarven_toughness = 0

#player race
player_race = base
player_subrace = base

#proficient gear
proficient_armor = []
proficient_weapons = []

#proficient skills
proficient_skills = []

#known spells
known_cantrips = []

#special functions
def d20():
    global roll_result
    roll_result = random.randint(1, 20)
    return roll_result

def lucky():
    global roll_result
    if roll_result == 1:
        reroll = input("Would you like to reroll using Lucky? ").lower()
        while reroll not in yes_l and reroll not in no_l:
            reroll = input("Would you like to reroll using Lucky? ").lower()
        if reroll in yes_l:
            roll_result = d20()