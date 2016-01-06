import random
import math
import re
import TABLES

#from tkinter import *  #Will be adding a GUI to select stats and show player/npc activity


#********************************CLASSES********************************
class Creature():
    def __init__(self, base_stats):
        #/These stats will be replaced by Point Buy System once created\
        self.base_str = base_stats['STR']
        self.base_dex = base_stats['DEX']
        self.base_con = base_stats['CON']
        self.base_wis = base_stats['WIS']
        self.base_int = base_stats['INT']
        self.base_cha = base_stats['CHA']



class Class():
    def __init__(self, class_import):
        self.class_name = class_import['Class Name']
        self.class_level = class_import['Class Level']
        self.start_hp = class_import['Start HP']
        self.hp_per_level = class_import['HP Per Level']
        self.armor = class_import['Armor']
        self.currently_equipped = class_import['Weapon Name']
        self.weapon_damage = class_import['Weapon Damage']
        self.weapon_magic_bonus = class_import['Weapon Magic Bonus']



class AbilityStats():
    def __init__(self, race, base):
        #Defining Total Player Ability Values (create def?)
        self.str_stat = race['Str Bonus']+base.base_str
        self.dex_stat = race['Dex Bonus']+base.base_dex
        self.con_stat = race['Con Bonus']+base.base_con
        self.wis_stat = race['Wis Bonus']+base.base_wis
        self.int_stat = race['Int Bonus']+base.base_int
        self.cha_stat = race['Cha Bonus']+base.base_cha

    def get_stat(self, stat):
        if stat == 'STR':
            return self.str_stat
        elif stat == 'DEX':
            return self.dex_stat
        elif stat == 'CON':
            return self.con_stat
        elif stat == 'WIS':
            return self.wis_stat
        elif stat == 'INT':
            return self.int_stat
        elif stat == 'CHA':
            return self.cha_stat
        else: print('NOT A VALID OPTION')

    def get_mod(self, stat):
        if stat == 'STR':
            return (self.str_stat-10)//2
        elif stat == 'DEX':
            return (self.dex_stat-10)//2
        elif stat == 'CON':
            return (self.con_stat-10)//2
        elif stat == 'WIS':
            return (self.wis_stat-10)//2
        elif stat == 'INT':
            return (self.int_stat-10)//2
        elif stat == 'CHA':
            return (self.cha_stat-10)//2
        else: print('NOT A VALID OPTION')



class Player():
    def __init__(self, name, race, p_class, stats):
        #Defined by creating the character:
        #example: character = Player('Player Name',race, class, AbilityStats(race, creature_stats))
        self.name = name
        self.race = race
        self.p_class = p_class
        self.stats = stats

        #Defined by Class Starting HP and HP per Level gains
        self.start_hp = p_class.start_hp
        self.hp_per_level = p_class.hp_per_level

        #For all starting Players no matter what race/class
        self.level = 1                 #Will increase with XP gained if Player
        self.x = 0                     #Can be modified by Player Controls
        self.y = 0
        self.xp = 0


    def max_hp(self):
        max_health = (self.start_hp)+(self.hp_per_level*(self.level-1))
        return max_health

    #For reporting current Player Location as a tuple back to user (mainly for testing purposes)
    def get_loc(self):
        location = (self.x,self.y)
        return location

    #Player Movement Controls (Player will be moved by Buttons)
    def move_up(self):
        print(self.name, 'attempts to move up.')
        self.y += 1
    def move_down(self):
        print(self.name, 'attempts to move down.')
        self.y -= 1
        if self.y < 0:
            self.y = 0
            print('You can not move there!')
    def move_right(self):
        print(self.name, 'attempts to move right.')
        self.x += 1
    def move_left(self):
        print(self.name, 'attempts to move left.')
        self.x -= 1
        if self.x < 0:
            self.x = 0
            print('You can not move there!')


#*************************************************************************
#********************************FUNCTIONS********************************

#Double Movement on every other diagonal
def distance_calc_eucl(creature_1, creature_2):
    distance = int(math.sqrt(((creature_1.x-creature_2.x)**2)+(creature_1.y-creature_2.y)**2))
    return distance

#Gives User a List of all Weapons and Attributes
def weapon_recall():
    for x in weapons_table:
        print(x)
        for xx in weapons_table[x]:
            print('    ',xx)
            for xxx in weapons_table[x][xx]:
                print('        ', xxx,':', weapons_table[x][xx][xxx])

def attack_roll(player_or_npc, weapon):
    if weapon == player_or_npc.p_class.currently_equipped:
        print('%s attacks with a %s!' % (player_or_npc.name, player_or_npc.p_class.currently_equipped))
        attack_dice = int(random.randrange(1,21))
        attack = attack_dice+player_or_npc.stats.get_mod('STR')
        print('Attack:  %s + %s: %s' % (attack_dice, player_or_npc.stats.get_mod('STR'), attack))
        return attack
    else: print('You do not have a %s equipped!' % weapon)

def attack_damage(attacker, defender):
    pass





#*************************************************************************************
#********************************PLAYER/NPC ASSIGNMENT********************************






#***********************************************************************
#**************************GLOBAL TABLES/DICTS**************************
#see TABLES.py

weapons_table = TABLES.weapons_table

#**********Assigning Creature Stats***********
  #Will be determined by a separate menu later (GUI Input)
base_stats = {'STR':10, 'DEX':10, 'CON':10, 'WIS':10, 'INT': 10, 'CHA':10}
creature_stats = Creature(base_stats)

#Need to add more attributes such as proficiencies and skills, attacks - import to Class()
fighter = TABLES.fighter
barbarian = TABLES.barbarian

#*****Races (see TABLES.py)- will add more options later (proficiencies, bonus skills/abilities)*****
human_race = TABLES.hr1
elf_high = TABLES.erh1
elf_wood = TABLES.erw1
elf_dark = TABLES.erd1


#*******************************************************************************
#***********************************TESTING*************************************

p1 = Player('Test Guy', human_race, Class(fighter), AbilityStats(human_race, creature_stats))
print(p1.name)
p2 = AbilityStats(human_race, creature_stats)
print(p1.race)
print(p1.stats.get_stat('STR'))
print(p1.stats.get_mod('STR'))
p1.stats.str_stat +=1
print(p1.stats.get_stat('STR'))
print(p1.stats.get_mod('STR'))
print(p1.max_hp())
p1.level += 1
print(p1.max_hp())
print(p1.race['Vision'])

attack_roll(p1, 'Greatsword')
attack_roll(p1, 'Dummy Sword')
