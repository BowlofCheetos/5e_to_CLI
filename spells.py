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

#bard
#cantrips
blade_ward = spell("Blade Ward", "A", False, 1, None, None, None, "Resistance to bludgeoning, piercing, and slashing.", False)
dancing_lights = spell("Dancing Lights", "A", True, 10, None, None, None, "Creates lights", True)
friends = spell("Friends", "A", False, 10, None, None, None, "Advantage on all Charisma checks", True)
light = spell("Light", "A", False, 600, None, None, None, "Objects emits bright light", False)
mage_hand = spell("Mage Hand", "A", True, 10, None, None, None, "Create spectral hand", False)
mending = spell("Mending", "A", False, 1, None, None, None, "Repair a break or tear in an object", False)
message = spell("Message", "A", True, 1, None, None, None, "Send a short message", False)
minor_illusion = spell("Minor Illusion", "A", False, 1, None, None, None, "Create a sound or an image", False)
prestidigitation = spell("Prestidigitation", "A", False, 600, None, None, None, "Perform simple magical effects", False)
thunderclap = spell("Thunderclap", "A", False, None, True, 6, "Thunder", "Creates a burst of thunderous sound.", False)
true_strike = spell("True Strike","A", True, 10, False, False, False, "Gain advantage on your first attack against one target", True)
vicious_mockery = spell("Vicious Mockery", "A", True, 1, True, 4, "Psychic", "Disadvantage on the next attack roll", False)
bard_cantrips = [blade_ward, dancing_lights, friends, light, mage_hand, mending, message, minor_illusion, prestidigitation, true_strike, vicious_mockery]

#level_1
animal_friendship = spell("Animal Friendship","A", True, 14400, True, None, None, "Convince a beast that you mean no harm.", False)
bane = spell("Bane","A", True, 10, True, None, None, "Up to three creatures have a disadvantage on attack rolls and saving throws", True)
charm_person = spell("Charm Person", "A", True, 600, True, None, None, "Charm a humanoid", False)
comprehend_languages = spell("Comprehend Languages", "A", False, 600, False, None, None, "Understand the meaning of any spoken language", False)
cure_wounds = spell("Cure Wounds", "A", False, 1, False, None, None, "Creature you touch regains hp", False)
detect_magic = spell("Detect Magic", "A", False, 60, False, None, None, "Sense the presence of magic within 30ft", True)
disguise_self = spell("Disguise Self", "A", False, 600, True, None, None, "Make yourself look different", False)
dissonent_whispers = spell("Dissonent Whispers", "A", True, 1, True, True, "Psychic", "Whisper a discordany melody", True)
faerie_fire = spell("Faerie Fire", "A", True, 60, True, None, None, "Any creature within a range is outlined in blue,green, or violet", True)
feather_fall = spell("Feather Fall", "B", True, 10, False, None, None, "Up to 5 falling creatures slowly descend", False)
healing_word = spell("Healing Word", "B", True, 1, False, None, None, "Creature of your choice regains HP", False)
heroism = spell("Heroism", "A", False, 10, False, False, None, "A willing creature you touch is imbued with bravery", True)
identify = spell("Identify", "R", False, 1, False, None, None, "If the item was created by a spell, you learn which spell created it.", False)
illusory_script = spell("Illusory Script", "R", False, 144000, False, False, None, "You imbue illusion writtings on paper", False)
longstrider = spell("Longstrider", "A", False, 600, False, None, None, "Speed increases by 10ft", False)
silent_image = spell("Silent Image", "A", True, 60, True, None, None, "Create a purely visual image of an object or creature", True)
sleep = spell("Sleep", "A", True, 10, False, None, None, "Sends creatures into a magical slumber", False)
speak_with_animals = spell("Speak with Animals", "A", False, 100, False, None, None, "The ability to comprehend and verbally communicate with beasts", False)
tashas_hideous_laughter = spell("Tasha's Hideous Laughter", "A", True, 10, True, None, None, "A creature perceives everything as hilariously funny and falls into fits of laughter", True)
thunderwave = spell("Thunderwave", "A", True, 1, True, True, "Thunder", "A wave of thunderous force sweeps out from you", False)
unseen_servant = spell("Unseen Servant", "A", True, 600, False, None, None, "This spell creates an invisible, mindless, shapeless, Medium force", False)
bard_level_1_spells = [animal_friendship, bane, charm_person, comprehend_languages, cure_wounds, detect_magic, disguise_self, dissonent_whispers, faerie_fire, feather_fall, healing_word, heroism, identify, illusory_script, longstrider, silent_image, sleep, speak_with_animals, tashas_hideous_laughter, thunderwave, unseen_servant]

#level_2
aid = spell("Aid", "A", True, 4800, False, None, None, "Your spell bolsters your allies with toughness and resolve", False)
animal_messenger = spell("Animal Messenger", "A", True, 14400, False, None, None, "You use an animal to deliver a message",False)
blindness_deafness = spell("Blindness/Deafness", "A", True, 1, True, None, None, "You can blind or deafen a foe.", False)
calm_emotions = spell("Calm Emotions", "A", True, 10, True, None, None, "You attempt to suppress strong emotions in a group of people", True)
cloud_of_daggers = spell("Cloud of Daggers", "A", True, 10, False, 16, "Slashing", "You fill the air with spinning daggers in a cube 5 feet on each side", True)
crown_of_madness = spell("Crown of Madness", "A", True, 10, True, None, None, "A twisted crown of jagged iron appears on humanoid of your choice", True)
detect_thoughts = spell("Detect Thoughts", "A", False, 10, True, None, None, "You can read the thoughts of certain creatures", True)
enhance_ability = spell("Enhance Ability", "A", False, 600, False, None, None, "Bestow a magical enhancement", True)
enthrall = spell("Enthrall", "A", True, 1, True, None, None, "Weave a distracing string of words", False)
gift_of_gab = spell("Gift of Gab", "B", False, 1, False, None, None, "Skillfully reshape the memories of listeners", False)
heat_metal = spell("Heat Metal", "A", True, 10, True, 16, "Fire", "You cause the object to glow red-hot.", True)
hold_person = spell("Hold Person", "A", True, 10, True, None, None, "Choose a humanoid in range and paralyze", True)
invisibility = spell("Invisibility", "A", False, 600, False, None, None, "Creature you touch becomes invisible", True)
knock = spell("Knock", "A", True, 1, False, None, None, "A target that is held shut by a mundane lock or that is stuck or barred becomes unlocked", False)
lesser_restoration = spell("Lesser Restoration", "A", False, 1, False, None, None, "You touch a creature and can end either one disease or one condition afflicting it.", False)
locate_animals_or_plants = spell("Locate Animals or Plants", "A", False, 1, False, None, None, "You learn the direction and distance to the closest creature or plant", False)
locate_object = spell("Locate Object", "A", False, 100, False, None, None, "Describe or name an object that is familiar to you", True)
magic_mouth = spell("Magic Mouth", "R", True, 1, False, None, None, "You implant a message within an object in range, a message that is uttered when a trigger condition is met.", False)
phantasmal_force = spell("Phantasmal Force", "A", True, 10, True, None, None, "You craft an illusion that takes root in the mind of a creature that you can see within range.", True)
see_invisibility = spell("See Invisibiltiy", "A", False, 600, False, None, None, "For the duration, you see invisible creatures and objects as if they were visible", False)
shatter = spell("Shatter", "A", True, 1, True, 24, "Thunder", "A sudden loud ringing noise, painfully intense, erupts from a point of your choice within range.", False)
silence = spell("Silence", "A", True, 100, False, None, None, "No sound can be created within or pass through a 20-foot-radius sphere", True)
suggestion = spell("Suggestion", "A", True, 4800, True, None, None, "You suggest a course of activity (limited to a sentence or two) and magically influence a creature", True)
zone_of_truth = spell("Zone of Truth", "A", True, 100, True, None, None, "You create a magical zone that guards against deception ", False)
bard_level_2_spells = [aid, animal_messenger, blindness_deafness, calm_emotions, cloud_of_daggers, crown_of_madness, detect_thoughts, enhance_ability, enthrall, gift_of_gab, heat_metal, hold_person, invisibility, knock, lesser_restoration, locate_animals_or_plants, locate_object, magic_mouth, phantasmal_force, see_invisibility, shatter, silence, suggestion, zone_of_truth]

#cleric
#cantrips

#druid
#cantrips

#wizard
#cantrips
acid_splash = spell("Acid Splash", "A", True, 1, "DEX", 6, "Acid", None, False)
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
ray_of_frost = spell("Ray of Frost", "A", True, 1, None, 8, "Cold", "Reduce speed by 10 feet", False)
shocking_grasp = spell("Shocking Grasp", "A", False, 1, None, 8, "Lightning", "Target can't take reactions", False)
wizard_cantrips = [acid_splash, chill_touch, dancing_lights, fire_bolt, friends, light, mage_hand, mending, message, minor_illusion, prestidigitation, ray_of_frost, shocking_grasp]