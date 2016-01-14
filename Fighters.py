import random           #Used in the calculations for dice rolls
import math             #Used in the calculations for distance
import re               #Used in the search for dice values (Ex: '1d6' = [1, 6])
import TABLES           #TABLES.py - stores all character/creature dicts/lists/tables
from tkinter import *   #Allows for GUI input from the user
from PIL import Image, ImageTk

#THINGS TO DO:
#   --PLAYER--
#  Build GUI Interface for Player stats, race, and class selection and storage [start with input('')]
#  Expand race and class stats in TABLES
#  Create either Attack() or def Attacks in Class() - replace global function for attack_roll()
#
#   --ENEMIES--
#  Create Enemy() class, also define a few enemy options/stats (Kobold, Wolf, etc)
#  Create Conditions() class (Slowed, Blinded, Prone, etc), import to Player/Creature
#  Create NPC generator function (max 3 enemies until Player 2/NPC)
#
#   --WORLD--
#  Differentiate Melee vs. Ranged attacks
#  Determine Advantage/Disadvantage possibilities (dict?)
#  Set up Turn-Based scenarios between Player and (any/all) enemies currently on the board
#  Set up overall GUI for game [left panel(Player),middle large panel (grid/board), right panel(Enemy/Enemies)]

#**************************GLOBAL TABLES/DICTS**************************
#see TABLES.py
weapons_table = TABLES.weapons_table

#Need to add more attributes such as proficiencies and skills, attacks - import to Class()
fighter = TABLES.fighter
barbarian = TABLES.barbarian

#*****Races (see TABLES.py)- will add more options later (proficiencies, bonus skills/abilities)*****
human_race = TABLES.hr1
elf_high = TABLES.erh1
elf_wood = TABLES.erw1
elf_dark = TABLES.erd1

#*******OTHER********
selected_race = human_race
selected_class = fighter
player_name = {'Name': 'Player 1'}
player_start_stats = []
player_race_stats = []

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
#********************************CLASSES********************************

class PlayerFrame(Frame):
    """Define Player-side Info/Option Window"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        token_name = 'Aki Tohko Token.png'  #Replace with Player Defined Token in future updates
        self.token(token_name)
        self.p_buttons()


    def token(self, token_name):
        """Player Token Image"""
        player_img = Image.open(token_name)
        resized_p_img = player_img.resize((75,75), Image.ANTIALIAS)
        p_token = ImageTk.PhotoImage(resized_p_img)
        img_label = Label(self, image=p_token)
        img_label.image = p_token
        img_label.grid(row=0)

    def p_buttons(self):
        """Show everything on the left side of the screen - Player Menu"""
        showStats = Label(self, text=('Player Name: %s \n'
                                      'Player Race: %s \n'
                                      'Player Class: %s' % 
                                      (player_name['Name'], selected_race['Name'], selected_class['Class Name'])))
        showStats.grid(row=1)

        showWeap = Button(self, text="Weapons List", command=weapon_recall)
        showWeap.grid(row=2)

        showWeap2 = Button(self, text="Weapons List2", command=weapon_recall)
        showWeap2.grid(row=3)

        showWeap3 = Button(self, text="Weapons List3", command=weapon_recall)
        showWeap3.grid(row=4)





class CenterGrid(Frame):
    """Define Center Play Grid"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.playGrid()

    def playGrid(self):  #NOT WORKING YET
        """Area in Center"""
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        area = Frame(self, bg='Grey')
        area.grid(row=0, column=0, columnspan=2, rowspan=4, padx=5, pady=5, sticky=E+W+S+N)



class EnemyFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.show_enemies()

    def show_enemies(self):
        enemy_list_button = Button(self, text="Enemy List")
        enemy_list_button.grid()


class MainAppFrame(Frame):
    """Initialize main window"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.player_frame = PlayerFrame(master)
        self.center_grid = CenterGrid(master)
        self.enemy_frame = EnemyFrame(master)
        self.mainUI()

    def mainUI(self):
        """Main Window Layout"""
        self.master.title('Fighters(Main)')

        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label='Create Character')  #Need to add def for character create
        fileMenu.add_command(label='Exit', command=self.exit)
        menubar.add_cascade(label='File', menu=fileMenu)

        self.player_frame.pack(side=LEFT,fill=Y, expand=False)
        self.center_grid.pack(side=LEFT,fill=BOTH,expand=True)
        self.enemy_frame.pack(side=LEFT,fill=Y, expand=False)
        #Buttons on Right - will make class later for this


    def exit(self):
        self.quit()



class AbilityStats():
    """Defines player/creature ability stats, allows for __add__"""
    def __init__(self, common=0, strength=0, dexterity=0, constitution=0, wisdom=0, intelligence=0, charisma=0):
        self.str_stat = common+strength
        self.dex_stat = common+dexterity
        self.con_stat = common+constitution
        self.wis_stat = common+wisdom
        self.int_stat = common+intelligence
        self.cha_stat = common+charisma

    def __add__(self, other):
        STR = self.str_stat + other.str_stat
        DEX = self.dex_stat + other.dex_stat
        CON = self.con_stat + other.con_stat
        WIS = self.wis_stat + other.wis_stat
        INT = self.int_stat + other.int_stat
        CHA = self.cha_stat + other.cha_stat
        return AbilityStats(0,STR, DEX, CON, WIS, INT, CHA)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

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



class Class():
    """Allow player to assign class stats (fighter, wizard, etc)"""
    def __init__(self, class_import):
        self.class_name = class_import['Class Name']
        self.class_level = class_import['Class Level']
        self.start_hp = class_import['Start HP']
        self.hp_per_level = class_import['HP Per Level']
        self.armor = class_import['Armor']
        self.currently_equipped = class_import['Weapon Name']
        self.weapon_damage = class_import['Weapon Damage']
        self.weapon_magic_bonus = class_import['Weapon Magic Bonus']

    def class_ability(self):
        """Define class-only ability"""
        pass



class Player():
    """Combines all stats to allow creation of Player"""
    def __init__(self, name, race, p_class, stats):
        #Defined by creating the character:
        #example: character = Player('Player Name',race, Class(class_name), stats_total))
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


#********************************FUNCTIONS********************************
#*************************************************************************


def distance_calc_eucl(creature_1, creature_2):
    """Calculates the distance between two creatures.
    Double Movement on every other diagonal
    """
    distance = int(math.sqrt(((creature_1.x-creature_2.x)**2)+(creature_1.y-creature_2.y)**2))
    return distance

def weapon_recall():
    """Provides a breakdown of stored weapons."""
    for x in weapons_table:
        print(x)
        for xx in weapons_table[x]:
            print('    ',xx)
            for xxx in weapons_table[x][xx]:
                print('        ', xxx,':', weapons_table[x][xx][xxx])

def attack_roll(player_or_npc, weapon):
    """Provides an attack roll, determines if weapon is held"""
    if weapon == player_or_npc.p_class.currently_equipped:
        print('%s attacks with a %s!' % (player_or_npc.name, player_or_npc.p_class.currently_equipped))
        attack_dice = int(random.randrange(1,21))
        attack = attack_dice+player_or_npc.stats.get_mod('STR')
        print('Attack:  %s + %s = [%s vs. AC]' % (attack_dice, player_or_npc.stats.get_mod('STR'), attack))
        return attack
    else: print('You do not have a %s equipped!' % weapon)

def attack_sequence(attacker, defender):
    """Determine if hit, HP, Player/Creature death, Damage"""
    pass

def test_stats(player_1):
    """For debugging purposes, tests all stats - not complete yet"""
    print('%s is a %s %s.  He carries a %s that deals %s Damage on a hit.' % (
    player_1.name, player_1.race['Name'], player_1.p_class.class_name,
    player_1.p_class.currently_equipped, player_1.p_class.weapon_damage
    ))

def create_character():  #Testing Button-command function
    print('Current Names:')
    for x in character_name: print(x)
    character_name.append(input('What is the name?: '))
    print('New Entry Saved!')

def create_main_window():
    root = Tk()
    root.geometry('720x480')
    p_window = MainAppFrame(root).pack(expand=True)
    root.mainloop()

#***********************************************************************



#*******************************************************************************
#***********************************TESTING*************************************

#AblityStats() Testing:

base_stats = AbilityStats(common=10, strength=2, dexterity=1)
start_stats = AbilityStats(common=1)
level4_stats = AbilityStats(dexterity=1, constitution=1)
level8_stats = AbilityStats(dexterity=2)

player_stats = base_stats+\
               start_stats+\
               level4_stats+\
               level8_stats

#---------------------------------
#Creation of Player testing
#player_1 = Player('Test Guy 1', human_race, Class(fighter), player_stats)

create_main_window()
