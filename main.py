#module imports
import random
from prettytable import PrettyTable

#global basic variables
base = 0
point_buy_starting_score = 8
point_buy_starting_mod = -1

#base scores
player_str_score = point_buy_starting_score
player_dex_score = point_buy_starting_score
player_con_score = point_buy_starting_score
player_int_score = point_buy_starting_score
player_wis_score = point_buy_starting_score
player_cha_score = point_buy_starting_score

#base modifiers
player_str_mod = point_buy_starting_mod
player_dex_mod = point_buy_starting_mod
player_con_mod = point_buy_starting_mod
player_int_mod = point_buy_starting_mod
player_wis_mod = point_buy_starting_mod
player_cha_mod = point_buy_starting_mod

#player base stats
player_speed = base
player_hp = base
player_languages = ["Common"]
player_prof_bonus = 2

#d20
def d20():
    global d20_result
    d20_result = random.randint(1,20)

#global lists
yes_l = ['yes', 'y']
no_l = ['no', 'n']
dwarf_subraces = ['Hill', 'Mountain']
elf_subraces = ['High', 'Wood', 'Drow']
halfling_subraces = ['Lightfoot', 'Stout']
all_languages = ['Abyssal', 'Celestial', 'Draconic', 'Deep Speech', 'Dwarvish', 'Elvish', 'Giant', 'Gnomish', 'Goblin', 'Halfling', 'Infernal', 'Orc', 'Primordial', 'Sylvan', 'Undercommon']

#weapon skeleton
class melee_weapon:
    def __init__(self, name, weapon_type, max_damage, finesse, light, versatile, two_handed, heavy, damage_type):
        self.name = name
        self.weapon_type = weapon_type
        self.max_damage = max_damage
        self.finesse = finesse
        self.light = light
        self.versatile = versatile
        self.two_handed = two_handed
        self.heavy = heavy
        self.damage_type = damage_type
class ranged_weapon:
    def __init__(self, name, weapon_type, max_damage, range, two_handed, light, damage_type):
        self.name = name
        self.weapon_type = weapon_type
        self.max_damage = max_damage
        self.range = range
        self.two_handed = two_handed
        self.light = light
        self.damage_type = damage_type

#breath weapon skeleton
class breath_weapon:
    def __init__(self, name, damage_type, max_damage, save_dc, range, shape):
        self.name = name
        self.damage_type = damage_type
        self.max_damage = max_damage
        self.save_dc = save_dc
        self.range = range
        self.shape = shape

#breath weapons
black_breath_weapon = breath_weapon("Black", "Acid", ([8 + player_con_mod + player_prof_bonus]), "DEX", 30, "Line")
blue_breath_weapon = breath_weapon("Blue", "Lightning", ([8 + player_con_mod + player_prof_bonus]), "DEX", 30, "Line")
brass_breath_weapon = breath_weapon("Brass", "Fire", ([8 + player_con_mod + player_prof_bonus]), "DEX", 30, "Line")
bronze_breath_weapon = breath_weapon("Bronze", "Lightning", ([8 + player_con_mod + player_prof_bonus]), "DEX", 30, "Line")
copper_breath_weapon = breath_weapon("Copper", "Acid", ([8 + player_con_mod + player_prof_bonus]), "DEX", 30, "Line")
gold_breath_weapon = breath_weapon("Gold", "Fire", ([8 + player_con_mod + player_prof_bonus]), "DEX", 15, "Cone")
green_breath_weapon = breath_weapon("Green", "Poison", ([8 + player_con_mod + player_prof_bonus]), "CON", 15, "Cone")
red_breath_weapon = breath_weapon("Red", "Fire", ([8 + player_con_mod + player_prof_bonus]), "DEX", 15, "Cone")
silver_breath_weapon = breath_weapon("Silver", "Cold", ([8 + player_con_mod + player_prof_bonus]), "CON", 15, "Cone")
white_breath_weapon = breath_weapon("White", "Cold", ([8 + player_con_mod + player_prof_bonus]), "CON", 15, "Cone")

#simple melee weapons
club = melee_weapon("Club", "Simple Melee", 4, "", "Light", "", "", "", "Bludgeoning")
dagger = melee_weapon("Dagger", "Simple Melee", 4, "Finesse", "Light", "", "", "", "Piercing")
greatclub = melee_weapon("Greatclub", "Simple Melee", 8, "", "", "", "Two Handed", "", "Bludgeoning")
handaxe = melee_weapon("Handaxe", "Simple Melee", 6, "", "Light", "", "", "", "Slashing")
javelin = melee_weapon("Javelin", "Simple Melee", 6, "", "",  "", "", "", "Piercing")
light_hammer = melee_weapon("Light Hammer", "Simple Melee", 4, "", "Light", "", "", "", "Bludgeoning")
mace = melee_weapon("Mace", "Simple Melee", 6, "", "", "", "", "", "Bludgeoning")
quarterstaff = melee_weapon("Quarterstaff", "Simple Melee", 8, "", "", "Versatile", "", "", "Bludgeoning")
sickle = melee_weapon("Sickle", "Simple Melee", 4, "", "Light", "", "", "", "Slashing")
spear = melee_weapon("Spear", "Simple Melee", 6, "", "", "Versatile", "", "", "Piercing")
unarmed_strike = melee_weapon("Unarmed Strike", "Simple Melee", player_str_mod, "", "", "", "", "", "Bludgeoning")
simple_melee_weapons = [club, dagger, greatclub, handaxe, javelin, light_hammer, mace, quarterstaff, sickle, unarmed_strike]

#simple ranged weapons
light_crossbow = ranged_weapon("Light Crossbow", "Simple Ranged", 8, 80, "Two Handed", "", "Piercing")
dart = ranged_weapon("Dart", "Simple Ranged", 4, 20, "", "", "Piercing")
shortbow = ranged_weapon("Shortbow", "Simple Ranged", 6, 80, "Two Handed", "", "Piercing")
sling = ranged_weapon("Sling", "Simple Ranged", 4, 30, "", "", "Bludgeoning")
simple_ranged_weapons = [light_crossbow, dart, shortbow, sling]

#martial melee weapons
battleaxe = melee_weapon("Battleaxe", "Martial Melee", 8, "", "", "Versatile", "", "", "Slashing")
flail = melee_weapon("Flail", "Martial Melee", 8, "", "", "", "", "", "Bludgeoning")
glaive = melee_weapon("Glaive", "Martial Melee", 10, "", "", "", "Two Handed", "Heavy", "Slashing")
greataxe = melee_weapon("Greataxe", "Martial Melee", 12, "", "", "", "Two Handed", "Heavy", "Slashing")
greatsword = melee_weapon("Greatsword", "Martial Melee", 12, "", "", "", "Two Handed", "Heavy", "Slashing")
halberd = melee_weapon("Halberd", "Martial Melee", 10, "", "", "", "Two Handed", "Heavy", "Slashing")
longsword = melee_weapon("Longsword", "Martial Melee", 8, "", "", "Versatile", "", "", "Slashing")
maul = melee_weapon("Maul", "Martial Melee", 12, "", "", "", "Two Handed", "Heavy", "Bludgeoning")
morningstar = melee_weapon("Morningstar", "Martial Melee", 8, "", "", "", "", "", "Piercing")
pike = melee_weapon("Pike", "Martial Melee", 10, "", "", "", "Two Handed", "Heavy", "Piercing")
rapier = melee_weapon("Rapier", "Martial Melee", 8, "Finesse", "", "", "", "", "Piercing")
scimitar = melee_weapon("Scimitar", "Martial Melee", 6, "Finesse", "Light", "", "", "", "Slashing")
shortsword = melee_weapon("Shortsword", "Martial Melee", 6, "Finesse", "Light", "", "", "", "Piercing")
trident = melee_weapon("Trident", "Martial Melee", 6, "", "", "Versatile", "", "", "Piercing")
warpick = melee_weapon("Warpick", "Martial Melee", 8, "", "", "", "", "", "Piercing")
warhammer = melee_weapon("Warhammer", "Martial Melee", 8, "", "", "Versatile", "", "", "Bludgeoning")
whip = melee_weapon("Whip", "Martial Melee", 4, "Finesse", "", "", "", "", "Slashing")

#martial ranged weapons
blowgun = ranged_weapon("Blowgun", "Martial Ranged", 1, 25, "", "", "")
crossbow_hand = ranged_weapon("Hand Crossbow", "Martial Ranged", 6, 30, "", "Light", "")
crossbow_heavy = ranged_weapon("Heavy Crossbow", "Martial Ranged", 10, 30, "Two Handed", "", "")
longbow = ranged_weapon("Longbow", "Martial Ranged", 8, 30, "Two Handed", "", "")

#armor skeleton
class armor:
    def __init__(self, name, armor_type, base_ac, stealth_disadv):
        self.name = name
        self.armor_type = armor_type
        self.base_ac = base_ac
        self.stealth_disadv = stealth_disadv

#light armor
padded_armor = armor("Padded Armor", "Light", 11, True)
leather_armor = armor("Leather Armor", "Light", 11, False)
studded_leather_armor = armor("Studded Leather Armor", "Light", 12, False)
light_armor = [padded_armor, leather_armor, studded_leather_armor]

#medium armor
hide_armor = armor("Hide Armor", "Medium", 12, False)
chain_shirt = armor("Chain Shirt", "Medium", 13, False)
scale_mail = armor("Scale Mail", "Medium", 14, True)
breastplate = armor("Breastplate", "Medium", 14, False)
half_plate = armor("Half Plate", "Medium", 15, True)
medium_armor = [hide_armor, chain_shirt, scale_mail, breastplate, half_plate]

#heavy armor
ring_mail = armor("Ring Mail", "Heavy", 14, True)
chain_mail = armor("Chain Mail", "Heavy", 16, True)
splint_armor = armor("Splint", "Heavy", 17, True)
plate_armor = armor("Plate Armor", "Heavy", 18, True)
heavy_armor = [ring_mail, chain_mail, splint_armor, plate_armor]

#shield
shield_bonus = 2
shield_prof = False

#spell skeleton
class spell:
    def __init__(self, name, level, range, max_damage, damage_type, saving_throw_type, condition):
        self.name = name
        self.level = level
        self.range = range
        self.max_damage = max_damage
        self.damage_type = damage_type
        self.saving_throw_type = saving_throw_type
        self.condition = condition

#wizard spells
class Spell:
    def __init__(self, name, level, spell_range, max_damage, damage_type, saving_throw_type, condition):
        self.name = name
        self.level = level
        self.spell_range = spell_range
        self.max_damage = max_damage
        self.damage_type = damage_type
        self.saving_throw_type = saving_throw_type
        self.condition = condition

#wizard spells
#cantrips
acid_splash = Spell("Acid Splash", 0, 60, 6, "Acid", "DEX", "")
chill_touch = Spell("Chill Touch", 0, 120, 8, "Necrotic", "", "Can't regain hit points")
fire_bolt = Spell("Fire Bolt", 0, 120, 10, "Fire", "", "")
light = Spell("Light", 0, 5, "", "", "", "")
mage_hand = Spell("Mage Hand", 0, 30, "", "", "", "")
minor_illusion = Spell("Minor Illusion", 0, 30, "", "", "", "")
poison_spray = Spell("Poison Spray", 0, 10, 12, "Poison", "CON", "")
prestidigitation = Spell("Prestidigitation", 0, 10, "", "", "", "")
ray_of_frost = Spell("Ray Of Frost", 0, 60, 8, "Cold", "none", "Speed reduced by 10 feet")
shocking_grasp = Spell("Shocking Grasp", 0, 5, 8, "Lightning", "", "Can't take reactions")
dancing_lights = Spell("Dancing Lights", 0, 120, "", "", "", "")
wizard_cantrips = [acid_splash.name, chill_touch.name, fire_bolt.name, light.name, mage_hand.name, minor_illusion.name, poison_spray.name, prestidigitation.name, ray_of_frost.name, shocking_grasp.name, dancing_lights.name]

#player spells
player_spells = []

#player weapon proficiencies
proficient_weapons = []

#player armor proficiencies
proficient_armor = []

#player skill proficiencies
proficient_skills = []

#player saving throw proficiencies
proficient_saving_throws = []

#player damage adjustments
damage_resistances = []
damage_immunities = []

#player special traits
player_darkvision = False
player_superior_darkvision = False
dwarven_toughness = False
fey_ancestry = False
mask_of_the_wild = False
lucky = False
naturally_stealthy = False

#ability score table
def modifier(score):
    global score_modifier
    if score == 1:
        score_modifier = -5
    elif score > 1 and score < 4:
        score_modifier = -4
    elif score > 3 and score < 6:
        score_modifier = -3
    elif score > 5 and score < 8:
        score_modifier = -2
    elif score > 7 and score < 10:
        score_modifier = -1
    elif score > 9 and score < 12:
        score_modifier = 0
    elif score > 11 and score < 14:
        score_modifier = 1
    elif score > 13 and score < 16:
        score_modifier = 2
    elif score > 15 and score < 18:
        score_modifier = 3
    elif score > 17 and score < 20:
        score_modifier = 4
    elif score > 19 and score < 22:
        score_modifier = 5
    elif score > 21 and score < 24:
        score_modifier = 6
    elif score > 23 and score < 26:
        score_modifier = 7
    elif score > 25 and score < 28:
        score_modifier = 8
    elif score > 27 and score < 30:
        score_modifier = 9
    else:
        score_modifier = 10

#player races
player_races = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Dragonborn', 'Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling']

#player classes
player_classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

#introduction
print("Welcome to the alpha release of 5e CLI!")

#get player name
player_name = input("Let's first start off with your name adventurer: ").title()
print("Welcome to the Forgotten Realms " + player_name + "!")

#explain point buy and assign cost values
print("Next, determine your stats.\nYou have 27 points to spend on your ability scores.\n Below are the values for each of the scores:\n ")
point_buy_scores = [15, 14, 13, 12, 11, 10, 9, 8]
point_buy_table = PrettyTable(["Score", "Cost"])
point_buy_table.add_row(["8", "0"])
point_buy_table.add_row(["9", "1"])
point_buy_table.add_row(["10", "2"])
point_buy_table.add_row(["11", "3"])
point_buy_table.add_row(["12", "4"])
point_buy_table.add_row(["13", "5"])
point_buy_table.add_row(["14", "7"])
point_buy_table.add_row(["15", "9"])
print(point_buy_table)

#player score assignment
player_points = 27
def score_assignment(score, modifier_choice):
    global output_score
    global player_points
    score_keep = False
    print("You currently have " + str(player_points) + " points.")
    while score_keep == False and player_points > 0:
        score = input("What would you like your " + modifier_choice + " to be? ")
        try:
            score = int(score)
        except ValueError:
            while type(score) != int:
                print("You must input an integer.")
                score = input("What would you like your " + modifier_choice + " to be? ")
                try:
                    score = int(score)
                except ValueError:
                    print("You must input an integer.")
        else:
            score = int(score)
        print(str(score))
        if score == 15 and player_points < 9:
            print("You do not have enough points to assign this value.")
            score_keep = False
        elif score == 15 and player_points >= 9:
            player_points -= 9
            score_keep = True
        elif score == 14 and player_points < 7:
            print("You do not have enough points to assign this value.")
            score_keep = False
        elif score == 14 and player_points >= 7:
            player_points -= 7
            score_keep = True
        elif score == 13 and player_points < 5:
            print("You do not have enough points to assign this value.")
            score_keep = False
        elif score == 13 and player_points >= 5:
            player_points -= 5
            score_keep = True
        elif score == 12 and player_points < 4:
            print("You do not have enough points to assign this value.")
            score_keep = False
        elif score == 12 and player_points >= 4:
            player_points -= 4
            score_keep = True
        elif score == 11 and player_points < 3:
            print("You do not have enough points to assign this value.")
            score_keep = False
        elif score == 11 and player_points >= 3:
            player_points -= 3
            score_keep = True
        elif score == 10 and player_points < 2:
            print("You do not have enough points to assign this value.")
            score_keep = False
        elif score == 10 and player_points >= 2:
            player_points -= 2
            score_keep = True
        elif score == 9 and player_points < 1:
            print("You do not have enough points to assign this value.")
            score_keep = False
        elif score == 9 and player_points >= 1:
            player_points -= 1
            score_keep = True
        elif score == 8 and player_points < 0:
            print("You do not have enough points to assign this value.")
            score_keep = False
        elif score == 8 and player_points >= 0:
            player_points -= 0
            score_keep = True
        elif score not in point_buy_scores:
            print("Select a value within point buy score table.")
        else:
            print("You have run out of points, keeping score 8 (-1)")
            score_keep = True
    if player_points == 0 and score_keep == False:
        score = 8
        print("You have run out of points, keeping " + modifier_choice + " score 8 (-1)")
    output_score = score

#strength score assignment
score_assignment(player_str_score, "Strength")
player_str_score = output_score
modifier(player_str_score)
player_str_mod = score_modifier

#dexterity score assignment
score_assignment(player_dex_score, "Dexterity")
player_dex_score = output_score
modifier(player_dex_score)
player_dex_mod = score_modifier

#constitution score assignment
score_assignment(player_con_score, "Consitution")
player_con_score = output_score
modifier(player_con_score)
player_con_mod = score_modifier

#intelligence score assignment
score_assignment(player_int_score, "Intelligence")
player_int_score = output_score
modifier(player_int_score)
player_int_mod = score_modifier

#wisdom score assignment
score_assignment(player_wis_score, "Widsom")
player_wis_score = output_score
modifier(player_wis_score)
player_wis_mod = score_modifier

#charisma score assignment
score_assignment(player_cha_score, "Charisma")
player_cha_score = output_score
modifier(player_cha_score)
player_cha_mod = score_modifier

#dwarf info
def dwarf_info():
    print("As a Dwarf you gain main features, they are listed below:")
    dwarf_feature_table = PrettyTable(["Feature", "Description"])
    dwarf_feature_table.add_row(["Ability Score Increase", "Your Constitution Score increases by 2."])
    dwarf_feature_table.add_row(["Speed", "Your base walking speed is 25 feet, which is not reduced by wearing heavy armor."])
    dwarf_feature_table.add_row(["Darkvision", "You can see in dim light within 60 feet of you in shades of grey."])
    dwarf_feature_table.add_row(["Dwarven Combat Training", "You gain Proficiency with the battleaxe, handaxe, light hammer, and warhammer."])
    dwarf_feature_table.add_row(["Languages", "You can speak, write, and read Common and Dwarvish."])
    print(dwarf_feature_table)
    print("Subrace information Below:")
    dwarf_subrace_feature_table = PrettyTable(["Subrace", "Feature", "Description"])
    dwarf_subrace_feature_table.add_row(["Hill Dwarf", "Ability Score Increase", "Your Constitution Score increases by 2."])
    dwarf_subrace_feature_table.add_row(["Hill Dwarf", "Dwarven Toughness", "Your hit point maxiumum increases by 1 and also by 1 every time you gain a level."])
    dwarf_subrace_feature_table.add_row(["Mountain Dwarf", "Ability Score Increase", "Your Strength Score increases by 2."])
    dwarf_subrace_feature_table.add_row(["Mountain Dwarf", "Dwarven Armor Training", "You have proficiency with light and medium armor."])
    print(dwarf_subrace_feature_table)

#dwarven traits
def dwarven_traits():
    global player_str_mod, player_wis_mod, light_armor, medium_armor, proficient_armor, proficient_weapons, player_con_mod, player_languages, player_speed, player_con_score, player_darkvision, dwarf_subrace, player_wis_score, player_str_score, dwarven_toughness
    #basic dwarf traits
    player_darkvision = True
    proficient_weapons += battleaxe, handaxe, light_hammer, warhammer
    player_con_score += 2
    modifier(player_con_score)
    player_con_mod = score_modifier
    player_speed = 25
    player_languages.append("Dwarvish")
    #subrace
    dwarf_subrace_information = input("Would you like to view subrace information? ").lower()
    while dwarf_subrace_information not in yes_l and dwarf_subrace_information not in no_l:
        dwarf_subrace_information = input("Would you like to view subrace information? ").lower()
    if dwarf_subrace_information in yes_l:
        dwarf_subrace_feature_table = PrettyTable(["Subrace", "Feature", "Description"])
        dwarf_subrace_feature_table.add_row(["Hill Dwarf", "Ability Score Increase", "Your Wisdom Score increased by 1."])
        dwarf_subrace_feature_table.add_row(["Hill Dwarf", "Dwarven Toughness", "Your hit point maxiumum increases by 1 and also by 1 every time you gain a level."])
        dwarf_subrace_feature_table.add_row(["Mountain Dwarf", "Ability Score Increase", "Your Strength Score increases by 2."])
        dwarf_subrace_feature_table.add_row(["Mountain Dwarf", "Dwarven Armor Training", "You have proficiency with light and medium armor."])
        print(dwarf_subrace_feature_table)
    dwarf_subrace = input("What subrace do you choose? (Hill or Mountain) ").title()
    while dwarf_subrace not in dwarf_subraces:
        dwarf_subrace = input("What subrace do you choose? (Hill or Mountain) ").title()
    #hill
    if dwarf_subrace == dwarf_subraces[0]:
        print("Welcome " + player_name + ", the Hill Dwarf!")
        player_wis_score += 1
        modifier(player_wis_score)
        player_wis_mod = score_modifier
        dwarven_toughness = True
    #dwarf
    else:
        print("Welcome " + player_name + ", the Mountain Dwarf!")
        player_str_score += 2
        modifier(player_str_score)
        player_str_mod = score_modifier
        proficient_armor += light_armor, medium_armor 

#elf info
def elf_info():
    print("As an Elf you gain main features, they are listed below:")
    elf_feature_table = PrettyTable(["Feature", "Description"])
    elf_feature_table.add_row(["Ability Score Increase", "Your Dexterity Score increases by 2."])
    elf_feature_table.add_row(["Speed", "Your base walking speed is 30 feet."])
    elf_feature_table.add_row(["Darkvision", "You can see in dim light within 60 feet of you in shades of grey."])
    elf_feature_table.add_row(["Keen Senses", "You gain Proficiency in the Perception skill."])
    elf_feature_table.add_row(["Fey Ancestry", "You have advantage against being charmed and magic can't put you to sleep."])
    elf_feature_table.add_row(["Languages", "You can speak, write, and read Common and Elvish."])
    print(elf_feature_table)
    print("Subrace information Below:")
    elf_subrace_feature_table = PrettyTable(["Subrace", "Feature", "Description"])
    elf_subrace_feature_table.add_row(["High Elf", "Ability Score Increase", "Your Intelligence Score increases by 1."])
    elf_subrace_feature_table.add_row(["High Elf", "Elf Weapon Training", "You have proficiency with the longsword, shortsword, shortbow and longbow."])
    elf_subrace_feature_table.add_row(["High Elf", "Cantrip", "You know one cantrip from the Wizard spell list. Intelligence is your spellcasting ability for it."])
    elf_subrace_feature_table.add_row(["High Elf", "Extra Language", "You can speak, read and write one extra language of your choice."])
    elf_subrace_feature_table.add_row(["Wood Elf", "Ability Score Increase", "Your Widsom Score increases by 1."])
    elf_subrace_feature_table.add_row(["Wood Elf", "Elf Weapon Training", "You have proficiency with the longsword, shortsword, shortbow and longbow."])
    elf_subrace_feature_table.add_row(["Wood Elf", "Fleet of Foot", "Your base walking speed increases to 35 feet."])
    elf_subrace_feature_table.add_row(["Wood Elf", "Mask of the Wild", "You can hide while only being lightly obscured."])
    elf_subrace_feature_table.add_row(["Drow", "Ability Score Increase", "Your Charisma score inscreases by 1."])
    elf_subrace_feature_table.add_row(["Drow", "Superior Darkvision", "Your darkvision has a radius of 120 feet."])
    elf_subrace_feature_table.add_row(["Drow", "Drow Magic", "You learn the dancing lights cantrip.\nWhen you reach 3rd level you can cast the faerie fire spell once per day.\nWhen you reach 5th level you can cast the Darkness spell. Charisma is your spellcasting ability for these spells."])
    elf_subrace_feature_table.add_row(["Drow", "Drow Weapon Training", "You have proficiency with rapiers, shortswords and hand crossbows."])
    print(elf_subrace_feature_table)

#elven traits
def elven_traits():
    global player_cha_mod, player_cha_score, mask_of_the_wild, player_wis_mod, player_wis_score, proficient_weapons, player_int_mod, player_darkvision, perception_prof, player_dex_mod, player_speed, player_dex_score, player_languages, fey_ancestry, proficient_saving_throws, player_int_score
    #basic elf traits
    player_darkvision = True
    perception_prof = True
    fey_ancestry = True
    proficient_saving_throws.append("Charmed")
    player_dex_score += 2
    modifier(player_dex_score)
    player_dex_mod = score_modifier
    player_speed = 30
    player_languages.append("Elvish")
    #subrace
    elf_subrace_information = input("Would you like to view subrace information? ").lower()
    while elf_subrace_information not in yes_l and elf_subrace_information not in no_l:
        elf_subrace_information = input("Would you like to view subrace information? ").lower()
    if elf_subrace_information in yes_l:
        print("Subrace information Below:")
        elf_subrace_feature_table = PrettyTable(["Subrace", "Feature", "Description"])
        elf_subrace_feature_table.add_row(["High Elf", "Ability Score Increase", "Your Intelligence Score increases by 1."])
        elf_subrace_feature_table.add_row(["High Elf", "Elf Weapon Training", "You have proficiency with the longsword, shortsword, shortbow and longbow."])
        elf_subrace_feature_table.add_row(["High Elf", "Cantrip", "You know one cantrip from the Wizard spell list. Intelligence is your spellcasting ability for it."])
        elf_subrace_feature_table.add_row(["High Elf", "Extra Language", "You can speak, read and write one extra language of your choice."])
        elf_subrace_feature_table.add_row(["Wood Elf", "Ability Score Increase", "Your Widsom Score increases by 1."])
        elf_subrace_feature_table.add_row(["Wood Elf", "Elf Weapon Training", "You have proficiency with the longsword, shortsword, shortbow and longbow."])
        elf_subrace_feature_table.add_row(["Wood Elf", "Fleet of Foot", "Your base walking speed increases to 35 feet."])
        elf_subrace_feature_table.add_row(["Wood Elf", "Mask of the Wild", "You can hide while only being lightly obscured."])
        elf_subrace_feature_table.add_row(["Drow", "Ability Score Increase", "Your Charisma score inscreases by 1."])
        elf_subrace_feature_table.add_row(["Drow", "Superior Darkvision", "Your darkvision has a radius of 120 feet."])
        elf_subrace_feature_table.add_row(["Drow", "Drow Magic", "You learn the dancing lights cantrip.\nWhen you reach 3rd level you can cast the faerie fire spell once per day.\nWhen you reach 5th level you can cast the Darkness spell. Charisma is your spellcasting ability for these spells."])
        elf_subrace_feature_table.add_row(["Drow", "Drow Weapon Training", "You have proficiency with rapiers, shortswords and hand crossbows."])
        print(elf_subrace_feature_table)
    elf_subrace = input("What subrace do you choose? (High, Wood, or Drow) ").title()
    while elf_subrace not in elf_subraces:
        elf_subrace = input("What subrace do you choose? (High, Wood, or Drow) ").title()
    #high elf
    if elf_subrace == elf_subraces[0]:
        print("Welcome " + player_name + ", the High Elf!")
        player_int_score += 1
        modifier(player_int_score)
        player_int_mod = score_modifier
        proficient_weapons += longsword, shortsword, shortbow, longbow
        print(wizard_cantrips)
        cantrip_choice = input("What cantrip would you like? ").title()
        while cantrip_choice not in wizard_cantrips:
            print(wizard_cantrips)
            cantrip_choice = input("What cantrip would you like? ").title()
        if cantrip_choice == acid_splash.name:
            player_spells.append(acid_splash)
        elif cantrip_choice == chill_touch.name:
            player_spells.append(chill_touch)
        elif cantrip_choice == fire_bolt.name:
            player_spells.append(fire_bolt)    
        elif cantrip_choice == light.name:
            player_spells.append(light)
        elif cantrip_choice == mage_hand.name:
            player_spells.append(mage_hand)
        elif cantrip_choice == minor_illusion.name:
            player_spells.append(minor_illusion)
        elif cantrip_choice == poison_spray.name:
            player_spells.append(poison_spray)
        elif cantrip_choice == prestidigitation.name:
            player_spells.append(prestidigitation)
        elif cantrip_choice == ray_of_frost.name:
            player_spells.append(ray_of_frost)
        elif cantrip_choice == shocking_grasp.name:
            player_spells.append(shocking_grasp)
        print(cantrip_choice + ", a fine cantrip!")
        print(all_languages)
        language_choice = input("What language would you like to learn? ").title()
        if language_choice == all_languages[5]:
            while language_choice == all_languages[5]:
                print("You already know elvish, what language would you like choose?")
                print(all_languages)
                language_choice = input("What language would you like to learn? ").title()
        while language_choice not in all_languages:
            print(all_languages)
            language_choice = input("What language would you like to learn? ").title()
        player_languages.append(language_choice)
    #wood elf
    elif elf_subrace == elf_subraces[1]:
        print("Welcome " + player_name + ", the Wood Elf!")
        player_wis_score += 1
        modifier(player_wis_score)
        player_wis_mod = score_modifier
        proficient_weapons += longsword, shortsword, shortbow, longbow
        player_speed = 35
        mask_of_the_wild = True
    #drow
    else:
        print("Welcome " + player_name + ", the Drow!")
        player_cha_score += 1
        modifier(player_cha_score)
        player_cha_mod = score_modifier
        player_spells.append(dancing_lights)
        proficient_weapons += rapier, shortsword, crossbow_hand

#halfling info
def halfling_info():
    print("As a Halfling you gain main features, they are listed below:")
    halfling_feature_table = PrettyTable(["Feature", "Description"])
    halfling_feature_table.add_row(["Ability Score Increase", "Your Dexterity Score increases by 2."])
    halfling_feature_table.add_row(["Speed", "Your base walking speed is 25 feet."])
    halfling_feature_table.add_row(["Lucky", "When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll and must use the new die."])
    halfling_feature_table.add_row(["Brave", "You have advantage on saving throws against being frightened."])
    halfling_feature_table.add_row(["Languages", "You can speak, write, and read Common and Halfling."])
    print(halfling_feature_table)
    print("Subrace information Below:")
    halfling_subrace_feature_table = PrettyTable(["Subrace", "Feature", "Description"])
    halfling_subrace_feature_table.add_row(["Lightfoot", "Ability Score Increase", "Your Charisma Score increases by 1."])
    halfling_subrace_feature_table.add_row(["Lightfoot", "Naturally Stealthy", "You can attempt tp hide as long as one of your party members is within 5 feet of you."])
    halfling_subrace_feature_table.add_row(["Stout", "Ability Score Increase", "Your Constitution score increases by 1."])
    halfling_subrace_feature_table.add_row(["Stout", "Stout Resilience", "You have advantage on saving throws against poison, and you have resistance to poison damage."])
    print(halfling_subrace_feature_table)

#halfling traits
def halfling_traits():
    global player_dex_score, player_dex_mod, player_speed, lucky, player_cha_score, player_cha_mod, naturally_stealthy, player_con_score, player_con_mod
    #basic halfling traits
    player_dex_score += 2
    modifier(player_dex_score)
    player_dex_mod = score_modifier
    player_speed = 25
    lucky = True
    proficient_saving_throws.append("Frightened")
    #subrace
    halfling_subrace_information = input("Would you like to view subrace information? ").lower()
    while halfling_subrace_information not in yes_l and halfling_subrace_information not in no_l:
        halfling_subrace_information = input("Would you like to view subrace information? ").lower()
    if halfling_subrace_information in yes_l:
        print("Subrace information Below:")
        halfling_subrace_feature_table = PrettyTable(["Subrace", "Feature", "Description"])
        halfling_subrace_feature_table.add_row(["Lightfoot", "Ability Score Increase", "Your Charisma Score increases by 1."])
        halfling_subrace_feature_table.add_row(["Lightfoot", "Naturally Stealthy", "You can attempt tp hide as long as one of your party members is within 5 feet of you."])
        halfling_subrace_feature_table.add_row(["Stout", "Ability Score Increase", "Your Constitution score increases by 1."])
        halfling_subrace_feature_table.add_row(["Stout", "Stout Resilience", "You have advantage on saving throws against poison, and you have resistance to poison damage."])
        print(halfling_subrace_feature_table)
    halfling_subrace = input("What subrace do you choose? (Lightfoot or Stout) ").title()
    while halfling_subrace not in halfling_subraces:
        halfling_subrace = input("What subrace do you choose? (Lightfoot or Stout) ").title()
    #lightfoot
    if halfling_subrace == halfling_subraces[0]:
        print("Welcome " + player_name + ", the Lightfoot Halfling!")
        player_cha_score += 1
        modifier(player_cha_score)
        player_cha_mod = score_modifier
        naturally_stealthy = True
    else:
        print("Welcome " + player_name + ", the Stout Halfling!")
        player_con_score += 1
        modifier(player_con_score)
        player_con_mod = score_modifier
        proficient_saving_throws.append("Poison")
        damage_resistances.append("Poison")

#human info
def human_info():
    print("As a Human you gain main features, they are listed below:")
    human_feature_table = PrettyTable(["Feature", "Description"])
    human_feature_table.add_row(["Ability Score Increase", "Your ability scores each increase by 1."])
    human_feature_table.add_row(["Speed", "Your base walking speed is 30 feet."])
    human_feature_table.add_row(["Languages", "You can speak, write, and read Common and one extra language of your choice."])
    print(human_feature_table)

#human traits
def human_traits():
    global player_str_score, player_dex_score, player_con_score, player_int_score, player_wis_score, player_cha_score, player_str_mod, player_dex_mod, player_con_mod, player_int_mod, player_wis_mod, player_cha_mod, player_speed
    player_str_score += 1
    player_dex_score += 1
    player_con_score += 1
    player_int_score += 1
    player_wis_score += 1
    player_cha_score += 1
    modifier(player_str_score)
    player_str_mod = score_modifier
    modifier(player_dex_score)
    player_dex_mod = score_modifier
    modifier(player_con_score)
    player_con_mod = score_modifier
    modifier(player_int_score)
    player_int_mod = score_modifier
    modifier(player_wis_score)
    player_wis_mod = score_modifier
    modifier(player_cha_score)
    player_cha_mod = score_modifier
    player_speed = 30
    print(all_languages)
    language_choice = input("What language would you like to learn? ").title()
    while language_choice not in all_languages:
        print(all_languages)
        language_choice = input("What language would you like to learn? ").title()
    player_languages.append(language_choice)

#dragonborn info
def dragonborn_info():
    global draconic_ancestry_list
    draconic_ancestry_list = ["Black", "Blue", "Brass", "Bronze", "Copper", "Gold", "Green", "Red", "Silver", "White"]
    print("As a Dragonborn you gain main features, they are listed below:")
    dragonborn_feature_table = PrettyTable(["Feature", "Description"])
    dragonborn_feature_table.add_row(["Ability Score Increase", "Your Strength score increases by 2, and your Charisma score increases by 1."])
    dragonborn_feature_table.add_row(["Speed", "Your base walking speed is 30 feet."])
    dragonborn_feature_table.add_row(["Draconic Ancestry", "Choose one type from the Draconic Ancestry table below. Your breath weapon and resistance use this typle."])
    dragonborn_feature_table.add_row(["Languages", "You can speak, read and write Common and Draconic."])
    print(dragonborn_feature_table)
    draconic_ancestry_feature_table = PrettyTable(["Dragon", "Damage Type", "Save Type", "Range", "Shape"])
    draconic_ancestry_feature_table.add_row(["Black", "Acid", "Dex", "30ft", "Line"])
    draconic_ancestry_feature_table.add_row(["Blue", "Lightning", "DEX", "30ft", "Line"])
    draconic_ancestry_feature_table.add_row(["Brass", "Fire", "DEX", "30ft", "Line"])
    draconic_ancestry_feature_table.add_row(["Bronze", "Lightning", "DEX", "30ft", "Line"])
    draconic_ancestry_feature_table.add_row(["Copper", "Acid", "DEX", "30ft", "Line"])
    draconic_ancestry_feature_table.add_row(["Gold", "Fire", "DEX", "15ft", "Cone"])
    draconic_ancestry_feature_table.add_row(["Green", "Poison", "CON", "15ft", "Cone"])
    draconic_ancestry_feature_table.add_row(["Red", "Fire", "DEX", "15ft", "Cone"])
    draconic_ancestry_feature_table.add_row(["Silver", "Cold", "CON", "15ft", "Cone"])
    draconic_ancestry_feature_table.add_row(["White", "Cold", "CON", "15ft", "Cone"])
    print(draconic_ancestry_feature_table)

#dragonborn traits
def dragonborn_traits():
    global player_str_score, player_str_mod, player_cha_score, player_cha_mod, plr_breath_weapon
    player_str_score += 2
    modifier(player_str_score)
    player_str_mod = score_modifier
    player_cha_score += 1
    modifier(player_cha_score)
    player_cha_mod = score_modifier
    ancestry_table = input("Would you like to see the draconic ancestry table? ").lower()
    while ancestry_table not in yes_l and ancestry_table not in no_l:
        ancestry_table = input("Would you like to see the draconic ancestry table? ").lower()
    if ancestry_table in yes_l:
        draconic_ancestry_feature_table = PrettyTable(["Dragon", "Damage Type", "Save Type", "Range", "Shape"])
        draconic_ancestry_feature_table.add_row(["Black", "Acid", "Dex", "30ft", "Line"])
        draconic_ancestry_feature_table.add_row(["Blue", "Lightning", "DEX", "30ft", "Line"])
        draconic_ancestry_feature_table.add_row(["Brass", "Fire", "DEX", "30ft", "Line"])
        draconic_ancestry_feature_table.add_row(["Bronze", "Lightning", "DEX", "30ft", "Line"])
        draconic_ancestry_feature_table.add_row(["Copper", "Acid", "DEX", "30ft", "Line"])
        draconic_ancestry_feature_table.add_row(["Gold", "Fire", "DEX", "15ft", "Cone"])
        draconic_ancestry_feature_table.add_row(["Green", "Poison", "CON", "15ft", "Cone"])
        draconic_ancestry_feature_table.add_row(["Red", "Fire", "DEX", "15ft", "Cone"])
        draconic_ancestry_feature_table.add_row(["Silver", "Cold", "CON", "15ft", "Cone"])
        draconic_ancestry_feature_table.add_row(["White", "Cold", "CON", "15ft", "Cone"])
        print(draconic_ancestry_feature_table)
    else:
        print(draconic_ancestry_list)
        ancestry_pick = input("Which ancestry would you like to choose? ").title()
        while ancestry_pick not in draconic_ancestry_list:
            print(draconic_ancestry_list)
            ancestry_pick = input("Which ancestry would you like to choose? ")
        if ancestry_pick == draconic_ancestry_list[0]:
            damage_resistances.append("Acid")
            plr_breath_weapon = black_breath_weapon
        elif ancestry_pick == draconic_ancestry_list[1]:
            damage_resistances.append("Lightning")
            plr_breath_weapon = blue_breath_weapon
        elif ancestry_pick == draconic_ancestry_list[2]:
            damage_resistances.append("Fire")
            plr_breath_weapon = brass_breath_weapon
        elif ancestry_pick == draconic_ancestry_list[3]:
            damage_resistances.append("Lightning")
            plr_breath_weapon = bronze_breath_weapon
        elif ancestry_pick == draconic_ancestry_list[4]:
            damage_resistances.append("Acid")
            plr_breath_weapon = copper_breath_weapon
        elif ancestry_pick == draconic_ancestry_list[5]:
            damage_resistances.append("Fire")
            plr_breath_weapon = gold_breath_weapon
        elif ancestry_pick == draconic_ancestry_list[6]:
            damage_resistances.append("Poison")
            plr_breath_weapon = green_breath_weapon
        elif ancestry_pick == draconic_ancestry_list[7]:
            damage_resistances.append("Fire")
            plr_breath_weapon = red_breath_weapon
        elif ancestry_pick == draconic_ancestry_list[8]:
            damage_resistances.append("Cold")
            plr_breath_weapon = silver_breath_weapon
        else:
            damage_resistances.append("Cold")
            plr_breath_weapon = white_breath_weapon

#gnome info
def gnome_info():
    print("As a Gnome you gain main features, they are listed below:")
    gnome_feature_table = PrettyTable(["Feature", "Description"])
    gnome_feature_table.add_row(["Ability Score Increase", "Your Intelligence Score increases by 2."])
    gnome_feature_table.add_row(["Speed", "Your base walking speed is 25 feet."])
    gnome_feature_table.add_row(["Darkvision", "You can see in dim light within 60 feet of you in shades of grey."])
    gnome_feature_table.add_row(["Gnome Cunning", "You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic."])
    gnome_feature_table.add_row(["Languages", "You can speak, write, and read Common and Gnomish."])
    print(gnome_feature_table)
    print("Subrace information Below:")
    gnome_subrace_feature_table = PrettyTable(["Subrace", "Feature", "Description"])
    gnome_subrace_feature_table.add_row(["Forest", "Ability Score Increase", "Your Dexterity Score increases by 1."])
    gnome_subrace_feature_table.add_row(["Forest", "Natural Illusion", "You know the Minor Illusion cantrip. Intelligence is your modifier for it."])
    gnome_subrace_feature_table.add_row(["Rock", "Ability Score Increase", "Your Constitution score increases by 1."])
    gnome_subrace_feature_table.add_row(["Rock", "Artificer's Lore", "Whenever you make a History check related to magic items, alchemical objects, or devices, you can add double proficieny bonus."])
    gnome_subrace_feature_table.add_row(["Rock", "Tinker", "You can use tinker's tools to create a small toy that can give advantage on Performance checks."])
    print(gnome_subrace_feature_table)

#gnome traits
def gnome_traits():
    global player_int_score, player_int_mod
    player_int_score += 2
    modifier(player_int_score)
    player_int_mod = score_modifier

#get player race
race_explanation = input("Would you like to see race information? ").lower()
while race_explanation not in yes_l and race_explanation not in no_l:
    race_explanation = input("Would you like to see race information? ").lower()
if race_explanation in yes_l:
    race_explanation = True
else:
    race_explanation = False
while race_explanation == True:
    race_explanation_category = input("Which race would you like to view? (Dwarf, Elf, Halfling, Human, Dragonborn, Gnome, Half-Elf, Half-Orc, Tiefling) ").title()
    while race_explanation_category not in player_races:
        print(player_races)
        race_explanation_category = input("Which race would you like to view? ").title()
    if race_explanation_category == player_races[0]:
        dwarf_info()
        race_info_completed = input("Would you like to view another race? ").lower()
        while race_info_completed not in yes_l and race_info_completed not in no_l:
            race_info_completed = input("Would you like to view another race? ").lower()
        if race_info_completed in no_l:
            race_explanation = False
    elif race_explanation_category == player_races[1]:
        elf_info()
        race_info_completed = input("Would you like to view another race? ").lower()
        while race_info_completed not in yes_l and race_info_completed not in no_l:
            race_info_completed = input("Would you like to view another race? ").lower()
        if race_info_completed in no_l:
            race_explanation = False
    elif race_explanation_category == player_races[2]:
        halfling_info()
        race_info_completed = input("Would you like to view another race? ").lower()
        while race_info_completed not in yes_l and race_info_completed not in no_l:
            race_info_completed = input("Would you like to view another race? ").lower()
        if race_info_completed in no_l:
            race_explanation = False
    elif race_explanation_category == player_races[3]:
        human_info()
        race_info_completed = input("Would you like to view another race? ").lower()
        while race_info_completed not in yes_l and race_info_completed not in no_l:
            race_info_completed = input("Would you like to view another race? ").lower()
        if race_info_completed in no_l:
            race_explanation = False
    elif race_explanation_category == player_races[4]:
        dragonborn_info()
        race_info_completed = input("Would you like to view another race? ").lower()
        while race_info_completed not in yes_l and race_info_completed not in no_l:
            race_info_completed = input("Would you like to view another race? ").lower()
        if race_info_completed in no_l:
            race_explanation = False
    elif race_explanation_category == player_races[5]:
        gnome_info()
        race_info_completed = input("Would you like to view another race? ").lower()
        while race_info_completed not in yes_l and race_info_completed not in no_l:
            race_info_completed = input("Would you like to view another race? ").lower()
        if race_info_completed in no_l:
            race_explanation = False

player_race = input("What is your race? (Dwarf, Elf, Halfling, Human, Dragonborn, Gnome, Half-Elf, Half-Orc, Tiefling) ").title()
while player_race not in player_races:
    player_race = input("What is your race? (Dwarf, Elf, Halfling, Human, Dragonborn, Gnome, Half-Elf, Half-Orc, Tiefling) ").title()
print("So you've chosen " + player_race + ", a great choice!")
if player_race == player_races[0]:
    dwarven_traits() 
elif player_race == player_races[1]:
    elven_traits()
elif player_race == player_races[2]:
    halfling_traits()
elif player_race == player_races[3]:
    human_traits()
elif player_race == player_races[4]:
    dragonborn_traits()
elif player_race == player_races[5]:
    gnome_traits()