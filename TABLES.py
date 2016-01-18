#*****Class(dict('Class Name', Class Level, Start HP, HP Per Level... etc))*****
#Need to add more attributes such as proficiencies and skills, attacks - import to Class()
fighter = {'Class Name':'Fighter',
           'Class Level': 1,
           'Start HP': 10,
           'HP Per Level': 6,
           'Armor': 14,
           'Weapon Damage': '2d6',
           'Weapon Name':'Greatsword',
           'Weapon Magic Bonus': 0}


barbarian = {'Class Name':'Barbarian',
             'Class Level':1,
             'Start HP': 12,
             'HP Per Level': 7,
             'Armor': 15,
             'Weapon Damage': '2d6',
             'Weapon Name':'Greatsword',
             'Weapon Magic Bonus': 0}



#race_title = ['Name', 'Size', 'Speed', 'Str Bonus', 'Dex Bonus', 'Con Bonus', 'Wis Bonus', 'Int Bonus', 'Cha Bonus', 'Languages', 'Vision']
#print({k: v for k, v in zip(race_title, elven_race_dark)})

#Humans
hr1 = {'Int Bonus': 1,
       'Wis Bonus': 1,
       'Languages': ['Common', 'Extra Language'],
       'Con Bonus': 1,
       'Str Bonus': 1,
       'Dex Bonus': 1,
       'Vision': 'Normal',
       'Size': 'Medium',
       'Name': 'Human',
       'Speed': 30,
       'Cha Bonus': 1}

#Elves (High)
erh1 = {'Vision': 'Darkvision (60ft)',
        'Cha Bonus': 0,
        'Size': 'Medium',
        'Name': 'High Elf',
        'Str Bonus': 0,
        'Con Bonus': 0,
        'Int Bonus': 1,
        'Languages': ['Common', 'Elvish', '1 Extra Language'],
        'Dex Bonus': 2,
        'Wis Bonus': 0,
        'Speed': 30}

#Elves (Wood)
erw1 = {'Dex Bonus': 2,
        'Name': 'Wood Elf',
        'Str Bonus': 0,
        'Speed': 35,
        'Languages': ['Common', 'Elvish'],
        'Cha Bonus': 0,
        'Con Bonus': 0,
        'Int Bonus': 0,
        'Wis Bonus': 1,
        'Vision': 'Darkvision (60ft)',
        'Size': 'Medium'}

#Elves (Dark/Drow)
erd1 = {'Str Bonus': 0,
        'Int Bonus': 0,
        'Name': 'Drow',
        'Speed': 30,
        'Cha Bonus': 1,
        'Size': 'Medium',
        'Languages': ['Common', 'Elvish'],
        'Dex Bonus': 2,
        'Con Bonus': 0,
        'Vision': 'Darkvision (120ft)',
        'Wis Bonus': 0}





#CREATION OF WEAPONS TABLE - 4 MELEE EXAMPLES (TWO WITH RANGED PROPERTIES), 1 PURELY RANGED
weapons_table = {'Simple Melee':
                    {'Club':
                         {'Damage':'1d4','Damage Type':'Bludgeoning','Weight':2,'Properties':['Light']},
                    'Dagger':
                         {'Damage':'1d4','Damage Type':'Piercing','Weight':2,'Properties':['Finesse', 'Light', 'Thrown 20/60']},
                    'Greatclub':
                         {'Damage':'1d8','Damage Type':'Bludgeoning', 'Weight':10,'Properties':['Two-Handed']},
                    'Handaxe':
                         {'Damage':'1d6', 'Damage Type':'Slashing', 'Weight':2,'Properties':['Light, Thrown 20/60']}},
                'Simple Ranged':
                    {'Shortbow':
                         {'Damage':'1d6','Damage Type':'Piercing','Weight':2,'Properties':['Ammunition','Two-Handed', 'Range 80/320']}
                        }}
# Printing a Property of a weapon example:
# print(weapons_table['Simple Ranged']['Shortbow']['Properties'][2])  #Notes for later: user input to select currently equipped weapon
