from jasminhello.sonVolume import Enceinte
class enfant(Enceinte):

    def __init__(self,music, genre, volume, pressure):
        self.music = music
        self.genre = genre
        super(enfant, self).__init__(volume,pressure)

    def getVolPress(self):
        print("Volume : " + str(self.getVolume()) + " Pressure : " + str(self.getPressure()))

    def getGenre(self):
        print("Genre : ", self.genre)

    def getSong(self):
        print("Chanson : ", self.music)

e = enfant("aveMaria", "classical", 4.5, 6.6)
e.getVolPress()
e.getSong()
e.getGenre()
