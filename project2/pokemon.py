import math, random

baseStatLookupTable = [
    #HP, ATK, DEF, SPA, SPD, SPE
    [0,   0,   0,   0,   0,   0],   #000 - ???
    [45,  49,  49,  65,  65,  45],  #001 - Bulbasaur
    [60,  62,  63,  80,  80,  60],  #002 - Ivysaur
    [80,  82,  83,  100, 100, 80],  #003 - Venusaur
    [39,  52,  43,  60,  50,  65],  #004 - Charmander
    [58,  64,  58,  80,  65,  80],  #005 - Charmeleon
    [78,  84,  78,  109, 85,  100], #006 - Charizard
    [44,  48,  65,  50,  64,  43],  #007 - Squirtle
    [59,  63,  80,  65,  80,  58],  #008 - Wartortle
    [79,  83,  100, 85,  105, 78],  #009 - Blastoise
    [45,  30,  35,  20,  20,  45],  #010 - Caterpie
    [50,  20,  55,  25,  25,  30],  #011 - Metapod
    [60,  45,  50,  90,  80,  70],  #012 - Butterfree
    [40,  35,  30,  20,  20,  50],  #013 - Weedle
    [45,  25,  50,  25,  25,  35],  #014 - Kakuna
    [65,  90,  40,  45,  80,  75],  #015 - Beedrill
    [40,  45,  40,  35,  35,  56],  #016 - Pidgey
    [63,  60,  55,  50,  50,  71],  #017 - Pidgeotto
    [83,  80,  75,  70,  70,  101], #018 - Pidgeot
    [30,  56,  35,  25,  35,  72],  #019 - Rattata
    [55,  81,  60,  50,  70,  97],  #020 - Raticate
    [40,  60,  30,  31,  31,  70],  #021 - Spearow
    [65,  90,  65,  61,  61,  100], #022 - Fearow
    [35,  60,  44,  40,  54,  55],  #023 - Ekans
    [60,  95,  69,  65,  79,  80],  #024 - Arbok
    [35,  55,  40,  50,  50,  90],  #025 - Pikachu
    [60,  90,  55,  90,  80,  110], #026 - Raichu
    [50,  75,  85,  20,  30,  40],  #027 - Sandshrew
    [75,  100, 110, 45,  55,  65],  #028 - Sandslash
    [55,  47,  52,  40,  40,  41],  #029 - Nidoran♀
    [70,  62,  67,  55,  55,  56],  #030 - Nidorina
    [90,  92,  87,  75,  85,  76],  #031 - Nidoqueen
    [46,  57,  40,  40,  40,  50],  #032 - Nidoran♂
    [61,  72,  57,  55,  55,  65],  #033 - Nidorino
    [81,  102, 77,  85,  75,  85],  #034 - Nidoking
    [70,  45,  48,  60,  65,  35],  #035 - Clefairy
    [95,  70,  73,  95,  90,  60],  #036 - Clefable
    [38,  41,  40,  50,  65,  65],  #037 - Vulpix
    [73,  76,  75,  81,  100, 100], #038 - Ninetales
    [115, 45,  20,  45,  25,  20],  #039 - Jigglypuff
    [140, 70,  45,  85,  50,  45],  #040 - Wigglytuff
    [40,  45,  35,  30,  40,  55],  #041 - Zubat
    [75,  80,  70,  65,  75,  90],  #042 - Golbat
    [45,  50,  55,  75,  65,  30],  #043 - Oddish
    [60,  65,  70,  85,  75,  40],  #044 - Gloom
    [75,  80,  85,  110, 90,  50],  #045 - Vileplume
    [35,  70,  55,  45,  55,  25],  #046 - Paras
    [60,  95,  80,  60,  80 , 30],  #047 - Parasect
    [60,  55,  50,  40,  55,  45],  #048 - Venonat
    [70,  65,  60,  90,  75,  90],  #049 - Venomoth
    [10,  55,  25,  35,  45,  95],  #050 - Diglett
    [35,  100, 50,  50,  70,  120], #051 - Dugtrio
    [40,  45,  35,  40,  40,  90],  #052 - Meowth
    [65,  70,  60,  65,  65,  115], #053 - Persian
    [50,  52,  48,  65,  50,  55],  #054 - Psyduck
    [80,  82,  78,  95,  80,  85],  #055 - Golduck
    [40,  80,  35,  35,  45,  70],  #056 - Mankey
    [65,  105, 60,  60,  70,  95],  #057 - Primeape
    [55,  70,  45,  70,  50,  60],  #058 - Growlithe
    [90,  110, 80,  100, 80,  95],  #059 - Arcanine
    [40,  50,  40,  40,  40,  90],  #060 - Poliwag
    [65,  65,  65,  50,  50,  90],  #061 - Poliwhirl
    [90,  95,  95,  70,  90,  70],  #062 - Poliwrath
    [25,  20,  15,  105, 55,  90],  #063 - Abra
    [40,  35,  30,  120, 70,  105], #064 - Kadabra
    [55,  50,  45,  135, 95,  120], #065 - Alakazam
    [70,  80,  50,  35,  35,  35],  #066 - Machop
    [80,  100, 70,  50,  60,  45],  #067 - Machoke
    [90,  130, 80,  65,  85,  55],  #068 - Machamp
    [50,  75,  35,  70,  30,  40],  #069 - Bellsprout
    [65,  90,  50,  85,  45,  55],  #070 - Weepinbell
    [80,  105, 65,  100, 70,  70],  #071 - Victreebel
    [], #072 - 
    [], #073 - 
    [], #074 - 
    [], #075 - 
    [], #076 - 
    [], #077 - 
    [], #078 - 
    [], #079 - 
    [], #080 - 
    [], #081 - 
    [], #082 - 
    [], #083 - 
    [], #084 - 
    [], #085 - 
    [], #086 - 
    [], #087 - 
    [], #088 - 
    [], #089 - 
    [], #090 - 
    [], #091 - 
    [], #092 - 
    [], #093 - 
    [], #094 - 
    [], #095 - 
    [], #096 - 
    [], #097 - 
    [], #098 - 
    [], #099 - 
    [], #100 - 
    [], #101 - 
    [], #102 - 
    [], #103 - 
    [], #104 - 
    [], #105 - 
    [], #106 - 
    [], #107 - 
    [], #108 - 
    [], #109 - 
    [], #110 - 
    [], #111 - 
    [], #112 - 
    [], #113 - 
    [], #114 - 
    [], #115 - 
    [], #116 - 
    [], #117 - 
    [], #118 - 
    [], #119 - 
    [], #120 - 
    [], #121 - 
    [], #122 - 
    [], #123 - 
    [], #124 - 
    [], #125 - 
    [], #126 - 
    [], #127 - 
    [], #128 - 
    [], #129 - 
    [], #130 - 
    [], #131 - 
    [], #132 - 
    [], #133 - 
    [], #134 - 
    [], #135 - 
    [], #136 - 
    [], #137 - 
    [], #138 - 
    [], #139 - 
    [], #140 - 
    [], #141 - 
    [], #142 - 
    [], #143 - 
    [], #144 - 
    [], #145 - 
    [], #146 - 
    [], #147 - 
    [], #148 - 
    [], #149 - 
    [], #150 - 
    [], #151 - 
]

natureLookupTable = [
    [1,   1,   1,   1,   1],    # HARDY   (Neutral)
    [1.1, 0.9, 1,   1,   1],    # LONELY  (+ ATK, - DEF)
    [1.1, 1,   1,   1,   0.9],  # BRAVE   (+ ATK, - SPE)
    [1.1, 1,   0.9, 1,   1],    # ADAMANT (+ ATK, - SPA)
    [1.1, 1,   1,   0.9, 1],    # NAUGHTY (+ ATK, - SPD)
    [0.9, 1.1, 1,   1,   1],    # BOLD    (+ DEF, - ATK)
    [1,   1,   1,   1,   1],    # DOCILE  (Neutral)
    [1,   1.1, 1,   1,   0.9],  # RELAXED (+ DEF, - SPE)
    [1,   1.1, 0.9, 1,   1],    # IMPISH  (+ DEF, - SPA)
    [1,   1.1, 1,   0.9, 1],    # LAX     (+ DEF, - SPD)
    [0.9, 1,   1,   1,   1.1],  # TIMID   (+ SPE, - ATK)
    [1,   0.9, 1,   1,   1.1],  # HASTY   (+ SPE, - DEF)
    [1,   1,   1,   1,   1],    # SERIOUS (Neutral)
    [1,   1,   0.9, 1,   1.1],  # JOLLY   (+ SPE, - SPA)
    [1,   1,   1,   0.9, 1.1],  # NAIVE   (+ SPE, - SPD)
    [0.9, 1,   1.1, 1,   1],    # MODEST  (+ SPA, - ATK)
    [1,   0.9, 1.1, 1,   1],    # MILD    (+ SPA, - DEF)
    [1,   1,   1.1, 1,   0.9],  # QUIET   (+ SPA, - SPE)
    [1,   1,   1,   1,   1],    # BASHFUL (Neutral)
    [1,   1,   1.1, 0.9, 1],    # RASH    (+ SPA, - SPD)
    [0.9, 1,   1,   1.1, 1],    # CALM    (+ SPD, - ATK)
    [1,   0.9, 1,   1.1, 1],    # GENTLE  (+ SPD, - DEF)
    [1,   1,   1,   1.1, 0.9],  # SASSY   (+ SPD, - SPE)
    [1,   1,   0.9, 1.1, 1],    # CAREFUL (+ SPD, - SPA)
    [1,   1,   1,   1,   1],    # QUIRKY  (Neutral)
]

class Pokemon():
    def __init__(self, id: int, level: int):
        self.id = id
        self.ev = [0, 0, 0, 0, 0, 0]
        self.iv = [random.randint(0, 31), random.randint(0, 31), random.randint(0, 31),
                   random.randint(0, 31), random.randint(0, 31), random.randint(0, 31)]
        self.level = level
        self.nature = random.randint(0, 24)
        
        self.updateStats()
        self.hp = self.stat[0]

    def updateStats(self):
        self.stat = []

        self.stat.append(math.floor(
            ((2 * baseStatLookupTable[self.id][0] + self.iv[0] + math.floor(self.ev[0]/4)) * self.level)/100
            ) + self.level + 10
        ) # HP
        
        for i in range(1, 6): # Attack, Defense, Sp. Atk, Sp. Def, Speed
            self.stat.append(math.floor((math.floor(
                ((2 * baseStatLookupTable[self.id][i] + self.iv[i] + math.floor(self.ev[i]/4)) * self.level)/100
                ) + 5) * natureLookupTable[self.nature][i - 1])
            )
    
    def print(self):
        print(f'== (No.{str(self.id).zfill(3):>3}) ==')
        print(f'· Lv.{self.level}')
        print(f'· HP     : {self.hp}/{self.stat[0]} ({self.ev[0]}, {self.iv[0]})')
        print(f'· Attack : {self.stat[1]} ({self.ev[1]}, {self.iv[1]})')
        print(f'· Defense: {self.stat[2]} ({self.ev[2]}, {self.iv[2]})')
        print(f'· Sp. Atk: {self.stat[3]} ({self.ev[3]}, {self.iv[3]})')
        print(f'· Sp. Def: {self.stat[4]} ({self.ev[4]}, {self.iv[4]})')
        print(f'· Speed  : {self.stat[5]} ({self.ev[5]}, {self.iv[5]})')

a = Pokemon(random.randint(1, 65), random.randint(1, 100))
a.print()