#forgotten realms intro
def intro():
    print("Welcome to the Forgotten Realms, a vast and diverse fantasy world filled with magic, mythical creatures, and ancient lore.\nAs you embark on your adventure, prepare to explore intricate cities, delve into forgotten dungeons, and encounter a rich tapestry of cultures that shape this enchanting realm.")

#player_name
def player_name():
    player_name = input("What is your name traveler? ").strip().title()
    print("Welcome to the Forgotten Realms " + player_name + "!")