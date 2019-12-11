from bestiary import enemies_data
from random import randint
from utils import get_num_option
import os
import time

class Enemy():
    def __init__(self, race, description, hp=10, weapon=None, armour=[]):
        self.name = race
        self.description = description
        self.weapon = weapon
        self.race = race
        self.health = hp
        self.dead = False
        self.equipped = {
            "head": None,
            "chest": None,
            "legs": None,
            "hand": weapon,
            "offhand": None
        }
        for item in armour:
            self.equipped[item.type] = item

    def __str__(self):
        return " - {0:{2}}  {1}hp".format(self.name, self.health, len(self.name))

    def hit(self, dmg):
        self.health -= dmg
        if self.health <= 0: 
            self.health = 0
            self.dead = True



class Combat():
    def __init__(self, player):
        self.enemies = gen_rand_enemies()
        self.player = player
        self.type = self.enemies[0].race
        for enemy in self.enemies:
            if enemy.race != self.type:
                self.type = "bandits"
                break
      

    def __str__(self):
        log = []
        log.append("You've been ambushed by a group of " + self.type + "s!\n")
        for enemy in self.enemies:
            if not enemy.dead:
                log.append(str(enemy))
        log.append("")
        log.append("{} - {}hp".format(self.player.name, self.player.health))
        log.append("")
        log.append("1) " + self.player.get_combat_options()[0])
        log.append("2) " + self.player.get_combat_options()[1])
        log.append("3) Item")
        log.append("4) Run Away")
        log.append("")
        return "\n".join(log)


    def get_alive_enemies(self):
        alive_enemies = []
        for enemy in self.enemies:
            if not enemy.dead:
                alive_enemies.append(enemy)
        return alive_enemies


    def attack(self, mode, dmg):
        alive_enemies = self.get_alive_enemies()

        if mode == "Slash":
            # Check for a miss
            if randint(0, 6) == 1:
                return("You swung, but missed the " + self.type)
            # Choose 2 - 4 enemies to attach
            num = randint(1, len(alive_enemies) if len(alive_enemies) < 5 else 4)
            total_dmg = 0
            for enemy in alive_enemies[randint(0, len(alive_enemies) - num):]:
                dmg_dealt = randint(dmg - 3, dmg-1)
                if dmg_dealt <= 0 : dmg_dealt = 1
                total_dmg += dmg_dealt
                if dmg_dealt < 1: dmg_dealt = 1
                enemy.hit(dmg_dealt)

            race = self.type if num == 1 else self.type + 's'
            if total_dmg == 0:
                return "You hit {} {}, but they just shrugged it off".format(num, race)
            else:
                return "You hit {} {}, dealing {} total damage.".format(num, race, total_dmg)

        elif mode == "Stab":
            # Check for a miss
            if randint(0, 20) == 1:
                return("You swung, but missed the " + self.type)
            # Choose an enemy
            i = randint(0, len(alive_enemies) - 1)
            dmg_dealt = randint(dmg, dmg * 4)
            enemy = alive_enemies[i]
            enemy.hit(dmg_dealt)
            return("You hit 1 {}, dealing {} damage.".format(self.type, dmg_dealt))


    def enemy_attack(self):
        total_damage = 0
        num_misses = 0
        num_hits = 0
        for enemy in self.get_alive_enemies():
            if randint(0, 5) == 2:
                num_misses += 1
            else:
                num_hits += 1
                dmg = round(enemy.weapon.damage / 2)
                if dmg < 1: dmg = 1
                dealt = randint(dmg-4, dmg)
                if dealt < 0: dealt = 0
                total_damage += dealt


        self.player.take_damage(total_damage)
        return("{} {} hit you, dealing {} damage".format(num_hits, self.type if num_hits == 1 else self.type + "s", total_damage))


    def combat_loop(self):
        attacks = self.player.get_combat_options()

        player_damage = self.player.equipped["hand"]
        if player_damage == None:
            player_damage = 2
        else:
            player_damage = player_damage.damage

        os.system("clear")
        print(self)


        choice = get_num_option(4)

        while choice != "q" and len(self.get_alive_enemies()) > 0:

            os.system("clear")

            your_response = ""
            enemy_response = ""

            if choice == 0: 
                your_response = self.attack(attacks[0], player_damage)
            if choice == 1: 
                your_response = self.attack(attacks[1], player_damage)
            if choice == 2: return False
            if choice == 3: return False


            print(self)
            print(your_response)

            if len(self.get_alive_enemies()) < 1: 
                break


            enemy_response = self.enemy_attack()

   

            os.system("clear")
            print(self)
            print(your_response)
            print("")
            print(enemy_response)
            print("")

            if self.player.health < 1: 
                print("\nYou passed out. When you woke up the " + self.type + " were gone.")
                return False

            choice = get_num_option(4)

        if choice == "q":
            return False

        race = self.type if len(self.enemies) == 0 else self.type + "s"
        print()

        print("\n\n    You fought off the " + race)
        return True





def gen_rand_enemies():
    output = []
    enemy = enemies_data[randint(0, len(enemies_data)-1)]
    num = randint(enemy[4][0], enemy[4][1])
    for _ in range(0, num):
        weapon = enemy[2][randint(0, len(enemy[2])-1)]
        output.append(Enemy(enemy[0], enemy[1], randint(enemy[3][0], enemy[3][1]), weapon))
    return output
