import random
import screenplay

# TIPS
# - start simple
# - conceptually: it's all just text!
#   (within a light, heirarchical structure geared around storytelling and gameplay)
# - provide many characters and include "choose your character" as an early challenge,
#   or describe what kind of characters are possible and include "create your character"
# - crazyidea: try passing locations as characters, resources as challenges, etc

characters = [
    "lacadio hearn, aka yakumo koizumi (小泉 八雲), ghost story hunter"
    "colonel aureliano buendía, cartel rogue",
    "alexandra, ai researcher on neptune",
    "princess zelda [darkmode], grimes' final form",
]

locations = [
    "new york city",
    # "the astral plane",
    # "a jungle river, nitrogen rain sifting through memory of the outdoors",
    # "inside an autonomous space ship",
]

resources = [
    "historical knowledge related to the current location",
    "the scrolls of melquíades",
    # "compute power",
    # "florescent gems that summon robotic archangels in animal form",
]

challenges = [
    "explore the terrain and collect all rare artifacts within your local latent space",
    "fight the skeleton armies",
    "escape solitude",
    "save humanity",
]

for character in characters:
    screenplay.run(
        characters=[character],
        locations=locations,
        resources=resources,
        challenges=random.sample(challenges, 1),
        # later!
        # mechanics=[],
        # events=[],
    )
