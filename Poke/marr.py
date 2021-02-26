import os
import re
from glob import glob

import json
import requests
import urllib.request as req

baseurl = "https://pokeapi.co/api/v2/pokemon/"

baseurlTypes = "https://pokeapi.co/api/v2/type/"

main = {}


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


def getSprites():
    """
    Gets the front sprite for each pokemon
    """

    for i in range(1, 899):
        r = requests.get(baseurl + str(i) + "/")
        res = r.json()
        img = res['sprites']["front_default"]
        req.urlretrieve(
            img, r"C:/Users/bajab/Documents/Projects/Website/brandon-joseph.github.io\/Poke/sprites/" + str(i) + ".png")


# getAmounts()


def MoveByType():
    """
    Move pokemon into proper type folder
    """
    for i in range(0, 899):
        base = r"C:/Users/bajab/Documents/Projects/Website/brandon-joseph.github.io/Poke/sprites/all"
        end = str(i) + ".png"
        r = requests.get(baseurl + str(i) + "/")
        res = r.json()
        typ = res['types'][0]['type']['name']
        os.rename(base + end,
                  base + typ + "/" + end)


def MoveByTypeSecondary():
    """
    Move pokemon into proper secondary type folder
    """
    for i in range(1, 899):
        base = r"C:/Users/bajab/Documents/Projects/Website/brandon-joseph.github.io/Poke/sprites/all/"
        dst = r"C:/Users/bajab/Documents/Projects/Website/brandon-joseph.github.io/Poke/sprites/secondary/"
        end = str(i) + ".png"
        r = requests.get(baseurl + str(i) + "/")
        res = r.json()
        try:
            typ = res['types'][1]['type']['name'] + "Sec"
            os.rename(base + end,
                      dst + typ + "/" + end)
        except:
            os.rename(base + end,
                      dst + "none" + "/" + end)


def Arrange():
    """ 
    Makes variables for javascript code
    """
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


def ArrangeSecondary():
    """ 
    Makes variables secondary types for javascript code
    """
    folders = glob("./Poke/sprites/secondary/*/")
    print(folders)
    for folder in folders:
        _, _, filenames = next(os.walk(folder))
        typ = re.search(r'([^\\]+)\\$', folder).group(0)[:-1]

        final = f"var {typ[:-3]}Files2 = "
        finish = list(map(lambda x: "/sprites/secondary/" + typ +
                          "/" + x, filenames))
        sort_nicely(finish)

        # joined_string = ",".join(finish)
        with open('./Poke/ListsForVariables/' + typ + '.txt', 'w') as f:
            f.write(final + "%s\n" % finish)


def getNames():
    """
    Gets the name for each pokemon
    """
    names = []
    final = f"var pokeNames = "
    for i in range(0, 898):
        r = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=898")
        res = r.json()
        results = res['results']
        names.append(results[i]['name'])
    with open('./Poke/ListsForVariables/Pokenames.txt', 'w') as f:
        f.write(final + "%s\n" % names)


def getTypeDictionary():
    typeDic = {}
    final = f"var pokeTypesDic = "
    for i in range(1, 899):
        r = requests.get(baseurl + str(i) + "/")
        res = r.json()
        types = []
        length = len(res['types'])
        for i in range(length):
            types.append(res['types'][i]['type']['name'])
        typeDic[res['name']] = types
    with open('./Poke/ListsForVariables/typeDic.txt', 'w') as f:
        f.write(final + "%s\n" % typeDic)


# MoveByType()
# MoveByTypeSecondary()
# Arrange()
# ArrangeSecondary()
# getNames()
getTypeDictionary()
