from Quest import Quests, Quest 
import os
from Area import World, Area
from npc_data import arry_npc


quests = Quests()
quests.add_quest(Quest("A Hanky too far", "The princess has lost her gold-laced hankerchief, you of course being the noble squire you are must go fetch it"))
quests.add_quest(Quest("Royal Appointment", "Its that time of year, the king is overdue for his annual bath. He's asked for you to guard him on his journey to the natural springs north of town"))
quests.add_quest(Quest("Scape Goat", "Barry, the untrustworthy squire in the neighbouring room has told the king you nicked his favourite snuff-box. You better sort Barry out straight away"))


hasselbad_area = Area("Hasselbad", "A town on the easten shores of Lake Coleridge. Nestled in the southern foothills of the Shneeburg Alps it is a haven for outlaws, who hide amongst the fishermen and lumberjacks.")
korknev_area = Area("Korknev", "More of a roadside stop than a town, on the road between Hasselbad and Noamsted it carries a fair amount of merchantile traffic, hardly any of it legal")
noamsted_area = Area("Noamsted", "The main town of the region. Noamsted is home to all types, on one street you could buy a rug, a dead body and someone to dispose of them both. The ruling class is mostly made up of old money, originally brought here for the iron mining. It has its fair share of blacksmiths and armories.")

hasselbad_area.set_link("e", korknev_area)
korknev_area.set_link("e", noamsted_area)

hasselbad_area.add_npcs([arry_npc])

world = World(hasselbad_area)



has_quit = False
has_moved = True

while not has_quit:
    if has_moved: 
        os.system('cls||clear')
        print(world.current_area)
    has_moved = False

    prompt = input("\n> ").lower().strip()

    if prompt == "":
        continue
    elif prompt == "quit":
        has_quit = True
    elif prompt == "quests" or prompt == "quest":
        print(quests)
    elif prompt in ["e", "east", "n", "north", "s", "south", "w", "west"]:
        if not world.move(prompt[0]):
            print("Theres nothing in that direction")
        else:
            has_moved = True
    elif prompt[0:4] == "move":
        if not world.move(prompt[5]):
            print("Theres nothing in that direction")
        else:
            has_moved = True
    elif prompt[0:2] == "go":
        if not world.move(prompt[3]):
            print("Theres nothing in that direction")
        else:
            has_moved = True
    elif prompt[0:4] == "talk":
        if prompt.split(' ')[1] == "to":
            name = " ".join(prompt.split(" ")[2:])
        else:
            name = " ".join(prompt.split(" ")[1:])

        person = world.current_area.search_NPCs(name)
        if person:
            person.start_dialog()
            has_moved = True
        else:
            print("Theres no-one by that name here.", name)

    elif "quest" in prompt:
        quest_search = "quest".join(prompt.split("quest")[1:])
        searched_q = quests.search_quests(quest_search)
        if searched_q == None:
            print("You don't have the quest: \"" + prompt.replace("quest", "") + "\"")
        else:
            print("\n" + searched_q.__str__() + "\n")
    elif prompt[0] == "q":
        quest_search = prompt[1:]
        searched_q = quests.search_quests(quest_search)
        if searched_q == None:
            print("You don't have the quest: \"" + prompt.replace("quest", "") + "\"")
        else:
            print("\n" + searched_q.__str__() + "\n")
    else:
        print("I don't know what you mean by \"" + prompt + "\", sorry")



print("Quitting...")