import time

PLANT_BASE_STATS = {
    "dummy": {
        "name": "",
        "hp": 0,
        "atkRange": 0,
        "speed": 0,
        "ability1": "",
        "ability2": "",
        "ability3": "",
        "ability4": "",
        "ability5": "",
    },
    "cattail": {
        "name": "Cattail",
        "hp": 150,
        "atkRange": 5,
        "speed": 5,
        "ability1": "Tail Spike",
        "ability2": "Lightning Spike",
        "ability3": "Homing Missile",
        "ability4": "",
        "ability5": "",
    },
    "chomper": {
        "name": "Chomper",
        "hp": 150,
        "atkRange": 2,
        "speed": 5,
        "ability1": "Chomp",
        "ability2": "Finishing Bite",
        "ability3": "Burrow",
        "ability4": "",
        "ability5": "",
    },
    "citron": {
        "name": "Citron",
        "hp": 210,
        "atkRange": 5,
        "speed": 5,
        "ability1": "Orange Beam",
        "ability2": "Citron Ball",
        "ability3": "Navel Laser",
        "ability4": "",
        "ability5": "",
    },
    "guacodile": {
        "name": "Guacodile",
        "hp": 150,
        "atkRange": 5,
        "speed": 8,
        "ability1": "Pit Shot",
        "ability2": "Gatorush",
        "ability3": "Hungry Guacodiles",
        "ability4": "",
        "ability5": "",
    },
    "laserBean": {
        "name": "Laser Bean",
        "hp": 150,
        "atkRange": 8,
        "speed": 5,
        "ability1": "Laserbeam",
        "ability2": "Gamma-ray Blast",
        "ability3": "X-ray Flux",
        "ability4": "Overbean",
        "ability5": "",
    },
    "melonPult": {
        "name": "Melon-Pult",
        "hp": 150,
        "atkRange": 5,
        "speed": 3,
        "ability1": "Melon Lob",
        "ability2": "Spittling Slices",
        "ability3": "Melon Mortar",
        "ability4": "Melon Roll",
        "ability5": "Melon Rain",
    },
    "moonflower": {
        "name": "Moonflower",
        "hp": 150,
        "atkRange": 5,
        "speed": 5,
        "ability1": "Dark Staff",
        "ability2": "Lifesteal",
        "ability3": "",
        "ability4": "",
        "ability5": "",
    },
    "nightcap": {
        "name": "Nightcap",
        "hp": 150,
        "atkRange": 5,
        "speed": 5,
        "ability1": "Spore Strike",
        "ability2": "Fung Fu",
        "ability3": "Shadow Surge",
        "ability4": "",
        "ability5": "",
    },
    "peashooter": {
        "name": "Peashooter",
        "hp": 150,
        "atkRange": 5,
        "speed": 6,
        "ability1": "Pea Shot",
        "ability2": "Mega Gatling Pea",
        "ability3": "",
        "ability4": "",
        "ability5": "",
    },
    "puffShroom": {
        "name": "Puff-Shroom",
        "hp": 60,
        "atkRange": 3,
        "speed": 8,
        "ability1": "Puff Shot",
        "ability2": "",
        "ability3": "",
        "ability4": "",
        "ability5": "",
    },
    "rotobaga": {
        "name": "Rotobaga",
        "hp": 60,
        "atkRange": 5,
        "speed": 5,
        "ability1": "X-Shot",
        "ability2": "Rotating Rutablast",
        "ability3": "Corn Strike",
        "ability4": "Counter Cross",
        "ability5": "",
    },
    "snapdragon": {
        "name": "Snapdragon",
        "hp": 150,
        "atkRange": 5,
        "speed": 5,
        "ability1": "Flame Blower",
        "ability2": "Swoop Slam",
        "ability3": "Blue Blazes",
        "ability4": "Dragonfire",
        "ability5": "",
    },
    "starfruit": {
        "name": "Starfruit",
        "hp": 150,
        "atkRange": 5,
        "speed": 8,
        "ability1": "Twin Stars",
        "ability2": "Shooting Stars",
        "ability3": "Starburst",
        "ability4": "Starstruck",
        "ability5": "",
    },
    "wallNut": {
        "name": "Wall-Nut",
        "hp": 300,
        "atkRange": 5,
        "speed": 3,
        "ability1": "Wall-Nut Bowling",
        "ability2": "",
        "ability3": "",
        "ability4": "",
        "ability5": "",
    },
}

ZOMBIE_BASE_STATS = {
    "dummy": {
        "name": "",
        "hp": 0,
        "sunDrop": 0,
        "loCoinDrop": 0,
        "hiCoinDrop": 0,
    },
    "browncoat": {
        "name": "Browncoat Zombie",
        "hp": 25,
        "sunDrop": 5,
        "loCoinDrop": 7,
        "hiCoinDrop": 13,
    },
    "conehead": {
        "name": "Conehead Zombie",
        "hp": 60,
        "sunDrop": 10,
        "loCoinDrop": 12,
        "hiCoinDrop": 18,
    },
    "buckethead": {
        "name": "Buckethead Zombie",
        "hp": 100,
        "sunDrop": 15,
        "loCoinDrop": 17,
        "hiCoinDrop": 23,
    },
    "brickhead": {
        "name": "Brickhead Zombie",
        "hp": 175,
        "sunDrop": 20,
        "loCoinDrop": 22,
        "hiCoinDrop": 28,
    },
    "midManager": {
        "name": "Zombie Middle Manager",
        "hp": 40,
        "sunDrop": 15,
        "loCoinDrop": 17,
        "hiCoinDrop": 23,
    },
    "flagZombie": {
        "name": "Flag Zombie - Boss",
        "hp": 120,
        "sunDrop": 0,
        "loCoinDrop": 0,
        "hiCoinDrop": 0,
    },
    "frozenZombie": {
        "name": "Frozen Zombie",
        "hp": 70,
        "sunDrop": 5,
        "loCoinDrop": 7,
        "hiCoinDrop": 13,
    },
    "iceBlockZombie": {
        "name": "Ice Block Zombie",
        "hp": 210,
        "sunDrop": 20,
        "loCoinDrop": 22,
        "hiCoinDrop": 28,
    },
    "skiZombie": {
        "name": "Ski Zombie",
        "hp": 80,
        "sunDrop": 10,
        "loCoinDrop": 12,
        "hiCoinDrop": 18,
    },
    "icicleZombie": {
        "name": "Icicle Zombie",
        "hp": 40,
        "sunDrop": 10,
        "loCoinDrop": 12,
        "hiCoinDrop": 18,
    },
    "yetiImp": {
        "name": "Yeti Imp",
        "hp": 15,
        "sunDrop": 10,
        "loCoinDrop": 12,
        "hiCoinDrop": 18,
    },
    "zomboni": {
        "name": "Zomboni - Boss",
        "hp": 250,
        "sunDrop": 0,
        "loCoinDrop": 0,
        "hiCoinDrop": 0,
    },
}

LOWEST_ABILITY_ROLL_NUMBER = {
    "dummy": [],
    "cattail": [2, 6, 20],
    "chomper": [2, 5, 10],
    "citron": [2, 15, 20],
    "guacodile": [2, 13, 20],
    "laserBean": [2, 7, 13, 20],
    "melonPult": [2, 6, 10, 13, 20],
    "moonflower": [2, 12],
    "nightcap": [2, 7, 20],
    "peashooter": [2, 20],
    "puffShroom": [2],
    "rotobaga": [2, 10, 11, 20],
    "snapdragon": [2, 9, 10, 20],
    "starfruit": [2, 11, 13, 20],
    "wallNut": [2],
}

class Player():
    def __init__(self, name: str, charClass: str, level: int, exp: int, currentHP: int):
        self.name       = name
        self.charClass  = charClass
        self.level      = level
        self.exp        = exp

        self.currentHp  = currentHP
        self.maxHp      = PLANT_BASE_STATS[self.charClass]["hp"]
        self.atkRange   = PLANT_BASE_STATS[self.charClass]["atkRange"]
        self.speed      = PLANT_BASE_STATS[self.charClass]["speed"]
    
    def print(self):
        print(f"==== {self.name.upper()} the {PLANT_BASE_STATS[self.charClass]['name'].upper()} ====")
        print(f"Lv.{self.level} [Sun - {self.exp}/{self.level * 25}]")
        print(f"HP: {self.currentHp}/{self.maxHp}    ATK RANGE: {self.atkRange}    SPEED: {self.speed}\n")

players = [
    Player("Bean",      "laserBean",    2, 0,   150),
    Player("Chicken",   "cattail",      3, 10,  150),
    Player("Comet",     "starfruit",    2, 0,   150),
    Player("Cpiya",     "puffShroom",   4, 60,  60),
    Player("Dark",      "nightcap",     4, 40,  150),
    Player("Darten",    "moonflower",   4, 5,   150),
    Player("Dzaky",     "snapdragon",   2, 40,  150),
    Player("Endy",      "peashooter",   2, 5,   150),
    Player("Kenny",     "starfruit",    3, 60,  150),
    Player("Kray",      "citron",       4, 75,  210),
    Player("Nuttin'",   "wallNut",      3, 55,  230),
    Player("Player",    "melonPult",    5, 25,  125),
    Player("Rocky",     "guacodile",    4, 20,  150),
    Player("Sani",      "chomper",      2, 0,   150),
    Player("Wren",      "rotobaga",     2, 0,   60),
]

def firstScreenMenu():
    print("===== CHOOSE AN OPTION =====")
    print("1. Calculate Plant Damage (to Zombies/Hazards)")
    print("2. Calculate Zombie Damage (to Plants/Hazards)")
    print("3. Info")
    print("\n0. EXIT")
    try:
        option = int(input("> "))
    except ValueError:
        print("ERR: This value is not a valid number.")
        print("Input anything to return to the menu.")
        input()
        firstScreenMenu()
    else:
        if option > 3 or option < 0:
            print("ERR: The menu number entered doesn't exist.")
            print("Input anything to return to the menu.")
            input()
            firstScreenMenu()
        else:
            if option != 0:
                print()
                secondScreenMenu(option)
            else:
                time.sleep(1)

def secondScreenMenu(mode: int):
    if mode == 1: # Calculate Plant Damage
        print("== Which player is doing damage? ==")
        for k, v in enumerate(players):
            print(f"{str(k + 1) + '.':<3} {v.name:<12} ({PLANT_BASE_STATS[v.charClass]['name']})")
        print("\n0. BACK")

        try:
            option = int(input("> "))
        except ValueError:
            print("ERR: This value is not a valid number.")
            print("Input anything to return to the menu.")
            input()
            secondScreenMenu(mode)
        else:
            if option > len(players) or option < 0:
                print("ERR: The menu number entered doesn't exist.")
                print("Input anything to return to the menu.")
                input()
                secondScreenMenu(mode)
            else:
                if option != 0:
                    print()
                    plantAttackMenu(option - 1, players[option - 1].charClass)
                else:
                    print()
                    firstScreenMenu()
    elif mode == 2:
        print("== Which zombie is doing damage? ==")
        for k, v in enumerate(ZOMBIE_BASE_STATS):
            if v != "dummy":
                pass
                print(f"{str(k) + '.':<3} {ZOMBIE_BASE_STATS[v]['name']:<24}")
        print("\n0. BACK")

        option = int(input("> "))
    else:
        print("== Info Screen ==")
        print("1. Show Every Player Info")
        print("2. Show Every Zombie Info")

        print("\n0. BACK")

        try:
            option = int(input("> "))
        except ValueError:
            print("ERR: This value is not a valid number.")
            print("Input anything to return to the menu.")
            input()
            secondScreenMenu(mode)
        else:
            if option > 2 or option < 0:
                print("ERR: The menu number entered doesn't exist.")
                print("Input anything to return to the menu.")
                input()
                secondScreenMenu(mode)
            else:
                print()
                if option == 0:
                    firstScreenMenu()
                elif option == 1:
                    for k, v in enumerate(players):
                        v.print()
                    input("Input anything to return to the menu.\n")
                    secondScreenMenu(mode)
                elif option == 2:
                    for k, v in enumerate(ZOMBIE_BASE_STATS):
                        if v != "dummy":
                            print(f"==== {ZOMBIE_BASE_STATS[v]['name'].upper()} ====")
                            print(f"HP: {ZOMBIE_BASE_STATS[v]['hp']}", end = "    ")

                            if ZOMBIE_BASE_STATS[v]["sunDrop"] != 0:
                                print(f"SUN: {ZOMBIE_BASE_STATS[v]['sunDrop']}", end = "    ")
                            
                            if ZOMBIE_BASE_STATS[v]["loCoinDrop"] != 0 and ZOMBIE_BASE_STATS[v]["hiCoinDrop"] != 0:
                                print(f"COINS: {ZOMBIE_BASE_STATS[v]['loCoinDrop']}-{ZOMBIE_BASE_STATS[v]['hiCoinDrop']}", end = "")
                            print("\n")
                    input("Input anything to return to the menu.\n")
                    secondScreenMenu(mode)



def plantAttackMenu(playerIndex: int, mode: str):
    print("== Which ability? ==")
    match mode:
        case "cattail":
            print("1. Tail Spike            (2+)")
            print("2. Lightning Spike       (6+)")
            print("3. Homing Missile        (Nat 20)")
            print("\n0. BACK")
        case "chomper":
            print("1. Chomp                 (2+)")
            print("2. Finishing Bite        (5+)")
            print("3. Burrow                (10+)")
            print("\n0. BACK")
        case "citron":
            print("1. Orange Beam           (2+)")
            print("2. Citron Ball           (15+)")
            print("3. Navel Laser           (Nat 20)")
            print("\n0. BACK")
        case "guacodile":
            print("1. Pit Shot              (2+)")
            print("2. Gatorush              (13+)")
            print("3. Hungry Guacodiles     (Nat 20)")
            print("\n0. BACK")
        case "laserBean":
            print("1. Laserbeam             (2+)")
            print("2. Gamma-ray Blast       (7+)")
            print("3. X-ray Flux            (13+)")
            print("4. Overbean              (Nat 20)")
            print("\n0. BACK")
        case "melonPult":
            print("1. Melon Lob             (2+)")
            print("2. Splitting Slices      (6+)")
            print("3. Melon Mortar          (10+)")
            print("4. Melon Roll            (13+)")
            print("5. Melon Rain            (Nat 20)")
            print("\n0. BACK")
        case "moonflower":
            print("1. Dark Staff            (2+)")
            print("2. Lifesteal             (12+)")
            print("\n0. BACK")
        case "nightcap":
            print("1. Spore Strike          (2+)")
            print("2. Fung Fu               (7+)")
            print("3. Shadow Surge          (Nat 20)")
            print("\n0. BACK")
        case "peashooter":
            print("1. Pea Shot              (2+)")
            print("2. Mega Gatling Pea      (Nat 20)")
            print("\n0. BACK")
        case "puffShroom":
            print("1. Puff Shot             (2+)")
            print("\n0. BACK")
        case "rotobaga":
            print("1. X-Shot                (2+)")
            print("2. Rotating Rutablast    (10+)")
            print("3. Corn Strike           (11+)")
            print("4. Counter Cross         (Nat 20)")
            print("\n0. BACK")
        case "snapdragon":
            print("1. Flame Blower          (2+)")
            print("2. Swoop Slam            (9+)")
            print("3. Blue Blazes           (10+)")
            print("4. Dragonfire            (Nat 20)")
            print("\n0. BACK")
        case "starfruit":
            print("1. Twin Stars            (2+)")
            print("2. Shooting Stars        (11+)")
            print("3. Starburst             (13+)")
            print("4. Starstruck            (Nat 20)")
            print("\n0. BACK")
        case "wallNut":
            print("1. Wall-Nut Bowling      (2+)")
            print("\n0. BACK")
        case default:
            print("how did you found this message")
    
    try:
        option = int(input("> "))
    except ValueError:
        print("ERR: This value is not a valid number.")
        print("Input anything to return to the menu.")
        input()
        plantAttackMenu(playerIndex, mode)
    else:
        if ((mode == "puffShroom" or mode == "wallNut") and (option > 1)) or ((mode == "moonflower" or mode == "peashooter") and (option > 2)) or ((mode == "laserBean" or mode == "rotobaga" or mode == "snapdragon" or mode == "starfruit") and (option > 4)) or ((mode == "melonPult") and (option > 5)) or (option < 0):
            print("ERR: This value is not a valid number.")
            print("Input anything to return to the menu.")
            input()
            plantAttackMenu(playerIndex, mode)
        else:
            if (option > 3) and not (mode == "laserBean" or mode == "rotobaga" or mode == "snapdragon" or mode == "starfruit" or mode == "melonPult"):
                print("ERR: This value is not a valid number.")
                print("Input anything to return to the menu.")
                input()
                plantAttackMenu(playerIndex, mode)
            else:
                if option == 0:
                    print()
                    secondScreenMenu(1)
                else:
                    getDiceRoll(playerIndex, mode, option)

def getDiceRoll(playerIndex: int, plantClass: str, mode: int):
    if LOWEST_ABILITY_ROLL_NUMBER[plantClass][mode - 1] != 20:
        print(f"What is the dice roll result? ({LOWEST_ABILITY_ROLL_NUMBER[plantClass][mode - 1]}-20)")
        print("Write 'back' or 'BACK' to return to the previous menu.")
        temp = input("> ")
    else:
        temp = 20

    try:
        diceRoll = int(temp)
    except ValueError:
        if (type(temp) is str) and (temp.lower() == "back"):
            print()
            plantAttackMenu(playerIndex, plantClass)
        else:
            print("ERR: This value is not a valid number or a string containing 'BACK' or 'back'.")
            print("Input anything to return to the menu.")
            input()
            getDiceRoll(playerIndex, plantClass, mode)
    else:
        if diceRoll < LOWEST_ABILITY_ROLL_NUMBER[plantClass][mode - 1] or diceRoll > 20:
            print("ERR: The number inserted is not in range.")
            print("Input anything to return to the menu.")
            input()
            getDiceRoll(playerIndex, plantClass, mode)
        else:
            print()
            getZombieHp(playerIndex, plantClass, mode, diceRoll)

def getZombieHp(playerIndex: int, plantClass: str, ability: int, roll: int):
    print("What is the zombie's health? (Use comma for more than one targets)")
    print("Write 'back' or 'BACK' to return to the previous menu.")
    temp = input("> ")

    if temp.lower() != "back":
        zombieHealth = temp.split(",")
        junkData = []

        # filter out junk (non integers)
        for k, v in enumerate(zombieHealth):
            try:
                hp = int(v)
            except ValueError:
                junkData.append(v)
            else:
                zombieHealth[k] = hp # type: ignore
        
        # remove said junk
        for i in range(len(junkData)):
            zombieHealth.remove(junkData[i])
        
        if len(zombieHealth) < 1:
            print("ERR: The string of values aren't considered valid.")
            print("Input anything to return to the menu.")
            input()
            getZombieHp(playerIndex, plantClass, ability, roll)
        else:
            print()
            calculateDamage(playerIndex, plantClass, ability, roll, zombieHealth)
    else:
        print()
        getDiceRoll(playerIndex, plantClass, ability)

def calculateDamage(playerIndex: int, plantClass: str, ability: int, roll: int, zombieHealth: list):
    match plantClass:
        case "cattail":
            if ability == 1: # Tail Spike (2+)
                damage = (20 + roll) * players[playerIndex].level
            elif ability == 2: # Lightning Spike (6+)
                damage = (15 + roll) * players[playerIndex].level
            else: # Homing Missile (Nat20)
                damage = 75 * players[playerIndex].level
        case "chomper":
            if ability == 1: # Chomp (2+)
                damage = (20 + roll) * players[playerIndex].level
            elif ability == 2: # Finishing Bite (5+)
                damage = (5 + roll) * players[playerIndex].level
            else: # Burrow (10+)
                damage = (40 + roll) * players[playerIndex].level
        case "citron":
            if ability == 1: # Orange Beam (2+)
                damage = (26 + roll) * players[playerIndex].level
            elif ability == 2: # Citron Ball (15+)
                damage = (39 + roll) * players[playerIndex].level
            else: # Navel Laser (Nat 20)
                damage = 78 * players[playerIndex].level
        case "guacodile":
            if ability == 1: # Pit Shot (2+)
                damage = (20 + roll) * players[playerIndex].level
            elif ability == 2: # Gatorush (13+)
                damage = (25 + roll) * players[playerIndex].level
            else: # Hungry Guacodiles (Nat 20)
                damage = (25 + roll) * players[playerIndex].level
        case "laserBean":
            if ability == 1: # Laserbeam (2+)
                damage = (16 + roll) * players[playerIndex].level
            elif ability == 2: # Gamma-ray Blast (7+)
                damage = (24 + roll) * players[playerIndex].level
            elif ability == 3: # X-ray Flux (13+)
                damage = (80 + roll) * players[playerIndex].level
            else: # Overbean (Nat 20)
                damage = 64 * players[playerIndex].level
        case "melonPult":
            if ability == 1: # Melon Lob (2+)
                damage = (26 + roll) * players[playerIndex].level
            elif ability == 2: # Splitting Slices (6+)
                damage = (26 + roll) * players[playerIndex].level
            elif ability == 3: # Melon Mortar (10+)
                damage = (52 + roll) * players[playerIndex].level
            elif ability == 4: # Melon Roll (13+)
                damage = (20 + roll) * players[playerIndex].level
            else: # Melon Rain (Nat 20)
                damage = (26 + roll) * players[playerIndex].level
        case "moonflower":
            if ability == 1: # Dark Staff (2+)
                damage = (20 + roll) * players[playerIndex].level
            else: # Lifesteal (12+)
                damage = (30 + roll) * players[playerIndex].level
        case "nightcap":
            if ability == 1: # Spore Strike (2+)
                damage = (20 + roll) * players[playerIndex].level
            elif ability == 2: # Fung Fu (7+)
                damage = (30 + roll) * players[playerIndex].level
            else: # Shadow Surge (Nat 20)
                damage = 30 * players[playerIndex].level
        case "peashooter":
            if ability == 1: # Pea Shot (2+)
                damage = (22 + roll) * players[playerIndex].level
            else: # Mega Gatling Pea (Nat 20)
                damage = 77 * players[playerIndex].level
        case "puffShroom":
            # Puff Shot (2+)
            damage = (20 + roll) * players[playerIndex].level
        case "rotobaga":
            if ability == 1: # X-Shot (2+)
                damage = (20 + roll) * players[playerIndex].level
            elif ability == 2: # Rotating Rutablast (10+)
                damage = (20 + roll) * players[playerIndex].level
            elif ability == 3: # Corn Strike (11+)
                damage = (20 + roll) * players[playerIndex].level
            else: # Counter Cross (Nat 20)
                damage = 40 * players[playerIndex].level
        case "snapdragon":
            if ability == 1: # Flame Blower (2+)
                damage = (20 + roll) * players[playerIndex].level
            elif ability == 2: # Swoop Slam (9+)
                damage = (25 + roll) * players[playerIndex].level
            elif ability == 3: # Blue Blazes (10+)
                damage = (30 + roll) * players[playerIndex].level
            else: # Dragonfire (Nat 20)
                damage = 60 * players[playerIndex].level
        case "starfruit":
            if ability == 1: # Twin Stars (2+)
                damage = (20 + roll) * players[playerIndex].level
            elif ability == 2: # Shooting Stars (11+)
                damage = (20 + roll) * players[playerIndex].level
            elif ability == 3: # Starburst (13+)
                damage = (20 + roll) * players[playerIndex].level
            else: # Starstruck (Nat 20)
                damage = 40 * players[playerIndex].level
        case "wallNut":
            #Wall-Nut Bowling (2+)
            damage = (20 + roll) * players[playerIndex].level
        case default:
            damage = 0
    
    # print the initial text
    print(f"{players[playerIndex].name} the {PLANT_BASE_STATS[players[playerIndex].charClass]['name']} uses {PLANT_BASE_STATS[players[playerIndex].charClass][f'ability{ability}']} on ", end = "")

    if len(zombieHealth) > 1:
        print("Zombies with ", end = "")

        for i in range(len(zombieHealth)):
            print(f"{zombieHealth[i]} HP", end = "")

            if i < len(zombieHealth) - 1:
                print(", ", end = "")
    else:
        print(f"a Zombie with {zombieHealth[0]} HP", end = "")
    
    print(f" for {damage} damage!")

    for i in range(len(zombieHealth)):
        if i + 1 == 1:
            ordinal = "st"
        elif i + 1 == 2:
            ordinal = "nd"
        elif i + 1 == 3:
            ordinal = "rd"
        else:
            ordinal = "th"
        print(f"The {i + 1}{ordinal} zombie with {zombieHealth[i]} HP ", end = "")
        zombieHealth[i] -= damage

        if zombieHealth[i] > 0:
            print(f"now has {zombieHealth[i]} HP!")
        else:
            print("is defeated!")
    input("\nInput anything to continue.\n")
    secondScreenMenu(1)

def main():
    print()
    print("╔════════ WELCOME TO DUNGEONS & DUCKY TUBES CALCULATOR ════════╗")
    print("║     Program created by IAmPlayer. Discord: @notiamplayer     ║")
    print("║        Dungeon Master: DMDarkMatter (@darkmatter102)         ║")
    print("║        Server Owner/Game Manager: Nuttin' (@poopy38)         ║")
    print("╚══════════════════════════════════════════════════════════════╝", end= "\n\n")
    time.sleep(1)
    firstScreenMenu()

if __name__ == "__main__":
    main()