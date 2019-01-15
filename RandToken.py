from time import time
from MersenneTwister import Twister

class Rand:
    def __init__(self):
        self.__seed_mode = 1
        self.__steps = [2]
        self.newSeed()
        self.__rand = self.__seed
        self.__charlist = self.getCharList()

    def newSeed(self):
        if self.__seed_mode == 1:
            self.milliSeed()
        elif self.__seed_mode == 2:
            self.milliSeed()
            self.__rand = self.__seed
        elif self.__seed_mode == 3:
            self.timeSeed()
        else:
            self.timeSeed()
            self.__rand = self.__seed

    def milliSeed(self):
        self.__seed = int((time() % 1) * 100000000 // 1)

    def timeSeed(self):
        time_seed = int(time() // 1)
        seed_length = len(str(time_seed))
        self.__seed = time_seed // 10**(seed_length - 8)

    def applySteps(self):
        steps_dict = {1: self.newtonStep, 2: self.mersenneTwister}
        for step in self.__steps:
            func = steps_dict[step]
            func()

    def newtonStep(self):

        complete = self.__rand ** 2  #mettre le seed au carré
        # le Modulo 10**12 garde les 12 derniers chiffres et la division entiere par 10**4  efface les 4 derniers chiffres
        middle = (complete % 10**12) // 10**4

        complete = middle ** 2 #repetition du processus
        middle = (complete % 10**12) // 10**4
        self.__rand = middle

    def mersenneTwister(self):
        twis = Twister()
        twis.initialize_generator(self.__seed)
        rand = twis.extract_number()
        rand = (rand % 10**9) // 10
        self.__rand = rand

    def getRand(self):
        return self.__rand

    def createRand(self):
        self.newSeed()
        self.applySteps()

    def rand(self):
        self.createRand()
        to1 = self.__rand / 10**8
        return to1

    def range(self, end=1, start=0):
        rng = end - start
        rand1 = round(rng * self.rand())
        rand2 = rand1 + start
        return rand2

    def generateToken(self):
        chars = []
        for i in range(10):
            character = self.getTokenChar()
            chars += str(character)

        token = ''.join(chars)
        return token

    def getTokenChar(self):
        index = self.range(35)
        return self.__charlist[index]

    def getCharList(self):
        charlist = []
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for letter in alphabet:
            charlist += letter
            
        for i in range(10):
            charlist += [i]

        return charlist
    
    #temps d'execution pour la generation de 100  sequences
    def exe_time(self):
        start_time = time()
        print(start_time)

        i=1
        while i <= 100:
          self.range( 36)
          i+=1

        stop_time = time()
        print(stop_time)
        temps_exe = (stop_time - start_time)
        return temps_exe
    
test = Rand()
