# Hello World program in Python
# MIDDEL SQUARE METHODE
import math


digit = 10
seed  = 3994309523
def  random():
            global seed
            carre = seed*seed
            carreString = str(carre)
            while (len(carreString) < (digit*2)):
                carreString = "0" +carreString
            startNumber = math.floor(digit/2) 
            endNumber = startNumber + digit
            seed = int(carreString[int(startNumber):int(endNumber)]) 
            return seed
          
def  randomFloat():
                 return (random()/9999999999)

tableau = []
for i in range(100) :
    a = random()
    tableau.append(a)
    #print(tableau)
    if 3994309523 in tableau:
       print ("valeur trouvee")
       print(tableau)
       print(tableau.index(3994309523))
       break
    elif 0 in tableau:
        print(tableau)
        print("valeur 0")
        print(tableau.index(0))
        break
print(tableau)
print(100000) 
