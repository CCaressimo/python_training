"""
This script generates a random band name by selecting 2 or 3 words 
from a predefined list of words. The band name is printed to the console.
"""

import random

# print("Create a band name:")
# home_town = input("Where we you born?\n")
# pet_name = input("What was your first pet's name?\n")
# print("Your new band name is: " + home_town + " " + pet_name) 

band_words = [
    "Echo", "Phantom", "Starlight", "Velvet", "Nova", "Storm", "Vortex", "Horizon", "Rebel", "Sunset",
    "Silver", "Waves", "Dusk", "Crimson", "Flame", "Dream", "Fire", "Shadows", "Glory", "Serpent",
    "Pulse", "Crown", "Ghost", "Twilight", "Rising", "Prism", "Titan", "Ember", "Violet", "Haze",
    "Cobalt", "Mysterious", "Chrome", "Vampires", "Nebula", "Jagged", "Orion", "Phoenix", "Radiant",
    "Sonic", "Chroma", "Requiem", "Legend", "Moonlight", "Steel", "Grit", "Storms", "Bass", "Screams",
    "Spectre", "Lunar", "Soul", "Raven", "Alchemist", "Echoes", "Obsidian", "Astral", "Vanguard",
    "Eclipse", "Venom", "Steel", "Witch", "Cosmic", "Inferno", "Solar", "Dynasty", "Voltage", "Tide",
    "Ascension", "Enigma", "Warriors", "Electric", "Mirage", "Diamond", "Infernal", "Rapture", "Underground",
    "Moon", "Euphoria", "Odyssey", "Phantom", "Violet", "Angels", "Savage", "Reign", "Wicked", "Kingdom",
    "Neon", "Crater", "Echo", "Revolt", "Cloak", "Zephyr", "Pulse", "Neptune", "Velocity", "King",
    "Darkness", "Blaze", "Spectral", "Abyss", "Hunter", "Haze", "Vengeance", "Lands", "Rage", "Wildfire",
    "Exile", "Galaxy", "Eclipse", "Lust", "Journey", "Blackout", "Ashes", "Revolt", "Rapture", "Kings",
    "Fury", "Orbit", "Cloak", "Reckoning", "Frost", "Vow", "Serenity", "Tempest", "Ritual", "Embrace",
    "Talon", "Wanderers", "Evil", "Lords", "Moon", "Empire", "Waves", "Dark", "Ravens", "Savage", "Rise"
]

num_words = int(input("How many words would you like your band name be?\n"))

band_name = random.sample(band_words, num_words)

print(" ".join(band_name))
