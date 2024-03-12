#spell skeleton
class spell:
    def __init__(self, name, casting_time, ranged, duration, saving_throw, damage, damage_type, effect, concentration):
        self.name = name
        self.casting_time = casting_time
        self.ranged = ranged
        self.duration = duration
        self.saving_throw = saving_throw
        self.damage = damage
        self.damage_type = damage_type
        self.effect = effect
        self.concentration = concentration

# #bard
# #cantrips
# blade_ward = spell("Blade Ward", "A", False, 1, None, None, None, "Resistance to bludgeoning, piercing, and slashing.", False)
# dancing_lights = spell("Dancing Lights", "A", True, 10, None, None, None, "Creates lights", True)
# friends = spell("Friends", "A", False, 10, None, None, None, "Advantage on all Charisma checks", True)
# light = spell("Light", "A", False, 600, None, None, None, "Objects emits bright light", False)
# mage_hand = spell("Mage Hand", "A", True, 10, None, None, None, "Create spectral hand", False)
# mending = spell("Mending", "A", False, 1, None, None, None, "Repair a break or tear in an object", False)
# message = spell("Message", "A", True, 1, None, None, None, "Send a short message", False)
# minor_illusion = spell("Minor Illusion", "A", False, 1, None, None, None, "Create a sound or an image", False)
# prestidigitation = spell("Prestidigitation", "A", False, 600, None, None, None, "Perform simple magical effects", False)
# thunderclap = spell("Thunderclap", "A", False, 1, "CON", 6, "Thunder", "Creates a burst of thunderous sound.", False)
# true_strike = spell("True Strike","A", True, 10, None, None, None, "Gain advantage on your first attack against one target", True)
# vicious_mockery = spell("Vicious Mockery", "A", True, 1, "WIS", 4, "Psychic", "Disadvantage on the next attack roll", False)
# bard_cantrips = [blade_ward, dancing_lights, friends, light, mage_hand, mending, message, minor_illusion, prestidigitation, true_strike, vicious_mockery]

# #level_1
# animal_friendship = spell("Animal Friendship","A", True, 14400, "WIS", None, None, "Convince a beast that you mean no harm.", False)
# bane = spell("Bane","A", True, 10, "CHA", None, None, "Up to three creatures have a disadvantage on attack rolls and saving throws", True)
# charm_person = spell("Charm Person", "A", "WIS", 600, "WIS", None, None, "Charm a humanoid", False)
# comprehend_languages = spell("Comprehend Languages", "A", False, 600, None, None, None, "Understand the meaning of any spoken language", False)
# cure_wounds = spell("Cure Wounds", "A", False, 1, None, None, None, "Creature you touch regains hp", False)
# detect_magic = spell("Detect Magic", "A", False, 60, None, None, None, "Sense the presence of magic within 30ft", True)
# disguise_self = spell("Disguise Self", "A", False, 600, None, None, None, "Make yourself look different", False)
# dissonent_whispers = spell("Dissonent Whispers", "A", True, 1, "WIS", 18, "Psychic", "Whisper a discordany melody", True)
# faerie_fire = spell("Faerie Fire", "A", True, 60, "DEX", None, None, "Any creature within a range is outlined in blue,green, or violet", True)
# feather_fall = spell("Feather Fall", "B", True, 10, None, None, None, "Up to 5 falling creatures slowly descend", False)
# healing_word = spell("Healing Word", "B", True, 1, None, None, None, "Creature of your choice regains HP", False)
# heroism = spell("Heroism", "A", False, 10, None, None, None, "A willing creature you touch is imbued with bravery", True)
# identify = spell("Identify", "R", False, 1, None, None, None, "If the item was created by a spell, you learn which spell created it.", False)
# illusory_script = spell("Illusory Script", "R", False, 144000, None, None, None, "You imbue illusion writtings on paper", False)
# longstrider = spell("Longstrider", "A", False, 600, None, None, None, "Speed increases by 10ft", False)
# silent_image = spell("Silent Image", "A", True, 60, None, None, None, "Create a purely visual image of an object or creature", True)
# sleep = spell("Sleep", "A", True, 10, None, None, None, "Sends creatures into a magical slumber", False)
# speak_with_animals = spell("Speak with Animals", "A", False, 100, None, None, None, "The ability to comprehend and verbally communicate with beasts", False)
# tashas_hideous_laughter = spell("Tasha's Hideous Laughter", "A", True, 10, "WIS", None, None, "A creature perceives everything as hilariously funny and falls into fits of laughter", True)
# thunderwave = spell("Thunderwave", "A", True, 1, "CONE", 16, "Thunder", "A wave of thunderous force sweeps out from you", False)
# unseen_servant = spell("Unseen Servant", "A", True, 600, None, None, None, "This spell creates an invisible, mindless, shapeless, Medium force", False)
# bard_level_1_spells = [animal_friendship, bane, charm_person, comprehend_languages, cure_wounds, detect_magic, disguise_self, dissonent_whispers, faerie_fire, feather_fall, healing_word, heroism, identify, illusory_script, longstrider, silent_image, sleep, speak_with_animals, tashas_hideous_laughter, thunderwave, unseen_servant]

# #level_2
# aid = spell("Aid", "A", True, 4800, None, None, None, "Your spell bolsters your allies with toughness and resolve", False)
# animal_messenger = spell("Animal Messenger", "A", True, 14400, None, None, None, "You use an animal to deliver a message",False)
# blindness_deafness = spell("Blindness/Deafness", "A", True, 1, "Cone", None, None, "You can blind or deafen a foe.", False)
# calm_emotions = spell("Calm Emotions", "A", True, 10, "CHA", None, None, "You attempt to suppress strong emotions in a group of people", True)
# cloud_of_daggers = spell("Cloud of Daggers", "A", True, 10, False, 16, "Slashing", "You fill the air with spinning daggers in a cube 5 feet on each side", True)
# crown_of_madness = spell("Crown of Madness", "A", True, 10, "WIS", None, None, "A twisted crown of jagged iron appears on humanoid of your choice", True)
# detect_thoughts = spell("Detect Thoughts", "A", False, 10, "WIS", None, None, "You can read the thoughts of certain creatures", True)
# enhance_ability = spell("Enhance Ability", "A", False, 600, None, None, None, "Bestow a magical enhancement", True)
# enthrall = spell("Enthrall", "A", True, 1, "WIS", None, None, "Weave a distracing string of words", False)
# gift_of_gab = spell("Gift of Gab", "B", False, 1, None, None, None, "Skillfully reshape the memories of listeners", False)
# heat_metal = spell("Heat Metal", "A", True, 10, False, 16, "Fire", "You cause the object to glow red-hot.", True)
# hold_person = spell("Hold Person", "A", True, 10, "WIS", None, None, "Choose a humanoid in range and paralyze", True)
# invisibility = spell("Invisibility", "A", False, 600, None, None, None, "Creature you touch becomes invisible", True)
# knock = spell("Knock", "A", True, 1, None, None, None, "A target that is held shut by a mundane lock or that is stuck or barred becomes unlocked", False)
# lesser_restoration = spell("Lesser Restoration", "A", False, 1, None, None, None, "You touch a creature and can end either one disease or one condition afflicting it.", False)
# locate_animals_or_plants = spell("Locate Animals or Plants", "A", False, 1, None, None, None, "You learn the direction and distance to the closest creature or plant", False)
# locate_object = spell("Locate Object", "A", False, 100, None, None, None, "Describe or name an object that is familiar to you", True)
# magic_mouth = spell("Magic Mouth", "R", True, 1, None, None, None, "You implant a message within an object in range, a message that is uttered when a trigger condition is met.", False)
# phantasmal_force = spell("Phantasmal Force", "A", True, 10, "INT", None, None, "You craft an illusion that takes root in the mind of a creature that you can see within range.", True)
# see_invisibility = spell("See Invisibiltiy", "A", False, 600, None, None, None, "For the duration, you see invisible creatures and objects as if they were visible", False)
# shatter = spell("Shatter", "A", True, 1, "CON", 24, "Thunder", "A sudden loud ringing noise, painfully intense, erupts from a point of your choice within range.", False)
# silence = spell("Silence", "A", True, 100, None, None, None, "No sound can be created within or pass through a 20-foot-radius sphere", True)
# suggestion = spell("Suggestion", "A", True, 4800, "WIS", None, None, "You suggest a course of activity (limited to a sentence or two) and magically influence a creature", True)
# zone_of_truth = spell("Zone of Truth", "A", True, 100, "CHA", None, None, "You create a magical zone that guards against deception ", False)
# bard_level_2_spells = [aid, animal_messenger, blindness_deafness, calm_emotions, cloud_of_daggers, crown_of_madness, detect_thoughts, enhance_ability, enthrall, gift_of_gab, heat_metal, hold_person, invisibility, knock, lesser_restoration, locate_animals_or_plants, locate_object, magic_mouth, phantasmal_force, see_invisibility, shatter, silence, suggestion, zone_of_truth]

# #level_3
# bestow_curse = spell("Bestow Curse", "A", False, 1, "WIS", None, None, "A creature becomes cursed for a duration", True)
# clairvoyance = spell("Clairvoyance", 10, True, 100, None, None, None, "You create an invisible sensor within range", True)
# dispel_magic = spell("Dispel Magic", "A", True, 1, None, None, None, "Choose any creature, object, or magical effect within range to dispel", False)
# fear = spell("Fear", "A", False, 1, "WIS", None, None, "You project a phantasmal image of a creature’s worst fears.", True)
# feign_death = spell("Feign Death", "A", False, 600, None, None, None, "You touch a willing creature and put it into a cataleptic state that is indistinguishable from death.", False)
# glyph_of_warding = spell("Glyph of Warding", 600, False, 600, "DEX", None, None, "When you cast this spell, you inscribe a glyph that creates a magical effect triggered by other creatures", False)
# hypnotic_pattern = spell("Hypnotic Pattern", "A", True, 1, "WIS", None, None, "You create a twisting pattern of colors that weaves through the air inside a 30-foot cube within range", True)
# leomunds_tiny_hut = spell("Leomund's Tiny Hut", 1, False, 4800, None, None, None, "A 10-foot-radius immobile dome of force springs into existence", False)
# major_image = spell("Major Image", "A", True, 100, None, None, None, "You create the image of an object, a creature, or some other visible phenomenon that is no larger than a 20-foot cube", True)
# nondetection = spell("Nondetection", "A", False, 4800, None, None, None, "You hide a target that you touch from divination magic", False)
# plant_growth = spell("Plant Growth", "A", True, 1, None, None, None, "This spell channels vitality into plants within a specific area", False)
# sending = spell("Sending", "A", True, 1, None, None, None, "You send a short message of twenty-five words or less to a creature", False)
# speak_with_dead = spell("Speak with Dead", "A", True, 100, None, None, None, "You grant the semblance of life and intelligence to a corpse of your choice", False)
# speak_with_plants = spell("Speak with Plants", "A", True, 100, None, None, None, "You imbue plants within 30 feet of you with limited sentience and animation", False)
# stinking_cloud = spell("Stinking Cloud", "A", True, 1, "CON", None, None, "You create a 20-foot-radius sphere of yellow, nauseating gas", True)
# tongues = spell("Tongues", "A", False, 600, None, None, None, "Grants the creature you touch the ability to understand any spoken language", False)
# bard_level_3_spells = [bestow_curse, clairvoyance, dispel_magic, fear, feign_death, glyph_of_warding, hypnotic_pattern, leomunds_tiny_hut, major_image, nondetection, plant_growth, sending, speak_with_dead, speak_with_plants, stinking_cloud, tongues]

# #level_4
# compulsion = spell("Compulsion", "A", True, 1, "WIS", None, None, "A creature of your choice is affected by compulsion", True)
# confusion = spell("Confusion", "A", True, 1, "WIS", None, None, "This spell assaults and twists creatures’ minds, spawning delusions and provoking uncontrolled actions.", True)
# dimension_door = spell("Dimension Door", "A", True, 1, None, 24, "Force", "You teleport yourself from your current location to any other spot within range", False)
# freedom_of_movement = spell("Freedom of Movement", "A", False, 600, None, None, None, "Unaffected by difficult terrain, and spells and other magical effects", False)
# greater_invisibility = spell("Greater Invisibility", "A", False, 1, None, None, None, "You or a creature you touch becomes invisible until the spell ends", True)
# hallucinatory_terrain = spell("Hallucinatory Terrain", "A", True, 14400, None, None, None, "You make natural terrain in a 150-foot cube in range look, sound, and smell like some other sort of natural terrain", False)
# locate_creature = spell("Locate Creature", "A", False, 600, None, None, None, "You sense the direction to a creature’s location", True)
# polymorph = spell("Polymorph", "A", True, 600, "WIS", None, None, "This spell transforms a creature that you can see within range into a new form", True)
# bard_level_4_spells = [compulsion, confusion, dimension_door, freedom_of_movement, greater_invisibility, hallucinatory_terrain, locate_creature, polymorph]

# #level_5
# animate_objects = spell("Animate Object","A", True, 1, None, None, None, "Objects come to life at your command.", True)
# awaken = spell("Awaken", 4800, False, 1, None, None, None, "The target gains an Intelligence of 10", False)
# dominate_person = spell("Dominate Person","A", True, 1, "WIS", None, None, "You attempt to beguile a humanoid that you can see within range", True)
# dream = spell("Dream", 1, True, 4800, "WIS", None, None, "This spell shapes a creature’s dreams.", False)
# geas = spell("Geas", 1, True, 1440000, "WIS", 50, "Psychic", "You place a magical command on a creature", False)
# greater_restoration = spell("Greater Restoration","A", False, 1, None, None, None, "You imbue a creature you touch with positive energy to undo a debilitating effect", False)
# hold_monster = spell("Hold Monster","A", True, 1, "WIS", None, None, "Choose a creature to paralyze", True)
# legend_lore = spell("Legend Lore", 10, False, 1, None, None, None, "The spell brings to your mind a brief summary of the significant lore", False)
# mass_cure_wounds = spell("Mass Cure Wounds","A", True, 1, None, None, None, "A wave of healing energy washes out ", False)
# mislead = spell("Mislead","A", False, 1, None, None, None, "You become invisible at the same time that an illusory double of you appears", True)
# modify_memory = spell("Modify Memory","A", True, 1, "WIS", None, None, "You attempt to reshape another creature’s memories.", True)
# planar_binding = spell("Planar Binding", 60, True, 14400, "CHA", None, None, "With this spell, you attempt to bind a celestial, an elemental, a fey, or a fiend to your service", False)
# raise_dead = spell("Raise Dead","A", False, 1, None, None, None, "You return a dead creature you touch to life", False)
# scrying = spell("Scrying", 10, False, 10, "WIS", None, None, "You can see and hear a particular creature you choose that is on the same plane of existence as you", True)
# seeming = spell("Seeming","A", True, 4800, "CHA", None, None, "This spell allows you to change the appearance of any number of creatures", False)
# teleportation_circle = spell("Teleportation Circle", 1, True, 1, None, None, None, "Link your location to a permanent teleportation circle", False)
# bard__level_5_spells = [animate_objects, awaken, dominate_person, dream, geas, greater_restoration, hold_monster, legend_lore, mass_cure_wounds, mislead, modify_memory, planar_binding, raise_dead, scrying, seeming, teleportation_circle]

# #level_6
# eyebite = spell("Eyebite", "A", False, 1, "WIS", None, None, "Your eyes become an inky void imbued with dread power", True)
# find_the_path = spell("Find the Path", 1, False, 14400, None, None, None, "This spell allows you to find the shortest, most direct physical route", True)
# guards_and_wards = spell("Guards and Wards", 10, True, 14400, None, None, None, "You create a ward that protects up to 2,500 square feet of floor space", False)
# mass_suggestion = spell("Mass Suggestion", "A", True, 14400, "WIS", None, None, "You suggest a course of activity (limited to a sentence or two) and magically influence up to twelve creatures of your choice", False)
# ottos_irresistible_dance = spell("Otto's Irresistible Dance", "A", True, 1, "WIS", None, None, "A target begins a comic dance in place", True)
# programmed_illusion = spell("Programmed Illusion", "A", True, 1, None, None, None, "You create an illusion of an object, a creature, or some other visible phenomenon", False)
# true_seeing = spell("True Seeing", "A", False, 60, None, None, None, "This spell gives the willing creature you touch the ability to see things as they actually are", False)
# bard__level_6_spells = [eyebite, find_the_path, guards_and_wards, mass_suggestion, ottos_irresistible_dance, programmed_illusion, true_seeing]

# #level_7
# etherealness = spell("Etherealness", "A", False, 720, None, None, None, "You step into the border regions of the Ethereal Plane", False)
# forcecage = spell("Forcecage", "A", True, 60, "CHA", None, None, "An immobile, invisible, cube-shaped prison composed of magical force springs into existence", False)
# mirage_arcane = spell("Mirage Arcane", 10, True, 14400, None, None, None, "You make terrain in an area up to 1 mile square look, sound, smell, and even feel like some other sort of terrain", False)
# mordenkainens_magnificient_mansion = spell("Mordenkainen's Magnificient Mansion", "A", True, 14400, None, None, None, "You conjure an extradimensional dwelling", False)
# mordenkainens_sword = spell("Mordenkainen's Sword", "A", True, 1, None, 30, "Force", "You create a sword-shaped plane of force that hovers within range", True)
# project_image = spell("Project Image", "A", True, 14400, None, None, None, "You create an illusory copy of yourself that lasts for the duration", True)
# regenerate = spell("Regenerate", "A", False, 60, None, None, None, "You touch a creature and stimulate its natural healing ability", False)
# resurrection = spell("Resurrection", 60, False, 1, None, None, None, "Target returns to life with all its hit points", False)
# symbol = spell("Symbol", "A", False, 1, None, None, None, "When you cast this spell, you inscribe a harmful glyph", False)
# teleport = spell("Teleport", "A", True, 1, None, None, None, "This spell instantly transports you and up to eight willing creatures of your choice", False)
# bard__level_7_spells = [etherealness, forcecage, mirage_arcane, mordenkainens_magnificient_mansion, mordenkainens_sword, project_image, regenerate, resurrection, symbol, teleport]

# #level_8
# dominate_monster = spell("Dominate Monster", "A", True, 60, "WIS", None, None, "You attempt to beguile a creature that you can see within range", True)
# feeblemind = spell("Feeblemind", "A", True, 1, "INT", None, None, "You blast the mind of a creature that you can see within range", False)
# glibness = spell("Glibness", "A", False, 60, None, None, None, "Until the spell ends, when you make a Charisma check, you can replace the number you roll with a 15", False)
# mind_blank = spell("Mind Blank", "A", False, 14400, None, None, None, "Until the spell ends, one willing creature you touch is immune to psychic damage", False)
# power_word_stun = spell("Power Word Stun", "A", True, 1, "CON", None, None, "You speak a word of power that can overwhelm the mind of one creature you can see within range", False)
# bard__level_8_spells = [dominate_monster, feeblemind, glibness, mind_blank, power_word_stun]

# #level_9
# foresight = spell("Foresight", "A", False, 480, None, None, None, "You touch a willing creature and bestow a limited ability to see into the immediate future", False)
# power_word_heal = spell("Power Word Heal", "A", None, 1, False, None, None, "A wave of healing energy washes over a creature you touch.", False)
# power_word_kill = spell("Power Word Kill", "A", True, 1, None, 100, "Spell", "You utter a word of power that can kill instantly, 100hp or fewer", False)
# true_polymorph = spell("True Polymorph", "A", True, 60, "WIS", None, None, "Transform the creature into a different creature, the creature into a nonmagical object, or the object into a creature", True)
# bard__level_9_spells = [foresight, power_word_heal, power_word_kill, true_polymorph]

# #cleric
# #cantrips
# guidance = spell("Guidance", "A", False, 1, None, None, None, " Roll a d4 and add to one ability check", True)
# resistance = spell("Resistance", "A", False, 1, None, None, None, "Roll d4 and add to one saving throw", True)
# sacred_flame = spell("Sacred Flame", "A", True, 1, "DEX", 8, "Radiant", "Flame-like radiance descends on a creature", False)
# spare_the_dying = spell("Spare the Dying", "A", False, 1, None, None, None, "Creature at 0hp becomes stable", False)
# thaumaturgy = spell("Thaumaturgy", "A", True, 1, None, None, None, "You manifest a minor wonder", False)
# cleric_cantrips = [guidance, light, mending, resistance, sacred_flame, spare_the_dying, thaumaturgy]

# #level_1
# bless = spell("Bless", "A", True, 1, None, None, None, "You bless up to three creatures", True)
# command = spell("Command", "A", True, 1, "WIS", None, None, "You speak a one-word command to a creature", False)
# create_or_destroy_water = spell("Create or Destroy Water", "A", True, 1, None, None, None, "You either create or destroy water.", False)
# detect_evil_and_good = spell("Detect Evil and Good", "A", True, 10, None, None, None, "You detect aberrations, celestials, elementals, fey, fiends, or undead within 30ft", True)
# detect_poison_and_disease = spell("Detect Poison and Disease", "A", True, 10, None, None, None, "Sense poisons, poisonous creatures, and diseases", True)
# guiding_bolt = spell("Guiding Bolt", "A", True, 1, None, 24, "Radiant", "A flash of light streaks toward a creature of your choice", False)
# inflict_wounds = spell("Inflict Wounds", "A", False, 1, None, 30, "Necrotic", "On a hit deal necrotic damage", False)
# protection_from_evil_and_good = spell("Protection from Evil and Good", "A", False, 10, None, None, None, "Protected against aberrations, celestials, elementals, fey, fiends, and undead", True)
# purify_food_and_drink = spell("Purify Food and Drink", "A", True, 1, None, None, None,"All nonmagical food and drink is purified", False)
# sanctuary = spell("Santuary", "B", True, 1, "WIS", None, None, "You ward a creature within range against attack", False)
# shield_of_faith = spell("Shield of Faith", "B", True, 10, None, None, None, "A shimmering field appears and surrounds a creature", True)
# cleric_level_1_spells = [bane, bless, command, create_or_destroy_water, cure_wounds, detect_evil_and_good, detect_magic, detect_poison_and_disease, guiding_bolt, healing_word, inflict_wounds, protection_from_evil_and_good, purify_food_and_drink, sanctuary, shield_of_faith]

# #level_2
# augury = spell("")
# continual_flame = spell("")
# find_traps = spell("")
# gentle_repose = spell("")
# prayer_of_healing = spell("")
# protection_from_poison = spell("")
# spiritual_weapon = spell("")
# warding_bond = spell("")
# cleric_level_2_spells = [aid, augury, blindness_deafness, calm_emotions, continual_flame, enhance_ability, find_traps, gentle_repose, hold_person, lesser_restoration, locate_object, prayer_of_healing, protection_from_poison, silence, spiritual_weapon, warding_bond, zone_of_truth]

# #level_3
# animate_dead = spell("")
# beacon_of_hope = spell("")
# create_food_and_water = spell("")
# daylight = spell("")
# magic_circle = spell("")
# mass_healing_word = spell("")
# meld_into_stone = spell("")
# protection_from_energy = spell("")
# remove_curse = spell("")
# revivify = spell("")
# spirit_guardians = spell("")
# water_walk = spell("")
# cleric_level_3_spells = [animate_dead, beacon_of_hope, bestow_curse, clairvoyance, create_food_and_water, daylight, dispel_magic, feign_death, glyph_of_warding, magic_circle, mass_healing_word, meld_into_stone, protection_from_energy, remove_curse, revivify, sending, speak_with_dead]

# #level_4
# banishment = spell("")
# control_water = spell("")
# death_ward = spell("")
# divination = spell("")
# guardian_of_faith = spell("")
# stone_shape = spell("")
# cleric_level_4_spells = [banishment, control_water, death_ward, divination, guardian_of_faith, stone_shape]

# #level_5
# commune = spell("")
# contagion = spell("")
# dispel_evil_and_good = spell("")
# flame_strike = spell("")
# hallow = spell("")
# insect_plague = spell("")
# cleric_level_5_spells = [commune, contagion, dispel_evil_and_good, flame_strike, geas, greater_restoration, hallow, insect_plague, legend_lore, mass_cure_wounds, planar_binding, raise_dead, scrying]

# #level_6
# blade_barrier = spell("")
# create_undead = spell("")
# forbiddence = spell("")
# harm = spell("")
# heal = spell("")
# heroes_feast = spell("")
# planar_ally = spell("")
# word_of_recall = spell("")
# cleric_level_6_spells = [blade_barrier, create_undead, find_the_path, forbiddence, harm, heal, heroes_feast, planar_ally, true_seeing, word_of_recall]

# #level_7
# conjure_celestial = spell("")
# divine_word = spell("")
# fire_storm = spell("")
# plane_shift = spell("")
# cleric_level_7_spells = [conjure_celestial, divine_word, etherealness, fire_storm, plane_shift, regenerate, resurrection, symbol]

# #level_8
# antimagic_field = spell("")
# control_weather = spell("")
# earthquake = spell("")
# holy_aura = spell("")
# cleric_level_8_spells = [antimagic_field, control_weather, earthquake, holy_aura]

# #level_9
# astral_projection = spell("")
# gate = spell("")
# mass_heal = spell("")
# true_resurrection = spell("")
# cleric_level_9_spells = [astral_projection, gate, mass_heal, true_resurrection]

# #druid
# #cantrips
# druidcraft = spell()
# poison_spray = spell()
# produce_flame = spell()
# shillelagh = spell()
# thorn_whip = spell()
# druid_cantrips = [druidcraft, guidance, mending, poison_spray, produce_flame, resistance, shillelagh, thorn_whip]

# #level_1
# entangle = spell()
# fog_cloud = spell()
# goodberry = spell()
# jump = spell()
# druid_level_1_spells = [animal_friendship, charm_person, create_or_destroy_water, cure_wounds, detect_magic, detect_poison_and_disease, entangle, faerie_fire, fog_cloud, goodberry, healing_word, jump, longstrider, purify_food_and_drink, speak_with_animals, thunderwave]

# #level_2
# barkskin = spell()
# beast_sense = spell()
# darkvision = spell()
# flame_blade = spell()
# flaming_sphere = spell()
# gust_of_wind = spell()
# moonbeam = spell()
# pass_without_trace = spell()
# spike_growth = spell()
# druid_level_2_spells = [animal_messenger, beast_sense, darkvision, enhance_ability, find_traps, flame_blade, flaming_sphere, gust_of_wind, heat_metal, hold_person, lesser_restoration, locate_animals_or_plants, locate_object, moonbeam, pass_without_trace, protection_from_poison, spike_growth]

# #level_3
# call_lightning = spell()
# conjure_animals = spell()
# sleet_storm = spell()
# water_breathing = spell()
# wind_wall = spell()
# druid_level_3_spells = [call_lightning, conjure_animals, daylight, dispel_magic, feign_death, meld_into_stone, plant_growth, protection_from_energy, sleet_storm, speak_with_plants, water_breathing, water_walk, wind_wall]

# #level_4
# blight = spell()
# conjure_minor_elementals = spell()
# conjure_woodland_beings = spell()
# dominate_beast = spell()
# giant_insect = spell()
# grasping_vine = spell()
# ice_storm = spell()
# stoneskin = spell()
# wall_of_fire = spell()
# druid_level_4_spells = [blight, confusion, conjure_minor_elementals, conjure_woodland_beings, control_water, dominate_beast, freedom_of_movement, giant_insect, grasping_vine, hallucinatory_terrain, ice_storm, locate_creature, polymorph, stone_shape, stoneskin, wall_of_fire]

# #level_5
# antilife_shell = spell()
# commune_with_nature = spell()
# conjure_elemental = spell()
# reincarnate = spell()
# tree_stride = spell()
# wall_of_stone = spell()
# druid_level_5_spells = [antilife_shell, awaken, commune_with_nature, conjure_elemental, contagion, geas, greater_restoration, insect_plague, mass_cure_wounds, planar_binding, reincarnate, scrying, tree_stride, wall_of_stone]

# #level_6
# conjure_fey = spell()
# move_earth = spell()
# sunbeam = spell()
# transport_via_plants = spell()
# wall_of_thorns = spell()
# wind_walk = spell()
# druid_level_6_spells = [conjure_fey, find_the_path, heal, heroes_feast, move_earth, sunbeam, transport_via_plants, wall_of_thorns, wind_walk]

# #level_7
# reverse_gravity = spell()
# druid_level_7_spells = [fire_storm, mirage_arcane, plane_shift, regenerate, reverse_gravity]

# #level_8
# animal_shapes = spell()
# antipathy_sympathy = spell()
# control_weather = spell()
# sunburst = spell()
# tsunami = spell()
# druid_level_8_spells = [animal_shapes, antipathy_sympathy, control_weather, earthquake, feeblemind, sunburst, tsunami]

# #level_9
# shapechange = spell("")
# storm_of_vengeance = spell("")
# druid_level_9_spells = [foresight, shapechange, storm_of_vengeance, true_resurrection]

# #ranger

# #level_1
# alarm = spell("")
# ensnaring_strike = spell("")
# hail_of_thorns = spell("")
# hunters_mark = spell("")
# ranger_level_1_spells = [alarm, animal_friendship, cure_wounds, detect_magic, detect_poison_and_disease, ensnaring_strike, fog_cloud, goodberry, hail_of_thorns, hunters_mark, jump, longstrider, speak_with_animals]

# #level_2
# cordon_of_arrows = spell("")
# ranger_level_2_spells = [animal_messenger, barkskin, beast_sense, cordon_of_arrows, darkvision, find_traps, lesser_restoration, locate_animals_or_plants, locate_object, pass_without_trace, protection_from_poison, silence, spike_growth]

# #level_3
# conjure_barrage = spell("")
# lightning_arrow = spell("")
# ranger_level_3_spells = [conjure_animals, conjure_barrage, daylight, lightning_arrow, nondetection, plant_growth, protection_from_energy, speak_with_plants, water_breathing, water_walk, wind_wall]

# #level_4
# ranger_level_4_spells = [conjure_woodland_beings, freedom_of_movement, grasping_vine, locate_creature, stoneskin]

# #level_5
# conjure_volley = spell("")
# swift_quiver = spell("")
# ranger_level_5_spells = [commune_with_nature, conjure_volley, swift_quiver, tree_stride]

# #paladin
# #level_1
# paladin_level_1_spells = []

# #sorcerer
# #cantrips
# acid_splash = spell("Acid Splash", "A", True, 1, "DEX", 6, "Acid", None, False)
# chill_touch = spell("Chill Touch", "A", True, 1, None, 8, "Necrotic", "Cannot regain hit points", False)
# fire_bolt = spell("Fire Bolt", "A", True, 1, None, 10, "Fire", False, False)
# frost_ray = spell("Frost Ray", "A", True, 1, None, 8, "Cold", "Reduce speed by 10 feet", False)
# shocking_grasp = spell("Shocking Grasp", "A", False, 1, None, 8, "Lightning", "Target can't take reactions", False)
# sorcerer_cantrips = [acid_splash, blade_ward, chill_touch, dancing_lights, fire_bolt, friends, light, mage_hand, mending, message, minor_illusion, poison_spray, prestidigitation, frost_ray, shocking_grasp, true_strike]

# #level_1
# burning_hands = spell("")
# chromatic_orb = spell ("")
# color_spray = spell ("")
# expeditious_retreat = spell ("")
# false_life = spell ("")
# mage_armor = spell ("")
# magic_missile = spell ("")
# ray_of_sickness = spell ("")
# shield = spell ("")
# witch_bolt = spell ("")
# sorcerer_level_1_spells = [burning_hands, charm_person, chromatic_orb, color_spray, comprehend_languages, detect_magic, disguise_self, expeditious_retreat, false_life, feather_fall, fog_cloud, jump, mage_armor, magic_missile, ray_of_sickness, shield, silent_image, sleep, thunderwave, witch_bolt]

# #level_2
# alter_self = spell ("")
# blur = spell ("")
# darkness = spell ("")
# enlarge_reduce = spell ("")
# levitate = spell ("")
# mirror_image = spell ("")
# misty_step = spell ("")
# scorching_ray = spell ("")
# spider_climb = spell ("")
# web = spell ("")
# sorcerer_level_2_spells = [alter_self, blindness_deafness, blur, cloud_of_daggers, crown_of_madness, darkness, darkvision, detect_thoughts, enhance_ability, enlarge_reduce, gust_of_wind, hold_person, invisibility, knock, levitate, mirror_image, misty_step, phantasmal_force, scorching_ray, see_invisibility, shatter, spider_climb, suggestion, web]

# #level_3
# blink = spell ("")
# counterspell = spell ("")
# fireball = spell ("")
# fly = spell ("")
# gaseous_form = spell ("")
# haste = spell ("")
# lightning_bolt = spell ("")
# slow = spell ("")
# sorcerer_level_3_spells = [blink, clairvoyance, counterspell, daylight, dispel_magic, fear, fireball, fly, gaseous_form, haste, hypnotic_pattern, lightning_bolt, major_image, protection_from_energy, sleet_storm, slow, stinking_cloud, tongues, water_breathing, water_walk]

# #level_4
# sorcerer_level_4_spells = [banishment, blight, confusion, dimension_door, dominate_beast, greater_invisibility, ice_storm, polymorph, stoneskin, wall_of_fire]

# #level_5
# cloudkill = spell("")
# cone_of_cold = spell("")
# creation = spell("")
# telekinesis = spell("")
# sorcerer_level_5_spells = [animate_objects, cloudkill, cone_of_cold, creation, dominate_person, hold_monster, insect_plague, seeming, telekinesis, teleportation_circle, wall_of_stone]

# #level_6
# arcane_gate = spell("")
# chain_lightning = spell("")
# circle_of_death = spell("")
# disintegrate = spell("")
# globe_of_invulnerability = spell("")
# sorcerer_level_6_spells = [arcane_gate, chain_lightning, circle_of_death, disintegrate, eyebite, globe_of_invulnerability, mass_suggestion, move_earth, sunbeam, true_seeing]

# #level_7
# delayed_blast_fireball = spell("")
# finger_of_death = spell("")
# prismatic_spray = spell("")
# sorcerer_level_7_spells = [delayed_blast_fireball, etherealness, finger_of_death, fire_storm, plane_shift, prismatic_spray, reverse_gravity, teleport]

# #level_8
# incendiary_cloud = spell("")
# sorcerer_level_8_spells = [dominate_monster, earthquake, incendiary_cloud, power_word_stun, sunburst]

# #level_9
# meteor_swarm = spell("")
# time_stop = spell("")
# wish = spell("")
# sorcerer_level_9_spells = [gate, meteor_swarm, power_word_kill, time_stop, wish]

# #warlock
# #cantrips

#wizard
#cantrips
acid_splash = spell("Acid Splash", "A", True, 1, "DEX", 6, "Acid", None, False)
blade_ward = spell("Blade Ward", "A", False, 1, None, None, None, "Resistance to bludgeoning, piercing, and slashing.", False)
chill_touch = spell("Chill Touch", "A", True, 1, None, 8, "Necrotic", "Cannot regain hit points", False)
dancing_lights = spell("Dancing Lights", "A", True, 10, None, None, None, "Creates lights", False)
fire_bolt = spell("Fire Bolt", "A", True, 1, None, 10, "Fire", False, False)
friends = spell("Friends", "A", False, 10, None, None, None, "Advantage on all Charisma checks", False)
light = spell("Light", "A", False, 600, None, None, None, "Objects emits bright light", False)
mage_hand = spell("Mage Hand", "A", True, 10, None, None, None, "Create spectral hand", False)
mending = spell("Mending", "A", False, 1, None, None, None, "Repair a break or tear in an object", False)
message = spell("Message", "A", True, 1, None, None, None, "Send a short message", False)
minor_illusion = spell("Minor Illusion", "A", False, 1, None, None, None, "Create a sound or an image", False)
prestidigitation = spell("Prestidigitation", "A", False, 600, None, None, None, "Perform simple magical effects", False)
frost_ray = spell("Frost Ray", "A", True, 1, None, 8, "Cold", "Reduce speed by 10 feet", False)
shocking_grasp = spell("Shocking Grasp", "A", False, 1, None, 8, "Lightning", "Target can't take reactions", False)
wizard_cantrips = [acid_splash, blade_ward, chill_touch, dancing_lights, fire_bolt, friends, light, mage_hand, mending, message, minor_illusion, prestidigitation, frost_ray, shocking_grasp]