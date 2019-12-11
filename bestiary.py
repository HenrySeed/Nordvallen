from Player import Weapon, Armour


dagger = Weapon("Dagger", "A short dagger, crudely forged it will do, for now", 3, "dagger")
dirk = Weapon("Dirk", "A long dagger, probabley sat on some officers hip", 4, "dagger")

short_sword = Weapon("Short Sword", "Standard short sword, does the job. These types of swords are found all across the northwest", 5, "sword")
bastard_sword = Weapon("Bastard Sword", "A medium length blade. A favourite amongst the shock troops of the king. Just long enough to reach the enemy, light enough to get there quickly", 6, "sword")
rapier = Weapon("Rapier", "A thin, piercing blade, favoured amongst the coasta guards around Hasselbad", 6, "sword")

long_sword = Weapon("Long Sword", "If you keep missing your peasents from horseback, just get a longer sword.", 7, "longsword")
claymore = Weapon("Claymore", "Ever felt like swords should be more tree-trunk-shaped?", 7, "longsword")

shortstaff = Weapon("Shortstaff", "Gotta keep things simple. Nothing more than a piece of branch", 1, "staff")
quarterstaff = Weapon("Quarterstaff", "Looks like a stick, trimmed and smoothened into a staff. Add some cardboard stars and you're a wizard right?", 2, "staff")
bat = Weapon("Bat", "More of a block of wood than a plank, this can cause some serious blunt-force-trauma", 3, "staff")

wood_axe = Weapon("Wood Axe", "Just like one dad used to have. Fading red paint and a slightly rusty blade, this axe looks more at home in a peasents revolt than on the back of an adventurer, but here we are.", 4, "axe")
iron_war_axe = Weapon("Iron War Axe", "Pilfered off the back of a goblin, this axe still smells aweful, fits right in", 5, "axe")

short_bow = Weapon("Short Bow", "Flings sharp things at enemys not in arms length, whats not to love.", 4, "bow")
elven_bow = Weapon("Elven Bow", "Finer and more precise than the regular bow.", 6, "bow")
heavy_bow = Weapon("Heavy Bow", "Chunkier and heavier than regular bows, it fires bolts so quickly they disentigrate themselves, and anything in front of them into a fine mist.", 6, "bow")

longbow = Weapon("Longbow", "Good when yout enemies live far away", 7, "longbow")
compound_bow = Weapon("Compound Bow", "Fires arrows so precisely then always hit their target", 8, "longbow")


one_hand_weapons = [dirk, dagger, short_sword, bastard_sword, rapier, bat, iron_war_axe]
two_hand_weapons = [long_sword, claymore, shortstaff, quarterstaff, wood_axe]
ranged_weapons = [short_bow, elven_bow, heavy_bow, longbow, compound_bow]



enemies_data = [
    [
        "Ogre", "A large, hulking beast. Will rip off your arm, to use as a nose-picker.", 
        [dagger, short_sword, bat, quarterstaff, iron_war_axe, shortstaff, wood_axe, claymore, long_sword],
        [6, 14],
        [1, 3]
    ],
    [
        "Goblin", "Small nasty creatures, goblins dont do much more than rob, steal and smell up any room they inhabit", 
        [dagger, short_sword, bat, iron_war_axe],
        [3, 7],
        [4,6]
    ],
    [
        "Bandit", "Crossing the line is their middle name. Bandits rob, threaten and destry anything in their way.", 
        one_hand_weapons + two_hand_weapons,
        [5, 11],
        [2, 4]
    ],
]
