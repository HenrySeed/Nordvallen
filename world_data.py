from Area import World, Area
from npc_data import arry_npc
from Quest import Quests, Quest 
from Player import Item, Weapon, Armour


quests = Quests()
quests.add_quest(Quest("A Hanky too far", "The princess has lost her gold-laced hankerchief, you of course being the noble squire you are must go fetch it"))
quests.add_quest(Quest("Royal Appointment", "Its that time of year, the king is overdue for his annual bath. He's asked for you to guard him on his journey to the natural springs north of town"))
quests.add_quest(Quest("Scape Goat", "Barry, the untrustworthy squire in the neighbouring room has told the king you nicked his favourite snuff-box. You better sort Barry out straight away"))


hasselbad_area = Area("Hasselbad", "A town on the easten shores of Lake Coleridge. Nestled in the southern foothills of the Shneeburg Alps it is a haven for outlaws, who hide amongst the fishermen and lumberjacks.")
korknev_area = Area("Korknev", "More of a roadside stop than a town, on the road between Hasselbad and Noamsted it carries a fair amount of merchantile traffic, hardly any of it legal")
noamsted_area = Area("Noamsted", "The main town of the region. Noamsted is home to all types, on one street you could buy a rug, a dead body and someone to dispose of them both. The ruling class is mostly made up of old money, originally brought here for the iron mining. It has its fair share of blacksmiths and armories.")
tidefrost_area = Area("Tidefrost", "A small hunting village right on the edge of the Schneeburg alps. Any further north and there would be more foxbears than villagers.")

hasselbad_area.items += [Item("Fish on a stick", "Its a stick with a fish jammed on it.")]

hasselbad_area.set_link("e", korknev_area)
korknev_area.set_link("e", noamsted_area)
korknev_area.set_link("n", tidefrost_area)

hasselbad_area.add_npcs([arry_npc])

world = World(hasselbad_area)