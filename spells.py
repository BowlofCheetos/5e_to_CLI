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
<<<<<<< HEAD
animal_friendship spell()
=======
animal_friendship = spell()
>>>>>>> 53b8e1e (Bard cantrips and L1 spells created.)
bane = spell()
charm_person = spell()
comprehend_languages = spell()
cure_wounds = spell()
detect_magic = spell()
disguise_self = spell()
dissonent_whispers = spell()
faerie_fire = spell()
feather_fall = spell()
healing_word = spell()
heroism = spell()
identify = spell()
illusory_script = spell()
longstrider = spell()
silent_image = spell()
sleep = spell()
speak_with_animals = spell()
tashas_hideous_laughter = spell()
thunderwave = spell()
unseen_servant = spell()
bard_level_1_spells = []

#cleric
#cantrips

#druid
#cantrips

#bard
#cantrips

#level_1

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