from utils import text_wrap, print_loading_anim
from random import randint
from time import sleep
from ascii_text import get_ascii
from Combat import Enemy, Combat
import os


class Area():
    def __init__(self, name, description="", n=None, e=None, s=None, w=None):
        self.name = name
        self.description = description

        self.items = []
        self.npcs = []

        self.north = n
        self.east = e
        self.south = s
        self.west = w

    def search(self):
        print("  Searching area. ", end="\r")
        sleep(0.7)
        print("  Searching area.. ", end="\r")
        sleep(0.7)
        print("  Searching area... ")
        sleep(0.7)

        if len(self.items) == 0:
            print("You didnt find anything")
        else:
            print("\n  You found:")
            for obj in self.items:
                print("   " + str(obj))

   

    def add_npcs(self, npcs):
        for npc in npcs:
            if npc not in self.npcs:
                self.npcs.append(npc)

    def search_NPCs(self, search):
        simpleSearch = search.lower().replace(" ", "")
        best_option = None
        best_score = float("inf") # Lower is better

        for npc in self.npcs:
            simple_npc_name = npc.name.lower().replace(" ", "")
            if simpleSearch in simple_npc_name:
                score = len(simple_npc_name.replace(simpleSearch, ""))
                if score < best_score:
                    best_option = npc
                    best_score = score

        return best_option

    def set_link(self, direction, area):
        if direction == "n": 
            self.north = area
            area.south = self
        if direction == "e": 
            self.east = area
            area.west = self
        if direction == "s": 
            self.south = area
            area.north = self
        if direction == "w": 
            self.west = area
            area.east = self

    def get_map(self):
        top_line = ""
        mid_line = ""
        bottom_line = ""

        if self.west: 
            if self.west.west != None: mid_line += "... "
            mid_line += self.west.name + " --- "
        else:
            mid_line += "                  "
        mid_line += "[ {} ]".format(self.name)
        if self.east: 
            mid_line += " --- " + self.east.name 
            if self.east.east != None: mid_line += " ..."
        else:
            mid_line += "                  "

        middle_padding = round(len(mid_line)/2) * " "

        if self.north:
            north_name = self.north.name
            if self.north.west != None: north_name = "... " + north_name
            if self.north.east != None: north_name += " ..."

            padding = (round((len(mid_line) - len(north_name)) / 2)+1) * " "
            top_line = padding + north_name + "\n" + middle_padding + "|"

        if self.south:
            south_name = self.south.name
            if self.south.west != None: south_name = "... " + south_name
            if self.south.east != None: south_name += " ..."

            padding = round((len(mid_line) - len(south_name)) / 2) * " "
            bottom_line = middle_padding + "|" + "\n" + padding + south_name

        _ret = "{0}========  Area Map  ========{0}\n\n".format((round(len(mid_line)/2) - 14) * " ")
        if top_line != "": 
            _ret += top_line + "\n"
        else:
            _ret += "\n\n"
        _ret += mid_line
        if bottom_line != "": _ret += "\n" + bottom_line

        return "\n\n" + _ret

    def __str__(self):
        name = get_ascii(self.name).split("\n")

        log = name
        log.append("")
        log.append("\n".join(text_wrap(self.description)) + "\n")

        for npc in self.npcs:
            log.append(str(npc))

        log.append("")
        
        # if self.north != None:  log.append("North is " + self.north.name)
        # if self.east != None: log.append("East is " + self.east.name)
        # if self.south != None: log.append("South is " + self.south.name)
        # if self.west != None: log.append("West is " + self.west.name)

        log.append(self.get_map())
        log.append("")

        return "\n".join(log) + "\n"


class World():
    def __init__(self, start, player):
        self.start = start
        self.locations = [start]
        self.current_area = start
        self.player = player

    def __str__(self):
        return str(self.start)

    def move(self, direction):
        nextArea = None
        if direction == "n": nextArea = self.current_area.north
        if direction == "e": nextArea = self.current_area.east
        if direction == "s": nextArea = self.current_area.south
        if direction == "w": nextArea = self.current_area.west

        direction_names = {
            "n": "North",
            "e": "East",
            "s": "South",
            "w": "West"
        }

        if nextArea != None:
            distance = 3
            header = "   Travelling " + direction_names[direction] + " to " + nextArea.name
            print()
            safe = None

            for i in range(0, distance):
                print(header + ("." * i), end="\r")
                sleep(0.4)
                if randint(0,20) == 1:
                    rand_encounter = Combat(self.player)
                    safe = rand_encounter.combat_loop()
                    break

            if safe == None:
                print(header + "...  You made it safely.", end ="\r")
                self.current_area = nextArea
                sleep(1)
            elif safe == True:
                print()
                print_loading_anim("You made it to " + nextArea.name + " safely.", 3)
                self.current_area = nextArea
            else:
                print_loading_anim("You stumble back to " + self.current_area.name + ", defeated", 3)


            return True
        else:
            return False