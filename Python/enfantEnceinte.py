from jasminhello.sonVolume import Enceinte
class enfant(Enceinte):

    def __init__(self,music, genre, son):
        self.music = music
        self.genre = genre
        self.son = son

    def getVolPress(self):
        print("Volume : " + str(getattr(self.son, "volume")) + " Pressure : " + str(getattr(self.son, "pressure")))

    def getGenre(self):
        print("Genre : ", self.genre)

    def getSong(self):
        print("Chanson : ", self.music)

enc = Enceinte(5.9,22)
e = enfant("aveMaria", "classical", enc)
e.getVolPress()
e.getSong()
e.getGenre()
getattr(e.son, "checkState")()
e.son.checkState()