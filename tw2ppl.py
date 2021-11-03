"""
@author TheDoctorOne - Mahmut H. Koçaş
@date 3.11.2021 22:39
"""

import json
import sys
import os
from Person import Person
from util import *

saveFile = "people.json"
people = {}
openedFile = None
helpMessage = "======= Yardım Mesajı =======\nKomutlar / Kullanımları"
findPersonUsage = "<bul>\t\tkullanımı: bul <kullanıcı-adı>*"
momentUsage = "<anı>\t\tkullanımı: anı <kullanıcı-adı>* <anı>*"
addSeenPlace = "<göründü>\tkullanımı: göründü <kullanıcı-adı>* <göründüğü yer/dünya>*"
addPersonUsage = "<ekle>\t\tkullanımı: ekle <kullanıcı-adı>* <gerçek-isim>* <ilk göründüğü yer/dünya>* <yaş> <lokasyon> <iş>"
forcedAnnote = "( * içeren alanlar zorunludur. )"

personNotFound = "Aradığınız Kullanıcı Bulunamadı. :("

def buildHelp():
    return helpMessage + "\n" + addPersonUsage + "\n" + findPersonUsage + "\n" + addSeenPlace + "\n" + momentUsage + "\n" + forcedAnnote

def printHelp(args=None):
    print(buildHelp())

def printUsage(usageMes:str):
    print(usageMes, "\n" ,forcedAnnote)

def addPerson(args):
    cmd = args[0]
    args = args[1:]
    argLen = len(args)
    if argLen < 3:
        printUsage(addPersonUsage)
        return
    people = readSaveFile(saveFile)

    p = Person()
    p.ingame = args[0]
    p.name = args[1]
    p.firstSeenWorld = args[2]

    if argLen > 3:
        p.age = args[3]

    if argLen > 4:
        p.location = args[4]

    if argLen > 5:
        p.job = args[5]

    people[p.ingame] = p

    writeSaveFile(saveFile, people)

def findPerson(args):
    cmd = args[0]
    args = args[1:]
    argLen = len(args)
    if argLen == 0:
        printUsage(findPersonUsage)
        return
    
    people = readSaveFile(saveFile)

    nickname = args[0]

    try:
        people[nickname].prettyPrint();
    except:
        print(personNotFound)

def addMoment(args):
    cmd = args[0]
    args = args[1:]
    argLen = len(args)
    if argLen < 2:
        printUsage(momentUsage)
        return

        
    nickname = args[0]
    people = readSaveFile(saveFile)

    try:
        moment = ""
        for m in args[1:]:
            if m.strip() == "":
                continue
            moment += m + " "
        people[nickname].sharedMoments.append(moment)
    except:
        print(personNotFound)

    writeSaveFile(saveFile, people)

    nickname = args[0]

if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0]))
    args = sys.argv
    
    argDictionary = {}
    argDictionary["help"] = printHelp
    argDictionary["add"] = addPerson
    argDictionary["moment"] = addMoment
    argDictionary["find"] = findPerson
    addAKA(argDictionary, "help", "yardım")
    addAKA(argDictionary, "help", "h")
    addAKA(argDictionary, "help", "y")
    addAKA(argDictionary, "add", "ekle")
    addAKA(argDictionary, "add", "e")
    addAKA(argDictionary, "moment", "anı")
    addAKA(argDictionary, "find", "f")
    addAKA(argDictionary, "find", "bul")
    addAKA(argDictionary, "find", "b")

    #args = ["c:/Users/DoctorOne/Desktop/tw2users/tw2ppl.py", "e", "DoctorOne", "Mahmut", "WorldNum"]

    if len(args) <= 1:
        argDictionary["help"]();
    else:
        parseArgs(argDictionary, args[1:])
    pass