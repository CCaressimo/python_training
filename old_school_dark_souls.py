"""
Old school rpg with conditionals.
"""
import random

# Classes------------------------------------------------------------------------------------------
select_profession = {
    "knight":      {"health": 8, "strength": 14, "dexterity": 8, "intelligence": 4, "faith": 4},
    "warrior":     {"health": 6, "strength": 20, "dexterity": 7, "intelligence": 3, "faith": 3},
    "paladin":     {"health": 9, "strength": 14, "dexterity": 7, "intelligence": 5, "faith": 12},
    "sorcerer":    {"health": 5, "strength": 5, "dexterity": 6, "intelligence": 18, "faith": 2},
    "cleric":      {"health": 4, "strength": 7, "dexterity": 6, "intelligence": 6, "faith": 20},
    "warlock":     {"health": 6, "strength": 5, "dexterity": 7, "intelligence": 14, "faith": 7},
    "ranger":      {"health": 7, "strength": 7, "dexterity": 12, "intelligence": 5, "faith": 8},
    "thief":       {"health": 5, "strength": 6, "dexterity": 18, "intelligence": 6, "faith": 4},
    "reaver":      {"health": 6, "strength": 12, "dexterity": 8, "intelligence": 6, "faith": 4}
}

# Enemies-------------------------------------------------------------------------------------------
monsters = [
    {"name": "Hollow Soldier", "health": 2, "attack": 3, "damage": 1},
    {"name": "Undead Dog", "health": 1, "attack": 6, "damage": 1},
    {"name": "Asylum Demon", "health": 4, "attack": 15, "damage": 2},
    {"name": "Silver Knight", "health": 3, "attack": 4, "damage": 2},
    {"name": "Giant", "health": 4, "attack": 8, "damage": 1},
    {"name": "Crystal Lizard", "health": 1, "attack": 5, "damage": 1},
    {"name": "Darkwraith", "health": 4, "attack": 7, "damage": 2},
    {"name": "Gravelord Servant", "health": 3, "attack": 4, "damage": 1},
    {"name": "Hollow Archer", "health": 1, "attack": 10, "damage": 1},
    {"name": "Fallen Knight", "health": 2, "attack": 8, "damage": 1},
    {"name": "Cursed Hollow", "health": 1, "attack": 6, "damage": 1},
    {"name": "Chained Prisoner", "health": 2, "attack": 5, "damage": 1},
    {"name": "Gargoyle", "health": 3, "attack": 12, "damage": 2},
    {"name": "Basilisk", "health": 3, "attack": 7, "damage": 1},
    {"name": "Black Knight", "health": 6, "attack": 14, "damage": 3},
    {"name": "Vagrant", "health": 3, "attack": 13, "damage": 2},
    {"name": "Witch", "health": 1, "attack": 8, "damage": 2},
    {"name": "Hollow Mage", "health": 1, "attack": 6, "damage": 1},
    {"name": "Infant Wyrm", "health": 3, "attack": 7, "damage": 2},
    {"name": "Plague Rat", "health": 1, "attack": 4, "damage": 2},
    {"name": "Gravelord", "health": 5, "attack": 10, "damage": 2},
    {"name": "Troll", "health": 3, "attack": 9, "damage": 2},
    {"name": "Giant Spider", "health": 3, "attack": 5, "damage": 1},
    {"name": "Dreg", "health": 1, "attack": 2, "damage": 1},
    {"name": "Skeleton", "health": 1, "attack": 4, "damage": 1},
    {"name": "Witch's Servant", "health": 3, "attack": 6, "damage": 1},
    {"name": "Mimic", "health": 2, "attack": 18, "damage": 5},
    {"name": "Abyssal Walker", "health": 4, "attack": 12, "damage": 2},
    {"name": "Bloathead", "health": 1, "attack": 7, "damage": 1},
    {"name": "Moss Giant", "health": 5, "attack": 12, "damage": 2},
    {"name": "Dark Spirit", "health": 3, "attack": 16, "damage": 4},
    {"name": "Hallowed", "health": 3, "attack": 7, "damage": 1},
    {"name": "Giant Rat", "health": 1, "attack": 6, "damage": 2},
    {"name": "Revenant", "health": 3, "attack": 10, "damage": 1},
    {"name": "Ghoul", "health": 2, "attack": 5, "damage": 1},
    {"name": "Hellkite Dragon", "health": 8, "attack": 14, "damage": 4},
    {"name": "Lesser Demon", "health": 5, "attack": 14, "damage": 2},
    {"name": "Skeletal Mage", "health": 1, "attack": 6, "damage": 3},
    {"name": "Bonewraith", "health": 3, "attack": 7, "damage": 1}
]


bosses = [
    {"name": "Gwyn, Lord of Cinder", "health": 10, "attack": 16, "damage": 3},
    {"name": "Bed of Chaos", "health": 20, "attack": 5, "damage": 6},
    {"name": "Artorias the Abysswalker", "health": 15, "attack": 18, "damage": 3},
    {"name": "Nito, the First of the Dead", "health": 12, "attack": 15, "damage": 4},
    {"name": "The Four Kings", "health": 5, "attack": 16, "damage": 5},
    {"name": "Seath the Scaleless", "health": 8, "attack": 18, "damage": 6},
    {"name": "Manus, Father of the Abyss", "health": 15, "attack": 18, "damage": 4},
    {"name": "Ornstein and Smough", "health": 20, "attack": 12, "damage": 3},
    {"name": "Midir, the Darkeater", "health": 12, "attack": 19, "damage": 4},
    {"name": "Lorian, Elder Prince", "health": 18, "attack": 12, "damage": 5},
    {"name": "The Nameless King", "health": 25, "attack": 16, "damage": 3},
    {"name": "Abyss Watchers", "health": 12, "attack": 13, "damage": 2},
    {"name": "Pontiff Sulyvahn", "health": 16, "attack": 14, "damage": 2},
    {"name": "Slave Knight Gael", "health": 27, "attack": 15, "damage": 2},
    {"name": "Yhorm the Giant", "health": 25, "attack": 10, "damage": 5},
    {"name": "Sister Friede", "health": 12, "attack": 18, "damage": 4},
    {"name": "Champion Gundyr", "health": 15, "attack": 13, "damage": 2},
    {"name": "The Curse-rotted Greatwood", "health": 30, "attack": 8, "damage": 2},
    {"name": "Vordt of the Boreal Valley", "health": 12, "attack": 15, "damage": 3},
    {"name": "Demon Prince", "health": 18, "attack": 12, "damage": 4},
    {"name": "Oceiros, the Consumed King", "health": 16, "attack": 16, "damage": 3},
    {"name": "Dragonslayer Armour", "health": 20, "attack": 16, "damage": 4},
    {"name": "Iudex Gundyr", "health": 10, "attack": 12, "damage": 2},
    {"name": "Old Demon King", "health": 16, "attack": 13, "damage": 4},
    {"name": "Lords of Cinder", "health": 18, "attack": 16, "damage": 3}
]


# Player info---------------------------------------------------------------------------------------
def profession_list():
    """Select player profession"""
    print(f"{'Profession':<12}{'HP':<6}{'STR':<6}{'DEX':<6}{'INT':<6}")
    print("-" * 60)

    for profession, skill in select_profession.items():
        print(f"{profession.title():<12}{skill['health']:<6}{skill['strength']:<6}{skill['dexterity']:<6}{skill['intelligence']:<6}")
    print("-" * 60)

def character_info():
    """Display player information"""
    skills = get_player_stats()

    print(player_name)
    print(f"{'Profession':<12}{'HP':<6}{'STR':<6}{'DEX':<6}{'INT':<6}")
    print("-" * 60)
    print(f"{player_profession.title():<12}{skills['health']:<6}{skills['strength']:<6}{skills['dexterity']:<6}{skills['intelligence']:<6}")
    print("-" * 60)

def get_player_stats():
    """Returns the player's stats for the selected profession"""
    return select_profession[player_profession]

def get_strongest_skill(skills):
    """Excludes 'health' and find the strongest skill"""
    ignore_health = {key: value for key, value in skills.items() if key != 'health'}
    strong_skill = max(ignore_health, key=skills.get)
    return strong_skill


# Validate player name and profession---------------------------------------------------------------
player_name = input("Please enter you name:\n").strip()
profession_list()
while True:
    player_profession = input("Select a Profession:\n").strip().lower()

    # Validate input
    if player_profession in select_profession:
        print(f"Welcome, {player_name}! You have chosen {player_profession.title()}.")
        break
    else:
        print("Invalid profession. Please choose a valid class.")
        print(", ".join(select_profession.keys()))


# Random encounters---------------------------------------------------------------------------------
def random_combat():
    """Random combat encounter with a monster"""

    encounter_chance = random.randint(1, 15)
    if encounter_chance == 1:
        enemy = random.choice(bosses)
        print(f"You just walked into {enemy['name']}'s lair!")
    else:
        enemy = random.choice(monsters)
        print(f"You have encountered a {enemy['name']}!")

    while True:
        if int(enemy['health']) > 0:

            player_roll = random.randint(1, 20)
            skills = get_player_stats()
            strong_skill = get_strongest_skill(skills)
            player_damage = int(skills[strong_skill] / 4)
            print(f"Player rolled a: {player_roll} + {player_damage}")
            player_attack = player_roll + player_damage

            print(f"You attacked the {enemy['name']} with a {player_attack}!")

            if player_attack < enemy['attack']:
                print(f"Ouch you took damage from a {enemy['name']}!")
                select_profession[player_profession]['health'] -= enemy['damage']
            else:
                print(f"{enemy['name']} took {player_damage} damage!")
                enemy["health"] -= player_damage
                print(f"{enemy['name']} has {enemy['health']} health left!")
        else:
            print(f"You killed the {enemy['name']}!")
            break


def heal():
    """Allows the character a chance to heal"""
    player_roll = random.randint(1, 20)
    print(player_roll)
    skills = get_player_stats()

    if (player_roll + int(skills['intelligence'])) > 20:
        print("Get health potion")
        select_profession[player_profession]['health'] += 2
    else:
        print("Not enough to heal...")

#Active game----------------------------------------------------------------------------------------
while True:
    skills = get_player_stats()
    if int(skills['health']) > 0:
        character_info()
        random_combat()
        character_info()
        heal()

    else:
        print(f"{player_name} has died")
        break

# character_info()
# attack()
# character_info()
# health()
# character_info()
