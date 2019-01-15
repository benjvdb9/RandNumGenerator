from time import time
from MersenneTwister import Twister

class Rand:
    def __init__(self):
        self.__seed_mode = 1
        self.__steps = [1, 1, 1]
        self.newSeed()
        self.__rand = self.__seed

    #Crée un nouveau seed en fonction du seed_mode
    def newSeed(self):
        if self.__seed_mode == 1:
            self.milliSeed()
        elif self.__seed_mode == 2:
            self.milliSeed()
            self.__rand = self.__seed
        elif self.__seed_mode == 3:
            self.timeSeed()
            self.__rand = self.__seed
        else:
            self.__seed = 12345678
            self.__rand = self.__seed

    #Le Seed sera les milisecondes du timer. self.__rand
    #ne sera
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
        #print("Seed:", self.getSeed())
        #print("Rand:", self.getRand())
        complete = self.__rand ** 2
        middle = (complete % 10**12) // 10**4 #Modulo garde les 12 derniers chiffres
        complete = middle ** 2
        middle = (complete % 10**12) // 10**4 #Division efface les 4 derniers chiffres
        self.__rand = middle

    def mersenneTwister(self):
        twis = Twister()
        twis.initialize_generator(self.__seed)
        rand = twis.extract_number()
        rand = (rand % 10**9) // 10
        self.__rand = rand

    def getSeed(self):
        return self.__seed

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

test = Rand()
