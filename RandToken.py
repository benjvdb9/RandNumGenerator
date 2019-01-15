from time import time, clock
from MersenneTwister import Twister

class Rand:
    def __init__(self):
        self.__seed_mode = 2
        self.__steps = [2]
        self.newSeed()
        self.__rand = self.__seed
        self.__charlist = self.getCharList()
        self.__twister_exist = False
        

    #Crée un seed sur base du seed_mode
    #1 ->   on commence avec les ms mais ensuite on utilise
    #       l'ancien résultat comme seed
    #2 ->   on utilise le ms comme seed
    #3 ->   on utilise le temps (>1s) comme seed (pratiquement fixe)
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
            self.timeSeed()
            self.__rand = self.__seed

    #Rend les millisecondes du temps
    def milliSeed(self):
        self.__seed = int((time() % 1) * 100000000 // 1)

    #Rend le temps en secondes (secondes depuis 1970)
    def timeSeed(self):
        time_seed = int(time() // 1)
        seed_length = len(str(time_seed))
        self.__seed = time_seed // 10**(seed_length - 8)

    #Applique les fonctions spécifiès dans self.__steps
    def applySteps(self):
        steps_dict = {1: self.newtonStep, 2: self.mersenneTwister}
        for step in self.__steps:
            func = steps_dict[step]
            func()

    #Middle Square Methode:
    #   Mettre notre seed au carré et garder les 8 chiffres au milieu 
    def newtonStep(self):
        print("Seed:", self.__seed)
        print("Rand:", self.__rand)
        complete = self.__rand ** 2

        # le Modulo 10**12 garde les 12 derniers chiffres et
        # la division entiere par 10**4  efface les 4 derniers chiffres
        middle = (complete % 10**12) // 10**4
        
        complete = middle ** 2 #repetition du processus
        middle = (complete % 10**12) // 10**4
        self.__rand = middle

    #Application du Mersenne Twister
    def mersenneTwister(self):
        import pdb;pdb.set_trace()
        if not self.__twister_exist:
            self.__twis = Twister()
            self.__twister_exist = True
            self.__twis.initialize_generator(self.__seed)
        rand = self.__twis.extract_number()
        rand = (rand % 10**9) // 10
        self.__rand = rand

    #Getter seed
    def getSeed(self):
        return self.__seed

    #Getter rand
    def getRand(self):
        return self.__rand

    #Créé un chiffre aléatoire rand a 8 digits
    def createRand(self):
        self.newSeed()
        self.applySteps()

    #Convertit rand en un float entre 0 et 1
    #de 8 digits après la virgule
    def rand(self):
        self.createRand()
        to1 = self.__rand / 10**8
        return to1

    #Rend un chiffre aléatoire entre start et end
    def range(self, end=1, start=0):
        rng = end - start
        rand1 = round(rng * self.rand())
        rand2 = rand1 + start
        return rand2

    #Genere un token de 10 charactères
    def generateToken(self):
        chars = []
        for i in range(10):
            character = self.getTokenChar()
            chars += str(character)

        token = ''.join(chars)
        return token

    #Rend un charactère aléatoire
    def getTokenChar(self):
        index = self.range(35)
        return self.__charlist[index]

    #Crée notre liste de charactères pour le token
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

#Objet Rand utilisé pour les tests
test = Rand()
