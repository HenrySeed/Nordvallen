from utils import simple_search

equip_armour= {
    "helmet": "head",
    "hat": "head",
    "chestplate": "chest",
    "leggings": "legs"
}

class Player():
    def __init__(self, name):
        self.name = name
        self.weapons = []
        self.armour = []
        self.items = []
        self.health = 20

        self.equipped = {
            "head": None,
            "chest": None,
            "legs": None,
            "hand": None,
            "offhand": None
        }

    def search_item(self, search):
        simpleSearch = search.lower().replace(" ", "")
        best_option = None
        best_score = float("inf") # Lower is better

        for item in self.weapons + self.armour + self.items + list(self.equipped.values()):
            if item != None:
                simple_item_name = item.name.lower().replace(" ", "")
                if simpleSearch in simple_item_name:
                    score = len(simple_item_name.replace(simpleSearch, ""))
                    if score < best_score:
                        best_option = item
                        best_score = score

        return best_option

    def get_combat_options(self):
        return ["Stab", "Slash"]

    def equip(self, search):
        item = self.search_item(search)
        if item == None:
            print(self.get_inv_str())
            print("Couldnt find \"" + search + "\" in your inventory.")
            return False
        item_name = item.name

        if item in self.weapons:
            old_item = self.equipped["hand"]
            if old_item != None:
                self.add_item(old_item)

            self.weapons.remove(item)
            self.equipped["hand"] = item

        elif item in self.armour:
            old_item = self.equipped[equip_armour[item.type]]
            if old_item != None:
                self.add_item(old_item)

            self.armour.remove(item)
            self.equipped[equip_armour[item.type]] = item
        else:
            print(self.get_inv_str())
            print("You tried placed your " + item.name + " on your head, but it kept falling off.")
            return False

        print(self.get_inv_str())
        print("You equipped your " + item.name)

        return True


    def unequip(self, search):
        item = self.search_item(search)
        if item == None:
            print(self.get_inv_str())
            print("Couldnt find \"" + search + "\" in your inventory.")
            return False
        item_name = item.name

        if type(item) == Weapon:
            if self.equipped["hand"] != None:
                self.add_item(self.equipped["hand"])
                print(self.get_inv_str())
                print("You put your " + item.name + " away.")
                self.equipped["hand"] = None
            else:
                print(self.get_inv_str())
                print("Your " + item.name + " isnt equipped")

        elif type(item) == Armour:
            old_item = self.equipped[equip_armour[item.type]]
            if old_item != None:
                self.add_item(old_item)
                self.equipped[equip_armour[item.type]] = None
                print(self.get_inv_str())
                print("You took your" + item.name + " off.")
            else:
                print(self.get_inv_str())
                print("You aren't wearing your" + item.name + ".")


            self.armour.remove(item)
            self.equipped[equip_armour[item.type]] = item
        else:
            print(self.get_inv_str())
            print("You cant equip your " + item.name)


        return True


    def add_item(self, item):
        if type(item) == Weapon: self.weapons.append(item)
        if type(item) == Armour: self.armour.append(item)
        if type(item) == Item: self.items.append(item)


    def pickup_item(self, search, area):
        item = simple_search(search, area.items)
        if item != None:
            area.items.remove(item)
            self.add_item(item)
            print(self.get_inv_str())
            print("You picked up the " + item.name)

        else:
            print(self.get_inv_str())
            print("There is no " + search + " here.")

    def drop_item(self, search, area):
        item = simple_search(search, self.items + self.weapons + self.armour)
        if item != None:
            if item in self.items: self.items.remove(item)
            if item in self.weapons: self.weapons.remove(item)
            if item in self.armour: self.armour.remove(item)
            area.items.append(item)
            print(self.get_inv_str())
            print("You dropped your " + item.name)
        else:
            print(self.get_inv_str())
            print("You don't have a " + search)



    def get_inv_str(self):
        log = []
        col_maxs = [len("Inventory"), len("Damage")]

        allWeapons = self.weapons.copy()
        if self.equipped["hand"]: allWeapons += [self.equipped["hand"]]
        if self.equipped["offhand"]: allWeapons += [self.equipped["offhand"]]
        allarmour = self.armour.copy()
        if self.equipped["chest"]: allarmour += [self.equipped["chest"]]
        if self.equipped["legs"]: allarmour += [self.equipped["legs"]]
        if self.equipped["head"]: allarmour += [self.equipped["head"]]

        for item in allWeapons:
            if len(item.icon + "  " + item.name) > col_maxs[0]: col_maxs[0] = len(item.icon + "  " + item.name)
            if (len(str(item.damage)) + 3) > col_maxs[1]: col_maxs[1] = (len(str(item.damage)) + 3)
        for item in allarmour:
            if len(item.name) > col_maxs[0]: col_maxs[0] = len(item.name)
            if (len(str(item.defence)) + 3) > col_maxs[1]: col_maxs[1] = (len(str(item.defence)) + 3)
        for item in self.items:
            if len(item.name) > col_maxs[0]: col_maxs[0] = len(item.name)

        bar = "+-{0}-+-{1}-+".format(col_maxs[0]*"-", col_maxs[1]*"-")

        log.append("\n Equipped")
        log.append(bar)
        fountItem = False
        for key in self.equipped.keys():
            item = self.equipped[key]
            if item != None:
                fountItem = True
                if type(item) == Weapon:
                    log.append("| {0:{2}} | {1:{3}} |".format(item.icon + "  " + item.name, str(item.damage) + " DMG", col_maxs[0], col_maxs[1]))
                elif type(item) == Armour:
                    log.append("| {0:{2}} | {1:{3}} |".format(item.name, str(item.defence) + " DEF", col_maxs[0], col_maxs[1]))
                else:
                    log.append("| {0:{2}} | {1:{3}} |".format(item.name, "", col_maxs[0], col_maxs[1]))
            else:
                log.append("| {0:{2}} | {1:{3}} |".format("[ " + key.capitalize() + " ]", "", col_maxs[0], col_maxs[1]))

        log.append(bar)

        log.append("\n Inventory")
        log.append(bar)
        for item in self.weapons:
            log.append("| {0:{2}} | {1:{3}} |".format(item.icon + "  " + item.name, str(item.damage) + " DMG", col_maxs[0], col_maxs[1]))
        log.append(bar)
        for item in self.armour:
            log.append("| {0:{2}} | {1:{3}} |".format(item.name, str(item.defence) + " DEF", col_maxs[0], col_maxs[1]))
        if len(self.armour) > 0: log.append(bar)
        for item in self.items:
            log.append("| {0:{2}} | {1:{3}} |".format(item.name, "", col_maxs[0], col_maxs[1]))
        if len(self.items) > 0: log.append(bar)


        return "\n".join(log) + "\n"

    def __str__(self):
        return self.name



class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self): 
        return self.name


class Armour(Item):
    def __init__(self, name, description, defence, thistype):
        Item.__init__(self, name, description)
        self.defence = defence
        self.type = thistype

    def __str__(self): 
        return self.name + "  - " + str(self.defence) + " DEF"


weapon_sprites = {
    "dagger": "+-|==>",
    "sword": "+-|====>",
    "longsword": "+-{=======>",
    "staff": "==+======",
    "axe": "------7",
    "bow": "\\__--__/",
    "longbow": "\\____--____/"
}

class Weapon(Item):
    def __init__(self, name, description, damage, thistype):
        Item.__init__(self, name, description)
        self.damage = damage
        self.type = thistype
        self.icon = weapon_sprites[thistype]

    def __str__(self): 
        return self.icon + "  " + self.name + "  - " + str(self.damage) + " DMG"

