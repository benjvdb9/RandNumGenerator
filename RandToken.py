from time import time

class Rand:
    def __init__(self):
        self.__seed_mode = 2
        self.__steps = [1, 1, 1]
        self.newSeed()
        self.__rand = self.__seed

    def newSeed(self):
        if self.__seed_mode == 1:
            self.milliSeed()
        elif self.__seed_mode == 2:
            self.timeSeed()
        else:
            self.__seed = 0

    def milliSeed(self):
        self.__seed = int((time() % 1) * 100000000 // 1)

    def timeSeed(self):
        time_seed = int(time() // 1)
        seed_length = len(str(time_seed))
        self.__seed = time_seed // 10**(seed_length - 8)

    def applySteps(self):
        steps_dict = {1: self.newtonStep}
        for step in self.__steps:
            func = steps_dict[step]
            func()

    def newtonStep(self):
      #recupère un seed et on élève au carré
        complete = self.__rand ** 2
      #
        middle = (complete % 10**12) // 10**4 #Modulo garde les 12 derniers chiffres
        complete = middle ** 2
        middle = (complete % 10**12) // 10**4 #Division efface les 4 derniers chiffres
        self.__rand = middle

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

    #temps d'execution pour la generation de 100  sequences
    def exe_time(self):
      start_time = time()
      print(start_time)

      i=1
      while i <= 100:
        self.range( 36)
        i=i+1
      stop_time = time()
      print(stop_time)
      temps_exe = (stop_time - start_time )
      return temps_exe

test = Rand()
''
