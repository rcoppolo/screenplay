# 📺 Screenplay

Hi, I'm Ryan.

I'm working on an API for creating games.

I'd love to hear any feedback on the early designs: [create an issue](https://github.com/rcoppolo/screenplay/issues/new) or submit a PR.

## Python API
```python
import random
import screenplay

# TIPS
# - conceptually: it's all just text! (within a lightweight, heirarchical structure
#   geared around storytelling and gameplay)
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
```

## Plain text examples

```
characters
  lacadio hearn, aka yakumo koizumi (小泉 八雲), ghost story hunter
locations
  tokyo, 1892
challenges
  find tsukioka yoshitoshi
resources
  rumors, tales, and historical events as told by various non-player characters
```

<details>

<summary>tears_of_the_kingdom_intro.txt</summary>

```
characters
  link, our hero
  zelda, princess of hyrule
locations
  beneath hyrule castle
challenges
  discover the source of the strange gloom
  some dangerous bats
resources
  master sword
  hearts
  stamina
mechanics
  move around
  look around
  talk to zelda
  swing your sword
```
</details>

<details>

<summary>squirrel_life.txt</summary>

```
characters
  an agile, 2 year old squirrel named mindy
locations
  suburban new england
challenges
  find nuts to survive the winter
  avoid predators and curious children with sticks
  cross the road without getting squashed by volvos
resources
  nuts
  energy
mechanics
  move
  jump
  climb trees
```
</details>
