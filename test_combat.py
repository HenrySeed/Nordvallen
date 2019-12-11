from Combat import Enemy, Combat
from Player import Player, Weapon, Armour
from bestiary import *

player = Player("Hrothgar")
player.add_item(bastard_sword)
player.add_item(quarterstaff)
player.add_item(Armour("Leather Leggings", "", 1, "leggings"))
player.equip("sword")


rand_encounter = Combat(player)
rand_encounter.combat_loop()