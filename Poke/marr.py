def topack(pack):
    list = [y for y in (x.strip() for x in pack.splitlines()) if y]
    i = 0
    for word in list:
        if (i == 0):
            print("[" + word + ",")
        elif i == len(list)-1:
            print(word + "]")
        else:
            print(word + ',')
        i += 1
    return "------"


def flip(pack):
    list = [y for y in (x.strip() for x in pack.splitlines()) if y]
    for word in list:
        ind = word.find('|')
        first = word[0:ind]
        second = word[ind+1:]
        print(second + "|" + first)


dic = {"normal": 0,
       "fighting": 0,
       "flying": 0,
       "poison": 0,
       "ground": 0,
       "rock": 0,
       "bug": 0,
       "ghost": 0,
       "steel": 0,
       "fire": 0,
       "water": 0,
       "grass": 0,
       "electric": 0,
       "psychic": 0,
       "ice": 0,
       "dragon": 0,
       "dark": 0,
       "fairy": 0}


def create(pack):
    list = [y for y in (x.strip() for x in pack.splitlines()) if y]
    dice = {"normal": 0,
            "fighting": 0,
            "flying": 0,
            "poison": 0,
            "ground": 0,
            "rock": 0,
            "bug": 0,
            "ghost": 0,
            "steel": 0,
            "fire": 0,
            "water": 0,
            "grass": 0,
            "electric": 0,
            "psychic": 0,
            "ice": 0,
            "dragon": 0,
            "dark": 0,
            "fairy": 0}

    for word in list:
        ind = word.find(',')
        sep = word.find('|')
        first = word[sep+1:ind]
        if sep == -1:
            first = word[0:ind]

        second = int(word[ind+1:].strip())
        dice[first] = second
    newprint(dice)


list = ["normal",
        "fighting",
        "flying",
        "poison",
        "ground",
        "rock",
        "bug",
        "ghost",
        "steel",
        "fire",
        "water",
        "grass",
        "electric",
        "psychic",
        "ice",
        "dragon",
        "dark",
        "fairy"]


def newprint(dice):
    for word in list:
        print(dice[word])
