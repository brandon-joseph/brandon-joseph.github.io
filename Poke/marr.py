import os
import re
from glob import glob


def topack(pack):
    lst = [y for y in (x.strip() for x in pack.splitlines()) if y]
    i = 0
    for word in lst:
        if (i == 0):
            print("[" + word + ",")
        elif i == len(lst)-1:
            print(word + "]")
        else:
            print(word + ',')
        i += 1
    return "------"


def flip(pack):
    lst = [y for y in (x.strip() for x in pack.splitlines()) if y]
    for word in lst:
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
    lst = [y for y in (x.strip() for x in pack.splitlines()) if y]
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

    for word in lst:
        ind = word.find(',')
        sep = word.find('|')
        first = word[sep+1:ind]
        if sep == -1:
            first = word[0:ind]

        second = int(word[ind+1:].strip())
        dice[first] = second
    newprint(dice)


lst = ["normal",
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
    for word in lst:
        print(dice[word])


def tryint(s):
    try:
        return int(s)
    except:
        return s


def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [tryint(c) for c in re.split('([0-9]+)', s)]


def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """
    l.sort(key=alphanum_key)


def Arrange():
    folders = glob("./Poke/sprites/*/")
    print(folders)
    for folder in folders:
        _, _, filenames = next(os.walk(folder))
        typ = re.search(r'([^\\]+)\\$', folder).group(0)[:-1]

        final = f"var {typ}Files ="
        finish = list(map(lambda x: "/sprites/" + typ +
                          "/" + x, filenames))
        sort_nicely(finish)

        # joined_string = ",".join(finish)
        with open('./Poke/ListsForVariables/' + typ + '.txt', 'w') as f:
            f.write("%s\n" % finish)

        break


Arrange()
