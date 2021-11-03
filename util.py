"""
@author TheDoctorOne - Mahmut H. Koçaş
@date 3.11.2021 22:39
"""
import json
import os

from Person import Person

commandNotFoundMessage = "Girdiğiniz Komut Bulunamadı."
didYouMean = " Bunlardan birini mi demek istediniz? : "

def strMatchPercent(word1 : str, word2 : str):
    """
    Dirty string compare. For dirty needs.
    """
    w1Len = len(word1)
    w2Len = len(word2)
    m = max(w1Len, w2Len)
    if m == 0:
        return 100; # Well, they are exact. Not gonna lie.

    matchCount = 0

    for i in range(w1Len):
        for j in range(w2Len):
            if word1[i] == word2[j]:
                matchCount += 1
                break

    return matchCount/m * 100


def findPossibleCommands(argDictionary : dict, cmd, posLimit=75) -> list:
    pos = []
    for key in argDictionary.keys():
        if strMatchPercent(cmd, key) >= posLimit:
            pos.append(key)
    return pos
    
def parseArgs(argDictionary, args):
    """
    @param args are stripped to not include this file's path which always get included.
    """
    cmd = args[0]
    try:
        argDictionary[cmd](args)
    except KeyError:
        print(commandNotFoundMessage, end="") #Removing new line for didYouMean
        mean = findPossibleCommands(argDictionary, cmd)
        if len(mean) > 0:
            print(didYouMean, mean)
        else:
            print("") # For new line.
        argDictionary["help"]()


        
def makeItJSON(jsonableList):
    return json.dumps([z.__dict__ for z in jsonableList], indent=4, sort_keys=True)

def readSaveFile(saveFile : str) -> dict:
    people = {}
    peopleList = []
    if(os.path.isfile(saveFile)):
        openedFile = open(saveFile, "r")
        d = openedFile.read()
        if len(d) > 0:
            peopleList = json.loads(d)
        openedFile.close()

    for p in peopleList:
        pp = Person()
        pp.from_dict(p)
        people[pp.ingame] = pp

    return people
    
def writeSaveFile(saveFile : str, jsonableDict : dict):
    openedFile = open(saveFile, "w")
    openedFile.write(makeItJSON(jsonableDict.values()))
    openedFile.close()

    
def addAKA(argDictionary:dict, mainCommand:str,akaCommand:str):
    argDictionary[akaCommand] = argDictionary[mainCommand]