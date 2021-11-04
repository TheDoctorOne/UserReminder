"""
@author TheDoctorOne - Mahmut H. Koçaş
@date 3.11.2021 22:39
"""

from dictable import dictable

class Person(dictable):
    ingame : str
    name : str
    age : int
    location : str
    job : str
    firstSeenWorld : str
    seenWorlds = []
    sharedMoments = []

    def __init__(self, d=None):
        if d is not None:
            super().__init__(d)
        else:
            self.ingame = ""
            self.name = ""
            self.age = -1
            self.location = ""
            self.job = ""
            self.firstSeenWorld = -1
            self.seenWorlds = []
            self.sharedMoments = []

    def prettyPrint(self):
        print("Kullanıcı Adı:  \t",self.ingame)
        print("Gerçek Adı:     \t",self.name)
        print("Yaş:            \t",self.age)
        print("İlk Görünen Yer:\t",self.firstSeenWorld)
        print("Lokasyon:       \t",self.location)
        print("İş:             \t",self.job)
        print("Görünen Yerler: \t",self.seenWorlds)
        print("Anılar:         \t",self.sharedMoments)

        