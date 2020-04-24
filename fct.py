import os, sys, pickle, re
from datetime import datetime
from collections import Counter
from mesClass import *


def session(): #on instancie la session, caractérisée par la date du jour
    current = Bilan()
    #print("Bienvenu : session du ", current.date)
    return current.date

    
def CheckDate(): #vérifier si la date du jour existe dans le fichier
    scores = open("scores.txt","r")
    data = scores.read()
    date = datetime.now().strftime("%d/%m/%y")
    check = data.count(date)
    scores.close()
    existe = 0
    if check > 0 :
        existe = 1
    return existe

def gameOn():

    result = ""
    print('Résultat du match parmis ces choix')
    print('V = victoire')
    print('D = Defaite')
    print('-V = correction victoire')
    print('-D = correction defaite')
    print('Q = quitter')
    

gameOn()



