from utils import text_wrap
from random import randint

class Area():
    def __init__(self, name, description="", n=None, e=None, s=None, w=None):
        self.name = name
        self.description = description

        self.npcs = []

        self.north = n
        self.east = e
        self.south = s
        self.west = w

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

    def __str__(self):
        log = []
        log.append("  =====  " + self.name + "  =====")
        log.append("\n".join(text_wrap(self.description)) + "\n")

        for npc in self.npcs:
            log.append(str(npc))

        log.append("")
        
        if self.north != None:  log.append("North is " + self.north.name)
        if self.east != None: log.append("East is " + self.east.name)
        if self.south != None: log.append("South is " + self.south.name)
        if self.west != None: log.append("West is " + self.west.name)

        return "\n".join(log) + "\n"


class World():
    def __init__(self, start):
        self.start = start
        self.locations = [start]
        self.current_area = start

    def __str__(self):
        return str(self.start)

    def move(self, direction):
        nextArea = None
        if direction == "n": nextArea = self.current_area.north
        if direction == "e": nextArea = self.current_area.east
        if direction == "s": nextArea = self.current_area.south
        if direction == "w": nextArea = self.current_area.west

        if nextArea != None:
            self.current_area = nextArea
            return True
        else:
            return False