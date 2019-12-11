import os
from world_data import world, quests, player
from Player import Player, Item, Weapon, Armour
import time
from utils import get_term_cols_rows
from ascii_text import get_ascii


has_quit = False
soft_exit = False



os.system('clear')
print(world.current_area)
prompt = input("\n> ").lower().strip()


while not has_quit:
    os.system('clear')
    print(world.current_area)
    to_clear = False

    if prompt == "":
        continue

    elif prompt == "quit":
        has_quit = True
        soft_exit = True

    elif prompt == "q":
        has_quit = True

    elif prompt == "quests" or prompt == "quest":
        print(quests)

    elif prompt in ["e", "east", "n", "north", "s", "south", "w", "west"]:
        if not world.move(prompt[0]):
            print("Theres nothing in that direction")
        else:
            to_clear = True

    elif prompt[0:4] == "move":
        if not world.move(prompt[5]):
            print("Theres nothing in that direction")
        else:
            to_clear = True

    elif prompt[0:6] == "travel":
        if not world.move(prompt[7]):
            print("Theres nothing in that direction")
        else:
            to_clear = True

    elif prompt[0:2] == "go":
        if not world.move(prompt[3]):
            print("Theres nothing in that direction")
        else:
            to_clear = True

    elif prompt[0:4] == "talk":
        if prompt.split(' ')[1] == "to":
            name = " ".join(prompt.split(" ")[2:])
        else:
            name = " ".join(prompt.split(" ")[1:])
        person = world.current_area.search_NPCs(name)
        if person:
            person.start_dialog(world.current_area)
            to_clear = True
        else:
            print("Theres no-one by that name here.", name)

    elif "quest" in prompt:
        quest_search = "quest".join(prompt.split("quest")[1:])
        searched_q = quests.search_quests(quest_search)
        if searched_q == None:
            print("You don't have the quest: \"" + prompt.replace("quest", "") + "\"")
        else:
            print("\n" + searched_q.__str__() + "\n")

    elif prompt == "i" or "inventory" in prompt:
        print(player.get_inv_str())

    elif prompt[0:5] == "equip":
        player.equip(prompt[6:])

    elif prompt[0:7] == "unequip":
        player.unequip(prompt[8:])
    
    elif "search" in prompt or prompt == "look around":
        world.current_area.search()

    elif "pickup" in prompt:
        player.pickup_item(prompt.replace("pickup", "").strip(), world.current_area)

    elif "take" in prompt:
        player.pickup_item(prompt.replace("take", "").strip(), world.current_area)

    elif "drop" in prompt:
        player.drop_item(prompt.replace("drop", "").strip(), world.current_area)

    else:
        print("I don't know what you mean by \"" + prompt + "\", sorry")
        
    if to_clear:
        os.system('clear')
        print(world.current_area)

    if not has_quit:
        prompt = input("\n> ").lower().strip()


os.system('clear')


if soft_exit:
    dimens = get_term_cols_rows()
    top_padding = int(dimens[1]/2) if int(dimens[1]/2) < 10 else 10

    if dimens[0] < 50:
        logo = ["Nordvallen"]
    else:
        logo = get_ascii("Nordvallen").split('\n')
    leaving_title = "We'll be waiting when you get back"
    leaving_button = "[ Press Enter ]"

    print("\n" * top_padding)
    logo_padding = " " * int((dimens[0] - len(logo[0])) / 2)

    for line in logo:
        print(logo_padding + line)
    print("\n")
    print(" " * int((dimens[0] - len(leaving_title)) / 2) + leaving_title)
    print("\n")
    print(" " * int((dimens[0] - len(leaving_button)) / 2) + leaving_button)
    print()
    input(" " * (int(dimens[0] / 2)-1))

    os.system('clear')
