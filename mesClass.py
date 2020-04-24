import os, sys, pickle, re
from datetime import datetime


#voici ma future classe qui compte

class Bilan :
    """le but est de faire un bilan journalier victorie / défaite et le bilan
    c'est à dire victoire moins défaite"""

    
    def __init__(self): # Notre méthode constructeur
        self.date = datetime.now().strftime("%d/%m/%y")
        self.nbVictoire = 0 # Quelle originalité
        self.nbDefaite = 0 # Cela n'engage à rien

    #méthode pour ajotuer ou retirer des victoires
    def victoire(self):
        self.nbVictoire += 1

    def defaite(self):
        self.nbDefaite +=1

    #méthode pour ajotuer ou retirer des défaites
    def victoireC(self):
        self.nbVictoire -= 1

    def defaiteC(self):
        self.nbDefaite -=1

          
def test(): #fonction pour tester le comportement des méthodes
    test = Bilan()
    print("la date est le ",test.date)
    print('on commence avec ',test.nbVictoire,' victoires et ',test.nbDefaite,' défaites')
    test.victoire()
    test.victoire()
    test.defaite()
    print('on gagne deux fois et perd une fois')
    print('on a ',test.nbVictoire,' victoires et ',test.nbDefaite,' défaites')
    test.victoireC()
    test.defaiteC()
    print('je corrige une victoire et une défaite')
    print('on a ',test.nbVictoire,' victoires et ',test.nbDefaite,' défaites')     
